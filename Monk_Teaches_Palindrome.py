t=int(input())

for i in range(t):

    s=input()

    if s!=s[::-1]:

        print('NO')

    elif(len(s)%2==0):

        print('YES EVEN')

    else:

        print('YES ODD')