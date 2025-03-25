import re


def remove_specials(text):
    return re.sub(r'[^\w\s]|_', '', text)

def contains_char(text, char):
    return re.search(r'\b.*' + str(char) + r'.*\b', text)

def n_chars_long(text, n):
    return re.search(r'\b\w{' + str(n) + r'}\b', text)

def begins_with_ab_ends_with_s(text):
    return re.search(r'\b[ab]\S*s\b', text)