import discord
from discord.ext import commands
import yt_dlp
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def search_youtube(self, query):
        ytdl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'default_search': 'ytsearch',
        }
        with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            return info['entries'][0] if 'entries' in info else info

    @commands.command(name="play")
    async def play(self, ctx, *, query):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
            return await ctx.send("❌ Mày cần tham gia voice channel trước!")

        # Kết nối nếu chưa kết nối
        vc = ctx.voice_client or await voice_channel.connect()

        if vc.is_playing():
            return await ctx.send("🔊 Bot đang phát nhạc rồi. Hãy chờ hoặc dùng lệnh `!stop`.")

        await ctx.send(f"🔎 Đang tìm kiếm: `{query}`...")
        info = await self.search_youtube(query)
        url = info['url']
        title = info['title']

        await ctx.send(f"🎵 Đang phát: **{title}**")

        # Phát nhạc
        vc.play(
            discord.FFmpegPCMAudio(url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"),
            after=lambda e: print(f"Kết thúc phát nhạc: {e}" if e else "Phát xong")
        )

    @commands.command(name="stop")
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("⏹️ Đã dừng và rời voice channel.")
        else:
            await ctx.send("❌ Bot không đang ở trong voice channel.")

async def setup(bot):
    await bot.add_cog(Music(bot))
