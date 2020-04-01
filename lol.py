import discord

class gelu(discord.Client):
    async def on_ready(self):
        print("m-am trezit nahui damu,dani pasi")

    async def on_message(self,message):
        if message.author == client.user:
            return

        elif len(message.mentions) != 0: 
            await message.channel.send('da wai?')

        if message.content.lower() == 'ce faci?':
            await message.channel.send('stau')
            
            
client = gelu()
client.run("Njk0MTQ1MDU5MzEzOTQyNTgw.XoHXAQ.qwHa0I7P_4POA7NZkZVRMx1wQIk")
