# Funtion to Merge Sorted Lists
def Merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1
    #print('-',combined)
    return combined

# Use the Merge Function on Sorted Lists
print(Merge([1,3,7,8],[2,4,5,6]))

# Main Recursion Function to divide the Lists and call Merge

def Merge_Sort(my_list):
    #print(my_list)
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]

    return Merge(Merge_Sort(left),Merge_Sort(right))

List = [3,1,4,5,8,2,7,6,10,9,11]

Sorted_List = Merge_Sort(List)

print(List)
print(Sorted_List)









