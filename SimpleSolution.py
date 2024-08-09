import pdfplumber
import re

text = ""

def readFile(path):
    global text
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

def extractNumbers():
    numbers = re.findall(r'\b\d+\.?\d*\b', text)
    numbers = [float(num) for num in numbers]
    return numbers

def findSimpleLargestNumber(file_path):
    readFile(file_path)
    return max(extractNumbers())

# Sol: 3,330,000.0