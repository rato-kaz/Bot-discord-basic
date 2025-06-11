from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Chào {ctx.author.mention}!")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
