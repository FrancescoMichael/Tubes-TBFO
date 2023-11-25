import Rules

CT = ""
# Trie = 

def readhtmlFile(path):
    try:
        with open(path, "rt", encoding="utf8") as file:
            str = ""
            line = file.readline()
            while(line):
                str = str + line
                line = file.readline()
        file.close()
        return str
    except Exception as e:
        print(f"Unexpected error while reading HTML file - {e}")
    
# def createTrie(term):

    
def startToken(path):
    htmlString = readhtmlFile(path)
    # createTrie(Rules.terminal)