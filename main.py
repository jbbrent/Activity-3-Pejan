import EV_CALC as ec
import Stat_CALC as sc

print('1. Stat Calc ')
print('2. EV Calc ')

pokemon_nature_ATTACK = 1
pokemon_nature_DEFENSE = 1
pokemon_nature_SPATTACK = 1
pokemon_nature_SPDEFENSE = 1
pokemon_nature_SPEED = 1

ch = int(input('Enter: '))

if ch == 1:
    print('Stats')
    
    pokemon = str(input('Enter pokemon: '))

pokemon_LEVEL= int(input('Enter pokemon level: '))

pokemon_NATURE = str.lower(input('Enter Pokemon Nature: '))

pokemon_base = int(input('Enter pokemon base: '))

pokemon_IV = int(input('Enter pokemon IV: '))

pokemon_EV = int(input('enter pokemon_EV: '))
    
#NEUTRAL NATURE
if pokemon_NATURE in ['bashful','serious','quirky','docile','hardy']:
    pokemon_nature_ATTACK = 1
    pokemon_nature_DEFENSE = 1 
    pokemon_nature_SPATTACK = 1
    pokemon_nature_SPDEFENSE = 1
    pokemon_nature_SPEED = 1

#ATTACK NATURE
elif pokemon_NATURE in ['lonely','adamant','naughty','brave']:
    pokemon_nature_ATTACK = 1.1
    if pokemon_NATURE in ['lonely']:
        pokemon_nature_DEFENSE = 0.9
    elif pokemon_NATURE in ['adamant']:
        pokemon_nature_SPATTACK = 0.9
    elif pokemon_NATURE in ['naughty']:
        pokemon_nature_SPDEFENSE = 0.9
    elif pokemon_NATURE in ['brave']:
        pokemon_nature_SPEED = 0.9

#DEFENSE NATURE
elif pokemon_NATURE in ['bold','relaxed','impish','lax']:
    pokemon_nature_DEFENSE = 1.1
    if pokemon_NATURE in ['bold']:
        pokemon_nature_ATTACK = 0.9
    elif pokemon_NATURE in ['relaxed']:
        pokemon_nature_SPEED = 0.9
elif pokemon_NATURE in ['impish']:
        pokemon_nature_SPATTACK = 0.9
elif pokemon_NATURE in ['lax']:
        pokemon_nature_SPDEFENSE = 0.9
    
#SPEED NATURE
elif pokemon_NATURE in ['timid','hasty','jolly','naive']:
    pokemon_nature_SPEED = 1.1
    if pokemon_NATURE in ['timid']:
        pokemon_nature_ATTACK = 0.9
    elif pokemon_NATURE in ['hasty']:
        pokemon_nature_DEFENSE = 0.9
    elif pokemon_NATURE in ['jolly']:
        pokemon_nature_SPATTACK = 0.9
    elif pokemon_NATURE in ['naive']:
        pokemon_nature_SPDEFENSE = 0.9
#SPEED ATTACK NATURE
elif pokemon_NATURE in ['modest', 'mild', 'rash','quiet']:
    pokemon_nature_SPATTACK = 1.1
    if pokemon_NATURE in ['modest']:
        pokemon_nature_ATTACK = 0.9
    elif pokemon_NATURE in ['mild']:
         pokemon_nature_DEFENSE = 0.9
    elif pokemon_NATURE in ['rash']:
        pokemon_nature_SPDEFENSE = 0.9
    elif pokemon_NATURE in ['quiet']:
        pokemon_nature_SPEED = 0.9
#SPEED DEFENSE NATURE
elif pokemon_NATURE in ['calm', 'hasty', 'jolly' , 'naive']:
    pokemon_nature_SPDEFENSE = 1.1
    if pokemon_NATURE in ['calm']:
        pokemon_nature_ATTACK = 0.9
    elif pokemon_nature_DEFENSE ['hasty']:
        pokemon_nature_DEFENSE = 0.9
    elif pokemon_NATURE in ['jolly']:
        pokemon_nature_SPATTACK = 0.9
    elif pokemon_NATURE in ['naive']:
        pokemon_nature_SPEED = 0.9

print("1. HP")        
print("2. Attack")
print("3. Defense")
print ("4. Special Attack")
print ("5. Special Defense")
print ("6. Speed")

opt = int(input("Enter: "))

if opt == 1:
    pokemon_base_hp = int(input("Enter base hp: "))
    pokemon_IV = int(input("Enter Pokemon IV: "))
    pokemon_EV = int(input("Enter Pokemon EV: "))
    print("TOTAL HP: ", sc.Stat_CALC.Stat_Calc_HP(pokemon_base_hp, pokemon_IV, pokemon_EV, pokemon_LEVEL), "\n")
if opt == 2:
    pokemon_base_attack = int(input("Enter Base Attack: "))
    pokemon_IV = int(input("Enter Pokemon IV: "))
    print("TOTAL BASE ATTACK: ", sc.Stat_CALC.other_stat_att(pokemon_base_attack,pokemon_IV,pokemon_LEVEL,pokemon_nature_ATTACK), "\n")
if opt == 3:
    pokemon_base_def = int(input("Enter Base Defense: "))
    pokemon_IV = int(input("Enter IV: "))
    print("TOTAL BASE DEFENSE: ", sc.Stat_CALC.other_stat_def(pokemon_base_def,pokemon_IV,pokemon_LEVEL,pokemon_nature_DEFENSE), "\n")
if opt == 4:
    pokemon_base_SPAttack = int(input("Enter Base Special Attack: "))
    print_IV = int(input("Enter IV: "))
    print("TOTAL SPECIAL ATTACK: ", sc.Stat_CALC.other_stat_SPATTACK(pokemon_base_SPAttack,pokemon_IV,pokemon_LEVEL,pokemon_nature_SPATTACK), "\n")
if opt == 5:
    pokemon_base_SPDefense = int(input("Enter Base Special Defense: "))
    print_IV = int (input("Enter IV: "))
    print("TOTAL SPECIAL DEFENSE: ",  sc.Stat_CALC.other_stat_SPDEFENSE(pokemon_base_SPDefense,pokemon_IV,pokemon_LEVEL,pokemon_nature_SPDEFENSE), "\n")

if opt == 6:
    pokemon_base_speed = int(input("Enter Base Speed: "))
    print_IV = int (input("ENTER IV: "))
    print("Total Speed: ",  sc.Stat_CALC.other_stat_speed(pokemon_base_speed,pokemon_IV,pokemon_LEVEL,pokemon_nature_SPEED), "\n")

flag = True
pokemon_LEVEL= 0
Pokemon_Stat = ["HP" ,"Attack","Defense","Special Attack","Special Defense","Speed"]
pokemon_base = [6]
pokemon_IV = [6]
pokemon_EV = [6]

if ch == 2:
    print("Evs")

    while flag:
        pokemon_LEVEL= int(input("Enter Pokemon Level: "))
        if pokemon_LEVEL> 0 and pokemon_LEVEL< 101:
            flag = False
    
    pokemon_nature = str.lower(input("Enter Pokemon's Nature: "))

    print("Enter Base Stats")
    for x in range (1, 6):
        pokemon_base.append(int(input("Enter " + Pokemon_Stat[x] + ": ")))

    print ("Enter IV on each Stat")
    i = 1
    while i < 7:
        pokemon_IV.append(int(input("Enter " + Pokemon_Stat [i] + " IV: ")))
        if (pokemon_IV[i] < 0 or pokemon_IV[i] > 31):
            i = i - 1
            print("Must be between 0 and 31")
        i = i + 1

    print("Enter EV on each Stat")
    j = 1
    while j < 7:
        pokemon_EV.append(int(input("Enter "+Pokemon_Stat[j]+" EV: ")))
        if (pokemon_EV[j] < 0 or pokemon_EV[j] > 255 ):
            j = j - 1
            print("Must be between 0 and 255")
        j = j + 1

    #Pokemon Neutral Nature
    if pokemon_NATURE in ['quirky' , 'bashful', 'serious','docile','hardy']:
        pokemon_nature_ATTACK = 1
        pokemon_nature_DEFENSE = 1
        pokemon_nature_SPATTACK = 1
        pokemon_nature_SPDEFENSE = 1
        pokemon_nature_SPEED = 1

    #Pokemon Attack Nature
    elif pokemon_NATURE in ['lonely','brave','adamant','naughty']:
        pokemon_nature_ATTACK = 1.1
        if pokemon_NATURE in ['lonely']:
            pokemon_nature_DEFENSE = 0.9
        elif pokemon_NATURE in ['brave']:
            pokemon_nature_SPEED = 0.9
        elif pokemon_NATURE in ['adamant']:
            pokemon_nature_SPATTACK = 0.9
        elif pokemon_NATURE in ["naughty"]:
            pokemon_nature_SPDEFENSE = 0.9
    
    #Pokemon Nature Defense
    elif pokemon_NATURE in ['bold','relaxed','impish','lax']:
        pokemon_nature_DEFENSE = 1.1
        if pokemon_NATURE in ['bold']:
            pokemon_nature_ATTACK = 0.9
        elif pokemon_NATURE in ['relaxed']:
            pokemon_nature_SPEED = 0.9
        elif pokemon_NATURE in ['impish']:
            pokemon_nature_SPATTACK = 0.9
        elif pokemon_NATURE in ['lax']:
            pokemon_nature_SPDEFENSE = 0.9
    
    #Pokemon Speed Nature
    elif pokemon_NATURE in ['timid','hasty','jolly','naive']:
        pokemon_nature_SPEED = 1.1
        if pokemon_NATURE in ['timid']:
            pokemon_nature_ATTACK = 0.9
        elif pokemon_NATURE in ['hasty']:
            pokemon_nature_DEFENSE = 0.9
        elif pokemon_NATURE in ['jolly']:
            pokemon_nature_SPATTACK = 0.9
        elif pokemon_NATURE in ['naive']:
            pokemon_nature_SPDEFENSE = 0.9
    
    #Pokemon Special Attack Nature
    elif pokemon_NATURE in ['modest','mild','quiet','rash']:
        pokemon_nature_SPATTACK = 1.1
        if pokemon_NATURE in ['modest']:
            pokemon_nature_ATTACK = 0.9
        elif pokemon_NATURE in ['mild']:
            pokemon_nature_DEFENSE = 0.9
        elif pokemon_NATURE in ['quiet']:
            pokemon_nature_SPEED = 0.9
        elif pokemon_NATURE in ['rash']:
            pokemon_nature_SPDEFENSE = 0.9
    
    #Pokemon Special Defense Nature
    elif pokemon_NATURE in ['calm','gentle','sassy','careful']:
        pokemon_nature_SPDEFENSE = 1.1
        if pokemon_NATURE in ['calm']:
            pokemon_nature_ATTACK = 0.9
        elif pokemon_NATURE in ['gently']:
            pokemon_nature_DEFENSE = 0.9
        elif pokemon_NATURE in ['sassy']:
            pokemon_nature_SPEED = 0.9
        elif pokemon_NATURE in ['careful']:
            pokemon_nature_SPATTACK = 0.9
    

    print("1. Attack")
    print("2. Defense")
    print("3. Special Attack")
    print("4. Special Defense")
    print("5. Speed")

    opt = int(input("Enter: "))

    if opt == 1:
        Modifier = pokemon_nature_ATTACK
    if opt == 2:
        Modifier = pokemon_nature_DEFENSE
    if opt == 3:
        Modifier = pokemon_nature_SPATTACK
    if opt == 4:
        Modifier = pokemon_nature_SPDEFENSE
    if opt == 5:
        Modifier = pokemon_nature_SPEED

    Desired_Increase = int(input("Enter Desired Increase: "))

    D = ec.EV_Calc.EV_Calc_D (pokemon_base[opt+1],pokemon_IV[opt+1],pokemon_EV[opt+1],pokemon_LEVEL)

    EVs_needed = ec.EV_Calc.Ev_Calc_EV_Needed(Desired_Increase,Modifier,D,pokemon_LEVEL)

    print("The total amount of needed EV for your pokemon is ", EVs_needed)

    

    

    

