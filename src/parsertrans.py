result = []

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

# for i in range(len(result)):
#     print(result[i])

dest = 'res.txt'

f = open(dest, 'w')
i = 0
while i < len(result):
    f.write(result[i] + '\n')
    i+=1
    
f.close()
