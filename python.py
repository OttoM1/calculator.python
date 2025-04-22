import random
import python
import re




def calculate(e: str) -> float:
    t = re.findall(r'\d+\.?\d*|[+\-*/xX:]', e)
    if not t:
        raise ValueError("Error!")




    nt = []
    c = float(t[0])

    i = 1
    while i < len(t):
        o = t[i]
        n = float(t[i+1])
        if o in ('*', 'x', 'X'):
            c = c * n
        elif o in ('/', ':'):
            c = c / n
        else:
            nt.append(c)
            nt.append(o)
            c = n
        i += 2
    nt.append(c)




    r = nt[0]
    i = 1
    while i < len(nt):
        o = nt[i]
        num = nt[i+1]
        if o == '+':
            r += num
        elif o == '-':
            r -= num
        i += 2

    return r





if __name__ == '__main__':
    print("'exit' to quit)\n")
    while True:
        e = input("Enter calculation: ").strip()
        if e.lower() in ('exit', 'quit'):
            print("Bye!")
            break
        try:
            a = calculate(e)
            print(":", a, "\n")
        except Exception as e:
            print("Error! ", e, "\n")