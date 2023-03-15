import inspect

import PokemonTest


class color:
    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def test_a_function(fun:bool):
    """
    Test a function and display if the test success
    @param fun : the function to test
    """
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

def test_a_module(mod):
    """
    test all functions of a module
    @param mod : the module to test
    """
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    for key, value in all_functions:
        if str(inspect.signature(value)) == "()":
            test_a_function(value)

def launch_test():
    """
    launch all tests
    """
    test_a_module(PokemonTest)




"""
    for fun in dir(PokemonTest) :
        test_a_function(fun)
"""
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



