def ft_water_reminder():
   
    water = int(input("Days since last watering: "))
    F = "Water the plants!"
    print(F * (water > 2))

    water = int(input("Days since last watering: "))
    T = "Plants are fine"
    print(T * (water < 2))


ft_water_reminder()