if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)
    max_arr = max(arr)
    for i in arr:
        if i < max_arr:
            print(i)
            break
