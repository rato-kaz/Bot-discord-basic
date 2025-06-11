from discord.ext import commands

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.lower() == "ping":
            await message.channel.send("Ping cái lồn má mày")
        await self.bot.process_commands(message)  # không được quên để bot xử lý lệnh

async def setup(bot):
    await bot.add_cog(OnMessage(bot))
