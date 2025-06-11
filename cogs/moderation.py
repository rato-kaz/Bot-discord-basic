from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Không có lý do"):
        await member.kick(reason=reason)
        await ctx.send(f"👢 Đã kick {member.mention} vì: {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Không có lý do"):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 Đã ban {member.mention} vì: {reason}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
