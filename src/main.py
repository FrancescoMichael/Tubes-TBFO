import sys
import Rules
import Token

# python3 src/main.py PDA/test.txt "test/inputAcc.html"

if __name__ == "__main__":
    rulesPath = sys.argv[1]
    htmlPath = sys.argv[2] 
    htmlPath.replace('"', '')
    Rules.readrulesFile(rulesPath)
    Token.startToken(htmlPath)
