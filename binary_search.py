def search(arr, x):
    print(arr, x)
    a = 0
    b = len(arr) - 1
    while a <= b:
        mid = ((b - a) // 2) + a
        if x > arr[mid]:
            a = mid + 1
        else:
            b = mid - 1
    return a,b

print(search([10,12,14], 9))
print(search([10,12,14], 10))
print(search([10,12,14], 11))
print(search([10,12,14], 12))
print(search([10,12,14], 13))
print(search([10,12,14], 14))
print(search([10,12,14], 15))
