import re
import pandas as pd
"""
8 oder 11 Stellen
BBBB = Buchstabe oder Ziffer
CC = Buchstabe
LL = Buchstabe oder Ziffer; erstes Zeichen nicht 0 oder 1, zweites Zeichen nicht O
bbb = Buchstabe oder Ziffer, danach um XXX ergänzbar, aber kein Muss. 
"""

regex = re.compile(r'[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z2-9][A-NP-Z0-9]([XXX]{3,3}){0,1}')

def printStuff(text):
    print(text)

def isValid(bic):
    if re.fullmatch(regex, bic):
        printStuff("Vailid bic")
    else:
        printStuff("Invalid bic")


'''
testing the code
'''
bics = pd.read_excel("C:\Users\svenj\Downloads\blz-aktuell-xlsx-data.xlsx")


