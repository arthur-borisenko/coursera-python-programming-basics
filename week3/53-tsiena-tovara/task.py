def main():
    price = float(input())
    rub = int(price)
    kop = int(round(price - rub, 2) * 100)
    print(rub, kop)


if __name__ == '__main__':
    main()
