def SelectionSort(my_list):
    print(my_list)
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1,len(my_list)):
            #print(i,j)
            if my_list[min_index] > my_list[j]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
        #print(my_list)
    print(my_list)

SelectionSort([2,6,1,5,4,7,3])