def print_arguments(*args):
    def check(a):
        print(len(args))
        if(len(args) == 0):
            print(".")
        else:
            index = 1
            for n in args:
                print(index, ":", n)
                index += 1
    return check(args)
