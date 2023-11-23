import Rules

CT = ""
# Trie = 

def readhtmlFile(path):
    try:
        with open(path, "rt") as file:
            str = ""
            line = file.readline()
            while(line):
                str = str + line
                line = file.readline()
        file.close()
        return str
    except FileNotFoundError:
        print("HTML file is not found")
    except Exception as e:
        print(f"Unexpected error while reading HTML file - {e}")
    
# def createTrie(term):

    
def startToken(path):
    htmlString = readhtmlFile(path)
    # createTrie(Rules.terminal)