def factR(n):
    if n == 1:
        return n
    else:
        return n * factR(n-1)

if __name__ == "__main__":
    test_number = 3
    result = factR(test_number)
    print('{0}の階乗は{1}です。'.format(test_number,result))
