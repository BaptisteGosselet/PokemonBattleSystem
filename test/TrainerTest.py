from MockTrainer import MockTrainer

def waitForAction_Test():
    trainer = MockTrainer()
    a = trainer.getAction()
    trainer.waitForAction(trainer.getView())
    return a == None and trainer.getAction() != None

def switchPokemon_Test():
    trainer = MockTrainer()
    poke = trainer.getCurrentPokemon()
    trainer.switchPokemon(1)
    return trainer.getCurrentPokemon() != poke

def canContinue_Test():
    trainer = MockTrainer()
    trainer.setAllKO()
    return not trainer.canContinue()
