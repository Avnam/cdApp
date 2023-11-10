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
        game.runGame()
    else:
        break