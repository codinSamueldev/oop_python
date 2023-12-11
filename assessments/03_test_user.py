
class Fighter():
    def __init__(self, name: str, power: float, technique: str):
        self.name = name
        self.power = power
        self.technique = technique

    def __add__(self, fighter):
        fighters_fusioned = self.power + fighter.power
        technique_fusioned = self.technique + fighter.technique
        return self.__class__(self.name + fighter.name, fighters_fusioned, technique_fusioned)


fighters = []

def generate_fighter():
    name = input("""
          Type new fighter's name: """).capitalize()
    power = float(input("""          Type power level: """))
    technique = input("""          Type fighter's technique: """).capitalize()

    return Fighter(name, power, technique)


def show_fighters(fighters_list):
    if fighters_list:
        for i, j in enumerate(fighters_list):
            print(f"""
          {i}. {j.name, j.power, j.technique}""")

# {j.name, j.power, j.technique}

def merge_fighters(fighter_one, fighter_two):
    for element in fighters:
        if element == fighters[fighter_one]:
            first_fighter_selected = element.power

        if element == fighters[fighter_two]:
            second_fighter_selected = element.power

    fighter_fusionated = first_fighter_selected + second_fighter_selected

    return fighter_fusionated



while True:
    print("""
          -----------//----------
          1. Create new fighter
          2. Show fighters created
          3. Merge fighters
          4. Exit Game""")
    
    try:
        choice = int(input("""
          Select option: """))
    except:
        print("""
          Invalid input""")
    
    if choice == 1:
        print(f"""
          ### Create ###""")
        new_fighter = generate_fighter()
        fighters.append(new_fighter)
        print(f"""
          Fighter created""")
        
    elif choice == 2:
        print(f"""
          ### Show ###""")
        if len(fighters) < 1:
            print("""
          No fighter created yet.""")
        else:
            show_fighters(fighters)

    elif choice == 3:
        print(f"""
          ### Fusion ###""")
        if len(fighters) < 2:
            print("""
          Sorry dude, you need more fighters.""")
        else:
            show_fighters(fighters)
            first_fighter = int(input("""
           Type number of the first fighter to fusionate: """))
            second_fighter = int(input("""          Now, second fighter: """))
            power_merged = merge_fighters(first_fighter, second_fighter)
            print(f"""
           Your new fighter now has {power_merged}""")

    elif choice == 4:

        print("""
          ### Exit ###
          Thanks for playing!""")
        break
    
    else:
        print("""
          Type a valid option""")
