array = [2,1,5,4,3]
def bubbleSort(array):
    lenghtOfArray = len (array) - 1
    for i in range(lenghtOfArray):
        for j in range(lenghtOfArray-i):
             if array[j] < array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array
print(bubbleSort(array))