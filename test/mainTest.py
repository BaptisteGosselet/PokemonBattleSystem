import inspect
import sys
sys.path.insert(1, 'src')

import PokemonTest, PokemonFactoryTest, TypePkmnTest, StatusTest, EffectTest, TrainerTest, ActionTest

class color:

    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    TITLE = '\033[94m' #BLUE

def test_a_function(fun:bool):
    """
    Test a function and display if the test success
    @param fun : the function to test
    """
    line = "\t- "
    status = "\t\t\t"

    res = fun()
    if(res):
        line += color.OK
        status += "OK"
    else:
        line += color.FAIL
        status += "FAIL"

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
    print(color.TITLE,mod.__name__, color.RESET)
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    for key, value in all_functions:
        if str(inspect.signature(value)) == "()":
            test_a_function(value)
    print("\n")

def launch_test():
    """
    launch all tests
    """

    test_a_module(PokemonTest)
    test_a_module(PokemonFactoryTest)
    test_a_module(TypePkmnTest)
    test_a_module(StatusTest)
    test_a_module(EffectTest)
    test_a_module(TrainerTest)
    test_a_module(ActionTest)

launch_test()



