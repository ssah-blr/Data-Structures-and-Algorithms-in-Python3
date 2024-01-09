def InsertionSort(my_list):
    print(my_list)

    for i in range(1,len(my_list)):        
        temp = my_list[i]
        j = i -1
        #print(j,i)
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
        #print(my_list)

    print(my_list)

InsertionSort([2,6,1,5,4,7,3])