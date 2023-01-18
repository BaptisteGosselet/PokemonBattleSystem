from random import randint
from model.status.statusEffect.StatusEffect import StatusEffect
from model.status.statusPokemon.ParalysisPokemon import ParalysisPokemon

class ParalisysEffect(StatusEffect):

    def getStatusPokemon(self, pokemon)-> ParalysisPokemon :
        return ParalysisPokemon(pokemon)