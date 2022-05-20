class EV_CALC():
    def EV_Calc_D(pokemon_base,pokemon_IV,pokemon_EV,pokemon_LEVEL):
        D = ((2*pokemon_base + pokemon_IV +(pokemon_EV/4))*pokemon_LEVEL/100)
        return D
    def EV_Calc_EV_Needed(Desired_Increase, Modifier, D, pokemon_LEVEL):
        EVs_needed = ((((Desired_Increase/Modifier)-(D))*400/pokemon_LEVEL)/4)*4
        return EVs_needed

