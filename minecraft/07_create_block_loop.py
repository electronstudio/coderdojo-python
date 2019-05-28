# Same as program 06 but in a loop

from mcpi.minecraft import *
from mcpi.block import *
import time

mc = Minecraft.create()

while True:
    time.sleep(0.2)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    blocktype = ICE
    mc.setBlock(x, y, z, blocktype)

# TODO
# Make the block appear one meter BELOW the player's position
# Change the block to something else.  Ice?
