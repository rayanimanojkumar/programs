import math
#bubblesort
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


# blist = [4, 9, 5, 8, 3, 1, 0, 7, 6, 2]
# bubble_sort(blist)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


# slist = [64, 25, 12, 22, 11]
# selection_sort(slist)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)


# slist = [64, 25, 12, 22, 11]
# insertion_sort(slist)
import math


# Python3 program to sort an array
# using bucket sort
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b





def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')

    print()




# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print('given array is:', end='\n')
#     printlist(arr)
#     merge_sort(arr)
#     print('sorted array is:', end='\n')
#     printlist(arr)


def partition(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quick_sort(start, end, arr):
    if start < end:
        p = partition(start, end, arr)

        quick_sort(start, p-1, arr)
        quick_sort(p+1, end, arr)

# arr = [12, 11, 13, 5, 6, 7]
# quick_sort(0, len(arr)-1, arr)
# print(f'sorted array: {arr}')



def heapify(arr, n, i):
    smallest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)

    for i in range(int(n//2)-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    arr.reverse()


hlist = [12, 11, 13, 5, 6, 7]
heap_sort(hlist)
print(hlist)









