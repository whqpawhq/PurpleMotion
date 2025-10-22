import discord
from discord.ext import commands
import os

# Lấy token từ biến môi trường (Render -> Environment Variables)
TOKEN = os.getenv("DISCORD_TOKEN")

# Tạo intents để bot có thể nhận sự kiện trong server
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Tạo bot với prefix “!”
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! Mình đang online nè!")

@bot.command()
async def say(ctx, *, message: str):
    """Bot lặp lại tin nhắn"""
    await ctx.send(message)

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"🎉 Chào mừng {member.mention} đã tham gia server!")

bot.run(TOKEN)
