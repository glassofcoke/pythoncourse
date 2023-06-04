import _collections_abc as c

print(isinstance([],c.Iterable))
print(isinstance('abc', c.Iterable))
print(isinstance(100,c.Iterable))

l = [1,2,3,4,5]
l_iter = iter(l)
print(type(l_iter))
a = next(l_iter)
print(a)

#Generator
#use yield statement to construct a generator for fibonacci sequence

def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2 , num1+num2
        current += 1
        yield num
    yield "done"

g = fib(8)
for x in g:
    print(x)


def decorate(func):
    def decorated():
        print("I got decorated")
        func()
    return decorated
@decorate
def plain():
    print("I am plain")
plain()