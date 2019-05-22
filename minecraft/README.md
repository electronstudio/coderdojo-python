# HMCL

An open-source launcher that is useful if you only have the demo version of Minecraft and want
to play on a local server.  Still recommended you buy the full version because this won't allow you to
play on Internet servers.
(No guarantee this will work, but it's open source and free of viruses.)

https://github.com/huanghongxun/HMCL/releases

# Server setup

I suggest before you first run the server you edit the file Server/server.properties and change

    level-type=flat

to generate a flat world.  If you want to generate another world later you can change

    level-name=world2
    
and then run the server again.

Once server is running, to stop nighttime from happening I suggest you type this at the server console:

    gamerule doDaylightCycle false
    time set day

# Stopping

When you want to quit, first type

    stop

at the server console, so it saves your world.
