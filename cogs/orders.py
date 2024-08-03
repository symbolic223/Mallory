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
cursor.execute('''CREATE TABLE IF NOT EXISTS welcome (
                title TEXT,
                description TEXT
)
                
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS bye (
                title TEXT,
                description TEXT
)

''')

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
    @commands.slash_command(name = "welcome", description="прив)")
    @commands.has_permissions(ban_members = True)
    async def welcome(self, inter: disnake.ApplicationCommandInteraction, title: str, description: str):
        cursor.execute("SELECT title, description FROM welcome")
        welcome = cursor.fetchone()
        if welcome == []:
            cursor.execute("INSERT INTO welcome VALUES (?, ?)", (title, description))
            conn.commit()
            await inter.send("Сохранено")
        else:
            cursor.execute("UPDATE welcome SET title = ?, description = ?", (title, description))
            conn.commit()
            await inter.send("Сохранено")

    @commands.slash_command(name="bye", description="прив)")
    @commands.has_permissions(ban_members=True)
    async def bye(self, inter: disnake.ApplicationCommandInteraction, title: str, description: str):
        cursor.execute("SELECT title, description FROM bye")
        welcome = cursor.fetchone()
        if welcome == []:
            cursor.execute("INSERT INTO bye VALUES (?, ?)", (title, description))
            conn.commit()
            await inter.send("Сохранено")
        else:
            cursor.execute("UPDATE bye SET title = ?, description = ?", (title, description))
            conn.commit()
            await inter.send("Сохранено")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        cursor.execute("SELECT title, description FROM welcome")
        welcome = cursor.fetchone()
        if welcome == []:
            return
        if welcome:
            title, description = welcome
            if '{user.name}' in description:
                description = description.format(user=member)
            if '{user.name}' in title:
                title = title.format(user=member)
            e = disnake.Embed(
                title=title,
                description=description,
                color=disnake.Colour.random()
            )
            e.set_thumbnail(url=member.avatar)
            e.set_footer(text=f"Теперь нас {len(member.guild.members)} членов.")
            await self.bot.get_channel(1221283286710485113).send(embed=e)
    @commands.Cog.listener()
    async def on_member_remove(self):
        cursor.execute("SELECT title, description FROM bye")
        bye = cursor.fetchone()
        if bye == []:
            return
        if bye:
            title, description = bye
            if '{user.name}' in description:
                description = description.format(user=member)
            if '{user.name}' in title:
                title = title.format(user=member)
            e = disnake.Embed(
                title=title,
                description=description,
                color=disnake.Colour.random()
            )
            e.set_thumbnail(url=member.avatar)
            e.set_footer(text=f"Теперь нас {len(member.guild.members)} членов.")
            await self.bot.get_channel(1221283286710485113).send(embed=e)

def setup(bot: commands.Bot):
    bot.add_cog(OrdersCog(bot))