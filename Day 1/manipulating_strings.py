#this code
n = int(input())

words =[]

for i in range(0, n):
    st= input()
    words.append(st)

for i in range(0, n):
    for j in range(0, len(words[i]), 2):
        print(words[i][j],end='')
    print(end=' ')
    
    for j in range(1,len(words[i]), 2):
        print(words[i][j],end='')
    print()