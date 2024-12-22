import sys
import math

def is_float(value):
    try:
        float(value)
        return False  
    except ValueError:
        return True  

def get_coef(index, text):
    try:
        coef_s = sys.argv[index]             
    except:
        print(text)
        coef_s = input()
        while is_float(coef_s):
            coef_s = input()
    coef = float(coef_s)
    return coef


def get_roots(a, b, c):
    roots = []
    if a == 0:
        if b == 0:
            return roots
        else:
            if (-c/b) < 0:
                roots.append(math.sqrt(math.sqrt((-1)*(-c/b))))
                roots.append((-1)*roots[0])
            else:
                roots.append(math.sqrt(math.sqrt(-c/b)))
                roots.append((-1)*roots[0])
            return roots
    else:
        D = b**2 - 4*a*c
        if D == 0.0:
            if (-b / (2.0*a)) < 0:
                roots.append(math.sqrt((-1)*(-b / (2.0*a))))
                roots.append((-1)*roots[0])
            else:
                roots.append(math.sqrt(-b / (2.0*a)))
                roots.append((-1)*roots[0])    
        elif D > 0:
            if ((-b + math.sqrt(D)) / (2.0*a)) < 0:
                roots.append(math.sqrt((-1)*(-b + math.sqrt(D)) / (2.0*a)))
                roots.append((-1)*roots[0])
            else:
                roots.append(math.sqrt((-b + math.sqrt(D)) / (2.0*a)))
                roots.append((-1)*roots[0])
            if ((-b - math.sqrt(D)) / 2.0*a) < 0:
                roots.append(math.sqrt((-1)*(-b - math.sqrt(D)) / (2.0*a)))
                roots.append((-1)*roots[2])
            else:
                roots.append(math.sqrt((-b - math.sqrt(D)) / (2.0*a)))
                roots.append((-1)*roots[2])
            
    return roots

def main():
    a = get_coef(1, "Введите коэффициент A: ")
    b = get_coef(2, "Введите коэффициент B: ")
    c = get_coef(3, "Введите коэффициент C: ")

    roots = get_roots(a, b, c)

    if len(roots) == 0:
        print("Действительных корней нет")
    elif len(roots) == 2:
        print("x1 =", roots[0])
        print("x2 =", roots[1])
    else:
        print("x1 =", roots[0])
        print("x2 =", roots[1])
        print("x3 =", roots[2])
        print("x4 =", roots[3])

if __name__ == "__main__":
    main()
