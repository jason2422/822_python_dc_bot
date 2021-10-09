import discord 


intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
#Somewhere else:
#client = discord.Client(intents = intents)
#or
#form discord.ext improt commands
#bot = commands.Bot(command_prefix='!',intents=intents)

from discord.ext import commands
#建置dc bot 實體並儲存到bot裡
#command_prefix : 呼叫機器人時所需的命令字首
bot = commands.Bot(command_prefix="?",intents = intents)
#ep1
@bot.event
#定義功能要加async
async def on_ready():
   print(">> Bot is online <<") 
#ep2:member_join/left
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(896301108908154880)
    await channel.send(f"{member} join!")
    #print(f"{member} join!")#f string 可以讓文字做適當的改變
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(896301182006485012)#抓取頻道並丟給variable channel
    await channel.send(f"{member} leave!")
    #print(f"{member} leave!")
    
@bot.command()
async def ping(ctx):
    #ctx : context 上下文
    #A:嗨 (上文) (user, id, server, channel)
    #B:安安(下文)
    await ctx.send(f"{round(bot.latency*1000)}ms")#from ctx finding the attributes and sending text to the goal by the information from ctx.
    #bot.latency get the latency 
    #1000ms = 1s
    
bot.run("ODk2Mjc4MTU0Mzk2NzEzMDAw.YWEyFA.Zm6LEwEm30ZwRGK-rff8Sbrwajw")#括號裡面放token
