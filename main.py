


<<<<<<< HEAD
def function(n):

    if n % 2 != 0:
        print('weird')
    elif n % 2 == 0 and n in range(2, 5):
        print('not weird')
    elif n % 2 == 0 and n in range(6, 20):
        print('weird')
    else:
        print('not weird')
    # elif n % 2 == 0 and n > 20:
    #     print('not weird')
    return n

while True:
    n = int(input('enter the number: '))
    function(n)


def fun(a, b):
    n1 = a+b
    n2 = a-b
    n3 = a*b
    return n1,n2,n3
x=int(input())
y=int(input())
print(fun(x,y))

def plus_minus(arr):
    arr_len = len(arr)
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print('%.6f' % (pos/arr_len))
    print('%.6f' % (neg/arr_len))
    print('%.6f' % (zero/arr_len))


n = [1, 1, 0, -1, -1]
# arr = list(map(int, input().rstrip().split()))
plus_minus(n)

def min_max_sum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]), sum(arr[1:]))


n = [1, 2, 3, 4, 5]
min_max_sum(n)



def covert_time(str1):
    if str1[-2:] == 'AM' and str1[:2] == '12':
        return '00'+str1[2:-2]
    elif str1[-2:] == 'AM':
        return str1[:-2]
    elif str1[-2:] == 'PM' and str1[:2] == '12':
        return str1[:-2]
    else:
        return str(int(str1[:2])+12) + str1[2:8]


time = '12:34:23 PM'
print(covert_time(time))




from collections import Counter
def matching_strings(strings,queries):
    s = Counter(strings)
    res =[]
    for q in queries:
        res.append(s[q])
    return res



strings = ['ab', 'abc', 'bc']
queries = ['ab', 'abc', 'rm']
print(matching_strings(strings, queries))


def single_number(arr, n):
    res = arr[0]
    for i in range(1,n):
        res ^= arr[i]
    return res


ar = [1, 1, 2, 2, 3, 5, 5]
print(single_number(ar, len(ar)))



def square_matrix(arr,n):

    d1 = 0
    d2 = 0
    for i in range(0,n):
       d1 += arr[i][i]
       d2 += arr[i][len(arr)-1-i]
    return abs(d1-d2)


arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]
print(square_matrix(arr, len(arr)))
=======
# def function(n):
#
#     if n % 2 != 0:
#         print('weird')
#     elif n % 2 == 0 and n in range(2, 5):
#         print('not weird')
#     elif n % 2 == 0 and n in range(6, 20):
#         print('weird')
#     else:
#         print('not weird')
#     # elif n % 2 == 0 and n > 20:
#     #     print('not weird')
#     return n
#
# while True:
#     n = int(input('enter the number: '))
#     function(n)


# def fun(a, b):
#     n1 = a+b
#     n2 = a-b
#     n3 = a*b
#     return n1,n2,n3
# x=int(input())
# y=int(input())
# print(fun(x,y))

# def plus_minus(arr):
#     arr_len = len(arr)
#     pos = 0
#     neg = 0
#     zero = 0
#
#     for i in arr:
#         if i > 0:
#             pos += 1
#         elif i < 0:
#             neg += 1
#         else:
#             zero += 1
#     print('%.6f' % (pos/arr_len))
#     print('%.6f' % (neg/arr_len))
#     print('%.6f' % (zero/arr_len))
#
#
# n = [1, 1, 0, -1, -1]
# # arr = list(map(int, input().rstrip().split()))
# plus_minus(n)

# def min_max_sum(arr):
#     arr = sorted(arr)
#     print(sum(arr[:-1]), sum(arr[1:]))
#
#
# n = [1, 2, 3, 4, 5]
# min_max_sum(n)

# def covert_time(str1):
#     if str1[-2:] == 'AM' and str1[:2] == '12':
#         return '00'+str1[2:-2]
#     elif str1[-2:] == 'AM':
#         return str1[:-2]
#     elif str1[-2:] == 'PM' and str1[:2] == '12':
#         return str1[:-2]
#     else:
#         return str(int(str1[:2])+12) + str1[2:8]
#
#
# time = '12:34:23 PM'
# print(covert_time(time))

# from collections import Counter
# def matching_strings(strings,queries):
#     s = Counter(strings)
#     res =[]
#     for q in queries:
#         res.append(s[q])
#     return res
#
#
#
# strings = ['ab', 'abc', 'bc']
# queries = ['ab', 'abc', 'rm']
# print(matching_strings(strings, queries))


# def single_number(arr, n):
#     res = arr[0]
#     for i in range(1,n):
#         res ^= arr[i]
#     return res
#
#
# ar = [1, 1, 2, 2, 3, 5, 5]
# print(single_number(ar, len(ar)))
#

# def square_matrix(arr,n):
#
#     d1 = 0
#     d2 = 0
#     for i in range(0,n):
#        d1 += arr[i][i]
#        d2 += arr[i][len(arr)-1-i]
#     return abs(d1-d2)
#
#
# arr = [[11, 2, 4],
#        [4, 5, 6],
#        [10, 8, -12]]
# print(square_matrix(arr, len(arr)))

def factorial(n):
    assert n>=0 and int(n)==n, 'the number must be positive!'
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
>>>>>>> fa8fb7d (Initial commit)

















