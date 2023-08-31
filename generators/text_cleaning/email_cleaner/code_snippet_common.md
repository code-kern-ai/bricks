```python
import re

def email_cleaner(text):
        text = re.sub("DISCLAIMER((\w|\s|\S))+?(?=From:|\Z)", "",text, flags=re.IGNORECASE)
        text = re.sub("EXTERNAL EMAIL.*?(?=\.)\.", "", text, re.IGNORECASE)
        text = re.sub("\[cid:image.*?(?=\])\]", "",text, re.IGNORECASE)
        text = re.sub("signature((\w|\s|\S))+?(?=From:|\Z)","",text, re.IGNORECASE)
        return text

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

emails = ["""Hi Sofia, 
I hope this email finds you well. I have some exciting news to share with you regarding a potential new client for StellarDefense Insurance. We have recently received an application from a company called Bleyerstift and More, who are in need of insurance coverage. Bleyerstift and More is a reputable company in the manufacturing industry. They operate in the pharmaceutical sector, specializing in the production of medical supplies. With a workforce of approximately 500 employees, they are located at 123 Main Street, Anytown, USA. You can find more information about them on their website at www.bleyerstiftandmore.com. 
The client has requested a submission to be completed by April 1st, 2024. They are specifically interested in obtaining a comprehensive general liability insurance policy, with a coverage limit of $1 million for each occurrence. 
Please let me know if you require any additional information from them or if there are any specific questions you would like me to address. As for attachments, there is a document that provides a detailed breakdown of Bleyerstift and More's revenue and other pertinent financial information. 
I have included this attachment for your reference. I believe this opportunity has great potential for StellarDefense Insurance's growth and would appreciate your assistance in handling this case. If you have any questions or need any further information, please do not hesitate to reach out to me. Thank you for your time and support in this matter. 
[cid:image012915.png@C10DB1A7.DEFECF3B]
Best regards, 
Amelia Smith Insurance Broker StellarDefense Insurance

DISCLAIMER

The information contained in this communication from the sender is confidential. It is intended solely for use by the recipient and others authorized to receive it. If you are not the recipient, you are hereby notified that any disclosure, copying, distribution or taking action in relation of the contents of this information is strictly prohibited and may be unlawful.

This email has been scanned for viruses and malware, and may have been automatically archived by blubb.

From: Bender, Zoe <bender@2u.de>
Sent: 22 September 2022 16:55
To: Smith, Amelia <smith@stellardefence.de>
Subject: Small question

EXTERNAL EMAIL: This email originated from outside StellarDefense.
Dear Amelia, 
I just wanted to know if you have new information for me. If I remember correctly, you told me about a great deal with a new company. Love to hear more about it. 
All best
Zoe
[signature]"""]

def example_integration():
    texts = emails
    for text in texts:
        print(f"the emails will looked cleansed like this:\n{email_cleaner(text)}")
example_integration() 

```