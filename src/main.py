import os
import Rules
import sys
import Token

# python3 src/main.py PDA/test.txt "test/inputAcc.html"

def findPath(startDir, relativePath):
    for (root, dirs, files) in os.walk(startDir):
        for dirName in dirs:
            filePath = os.path.join(startDir, dirName, relativePath)
            if os.path.exists(filePath):
                return filePath
    return None


if __name__ == "__main__":
    states, terminal, stackSymbol, startState, startStack, acceptingState, acceptby, rules = None, None, None, None, None, None, None, None
    rulesPathRelative = sys.argv[1]
    htmlPathRelative = sys.argv[2] 
    htmlPathRelative.replace('"', '')
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    rootDir, dull = os.path.split(scriptDir)
    resDir = os.path.join(rootDir, "res")

    rulesPath = findPath(resDir, rulesPathRelative)
    print(rulesPath)
    if (rulesPath) == None:
        print("PDA file is not found")
    
    htmlPath = findPath(resDir, htmlPathRelative)
    print(htmlPath)
    if htmlPath == None:
        print("HTML file is not found")
    
    states, terminal, stackSymbol, startState, startStack, acceptingState, acceptby, rules = Rules.readrulesFile(rulesPath)
    Token.startToken(htmlPath)