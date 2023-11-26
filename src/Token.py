import Trie

CT = ""
anyText = "ANYTEXT"

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
    
def parseString(string : str):
    htmlUniformQuote = string.replace('”', '"')
    htmlAnyText = htmlUniformQuote.split('"')
    for i in range(len(htmlAnyText)):
        if (i & 1):
            htmlAnyText[i] = anyText

    htmlSplitted = []
    htmlParsed = []

    for i in range(len(htmlAnyText)):
        print(htmlAnyText[i])
        print("\n")
    
    for i in range(len(htmlAnyText)):
        htmlAnyText[i].replace('\n', ' ')
        htmlAnyText[i].replace('\t', ' ')
        htmlSplitted.append(None)
        htmlSplitted[i] = htmlAnyText[i].split()
        for j in range(len(htmlSplitted[i])):
            htmlParsed.append(htmlSplitted[i][j])
    return htmlParsed

def startTokenize(path, Terminal):
    htmlString = readhtmlFile(path)
    htmlParsed = parseString(htmlString)