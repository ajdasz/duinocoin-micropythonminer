# duinocoin-micropythonminer
    
This miner is created mainly for routers, micropython-lib uses only ~400kb! It probably can be installed on any router. 
## How to start mine on router:
- Your router must have installed openwrt or similar software.
- Copy content from file miner.py to your router with ssh using nano or similar text editor
- Change your username for your name from duinocoin (line 8)
- Save file as miner.py
- You must install micropython-lib (don't same micropython!).
- Write command on router: `opkg update && opkg install micropython-lib`
- Run miner using command: `micropyhon miner.py`

## How to mining on background?
- I recommend use screen. If you have small space you can use nohup (around 20kb)
- Write command: `opkg update && opkg install screen` - to install it
- Write command:  `screen -S miner` - to create "window" screen named as mining 
- Write command:  `micropython miner.py` - to run miner
- To detach screen just press: `ctrl + a + d` at once
- To restore screen just write: `screen -R miner`

## How efficiency is this miner?
- Low. If you have some time and experience you can create merge request for upgrade hash efficiency.

## I can use this miner on PC?
- Probably yes, but you must install newest version micropython, what cost much space and it's unprofitable, better use another dedicated mining solutions.
- I don't recommended this, because you can get a ban for a too fast mining. Legacy mining is not created to high efficiency devices.

## Example efficiency data:
Cpu: MediaTek MT7620A (580MHz) - 7-9kh/s