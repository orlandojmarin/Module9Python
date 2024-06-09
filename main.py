# Write a code that defines a function ‘fun(a)' that calculates b based on the 
# input a. If a is less than 4, it attempts a division by zero, causing a 
# ‘ZeroDivisionError'. The code calls fun(3) and fun(5) inside a try-except 
# block. It handles the ZeroDivisionError for fun(3) and prints 
# “ZeroDivisionError Occurred and Handled.” The ‘NameError' block is not 
# executed since there are no ‘NameError' exceptions in the code.

def fun(a):
    if (a < 4):
        b = a / 0
    print("The Value of b is " + b)


try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
