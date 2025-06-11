from discord.ext import commands
import discord

class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Tìm channel tên "general" hoặc id cụ thể bạn muốn gửi lời chào
        channel = discord.utils.get(member.guild.text_channels, name="thông-báo📣")

        if channel:
            await channel.send(f"👋 Chào mừng {member.mention} đến với **{member.guild.name}**!")
        else:
            print(f"Không tìm thấy channel phù hợp để gửi lời chào khi {member} tham gia.")

async def setup(bot):
    await bot.add_cog(OnMemberJoin(bot))


