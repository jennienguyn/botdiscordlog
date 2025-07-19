import os
import discord
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv
import datetime
from zoneinfo import ZoneInfo

# Tải biến môi trường
env_path = Path('.') / '.env'
print(f"Tìm thấy file .env: {env_path.exists()}")
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("DISCORD_TOKEN")
print(f"Token lấy được: {TOKEN}")

# Khởi tạo Intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)
LOG_CHANNEL_ID = 1381309750066675884 # ID kênh Discord dùng để gửi log

# --- Cấu hình và hàm ghi log vào file ---
LOG_DIR = "logs"
Path(LOG_DIR).mkdir(parents=True, exist_ok=True) # Tạo thư mục logs nếu chưa có

def write_to_log_file(log_message: str):
    """Ghi tin nhắn log vào file .txt theo ngày."""
    today_date = datetime.datetime.now(ZoneInfo("Asia/Bangkok")).strftime("%Y-%m-%d")
    log_filename = Path(LOG_DIR) / f"log-{today_date}.txt"
    timestamp = datetime.datetime.now(ZoneInfo("Asia/Bangkok")).strftime("%H:%M:%S")
    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {log_message}\n")

def create_embed(title, fields, color=discord.Color.blue()):
    embed = discord.Embed(title=title, color=color)
    embed.timestamp = datetime.datetime.now(ZoneInfo("Asia/Bangkok"))
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    return embed

# --- Các sự kiện Discord ---

@bot.event
async def on_message_delete(message):
    if message.author == bot.user or message.author.bot:
        return
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    
    # Chuỗi log cho file
    log_content = message.content or "[Không có nội dung]"
    log_message = f"Tin nhắn đã xóa: Tác giả: {message.author} ({message.author.id}), Kênh: #{message.channel.name} ({message.channel.id}), Nội dung: '{log_content}'"
    write_to_log_file(log_message)

    # Gửi embed lên kênh Discord
    if log_channel:
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

    # Chuỗi log cho file
    before_content = before.content or "[Không có nội dung]"
    after_content = after.content or "[Không có nội dung]"
    log_message = f"Tin nhắn đã chỉnh sửa: Tác giả: {before.author} ({before.author.id}), Kênh: #{before.channel.name} ({before.channel.id}), Trước: '{before_content}', Sau: '{after_content}'"
    write_to_log_file(log_message)

    # Gửi embed lên kênh Discord
    if log_channel:
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

    # Chuỗi log cho file
    log_content = message.content or "[Không có nội dung]"
    log_message = f"Tin nhắn mới: Tác giả: {message.author} ({message.author.id}), Kênh: #{message.channel.name} ({message.channel.id}), Nội dung: '{log_content}'"
    write_to_log_file(log_message)

    # Gửi embed lên kênh Discord (tùy chọn, có thể tắt nếu không muốn log mọi tin nhắn)
    if log_channel:
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
        # Chuỗi log cho file
        log_message = f"Tên kênh đã cập nhật: Kênh: #{before.name} ({before.id}) thay đổi thành #{after.name} ({after.id})"
        write_to_log_file(log_message)

        # Gửi embed lên kênh Discord
        if log_channel:
            embed = create_embed(
                title="📁 Kênh văn bản đã cập nhật",
                fields=[
                    ("Trước", f"**Tên:** {before.name}", True),
                    ("Sau", f"**Tên:** {after.name}", True),
                    ("ID Kênh", str(after.id), False),
                ],
                color=discord.Color.blurple()
            )
            await log_channel.send(embed=embed)
# Kích hoạt tất cả Intents cần thiết (bao gồm Server Members Intent)
intents = discord.Intents.default()
intents.members = True # Rất quan trọng: phải bật intents.members = True
intents.message_content = True # Để bot có thể đọc tin nhắn (nếu cần cho các lệnh khác)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot đã sẵn sàng với tên: {bot.user}')

@bot.event
async def on_member_join(member):
    # Tìm kênh mà bạn muốn gửi tin nhắn chào mừng
    # Bạn có thể tìm theo tên kênh hoặc ID kênh
    # Ví dụ tìm theo ID kênh:
    channel_id = 1352641589037633637  # Thay thế bằng ID kênh thực tế của bạn
    channel = bot.get_channel(1352641589037633637)

    if channel:
        # Gửi tin nhắn chào mừng và mention người dùng mới
        await channel.send(f'Chào mừng {member.mention} đã tham gia server! Mấy con vợ ra tiếp đón người mới cái :D')
    else:
        print(f"Không tìm thấy kênh với ID: 1352641589037633637")
bot.run(TOKEN)
