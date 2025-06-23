import discord
from discord.ext import commands
from discord import app_commands
from openai import OpenAI  # sử dụng client mới
import os
from dotenv import load_dotenv
from utils.database import save_chat_history

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # client API mới

class ChatBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree

    @app_commands.command(name="ask", description="Gửi câu hỏi cho trợ lý AI (OpenAI)")
    async def ask(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.defer(thinking=True)

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là một trợ lý thân thiện."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )
            reply = response.choices[0].message.content

            # Lưu lịch sử vào DB
            save_chat_history(
                user_id=interaction.user.id,
                guild_id=interaction.guild.id if interaction.guild else None,
                prompt=prompt,
                response=reply
            )

            await interaction.followup.send(reply)

        except Exception as e:
            await interaction.followup.send(f"Lỗi khi gọi OpenAI API: `{e}`")

async def setup(bot):
    await bot.add_cog(ChatBot(bot))
