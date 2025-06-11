# bot.py

import discord
from discord.ext import commands
import json
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.all()  # để dùng on_member_join, etc.
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

INITIAL_COGS = [
    "cogs.moderation",
    "cogs.music",
    "cogs.welcome"
]

EVENTS = [
    "events.on_ready",
    "events.on_member_join",
    "events.on_message"
]

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

async def main():
    for cog in INITIAL_COGS + EVENTS:
        try:
            await bot.load_extension(cog)
            print(f"Loaded {cog}")
        except Exception as e:
            print(f"Failed to load {cog}: {e}")

    await bot.start(os.getenv("BOT_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
