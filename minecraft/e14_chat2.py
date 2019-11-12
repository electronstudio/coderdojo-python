""" Your program can read chat messages posted by players.
# This program builds a block next to the player who
# says "build".  This is the first example that will
# work for more than one player. """

from mcpi.minecraft import *

mc = Minecraft.create()

mc.camera.setFixed()

while True:
    events = mc.events.pollChatPosts()


    for event in events:
        print(event)
        command, target = event.message.split()
        #id = mc.getPlayerEntityId(target)
        if command == "build":
            pos = mc.entity.getTilePos(id)
            x = pos.x
            y = pos.y
            z = pos.z
            mc.setBlock(x, y, z, 1)
            mc.postToChat("done building!")
        if command == "follow":
            print("follow")
            id = event.entityId
            mc.camera.setFollow(id)

"""
# TODO
# build a house around the player if the player says "house"
# build a lava trap if the player says "trap"
# use mc.getPlayerEntityId("fred") to get the id of a certain
#   player named Fred (or whatever your friend's player name is)
"""
