import os
import discord
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv
import os
import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

env_path = Path('.') / '.env'
print(f"Tìm thấy file .env: {env_path.exists()}")
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("DISCORD_TOKEN")
print(f"Token lấy được: {TOKEN}")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)
LOG_CHANNEL_ID = 1381309750066675884
def create_embed(title, fields, color=discord.Color.blue()):
    embed = discord.Embed(title=title, color=color)
    embed.timestamp = datetime.datetime.now(ZoneInfo("Asia/Bangkok"))
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    return embed

@bot.event
async def on_message_delete(message):
    if message.author == bot.user or message.author.bot:
        return
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    embed = create_embed(
        title="🗑️ Tin nhắn bị xóa",
        fields=[
            ("Tác giả", f"{message.author} (`{message.author.id}`)", False),
            ("Kênh", f"{message.channel.mention}", True),
            ("Nội dung", message.content or "*Không có nội dung*", False),
        ],
        color=discord.Color.red()
    )
    await log_channel.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user or before.author.bot:
        return
    if before.content == after.content:
        return
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    embed = create_embed(
        title="✏️ Tin nhắn đã chỉnh sửa",
        fields=[
            ("Tác giả", f"{before.author} (`{before.author.id}`)", False),
            ("Kênh", f"{before.channel.mention}", True),
            ("Trước", before.content or "*Không có nội dung*", False),
            ("Sau", after.content or "*Không có nội dung*", False),
        ],
        color=discord.Color.orange()
    )
    await log_channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return
    log_channel = bot.get_channel(LOG_CHANNEL_ID)

    embed = create_embed(
        title="💬 Tin nhắn mới",
        fields=[
            ("Tác giả", f"{message.author} (`{message.author.id}`)", False),
            ("Kênh", f"{message.channel.mention}", True),
            ("Nội dung", message.content or "*Không có nội dung*", False),
        ],
        color=discord.Color.green()
    )
    await log_channel.send(embed=embed)

    await bot.process_commands(message)

@bot.event
async def on_guild_channel_update(before, after):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if before.name != after.name:
        embed = create_embed(
            title="📁 Text channel updated",
            fields=[
                ("Before", f"**Name:** {before.name}", True),
                ("After", f"**Name:** {after.name}", True),
                ("Channel ID", str(after.id), False),
            ],
            color=discord.Color.blurple()
        )
        await log_channel.send(embed=embed)

bot.run(TOKEN)
