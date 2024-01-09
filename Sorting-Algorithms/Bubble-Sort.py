def BubbleSort(my_list):
    print(my_list)
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    print(my_list)

BubbleSort([2,6,1,5,4,3])