def counting(arr):
    maxValue = max(arr)
    count = [0]*(maxValue+1)

    while len(arr) > 0 :
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = counting(unsortedArr)
print("Sorted array:", sortedArr)