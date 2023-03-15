from PokemonTest import *

class color:
    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def test_a_function(fun:bool):
    line = ""
    status = ""

    res = fun()
    if(res):
        line = color.OK
        status = "OK"
    else:
        line = color.FAIL
        status = "FAIL"

    line += fun.__name__
    line += " : "
    line += status
    line += color.RESET
    
    print(line)

def launch_test():

    test_a_function(testPkm)

    #Pokemon
    #PokemonFactory
    #TypePkmn
    #Status
    #Move
    #Trainer
    #AiTrainer
    #Effect
    #Action

launch_test()



