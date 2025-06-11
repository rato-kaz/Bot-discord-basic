from discord.ext import commands

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot đã sẵn sàng dưới tên {self.bot.user}")

async def setup(bot):
    await bot.add_cog(OnReady(bot))
