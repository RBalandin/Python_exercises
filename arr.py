

def bubble_sort(arr=None):
    if not arr:
        return list()

    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    l = [99, 55, 1, 7, 25, 66, 128, 137, 129, 2, 3, 5, 34, 235, 345, 1, 23, 34, 52, 53, 55, 2, 12, 8]
    print(bubble_sort(l))
