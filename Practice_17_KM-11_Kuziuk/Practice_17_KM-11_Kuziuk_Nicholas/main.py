from factorial.factorial import *

from logarithm.logarithm import *

from exp_root.exponentiation import *
from exp_root.root import *


def main():
    print("""
    Please, choose the function:
    factorial - 1
    exp2 - 2
    exp3 - 3
    root2 - 4
    root3 - 5
    log - 6
    ln - 7
    lg - 8
    """)
    n = int(input(">>\033[32m"))
    if n == 1 :
        try:
            print(fact(int(input("For x! input x: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    elif n == 2 :
        try:
            print(exp2(float(input("For x^2 input x: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    elif n == 3 :
        try:
            print(exp3(float(input("For x^3 input x: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    elif n == 4 :
        try:
            print(root2(float(input("For √x input x: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    elif n == 5 :
        try:
            print(root3(float(input("For ∛x input x: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    elif n == 6 :
        try:
            print(log(float(input("For log[a] b input a: ")), float(input("For log[a] b input b: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    elif n == 7 :
        try:
            print(ln(float(input("For ln b input b: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    elif n == 8 :
        try:
            print(lg(float(input("For lg b input b: "))))
        except:
            print("\033[1m\033[31mError!\033[0m")
    else:
        print("\033[1m\033[31mTakyi variant vidpovidi vidsutniy")
if __name__ == '__main__':
    main()