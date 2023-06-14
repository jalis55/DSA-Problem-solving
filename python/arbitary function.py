# arbitary arguments
def greeting(*args):
    print(args)


greeting('a',[1,2],2.55)

#keyword arbitary arguments

def say_hello(**kwargs):
    print(kwargs)

say_hello(name="abc",age=55)
