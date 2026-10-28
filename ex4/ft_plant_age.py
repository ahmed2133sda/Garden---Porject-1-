def ft_plant_age():
   
    age = int(input("Enter plant age in days: "))
    ready = "Plant is ready to harvest!"
    print(ready * (age > 60)) # يفضح عرضها قد ما اخذت منعي وقت هاي

    age = int(input("Enter plant age in days: "))
    Nready = "Plant needs more time to grow."
    print(Nready * (age < 60))


ft_plant_age()