import sys

if __name__=="__main__":

    num_arguments = len(sys.argv) - 1
    if(num_arguments == 0):
        print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}", end='.')
    else:
        print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}", end='')

    if num_arguments > 0:
        print(":", end='')
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"\n{i}: {arg}", end='')

    # Add a new line
    print()
