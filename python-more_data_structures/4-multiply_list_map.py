def multiply_list_map(my_list=[], number=0):
    def numList(num):
        return num * number
    new_list=[]
    for i in my_list:
        mlist = map(numList, i)
        new_list.append(mlist)
    return new_list
