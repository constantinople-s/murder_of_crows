import re
'''This is a comment'''


def retrieve_monetary_values(text):
    results = re.findall(r"(?<=\$)\d*(?:\.\d{1,2})?\b", text)
    return sum([float(result) for result in results]) # this is a comment