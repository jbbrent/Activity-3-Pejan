class Stat_CALC():
    def Stat_Calc_HP(pokemon_base_hp, pokemon_IV, pokemon_EV, pokemon_LEVEL):
        HP= (((2 * pokemon_base_hp+ pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + pokemon_LEVEL + 10
        return HP
    
    def other_stat_ATTACK(pokemon_base_ATTACK, pokemon_IV, pokemon_EV, pokemon_LEVEL, pokemon_NATURE):
        stat_att = ((((2 * pokemon_base_ATTACK + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + 5) * (((2 * pokemon_base_ATTACK + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + pokemon_NATURE
        return stat_att
    
    def other_stat_DEFENSE(pokemon_base_DEFENSE, pokemon_IV, pokemon_EV, pokemon_LEVEL,pokemon_NATURE):
        stat_def = ((((2 * pokemon_base_DEFENSE + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + 5) * (((2 * pokemon_base_DEFENSE + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + pokemon_NATURE
        return stat_def
    
    def other_stat_SPATTACK(pokemon_base_SPATTACK, pokemon_IV, pokemon_EV, pokemon_LEVEL,pokemon_NATURE):
        stat_SPATTACK = ((((2 * pokemon_base_SPATTACK + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + 5) * (((2 * pokemon_base_SPATTACK + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + pokemon_NATURE
        return stat_SPATTACK
    
    def other_stat_SPDEFENSE(pokemon_base_SPDEFENSE, pokemon_IV, pokemon_EV, pokemon_LEVEL,pokemon_NATURE):
        stat_SPDEFENSE = ((((2 * pokemon_base_SPDEFENSE + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + 5) * (((2 * pokemon_base_SPDEFENSE + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + pokemon_NATURE
        return stat_SPDEFENSE
    
    def other_stat_speed(pokemon_base_speed, pokemon_IV, pokemon_EV, pokemon_LEVEL,pokemon_NATURE):
        stat_speed = ((((2 * pokemon_base_speed + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + 5) * (((2 * pokemon_base_speed + pokemon_IV + (pokemon_EV/4)) * pokemon_LEVEL)/100) + pokemon_NATURE
        return stat_speed


