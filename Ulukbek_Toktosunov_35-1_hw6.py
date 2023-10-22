def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  #возвр отсортированный список

# Пример использования:
my_list = [64, 245, 12, 222, 13]
sorted_list = bubble_sort(my_list)
print("Отсортированный список:", sorted_list)


def binary_search(a,value):
    n = len(a)
    first, last = 0, n-1
    while first <= last:
        middle = (first + last) // 2
        if a[middle] == value:
            print('Элемент найден')
            print(middle)
            first = last + 1
        elif a[middle] < value:
            first = middle + 1
        else:
            last = middle - 1
    print('Элемент не найден')

#example:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 15
binary_search(my_list, target)








