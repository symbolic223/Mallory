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
        if order == None:
            await ctx.reply("Не нашла челикса в таблице. Пускай заказ сделает чтоле.")
            return

        else:
            orders = order[0]
            e = disnake.Embed(
                title="Кол-во ваших заказов" if user == ctx.author else f"Кол-во заказов пользователя {user.name}",
                color=0xFF00E4
            )
            e.add_field(name="Я трахнула тебя:" if user == ctx.author else f"Я трахнула его:", value=f"{orders} раз")
            if uorder == None:
                e.add_field(name="Заказы:", value="Пользователь не делал заказов.")
            else:
                uorders = uorder[0]
                e.add_field(name="Заказы:", value=uorders)
            e.set_thumbnail(url = user.avatar)
            await ctx.reply(embed=e)

def setup(bot: commands.Bot):
    bot.add_cog(OrdersCog(bot))