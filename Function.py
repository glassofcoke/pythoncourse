#FUCTION STATEMENT

def myFunction(a, b):   # parameters A & B in the Parentheses
    c = a * b
    c = c + 1
    return c            #returns the Output

print(myFunction(10 , 10))


#High-Order Function

def loud(text):
    return text.upper() + "!!"
def quiet(text):
    return text.lower() + "..."
def speak(func, text):
    words = func(text)
    print(words)

speak(loud,"python is cool")
speak(quiet,"PYTHON IS COOL")

# ANONYMOUS FUNCTION

oldList = [1,2,3,4,5]

newList = list(filter(lambda x: (x%2==0), oldList))
print(newList)

def fibs(num):
    result = [0 , 1]
    for i in range(2,  num):
        a = result[i - 1] + result[i - 2]
        result.append(a)
    return result
print(fibs(7))
