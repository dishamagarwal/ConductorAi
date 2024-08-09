import pdfplumber, re, spacy

text = ""
nlp = spacy.load("en_core_web_sm")

# importing the file
def readFile(path):
    global text
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

def extract_numbers():
    doc = nlp(text)
    max_num = 0
    # reading sentences
    for sent in doc.sents:
        # finding numeric words in sentence
        context = None
        if "billions" in sent.text.lower():
            context = "billion"
        elif "millions" in sent.text.lower():
            context = "million"
        elif "thousands" in sent.text.lower():
            context = "thousand"
        elif "hundreds" in sent.text.lower():
            context = "hundred"
    
        # reading words in the setence
        for token in sent:
            # finding if each token is a number
            if token.like_num:
                try:
                    num = float(token.text.replace(',', ''))
                    if context == "billion":
                        num = num * 1_000_000_000
                    elif context == "million":
                        num = num * 1_000_000
                    elif context == "thousand":
                        num = num * 1_000
        
                    max_num = max(max_num, num)
                except ValueError:
                    continue
    return max_num

def findLargestNumber(file_path):
    global text
    readFile(file_path)
    return extract_numbers()

# Sol: 30,704,100,000.0