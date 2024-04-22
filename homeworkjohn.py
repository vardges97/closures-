# def counter(initial_value=0):
#     initialcount = initial_value
#
#     def increment(valu=1):
#         nonlocal initialcount
#         initialcount+=valu
#
#     def decrement(val=1):
#         nonlocal initialcount
#         initialcount-=val
#
#     def getval():
#         return initialcount
#     return increment,decrement,getval
#
# increment,decrement,getval = counter(10)
#
# counter()
# increment(10)
# decrement(15)
# print(getval())
#
#
# def outer(n):
#     def inner(m):
#         return n+m
#     return inner
#
# x=outer(5)
# print(x(6))
#
# def power_of(n):
#     def muller(m):
#         return n**m
#     return muller
# y = power_of(5)
# print(y(3))

def memorize(func):
    cache={}
    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            func[args] = cache[args]
    return inner

@memorize
def muller(n):
    res = n ** 2
    return res

print(muller(5))
print(muller(15))
print(muller(6))
print(muller(15))

def counter(foo):
    def inner(*args,**kwargs):
        inner.calls = 0
        return foo(*args,**kwargs)
        inner.calls += 1
        print(inner.calls)
    return inner


def idcontrol(id):
    access = 1234
    def inner():
        if access == id:
            print('access granted may proceed')
        else:
            print('wrong id try again')
    return inner

def counter(foo):
    def inner(*args,**kwargs):
        x = None
        inner.calls = 0
        if inner.calls > x:
            print("exceeded function calls cant continue")
        return foo(args,kwargs)
        inner.calls += 1
    return inner