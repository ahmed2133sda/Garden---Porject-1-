def ft_count_harvest_recursive(current: int, target:int) -> None:
    if current > target:
        print("Harvest time!")
    else:
        print("day " + str(current))
        ft_count_harvest_recursive(current + 1, target)

ft_count_harvest_recursive(1, int(input("Days until harvest: ")))