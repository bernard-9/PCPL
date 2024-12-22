using System;

double get_coef(string text){
    Console.WriteLine(text);
    double coef = 0;
    bool result = false;
    while(!result){
        string? input = Console.ReadLine();
        result = double.TryParse(input, out coef);
    }
    return coef;
}

static double [] get_roots(double a, double b, double c, ref int i){
    double[] roots = { 0, 0, 0, 0 };
    i = 0;
    if (a == 0){
        if (b == 0){
            return roots;
        }
        else{
            if ((-c/b) < 0){
                roots[i] = Math.Sqrt(Math.Sqrt((-1) * (-c / b)));
                roots[++i] = (-1)*roots[i - 1];
            }
            else{
                roots[i] = Math.Sqrt(Math.Sqrt((-c / b)));
                roots[++i] = (-1) * roots[i - 1];
            }
            return roots;
        }
    }
    else{
        i = 0;
        double D = Math.Pow(b, 2) - 4*a*c;
        if (D == 0.0){
            if ((-b / (2.0*a)) < 0){
                roots[i] = Math.Sqrt((-1) * (-b / (2.0 * a)));
                roots[++i] = (-1)*roots[i - 1];
            }
            else{
                roots[i] = Math.Sqrt(-b / (2.0 * a));
                roots[++i] = (-1)*roots[i - 1];
            }
        }
        else if (D > 0){
            i = 0;
            if (((-b + Math.Sqrt(D)) / (2.0 * a)) < 0){
                roots[i] = Math.Sqrt((-1) * (-b + Math.Sqrt(D)) / (2.0 * a));
                roots[++i] = (-1)*roots[i - 1];
            }
            else{
                roots[i] = Math.Sqrt((-b + Math.Sqrt(D)) / (2.0 * a));
                roots[++i] = (-1)*roots[i - 1];
            }
            if (((-b - Math.Sqrt(D)) / (2.0 * a)) < 0){
                roots[++i] = Math.Sqrt((-1) * (-b - Math.Sqrt(D)) / (2.0 * a));
                roots[++i] = (-1)*roots[i - 1];
            }
            else{
                roots[++i] = Math.Sqrt((-b - Math.Sqrt(D)) / (2.0 * a));
                roots[++i] = (-1)*roots[i - 1];
            }
        }
    }
    return roots;
}

void main(){
    double a = get_coef("Введите коэффициент A: ");
    double b = get_coef("Введите коэффициент B: ");
    double c = get_coef("Введите коэффициент C: ");
    int i = 0;
    double [] ans_roots = get_roots(a, b, c, ref i);
    if (i == 0){
        Console.WriteLine("Действительных корней нет");
    }
    else if (i == 1){
        Console.WriteLine("x1 = " + ans_roots[0]);
        Console.WriteLine("x2 = " + ans_roots[1]);
    }
    else{
        Console.WriteLine("x1 = " + ans_roots[0]);
        Console.WriteLine("x2 = " + ans_roots[1]);
        Console.WriteLine("x3 = " + ans_roots[2]);
        Console.WriteLine("x4 = " + ans_roots[3]);
    }
}

main();

