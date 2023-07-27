def multiply_list_map(my_list=[], number=0):
    new_list=[]
    for i in my_list:
        mlist = map((lambda x: x*number),i)
        new_list.append(mlist)
    return new_list
