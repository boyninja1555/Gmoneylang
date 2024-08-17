
def tokenize(code: str):
    lines = code.split("\n")
    tokens = []

    for line in lines:
        elements = line.split(" ")

        if len(line) == 0:
            continue

        for element in elements:
            if element == "string":
                tokens.append({
                    "type": "keyword",
                    "value": element
                })
            elif element == "int":
                tokens.append({
                    "type": "keyword",
                    "value": element
                })
            elif element.isdigit():
                tokens.append({
                    "type": "integer",
                    "value": int(element)
                })
            elif element == "=":
                tokens.append({
                    "type": "operator",
                    "value": element
                })
            elif element.startswith("\"") and element.endswith("\""):
                tokens.append({
                    "type": "string_literal",
                    "value": element.strip("\"")
                })
            elif element == "+":
                tokens.append({
                    "type": "operator",
                    "value": element
                })
            elif element == "log":
                tokens.append({
                    "type": "keyword",
                    "value": element
                })
            elif element:
                tokens.append({
                    "type": "identifier",
                    "value": element
                })
    
    return tokens
