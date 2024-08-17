"""
|===| Gmoneylang 1.0.0 source code |===|
Gmoneylang is licensed under the MIT license.
Open the LICENSE file for more details.
Copyright (c) 2024 boyninja15
"""

import lexer
import interpreter

code = """
string name = "Grant"
int age = 22
"""

def main():
    tokens = lexer.tokenize(code)
    print("Tokens:", tokens)
    interpreter.run(iter(tokens))

if __name__ == "__main__":
    main()
