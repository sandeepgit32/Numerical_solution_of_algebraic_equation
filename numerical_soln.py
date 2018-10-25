import math

# The equation to be solved is written in form f(x) = 0
def f(x):
    return x**3-3*x**2-7

def f_(x):
    # The derivative of f(x)
    return 3*x*2-6*x

def main():
    print('Type \'b\' for \'Bisection method\' \nType \'s\' for \'Secant method\' \nType \'n\' for \'Newton Raphson method\' \n\
Type \'r\' for \'Regula Falsi method\'\n')
    sel = input('Type : ')
    tol = 0.0001
    while sel != 'b' and sel != 's' and sel != 'n' and sel != 'r':
        print('Wrong character typed')
        sel = input('Type again: ')
    if sel == 'b':
        print('Solution = ', bisection_method(tol))
    if sel == 's':
        print('Solution = ', secant_method(tol))
    if sel == 'n':
        print('Solution = ', newton_raphson(tol))
    if sel == 'r':
        print('Solution = ', regulafalsi_method(tol))

def bisection_method(tol):
    print('Solution by Bisection method')
    print('~~~~~~~~~~~~~~~~~~~~~~')
    a = int(input('Type the value of initial guess a = '))
    b = int(input('Type the value of initial guess b = '))
    
    while f(a)*f(b) > 0:
        print('f(a) = ', f(a))
        print('f(b) = ', f(b))
        print('Solution cannot be found. Enter new values of a and b.')
        a = int(input('Type the value of initial guess a = '))
        b = int(input('Type the value of initial guess b = '))
    print('f(a) = ', f(a))
    print('f(b) = ', f(b))
    if f(a)*f(b) < 0:
        t = (a + b)/2
        error = abs(f(t))
        iteration_counter = 1;
        print('Iteration ',iteration_counter,': Value = ',t, ': Error = ', error)
        while error > tol:
            iteration_counter += 1
            if f(a)*f(t)>0: 
                a = t
            else:
                b = t          
            t = (a + b)/2
            error = abs(f(t))
            print('Iteration ',iteration_counter,': Value = ',t, ': Error = ', error)
    return t

def secant_method(tol):
    print('Solution by Secant method')
    print('~~~~~~~~~~~~~~~~~~~~~')
    x0 = int(input('Type the value of the first initial guess x0 = '))
    x1 = int(input('Type the value of the second initial guess x1 = '))
    iteration_counter = 0
    while abs(f(x1)) > tol and iteration_counter < 100:
        try:
            denominator = float(f(x1) - f(x0))/(x1 - x0)
            x = x1 - float(f(x1))/denominator
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
            sys.exit(1)     # Abort with error
        x0 = x1
        x1 = x
        iteration_counter += 1
        error = abs(f(x1))
        print('Iteration ', iteration_counter,': Value = ',x1, ': Error = ', error)
    return x1

def newton_raphson(tol):
    print('Solution by Newton Raphson method')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    x0 = int(input('Type the value of the first initial guess x0 = '))
    iteration_counter = 0
    error = abs(f(x0))
    if error <= tol:
        return x0
    while error >= tol and iteration_counter <= 100:
        x1 = x0 - (f(x0)/f_(x0))
        x0 = x1
        error = abs(f(x0))
        iteration_counter += 1
        print('Iteration ',iteration_counter,': Value = ',x1, ': Error = ', error)
    return x1

def regulafalsi_method(tol):
    print('Solution by Regula Falsi method')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    a = int(input('Type the value of initial guess a = '))
    b = int(input('Type the value of initial guess b = '))
    
    while f(a)*f(b) > 0:
        print('f(a) = ', f(a))
        print('f(b) = ', f(b))
        print('Solution cannot be found. Enter new values of a and b.')
        a = int(input('Type the value of initial guess a = '))
        b = int(input('Type the value of initial guess b = '))
    print('f(a) = ', f(a))
    print('f(b) = ', f(b))
    if f(a)*f(b) < 0:
        t = (a*f(b) - b*f(a))/(f(b) - f(a))
        error = abs(f(t))
        iteration_counter = 1;
        print('Iteration ',iteration_counter,': Value = ',t, ': Error = ', error)
        while error > tol:
            iteration_counter += 1
            if f(a)*f(t)>0: 
                a = t
            else:
                b = t          
            t = (a*f(b) - b*f(a))/(f(b) - f(a))
            error = abs(f(t))
            print('Iteration ',iteration_counter,': Value = ',t, ': Error = ', error)
    return t

if __name__ == "__main__":
    main()
