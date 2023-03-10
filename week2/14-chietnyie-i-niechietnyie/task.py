def main():
    inputList = [int(input()), int(input()), int(input())]
    chetnoeExists = False
    nechotnoeExists = False
    for number in inputList:
        if number % 2 == 0:
            chetnoeExists = True
        else:
            nechotnoeExists = True
    if chetnoeExists and nechotnoeExists:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
