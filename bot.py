# bot.py
import os

import discord
from dotenv import load_dotenv

from hv_scraper import HvScraper

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

custom_intents = discord.Intents.default()
custom_intents.message_content = True
custom_intents.members = True
client = discord.Client(intents=custom_intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "!keyword" in message.content:
        keyword = message.content.replace("!keyword", "").strip()
        scraper = HvScraper()
        await message.channel.send(scraper.generate_answer_string(keyword))

    # if "!test" in message.content:
    #    await message.channel.send("<https://foorum.hinnavaatlus.ee/viewtopic.php?t=842072&highlight=monitor&sid=afb32cde68b8cdc9f55049a83fd65a53>")


client.run(TOKEN)
