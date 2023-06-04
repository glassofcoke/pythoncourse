#Syntax error
#this is invalid syntax

#Division by zero
#print(1/0)

#Try-except statement
"""
try:
    print(1/0)
except Exception as e:
    print(e)
finally:
    print("Tried to divide 1 by 0")

#TRY-EXCEPT STATEMENT WITH INPUT
a = input()
try:
    b = [ i for i in range(int(a))]
    print(b[4]/0)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Value error")
except IndexError:
    print("List index out of range")
finally:
    print("i love big fat titties. I love deep vaginas!")


#Custom Exception
class MyError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self) #Initialize parent class
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

#Throw an Exception
raise MyError("My Exception! ")
"""
"""
#Assertion Error Statement
#def func(a,b):
    #assert a==b #if a!=b, python throws an exception
func(1,2)
"""
