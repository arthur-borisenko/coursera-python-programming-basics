def main():
    res = []
    for n in range(10, 100):
        if (n // 10) * (n % 10) * 2 == n:
            res.append(n)
    print(*res)


if __name__ == "__main__":
    main()
