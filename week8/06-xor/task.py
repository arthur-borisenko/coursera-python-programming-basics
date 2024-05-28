print(*map(
    lambda el: el * "1" + (not el) * "0",
    map(lambda el: (el[0] or el[1]) and not
                   (el[0] and el[1]),
        zip(
            map(
                lambda el: el == "1",
                input().split()
            ),
            map(
                lambda el: el == "1",
                input().split()
            )
        )
        )
)
      )
