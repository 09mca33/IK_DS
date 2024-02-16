def lumotos_helper(arr, start, end):
    if start >= end:
        return

    green = start

    for red in range(start + 1, end + 1):
        if arr[start] > arr[red]:
            green = green + 1
            arr[green],arr[red] = arr[red],arr[green]

    arr[start], arr[green] = arr[green], arr[start]

    lumotos_helper(arr,start, green - 1)
    lumotos_helper(arr, green + 1, end)


arr = [2,3,1,5,8,7,6]
# print(arr)
lumotos_helper(arr, 0, len(arr) - 1)
print(arr)
