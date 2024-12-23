import sys
import math

def is_float(value):
    try:
        float(value)
        return False  
    except ValueError:
        return True  

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

def solve_quadratic(a, b, c):
    return get_roots(a, b, c)