
# In your original code, the issue lies in the fact that you
# ('re modifying the list (list) while iterating over it. When '
#  'you remove an element from the list, it changes the indices of '
#  'subsequent elements. As a result, when you iterate over the modified list,'
#  you might skip or miss elements or encounter unexpected behavior.)

def unique(list=[]):
    list_x=list
    for x in list:
        ind= list.index(x)
        # print (x, ind)
        list2= list[ind+1:]
        print ("List for compare is:", list2)
        for y in list2:
            if x ==y:
                print ("Match", x,list.index(x), y, list.index(y))
                list_x.remove(y)
    print (list_x)

unique(['9','b','pp','bp','bpp','f','b'])



