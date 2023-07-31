from callLimit import callLimit
# We then use the @callLimit(3) syntax as a decorator
# on the f() function. This is equivalent
# to writing f = callLimit(3)(f).
# So first we will call the callLimit(3) this will
# return callLimiter function then we call
# callLimiter(f) this will return limit_function
# now in the for loop when you call f()
# it will actually call the limit_function()


@callLimit(3)
def f(*args: any):
    print(f"f(): {sum(args)}")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f(1, 2, 3)
    g()
