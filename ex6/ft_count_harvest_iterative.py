def ft_count_helper() -> None:

    day = int(input("Days until harvest: "))
    for days in range(1, day + 1):
        print("day " + str(days))
    print("Harvest time!")
ft_count_helper()

