"""
setBlocks lets us set many blocks at once
 What does setting a block to AIR do?
# We are defining a function so we can re-use it in other programs
# without typing it in again
"""

from mcpi.minecraft import *
from mcpi.block import *

def clear_space(mc, size):
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x-size, pos.y, pos.z-size, pos.x+size, pos.y+size, pos.z+size,
                 AIR)

mc = Minecraft.create()

clear_space(mc, 10)
