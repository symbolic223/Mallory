import disnake
from disnake.ext import commands
import sqlite3

conn = sqlite3.connect("Orders.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                user_id INTEGER PRIMARY KEY,
                orders_count INTEGER
)''')

class OrdersCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def count(self, ctx, user: disnake.User):
        cursor.execute("SELECT orders_count FROM orders WHERE user_id = ?", (user.id, ))
        order = cursor.fetchone()
        if order == None:
            await ctx.reply("Не нашла челикса в таблице. Пускай заказ сделает чтоле.")
            return
        else:
            orders = order[0]
            e = disnake.Embed(
                title=f"Кол-во заказов пользователя {user.name}",
                color=0xFF00E4
            )
            e.add_field(name="Я трахнула его:", value=f"{orders} раз")
            await ctx.reply(embed=e)

def setup(bot: commands.Bot):
    bot.add_cog(OrdersCog(bot))