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









Hi Ninjas

Great work everyone this term.  Particularly enjoyed the meteors game and the sound effects this week.
# Half Term Holidays

We will NOT be running a session on Wednesday 29th May.

We WILL be running a session on Friday 31st May, 10am - 3pm.  (Technically it will be a 'LYP Coding Club' event rather CoderDojo, but it's the same people, me and Nick, running it.)  I will send out a link to book tickets for this soon.  It will be Minecraft programming and will cost £10.

# Laptops

Most of you have now managed to obtain laptops, which is great, since you dont need to borrow ours and you can carry on your coding at home.  They claim it takes 10,000 hours to master a skill.  I don't know if that is true, but certainly the more you practise the better you will get!

If you haven't got a laptop, first you should try asking your family members if you can borrow one.  They might even have an old one that they no longer use because its "too slow" but if you get in touch with me we can probably re-install the software and get it working.  Alternatively if you want to buy one this Chromebook is very good, if you install Linux on it, which I can show you how to do. Or you could get a refurbished Windows laptop for the same price. (A bit slower, but probably easier to use than Linux.)
# Minecraft

I've had some requests from people eager to get started with Minecraft, so here's the details

You will need to own Minecraft Java Edition.  You can download it here

If you already have a Mojang account, click login.  If you haven't accessed it for years you may need to reset your password.  If you already own Minecraft it will then tell you.  If you don't have a Mojang account, create one, and buy Minecraft Java Edition.  It is on sale at half-price at the moment.

The rest of the set-up we can do in class, but for those who want a head start, read on.
## Server setup

Download the Adventures In Minecraft Starter Kit and unpack it in a folder on your desktop. There are videos on the site that explain how to set it up. 

I suggest before you first run the server you edit the file Server/server.properties and change

    level-type=flat

to generate a flat world.  (But it's up to you what sort of world you prefer!)

To run the server, double click the StartServer file.  It will open a server console window, and ask you press space. 

If you want to generate another world later you can change

    level-name=world2

and then run the server again.

Once server is running, to stop nighttime from happening I suggest you type this at the server console

    gamerule doDaylightCycle false
    time set day

You must leave the server console window open at all times.  When you want to quit, first type

    stop

at the server console, so it saves your world.

Minecraft setup

Run the Minecraft launcher you downloaded from minecraft.net.  We will not be using the default which is the latest version of Minecraft.  Instead we will be using version 1.12.

Click 'launch options' then 'add new', then set version to 'release 1.12'.  Then click 'save'.  Then click 'Minecraft' at the top.  Then click the arrow next to 'Play' at the bottom.  Then select '1.12'.  Then click 'Play'.

Minecraft will run.  Click 'multiplayer'.  Then 'add server'.  Enter the server address as

localhost

Click 'done'.  Click on your server to connect to it.
Mu setup

Mu is the Python editor we have already been using, so you probably already have it installed.  However you need to make sure you have the latest 'alpha version 1.1', not the regular 1.0.  You can download it from the links at the top of this page.

Run Mu.  Click 'Mode' and select 'Python3'.

Then click the small gadget icon in the bottom right hand corner of the window.  Click 'third party packages'.  Type

mcpi

Into the box.  Click OK.

Now you are ready to type in and run a Minecraft program.  Here is one to get you started.

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft World")

If that is all too confusing, don't worry.  I will show you how to do it together next week, and if you cant make that we will be doing it together the week after.

Phew that was a long email, but you guys did ask for it!

Richard the arrow next to 'Play' at the bottom.  Then select '1.12'.  Then click 'Play'.