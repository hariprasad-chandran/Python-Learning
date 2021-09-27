# program to find an element in the list using linear search

def search(list, n):
    i = 0

    for i in range(0, len(list), 1):
        if list[i] == n:
            return True

    return False


list = [4, 67, 34, 56, 76, 5, 7, 8, 9, 0]  # example list
n = 76  # n is the element which we have to find in the list

if search(list, n):
    print("Found")
else:
    print("Not found")
