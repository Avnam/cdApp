from re import X
from conf import *
from game import *

configurationGui = configurationGui()

while 1:
    gameConfiguration = configurationGui.createConfiguration()

    if gameConfiguration != None:
        print (gameConfiguration.small_numbers)
        print (gameConfiguration.big_numbers)
        game = gameGui(gameConfiguration)
        
        while 1:
            retValue = game.runGame()
            if retValue == "done":
                exit(0)
            if retValue == "conf":
                break
    else:
        break