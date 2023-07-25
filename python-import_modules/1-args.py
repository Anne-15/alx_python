import sys

def print_arguments():
    num_arguments = len(sys.argv)-1
    if num_arguments == 0:
        print("Number of arguments: .")
        return
    print("Number of arguments: .",num_arguments)
    print("Arguments:")
    for j, arg in enumerate(sys.argv[1:],start=1):
        print("{}:{}".format(j,argv))
if __name__ == '__main__':
    print_arguments()
