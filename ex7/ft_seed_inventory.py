def ft_seed_inventory(seed :str, quantity:int, unit:str):
    
    capitalized_seed = seed.capitalize()

    if unit == "packets":
        print(f"{capitalized_seed} seeds:  {quantity} packets available ")

    if unit == "grams":
        print(f"{capitalized_seed} seeds:  {quantity} grams total ")

    if unit == "area":
        print(f"{capitalized_seed} seeds: covers {quantity} square meters ")

ft_seed_inventory("carrot", 20, "grams")