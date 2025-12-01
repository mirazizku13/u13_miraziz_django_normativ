def foo():
    print("begin")
    for i in range(3):
        print("before yield")
        yield i
        print("after yild", i)
    print("end")

f = foo()

print(next(f))
print(next(f))
print(next(f))
print(next(f))

