result = []
states = []
stack = []
symbols = []

def isIn(arr, x):
    ada = False
    i = 0
    
    while i < len(arr) and not ada:
        if(arr[i] == x):
            ada = True
        i+=1
    
    return ada

source = 'trans.txt'
f = open(source, 'r')
s = f.readline()

while s != '.':
    n = len(s)
    res = ""
    i = 1
    while(i < n):
        if(s[i] == ','):
            res += ' '
            i+=1
        elif(s[i] == ')'):
            if(s[i+1] == '}'):
                i = n
            else: 
                i+=5
                res += ' '
        else:
            res+=s[i]
        i+=1 
    result.append(res)
    s = f.readline()
    
f.close()

for i in range(len(result)):
    h = result[i]
    j = 0
    space = 0
    temp = ''
    while j < len(h):
        if(h[j] == ' '):
            if(space == 0 or space == 3):
                if(not isIn(states, temp)):
                    states.append(temp)
            elif(space == 1):
                if(not isIn(symbols, temp)):
                    symbols.append(temp)
            else:
                if(not isIn(stack, temp)):
                    stack.append(temp)
            space += 1
            temp = ''
        else:
            temp += h[j]
        
        j+=1
    

# print("Result : ")
# for i in range(len(result)):
#     print(result[i])
# print("State : ")
# for i in range(len(states)):
#     print(states[i])
# print("Symbols : ")
# for i in range(len(symbols)):
#     print(symbols[i])
# print("Stack : ")
# for i in range(len(stack)):
#     print(stack[i])

strstate = ""
for i in range(len(states)):
    strstate += states[i]
    if(i != len(states) - 1):
        strstate += " "
strsymbols = ""
for i in range(len(symbols)):
    strsymbols += symbols[i]
    if(i != len(symbols) - 1):
        strsymbols += " "
strstack = ""
for i in range(len(stack)):
    strstack += stack[i]
    if(i != len(stack) - 1):
        strstack += " "

result.insert(0, strstack)
result.insert(0, strsymbols)
result.insert(0, strstate)

dest = 'res.txt'

f = open(dest, 'w')
i = 0
while i < len(result):
    f.write(result[i] + '\n')
    i+=1
    
f.close()
