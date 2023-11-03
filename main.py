from re import X
from conf import *

configurationGui = configurationGui()
configuration = configurationGui.createConfiguration()

print (configuration.small_numbers)
print (configuration.big_numbers)