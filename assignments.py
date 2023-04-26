import string


def count():
    a = input('string').split(sep=' ')
    count=0
    for i in a:
        j=str(i)
        count += len(j)
    print(count)

def case():
    a = input('string').split(sep=' ')
    countuc,countlc=0,0
    for i in a:
        j=str(i)
        for k in j:
            if k in list(string.ascii_uppercase):
                countuc+=1
            elif k in list(string.ascii_lowercase):
                countlc+=1
    print(f'Uppercase: {countuc}')
    print(f'Lowercase: {countlc}')

def val():
    a = int(input('Number'))
    val = a+int(2*str(a))+int(3*str(a))+int(4*str(a))
    return val

def listcomp():
    a=input('numbers').split(',')
    li = list(int(i)*int(i) for i in a if (int(i))%2!=0)
    return li

def netAmount():
    a=input('Transactions')
    net=0
    print(a)
    for i in a:
        if i[0]=='D':
            net+=int(i[1])
        elif i[0]=='W':
            net-=int(i[1])
    return net




