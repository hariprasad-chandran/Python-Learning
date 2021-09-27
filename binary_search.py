# program to find an element in the list using binary search.

pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1



list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]  # example list
n = 99  # n is the element which we have to find in the list

if search(list, n):
    print("Found at", pos + 1)
else:
    print("Not found")
