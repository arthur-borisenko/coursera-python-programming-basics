def sign(x):
    # returns sign :D
    if x<0:
        return -1
    elif x==0:
        return 0
    else:
        return 1
def main():
    x=int(input())
    print(sign(x))
if __name__ == '__main__':
    main()