def pivot(arr,start,end):
    #print(arr,start,end)
    swap = start 
    for i in range(start+1,end+1):
        if arr[start] > arr[i]:
            swap += 1
            arr[i],arr[swap] = arr[swap],arr[i]
        #print(arr,swap)
    
    arr[start],arr[swap]=arr[swap],arr[start]
    print(arr,swap)
    return(swap)

def quick_sort(arr,left,right):    
    #print(arr)
    if left < right:
        pivot_index = pivot(arr,left,right)
        quick_sort(arr,left,pivot_index-1)
        quick_sort(arr,pivot_index+1,right)
    return arr


def quick_sort_main(arr):
    print(quick_sort(arr,0,len(arr)-1))

quick_sort_main([4,6,1,7,3,2,5])
