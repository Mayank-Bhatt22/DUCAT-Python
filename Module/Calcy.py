def add(*n):
    return sum(n)

def sub(a=0,b=0):
    return a-b

def multiply(*n):
    p=1
    for i in n:
        p *=i
    return p
