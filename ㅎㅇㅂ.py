Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("크체게이")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/ㄹㅇ"):
        await message.channel.send("ㅋㅋ")


client.run("ODM2MjEzNTY1NTAwMTYyMDY4.YIaukg.jBibbE0nBtgMUguJidRwqvhJGww")
