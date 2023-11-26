import Trie

T = Trie.Trie()
anyText = "anyText"

def replaceAtIndex(string : str, start : int, end : int, replace : str):
    return string[:start] + replace + string[end:]

def readhtmlFile(path):
    try:
        str = ""
        with open(path, "rt", encoding="utf8") as file:
            line = file.readline()
            cnt = 1
            lineNum = []
            while(line):
                str = str + line
                lineNum.append(cnt)
                line = file.readline()
                cnt += 1
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
    exception = ["GET", "POST", "text", "password", "email", "number", "checkbox", "submit", "reset", "button"]
    splitQuote = htmlUniformQuote.split('"')
    htmlNoQuote = [None]
    htmlNoQuote[0] = splitQuote[0]
    for i in range(1, len(splitQuote)):
        htmlNoQuote.append('"')
        if (i & 1):
            isExcept = False
            for x in exception:
                if (splitQuote[i]==x):
                    htmlNoQuote.append(splitQuote[i])
                    isExcept = True
                    break
            if (not isExcept):
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

def createTrie():
    rawTerminal = ["<html", "<head", "<body", "<title", "<link", "<img", "<script", "<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<p", "<br", "<em", "<b", "<abbr", "<strong", "<small", "<hr", "<div", "<a", "<button", "<form", "<input", "<table", "<tr", 
                "<td", "<th", "</html", "</head", "</body", "</title", "</link", "</img", "</script", "</h1", "</h2", "</h3", "</h4", "</h5", "</h6", "</p", "</br", "</em", "</b", "</abbr", "</strong", "</small", "</hr", "</div", "</a", "</button", "</form", "</input", "</table", "</tr", 
                "</td", "</th", "<!--", "-->", "id", "class", "style", "src", "alt", "script", "rel", "href", "type", "action", "method", "GET", "POST", "text", "password", "email", "number", "checkbox", "submit", "reset", "button", "anyText", "A", "B", "C", "D", "E","F", "G", "H", "I","J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a" "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ">", "1", "2", "3", "4", "5", "6", "7", 
                "8", "9", "0", " ", "\n", "\t", "!", "-", "_", "@", "$", "#", "%", "^", "&", "*", "(", ")", "~", "'", "\"", ";", ":", "[", "]", "{", "}", "|", "+", "\\", "?", ",", ".", "="]
    for t in rawTerminal:
        T.insertToken(t)

def parseToken(parsed):
    tokenList = []
    for p in parsed:
        i = 0
        j = len(p)
        while (i != len(p)):
            if (T.searchToken(p[i:j])):
                tokenList.append(p[i:j])
                i = j
                j = len(p)
            else:
                j -= 1
    return tokenList

def startTokenize(path):
    htmlString = readhtmlFile(path)
    htmlAnyText = convertAnyText(htmlString)
    htmlParsed = parseString(htmlAnyText)
    createTrie()
    tokenList = parseToken(htmlParsed)
    return tokenList