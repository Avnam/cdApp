from re import X
from conf import *
from game import *

configurationGui = configurationGui()
gameConfiguration = configurationGui.createConfiguration()

print (gameConfiguration.small_numbers)
print (gameConfiguration.big_numbers)

game = gameGui(gameConfiguration)
game.runGame()