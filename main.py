import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable the message_content intent

bot_token = 'Insert Bot Token'
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message_edit(before, after):
    # Check if the edited message was sent by the bot itself
    if after.author == bot.user:
        return

    # Role IDs to exempt from message deletion
    roles_to_exempt = [Insert Role ID, Insert Role ID, Insert Role ID, Insert Role ID]

    for role_id in roles_to_exempt:
        role = discord.utils.get(after.author.roles, id=role_id)
        if role:
            return

    # Delete the edited message
    try:
        await after.delete()
    except discord.Forbidden:
        print("The bot doesn't have permissions to delete messages.")
    except discord.HTTPException:
        print("Failed to delete the message.")

@bot.event
async def on_message(message):
    # Save the message to the cache
    bot.messages_cache[message.id] = message

    # Your message processing logic here
    await bot.process_commands(message)

# You can create a dictionary to store the cached messages
bot.messages_cache = {}

bot.run(bot_token)
