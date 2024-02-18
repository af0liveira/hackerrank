def swap_case(s):
    """Swap cases of the input string s
    In other words, convert all lowercase letters to uppercase and vice versa.
    """
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
