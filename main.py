import disnake
from disnake.ext import commands
import os
import sys
import asyncio
import time

class PBot(commands.Bot):
    def __init__(self, *args, owner_ids=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner_ids = owner_ids or [318343838240342016, 386439272455995394]

    async def is_owner(self, user: disnake.User | disnake.Member) -> bool:
        if user.id in self.owner_ids:
            return True
        return await super().is_owner(user)

intents = disnake.Intents.all()
bot = PBot(command_prefix = "mel!", help_command = None, intents = intents)

@bot.event
async def on_ready():
    bot.start_time = time.time()
    print("Все, съеби, я работать.")
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def restart(ctx):
    if ctx.author.id == bot.owner.id:
        await ctx.reply("иди нахуй")
        await asyncio.sleep(1)

        dyrka = sys.executable
        os.execl(dyrka, dyrka, *sys.argv)

bot.run("MTI2MDI4MjEzMTEwODcyNDczNw.GIHsRc.NLAwWDsPmPH5t75FZZZIq92FnpL5HFYgcFD2dw")

#BabaxSous228