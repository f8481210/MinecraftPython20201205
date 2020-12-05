#1205-1
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    temp = mc.events.pollBlockHits() 
    #temp是清單
    if len(temp) > 0 : #判斷temp裡面有沒有東西
        hit = temp[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("你獵到了"+str(block))
    