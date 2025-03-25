import re


def clean_up_code(text):
    pattern = r'(#.*$)|' + \
        r'(\'\'\'[\s\S]*?\'\'\')|' + \
        r'(\"\"\"[\s\S]*?\"\"\")'
    result = re.sub(pattern, '', text, flags=re.MULTILINE)
    return '\n'.join(line.rstrip() for line in result.splitlines() if line.strip())

def main(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    return clean_up_code(text)

main('test_input.py')