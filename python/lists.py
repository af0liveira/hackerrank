if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        cmd, *args = input().split()
        args = [int(a) for a in args]
        match cmd:
            case 'insert':
                arr.insert(*args)
            case 'print':
                print(arr)
            case 'remove':
                arr.remove(*args)
            case 'append':
                arr.append(*args)
            case 'sort':
                arr.sort()
            case 'pop':
                arr.pop()
            case 'reverse':
                arr.reverse()
            case _:
                print(f"Invalid list method: {cmd}")