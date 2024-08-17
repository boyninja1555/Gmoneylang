
def run(tokens):
    variables = {}
    token_iter = iter(tokens)
    output = []

    for token in token_iter:
        if token["type"] == "keyword":
            if token["value"] == "log":
                expression = []
                
                while True:
                    next_token = next(token_iter, None)

                    if next_token is None or next_token["value"] == ";":
                        break

                    expression.append(next_token)

                result = evaluate_expression(expression, variables)
                output.append(result)
        elif token["type"] == "identifier":
            var_name = token["value"]
            next_token = next(token_iter, None)
            
            if next_token and next_token["type"] == "operator" and next_token["value"] == "=":
                value_token = next(token_iter, None)

                if value_token and value_token["type"] == "string_literal":
                    variables[var_name] = value_token["value"]
                elif value_token and value_token["type"] == "integer":
                    variables[var_name] = value_token["value"]
        elif token["type"] == "string_literal":
            pass
        elif token["type"] == "integer":
            pass

    print("Variables:", variables)

    for item in output:
        print(item)

def evaluate_expression(expression, variables):
    result = []

    for token in expression:
        if token["type"] == "identifier":
            value = variables.get(token["value"], token["value"])
            result.append(str(value))
        elif token["type"] == "string_literal":
            result.append(token["value"])
        elif token["type"] == "operator" and token["value"] == "+":
            result.append("+")
    
    return " ".join(result)
