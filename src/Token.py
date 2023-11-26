import Trie

CT = ""
anyText = "anyText"

def replaceAtIndex(string : str, start : int, end : int, replace : str):
    return string[:start] + replace + string[end:]

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

def convertAnyText(string : str):
    i = 0
    while i < len(string):
        if (string[i] == '<'):
            i += 1
            j = i
            if (string[i:i+3] == "!--"):
                while (j < len(string) and string[j:j+3] != "-->"):
                    j += 1
                if (j < len(string)):
                    length = j - i - 7 
                    string = replaceAtIndex(string, i+3, j, anyText)
                    i = j-1
                    i -= length
            else:
                while (j < len(string) and string[j] != '>'):
                    j += 1
                if (j < len(string)):
                    i = j + 1
                    j = i
                    whitespaceOnly = True
                while (j < len(string) - 1):
                    j += 1
                    if (string[j] == '<'):
                        break
                    if (not (string[j] == '\t' or string[j] == '\n' or string[j] == ' ')):
                        whitespaceOnly = False
                if (j < len(string) and not (whitespaceOnly)):
                    string = replaceAtIndex(string, i, j, anyText)
                    length = j - i - 7 
                    i = j-1
                    i -= length
        if (i < len(string)):
            i += 1
        else:
            break
    htmlUniformQuote = string.replace('”', '"')
    splitQuote = htmlUniformQuote.split('"')
    htmlNoQuote = [None]
    htmlNoQuote[0] = splitQuote[0]
    for i in range(1, len(splitQuote)):
        htmlNoQuote.append('"')
        if (i & 1):
            htmlNoQuote.append(anyText)
        else:
            htmlNoQuote.append(splitQuote[i])
    return htmlNoQuote
    
def parseString(htmlAnyText):
    htmlSplitted = []
    htmlParsed = []
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
    htmlAnyText = convertAnyText(htmlString)
    htmlParsed = parseString(htmlAnyText)