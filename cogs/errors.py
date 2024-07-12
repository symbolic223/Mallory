import disnake
from disnake.ext import commands

class ErrorCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, e):
        em = str(e)

        if isinstance(e, commands.CommandInvokeError):
            em = "Че еблан что-ли? Иди к моему разрабу че то пиши, я сама хз"
            print(e)

        elif isinstance(e, commands.NotOwner):
            em = "Нахуй иди, чмо"
            print(e)

        elif isinstance(e, commands.MissingRequiredArgument):
            em = "Очки надень, олух"
            print(e)

        elif isinstance(e, commands.MissingPermissions):
            em = "Хуй соси, маленький еще до такой команды"
            print(e)

        elif isinstance(e, commands.UserNotFound):
            em = "Шиза заиграла? Нет такого"
            print(e)

        elif isinstance(e, commands.MemberNotFound):
            em = "Тут нету его, пригласи его что-ли на сервер, додик"
            print(e)

        elif isinstance(e, commands.NSFWChannelRequired):
            em = "Тише будь, детей напугаешь"
            print(e)

        huy = disnake.Embed(
            title="БЛЯТЬ!",
            description=f"Когда ты прописал команду {inter.data.name} я че-то упала",
            color=0xff0000
        )
        huy.add_field(name="Это еще почему?", value=f"{em}", inline=False)
        await inter.response.send_message(embed=huy, ephemeral=True)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):
        em = str(e)

        if isinstance(e, commands.CommandInvokeError):
            em = "Че еблан что-ли? Иди к моему разрабу че то пиши, я сама хз"
            print(e)

        elif isinstance(e, commands.NotOwner):
            em = "Нахуй иди, чмо"
            print(e)

        elif isinstance(e, commands.MissingRequiredArgument):
            em = f"Очки надень, олух"
            print(e)

        elif isinstance(e, commands.MissingPermissions):
            em = "Хуй соси, маленький еще до такой команды"
            print(e)

        elif isinstance(e, commands.UserNotFound):
            em = "Шиза заиграла? Нет такого"
            print(e)

        elif isinstance(e, commands.MemberNotFound):
            em = "Тут нету его, пригласи его что-ли на сервер, додик"
            print(e)

        elif isinstance(e, commands.NSFWChannelRequired):
            em = "Тише будь, детей напугаешь"
            print(e)

        huy = disnake.Embed(
            title="БЛЯТЬ!",
            description=f"Когда ты прописал команду я че-то упала",
            color=0xff0000
        )
        huy.add_field(name="Это еще почему?", value=f"{em}", inline=False)
        await ctx.send(embed=huy)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorCog(bot))