
#ESharpAxe 20160119b
# Creates a cuboid near the player.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks ( pos.x + 2, pos.y, pos.z + 2, pos.x + 22, pos.y + 2, pos.z + 22, 57)

