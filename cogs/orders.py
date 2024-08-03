import disnake
from disnake.ext import commands
import sqlite3

conn = sqlite3.connect("Orders.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                user_id INTEGER PRIMARY KEY,
                orders_count INTEGER
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS uorders (
                user_id INTEGER PRIMARY KEY,
                orders_count INTEGER
)''')

welcome = ['Скажите прив вот этому масленку ---> {user.name}', 'Хааааай, {user.name})', 'Че тут забыл этот юзер? {user.name}']
welcome_desc = ['Ну драсьте, драсьте))', 'Не терпится поработать с ним 😏', 'Давай, развлекайся тут', 'Накакала соусами барбекю']
bye = ['Какой-то челикс ливнул отсюда. А конкретно вот этот ----> {user.name}', 'Пошел нахуй отсюда, {user.name}', 'Ну и больно надо, {user.name}.']
bye_desc = ['Ну и хуй с ним.', 'Съеби уже.', 'Давай, шевелись.', 'Нахуй приходил сюда тогда?']


class OrdersCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def count(self, ctx, user: disnake.User = None):
        if user == None:
            user = ctx.author
        cursor.execute("SELECT orders_count FROM orders WHERE user_id = ?", (user.id, ))
        order = cursor.fetchone()
        cursor.execute("SELECT orders_count FROM uorders WHERE user_id = ?", (user.id,))
        uorder = cursor.fetchone()




        e = disnake.Embed(
            title="Кол-во ваших заказов" if user == ctx.author else f"Кол-во заказов пользователя {user.name}",
            color=0xFF00E4
        )
        if order == None:
            e.add_field(name="Я трахнула тебя:" if user == ctx.author else f"Я трахнула его:", value=f"Еще не трахала")
        else:
            orders = order[0]
            e.add_field(name="Я трахнула тебя:" if user == ctx.author else f"Я трахнула его:", value=f"{orders} раз")
        if uorder == None:
            e.add_field(name="Заказы:", value="Пользователь не делал заказов.")
        else:
            uorders = uorder[0]
            e.add_field(name="Заказы:", value=uorders)
        e.set_thumbnail(url = user.avatar)
        await ctx.reply(embed=e)


    @commands.Cog.listener()
    async def on_member_join(self, member):

        e = disnake.Embed(
            title=title,
            description=description,
            color=disnake.Colour.random()
        )
        e.set_thumbnail(url=member.avatar)
        e.set_footer(text=f"Теперь нас {len(member.guild.members)} членов.")
        await self.bot.get_channel(1269342064169189417).send(embed=e)
    @commands.Cog.listener()
    async def on_member_remove(self, member):



        b = disnake.Embed(
            title=title,
            description=description,
            color=disnake.Colour.random()
        )
        b.set_thumbnail(url=member.avatar)
        b.set_footer(text=f"Теперь нас {len(member.guild.members)} членов.")
        await self.bot.get_channel(1269342064169189417).send(embed=b)


def setup(bot: commands.Bot):
    bot.add_cog(OrdersCog(bot))