def ft_count_harvest_recursive(day):
    if day <= 0:
        return
    
    ft_count_harvest_recursive(day - 1)
    
    print("day " + str(day))

user_days = int(input("Days until harvest: "))
ft_count_harvest_recursive(user_days)