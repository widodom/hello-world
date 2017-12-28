

def foo():
    print('foo is running')

    print("more print statements")
    print('and more')


print('dangling')


def bar():
    print('bar is running')
    print('still in bar')
    print('bar still running')


bar()
foo()
