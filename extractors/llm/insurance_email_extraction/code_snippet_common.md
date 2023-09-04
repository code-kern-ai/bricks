``` python
import openai
import re
import spacy
from typing import List, Tuple
import ast

def insurance_email_extraction(text: str, extraction_keyword: str, api_key: str, temperature: float) -> List[Tuple[str, int]]:
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content":   f"""
                    Please extract all {extraction_keyword} from following text:
                    {text}-
                    Only return things that are linked to {extraction_keyword}.
                    Return only a valid JSON with this structure. 
                    json
                    {{
                        "keywords": ["list with keywords goes here"]
                    }}
                    
                    Return nothing except this JSON. Make sure to only return {extraction_keyword} and nothing else. 
                    If you can't find any {extraction_keyword} in the text, just return nothing."""
                ,
            },
        ],
        temperature=temperature,
    )
    try: 
        out = response["choices"][0]["message"]["content"]
        output_dict = ast.literal_eval(out)

        # check if the output is really a dictionary
        if isinstance(output_dict, dict):
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(text)

            char_positions = []
            if len(output_dict["keywords"]) > 0:
                for found_keyword in output_dict["keywords"]:
                    regex = re.compile(f"{found_keyword}")
                    match =  regex.search(text)
                    start, end = match.span()
                    span = doc.char_span(start, end, alignment_mode="expand")
                    #char_positions.append((extraction_keyword, span.start, span.end)) 
                    char_positions.append((match[0], span.start, span.end)) 
            else:
                return "No matching keywords found."
            return char_positions
        else:
            return f"GPT response was not a valid dictionary. The response was: {response}."
    except: 
        return response["choices"][0]["message"]["content"]


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

emails_generated= [""" Dear Chloe,

Hope you're doing great! I have some exciting news regarding a new insurance policy we have secured for UnityCare Insure. Please find all the relevant details below.

Insured Company details:
Name: Yoga Health Life
Address: 123 Zen Way, Mindfulnessville, CA 98765, United States
Website: www.yogahealthlife.com
Number of Employees: Approximately 100 (estimated)

Policy Information:
Type of Insurance: Yoga Health Life
Starting Date: 01.01.2024 (as requested by the insured company)
Duration of Submission: Four to seven sentences (to confirm further details)
Sum Insured: Car 2 bil 

Attached to this email, you will find additional information regarding the terms and conditions of the policy, including coverage details and premium amounts. Please make sure to go through it thoroughly and let me know if you have any questions or require any revisions before approving the policy.

I believe this is an exceptional opportunity for UnityCare Insure to expand its coverage options and attract a diverse range of customers in the wellness and lifestyle industry. The Yoga Health Life policy offers comprehensive coverage for their yoga instructors, meditation facilities, and any liability arising from their business operations.

If you require any further information or assistance, please do not hesitate to reach out. I will be more than happy to provide you with any additional details you may need.

Looking forward to your positive response and approval for UnityCare Insure to proceed with the Yoga Health Life policy.

Warm regards,

Liam Brown
Insurance Broker""", 
"""Dear Luna,

I hope this email finds you well. It has been a while since we last caught up, but I have some exciting news to share with you today. Our team at SecureLife Underwriters has just taken up a new life well being case, with the insured company being none other than our own organization - SecureLife Underwriters itself!

Let me provide you with the key details regarding this insurance opportunity:

• Insured Company Name: SecureLife Underwriters
• Description: We are a large and renowned insurance and forwarding company.
• Number of Employees: Our organization currently employs around 500 staff members.
• Address: 123 Insurance Avenue, Central City, 56789.
• Website: www.securelifeunderwriters.com

The Life Well Being coverage will come into effect from October 1st, 2023. It aims to provide comprehensive protection for our valued employees, ensuring their overall well-being both in and out of the workplace.

We would like to submit the necessary information for this coverage within the next week to ensure prompt processing. Our submission will include details such as employee information, demographic data, specific health-related requirements, and any other information deemed necessary to provide utmost security to our personnel.

Additionally, we have attached our organizational revenue report for reference purposes. Please note that our estimated revenue for the current fiscal year stands at around $100 million.

Should you require any further details prior to processing this application, please feel free to reach out to me directly. You know me well, Luna, and I assure you that our organization greatly values the partnership we have with SecureLife Underwriters.

Looking forward to working closely with you on securing this life well being insurance for our organization.

Best regards,

Zoe Martinez
Insurance Broker""","""Dear Daniel,

I hope this email finds you well. It has been a pleasure working with you over the past years, and I trust this continued collaboration will strengthen the relationship between our companies.

I am writing to inform you of a new client that we, HeritageShield Assurance, have acquired. They are a reputable IT company called IT and More located at 123 Main Street, Cityville. With over 100 employees, IT and More specializes in providing comprehensive information technology solutions to businesses across various sectors.

To gain an insight into their operations, you can visit IT and More's website at www.itandmore.com. I encourage you to explore their corporate values and achievements to better understand their unique organizational culture.

Given their forthcoming expansion plans, IT and More is seeking your assistance in obtaining insurance coverage for their evolving needs. They prioritize getting back to us with a proposal as soon as possible to ensure they meet their targets.

The submission deadline for their custom-tailored insurance plan is [date]. The insurance package should include liability coverage, business interruption coverage, employee benefits, and property insurance among other standard provisions. The estimated annual revenue for IT and More is $10 million.

Please note that I have attached an additional document containing more specific details about IT and More's requirements and preferences. It will facilitate your team in crafting a policy proposal that aligns with their business objectives.

If you have any questions or require further clarification, please do not hesitate to reach out. I am available to discuss any concerns that you may have or coordinate a follow-up meeting with the decision-makers at IT and More.

Thank you for your prompt attention to this matter, Daniel. I fully trust that  HeritageShield Assurance will provide the top-notch insurance coverage tailored to accommodate IT and More's needs. I am looking forward to a fruitful partnership between our organizations.

Warm regards,

Charlotte Taylor
Chief Insurance Broker"""
]

def example_integration():
    # replace this list with a list containing your data
    api_key = "<API-KEY>"
    texts = emails_generated
    extraction_keywords = ["insurance companies", "insured company", "website of insured company", "address of insured company", "type of coverage", "date of submission", "amount of revenue", "description of insured company"]

    for text in texts:
        line = text.split('\n', 1)[0:3]
        print(f"The email {line} has:\n")
        for extract in extraction_keywords:
            extraction = insurance_email_extraction(text, extract, api_key, temperature=0.0) 
            print(f"{extract} -> {extraction}")

example_integration()

```