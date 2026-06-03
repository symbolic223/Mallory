import asyncio
import platform
import random
import disnake
from disnake.ext import tasks, commands
import sqlite3

conn = sqlite3.connect("Orders.db")
cursor = conn.cursor()

fuck = [
    "https://cdn.discordapp.com/attachments/1221283286710485113/1264555298375598091/z_3.gif?ex=669e4c65&is=669cfae5&hm=0ec4e60315ed48e1500b741dea9a889e833f224f9452998d2ed1518a5c1181a2&",
    "https://cdn.discordapp.com/attachments/1221283286710485113/1264555298811678841/z_2.gif?ex=669e4c65&is=669cfae5&hm=332b450adc8233e4e627586b4cb036cb183df665a5a8cf4f31c476a3b4075c0d&",
    "https://cdn.discordapp.com/attachments/1221283286710485113/1264555299298345113/z_1.gif?ex=669e4c65&is=669cfae5&hm=6625a957b4e7de0efa2f6900f0785a3fae66d6b396e25883c3ac14df6a9852ed&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1266313879215013978/1634125740_genshin_impact-keqing2.gif?ex=66a4b233&is=66a360b3&hm=d6ef6e6e45e1358da3515cfdd06684ec0ec61329f15363436f68a849993b7842&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1272670512471998475/902a86fb-8968-4e81-980f-0c4a14f3b4ae.gif?ex=66bc7b07&is=66bb2987&hm=25798fdb606c0fc0dfe5f90e9af1cc18ee04d20617fe0b28f30f8168d4fe4e66&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1272670495183208478/20ad0a93-ef94-4a91-9262-c364387fedc8.gif?ex=66bc7b03&is=66bb2983&hm=3013e71962147c2a117f051f4a079f9496f52345d842a3a004398b52bde6aff1&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1272670458017484922/vhms1i0jh2541.gif?ex=66bc7afa&is=66bb297a&hm=b27c8a095361c92a86e4da12de8d39736ab9f6a986d0d2924c10271bca859056&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1272670438941528086/5c0cb97e-175b-4eaf-92d1-51f56be2ae72.gif?ex=66bc7af5&is=66bb2975&hm=41000dc1710be28510dcd730d38d1ed6e7be2c058becc5a0abb41c3b2916ca55&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1272670424433426523/2feb2e63-ddfb-4cfa-9cff-0e23e6093e3e.gif?ex=66bc7af2&is=66bb2972&hm=8345032975230c27b1d5346f2e4b3a338b8967ced4c62270488ba7c7c8ac7a99&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1272670411917889576/2edf4021-801a-4cfa-b78a-d2e1f82d762c.gif?ex=66bc7aef&is=66bb296f&hm=fed0e9ff0b253c1d63526c68d6e03896a6ccc9d7ddee4adab697e43ee26f120f&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1272670385497702521/3cfe1373-da53-4208-9f00-65a4202e0d67.gif?ex=66bc7ae8&is=66bb2968&hm=0228579a8103c10184fa5f4d487f2c16d93bb87ec404aebc36ffd6c6a037c890&",
    "https://media.discordapp.net/attachments/827289915388985404/1178171866884612106/28.gif?ex=6777fece&is=6776ad4e&hm=d099933d2261d9723a7847fa276fbefad67c4eaa793187a47a0c359a029c4061&",
    "https://media.discordapp.net/attachments/827289915388985404/1031442011334639646/1665985332730.gif?ex=6778217a&is=6776cffa&hm=a5b9b6f3188a8865871e1d10d8ce85d44cad382ece57090a4e2f000b4f0da309&",
    "https://cdn.donmai.us/original/19/dd/19dd4e2d45356f22afc77fef77573f3c.gif"
]
suck = [
    "https://cdn.discordapp.com/attachments/667029937676615723/1264555887255752704/tumblr_o4a47pYNGR1uao6a1o2_400.gif?ex=669e4cf1&is=669cfb71&hm=34af47332de7b2994332169b354b3f3901b9c3fb1306225e3c04b30fcd69264e&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1264555949973311519/14e4b8c33533b6a1bb2ee3b82114a5cf1b9fd3a6.gif?ex=669e4d00&is=669cfb80&hm=91cf298ff6f61135af12240593e0e520386ebf204297d16cd0cf096845925c93&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1264555979840946227/sucking6.gif?ex=669e4d07&is=669cfb87&hm=f2737c79c31ae0a87042c30d030fe0244d6fa24c4ad9103172dd75096b7f00a6&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1269762624678264904/c210d50b-5691-4dee-a4c4-cac0902be564.gif?ex=66b13e18&is=66afec98&hm=b6579c0c7a7df59ac20c1a116ea3f95c148769e122697454a1d206fa0ae2f64d&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1270867418473828353/0085361146e87e6039c9db704efee723.gif?ex=66b73d44&is=66b5ebc4&hm=135a850d37a66f375d3db41ea64036b718d2da6943f4c3f32e52f14b91ecbd83&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1270855216518004747/d1be215c92594c0183697e13cbb2afed.gif?ex=66b731e6&is=66b5e066&hm=89e992d90b2f80be47b75216132f2cd9f13480b01ea40a71ef7eccc04f89880a&",
    "https://cdn.discordapp.com/attachments/667029937676615723/1270854839781429299/79a22912fe6578724a3f1d8219cc86ab.gif?ex=66b7318d&is=66b5e00d&hm=8966b1ecbd39222b67eb7241441efa81fcbc5babcd956913983ae0296b78b817&"
]
rfooter = ['Когда $екс?', 'Бойкиссер - чмо', 'Чем ближе крах империи тем безумнее ее законы', '{user1.display_name} долбоеб!', 'Поебитесь уже, голубки']

replies = ['Нахуй иди', 'Хули орешь?', 'Купи мою подписку на ютубе! Будешь смотреть мои сюжеты первым!', 'Я тебя забаню, падла']
class PrikolsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.status.start()


    @commands.slash_command(name = "ship", description = "Когда половые отношения?")
    @commands.is_nsfw()
    async def ship(self, inter, user1: disnake.Member, user2: disnake.Member):
        a = random.randint(0, 100)
        if user1 == user2:
            await inter.response.send_message("Ну и иди соси сам себе")
            return
        elif user1 == self.bot.user or user2 == self.bot.user:
            await inter.response.send_message("Я и так тебя найду и выебу)))")
            return
        e = disnake.Embed(
            title = f"{user1.display_name} и {user2.display_name} любят друг друга на {a}%",
            description=f"Если они забудут гандоны, то их отгрызка будут звать: {user1.display_name[:4] + user2.display_name[-5:]}",
            color = 0xff009e
        )
        f = random.choice(rfooter)
        if '{user1.display_name}' in f:
            f = f.replace('{user1.display_name}', user1.display_name)
        e.set_footer(text = f, icon_url = self.bot.user.avatar.url)
        await inter.response.send_message(embed = e)


    @commands.command()
    @commands.is_nsfw()
    async def fuck(self, ctx, user: disnake.Member):
        e = disnake.Embed(
            title = f"{ctx.author.display_name} выебал Меллори" if user == self.bot.user else f'{ctx.author.display_name} выебал сам себя' if user == ctx.author else f"{ctx.author.display_name} выебал {user.display_name}",
            color = 0x9B00FF
        )
        e.set_image(url=random.choice(fuck))
        await ctx.send(embed=e)

    @commands.command()
    @commands.is_nsfw()
    async def suck(self, ctx, user: disnake.Member):
        e = disnake.Embed(
            title=f"{ctx.author.display_name} отсосал Меллори" if user == self.bot.user else f'{ctx.author.display_name} отсосал сам себе' if user == ctx.author else f"{ctx.author.display_name} отсосал {user.display_name}",
            color=0x9B00FF
        )
        e.set_image(url=random.choice(suck))
        await ctx.send(embed=e)

    @commands.slash_command(name="ping", description="Показывает пинг бота.")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Пинг бота: {round(self.bot.latency * 1000)}ms")

    @commands.command()
    @commands.is_nsfw()
    async def order(self, ctx, user: disnake.User):
        cursor.execute("SELECT orders_count FROM uorders WHERE user_id = ?", (ctx.author.id,))
        uorder = cursor.fetchone()
        if user.id == ctx.author.id:
            await ctx.send('Еблан, я на тебя заказ выполнять не буду.')
            return
        if user.id == self.bot.user.id:
            await ctx.send("иди нахуй, паскуда")
            return
        await ctx.send("Связываюсь с сучкой...")
        try:
            babax = await user.send(f"Пользователь {ctx.author.mention} заказал вам меня. Не желаете развлечься? (на размышление 30 секунд)")
            await babax.add_reaction("✅")
            await babax.add_reaction("❌")

            def check(reaction, u):
                return u == user and str(reaction.emoji) in ["✅", "❌"] and reaction.message.id == babax.id
            try:
                reaction, u = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                if str(reaction.emoji) == "✅":
                    await ctx.send(f"Сучка на {user.name} одобрил выполнение заказика, щас как высушу ему писюнчик нахуй.")
                    await user.send(f'> **Меллори**: Ммм... Ну давай, хули')
                    await asyncio.sleep(3)
                    await user.send(f'> **Меллори и {user.name}**: *раздеваются*')
                    await asyncio.sleep(3)
                    await user.send(f'> **Меллори**: *начинает отсасывать хуй {user.name}')
                    await asyncio.sleep(3)
                    await user.send('> *прошло 5 минут*')
                    await asyncio.sleep(3)
                    await user.send('- **Меллори**: *ложится на кровать*')
                    await asyncio.sleep(3)
                    await user.send(f'- **{user.name}**: *водит хуем по пиздёнке*')
                    await asyncio.sleep(3)
                    await user.send(f'- **{user.name}**: *вставляет и начинает трахать*')
                    await asyncio.sleep(3)
                    await user.send('> **Меллори**: **АХ! ДАВАЙ, ТРАХАЙ МЕНЯ!**')
                    await asyncio.sleep(3)
                    await user.send(f'- **{user.name}**: _Ну че, сука, нравится?_')
                    await asyncio.sleep(3)
                    await user.send('> **Меллори**: _О, да, продолжай...._')
                    await asyncio.sleep(3)
                    await user.send('*прошло полчаса, Меллори вся потекла*')
                    await user.send('> **Меллори**: _Прошу, кончи в меня!!_')
                    await asyncio.sleep(3)
                    await user.send(f'- **{user.name}**: *готов кончить*')
                    await asyncio.sleep(3)
                    await user.send(f'> **Меллори**: *очень громко стонет*')
                    await asyncio.sleep(3)
                    await user.send(f'- **{user.name}**: *обкончал всю пизду Меллори*')
                    await asyncio.sleep(3)
                    await user.send(f'> **Меллори**: _Ну че, скажи спасибо {ctx.author.mention}. А я пошла еще с кем-нибудь поебусь._')
                    await ctx.send(f'Успешно ~~трахнула~~ выполнила заказ на {user.mention}.')

                elif str(reaction.emoji) == "❌":
                    await ctx.reply(f'Этот пидор отказался. Ну и больно надо трахаться с такими.')
                else:
                    pass

            except asyncio.TimeoutError:
                await ctx.reply(f'Короче, он не ответил вовремя. Ну и хуй с ним, с другим поебусь.')
        except:
            await ctx.reply("К сожалению, этому еблану не удалось написать.")
        if uorder is None:
            cursor.execute("INSERT INTO uorders (user_id, orders_count) VALUES (?, 1)", (ctx.author.id, ))
        else:
            cursor.execute("UPDATE uorders SET orders_count = orders_count + 1 WHERE user_id = ?", (ctx.author.id,))
        conn.commit()


    @commands.command()
    @commands.is_nsfw()
    async def services(self, ctx, action: str = commands.Param(choices=['Минет', 'Анал', 'Дрочка', '69'])):
        cursor.execute("SELECT orders_count FROM orders WHERE user_id = ?", (ctx.author.id,))
        order = cursor.fetchone()
        if action.lower() == 'минет':
            msg = await ctx.send(f'**Меллори**: Ну... приступаю')
            await asyncio.sleep(3)
            await msg.edit(f'**Меллори**: *снимает штаны {ctx.author.name}*')
            await asyncio.sleep(3)
            await msg.edit(f'**Меллори**: *жестко облизывает хуй и яйца*')
            await asyncio.sleep(3)
            await msg.edit(f'**Меллори**: _Ну что, нравится?_')
            await asyncio.sleep(3)
            await msg.edit(f'**Меллори**: *жестко заглатывет и трогает яйца*')
            await asyncio.sleep(3)
            await msg.edit('*проходит 5 минут*')
            await msg.edit(f'**Меллори**: *надрачивает*')
            await asyncio.sleep(3)
            await msg.edit(f'**Меллори**: _Обосперми мне лицо!_')
            await asyncio.sleep(3)
            await msg.edit(f'**{ctx.author.name}**: *кончил на еблет*')
            await asyncio.sleep(1)
            await msg.edit(f'**Меллори**: *еблет в сперме*')
            await asyncio.sleep(3)
            await msg.edit(f'**Меллори**: Всё, с тебя 300 бачей, сучка')
            if order is None:
                cursor.execute("INSERT INTO orders (user_id, orders_count) VALUES (?, 1)", (ctx.author.id, ))
                conn.commit()
            else:
                orders = order[0]
                orders += 1
                cursor.execute("UPDATE orders SET orders_count = ? WHERE user_id = ?", (orders, ctx.author.id))
                conn.commit()

        elif action.lower() == 'анал':
            msg = await ctx.send(f'> **Меллори**: Ммм... Ну давай, хули')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: *раздевается*')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: *трясет жопой*')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: _Чего ждем, ковбой?_')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *надевает гандон*')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *водит хуем по очку*')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *вставляет и начинает трахать*')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: **АХ! ДАВАЙ, ТРАХАЙ МЕНЯ!**')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: _Ну че, сука, нравится?_')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: _О, да, продолжай...._')
            await asyncio.sleep(3)
            await msg.edit('*прошло полчаса, Меллори вся потекла*')
            await msg.edit(f'- **{ctx.author.name}**: *достает хуй и начинает дрочить*')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: *открыла рот и ждет спермы*')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *жестко кончает в рот Меллори*')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: *весь рот и лицо в сперме*')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: _Неплохой у тебя револьвер, ковбой, а теперь гони 900 бачей нахуй_')
            if order is None:
                cursor.execute("INSERT INTO orders (user_id, orders_count) VALUES (?, 1)", (ctx.author.id, ))
                conn.commit()
            else:
                orders = order[0]
                orders += 1
                cursor.execute("UPDATE orders SET orders_count = ? WHERE user_id = ?", (orders, ctx.author.id))
                conn.commit()

        elif action.lower() == 'дрочка':
            msg = await ctx.send('> **Меллори**: Тебя это так заводит? Окей..')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: *встаёт на колени*')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: *снимает штаны с {ctx.author.name}*')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: *люто надрачивает хуёк {ctx.author.name}*')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: Да... Продолжай в том же духе, шлюшка.')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: _Да, мой господин!~_')
            await asyncio.sleep(3)
            await msg.edit(f'*проходит 20 минут, {ctx.author.name} на грани завершения*')
            await msg.edit('> **Меллори**: _Кончи мне в носяру, ты же так этого хочешь!_')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *кончил в носяру*')
            await asyncio.sleep(1)
            await msg.edit('> **Меллори**: *захлёбывается в сперме*')
            await asyncio.sleep(3)
            await msg.edit('> **Меллори**: Не забываемые *откашливается* ощущения... С тебя 1400 бачей за такой крутой мув, сынок')
            if order is None:
                cursor.execute("INSERT INTO orders (user_id, orders_count) VALUES (?, 1)", (ctx.author.id, ))
                conn.commit()
            else:
                orders = order[0]
                orders += 1
                cursor.execute("UPDATE orders SET orders_count = ? WHERE user_id = ?", (orders, ctx.author.id))
                conn.commit()

        elif action == '69':
            msg = await ctx.send('> **Меллори**: Ну, давай, раздевайся...')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори и {ctx.author.name}**: *раздеваются и сосутся*')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: *ложится на {ctx.author.name} и начинает сосать писюнчик*')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *активно лижет пиздёнку Меллори*')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: Давай... лижи мою пизду, сучка!')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *подходит к вальгалле*')
            await msg.edit(f'> **Меллори**: *чувствует это и начинает активно дрочить, насаживаясь пиздой на еблет {ctx.author.name}*')
            await asyncio.sleep(3)
            await msg.edit(f'- **{ctx.author.name}**: *обкончал весь еблет Меллори*')
            await asyncio.sleep(1)
            await msg.edit('> **Меллори**: *проглотила все до единой капли*')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: *ебейше сквиртанула на еблет {ctx.author.name}*')
            await asyncio.sleep(3)
            await msg.edit(f'> **Меллори**: *Как же я ебейше тебя намочила, {ctx.author.name}, давай свои 2200 бачей, а то после этого мне нужно идти жестко гантели 20 кг поднимать.*')
            if order is None:
                cursor.execute("INSERT INTO orders (user_id, orders_count) VALUES (?, 1)", (ctx.author.id, ))
                conn.commit()
            else:
                orders = order[0]
                orders += 1
                cursor.execute("UPDATE orders SET orders_count = ? WHERE user_id = ?", (orders, ctx.author.id))
                conn.commit()
        else:
            await ctx.send('Абалдуй, у меня нет такой услуги. Я могу делать: минет, анал, дрочку или 69. А то что ты попросил это просто пиздец какой-то иди нахуй.')

    @commands.slash_command(name="stats", description="Я шлюха")
    @commands.has_permissions(ban_members = True)
    async def stats(self, inter: disnake.ApplicationCommandInteraction):
        footer = ['Пошел нахуй!', 'Poshel nahui', '!йухан лешоП']

        formatted_time = f"<t:{int(self.bot.start_time)}:R>"
        commands = len(inter.bot.commands) + len(inter.bot.slash_commands)
        guilds = len(self.bot.guilds)

        import_info = [
            f'~~Стою на трасе~~ Работаю __**{formatted_time}**__',
            f'Версия: __6.9__'
        ]

        about_bot_info = [
            f"__**Python {platform.python_version()}**__",
        ]

        other_info = [
            f"Кол-во хуев: __**{commands}**__",
            f"Кол-во борделей: __**{guilds}**__",
        ]

        emb = disnake.Embed(title="Мои оценки в стрип клубе", color=disnake.Color.gold())
        emb.add_field(name="> Стаж", value='\n'.join(import_info), inline=False)
        emb.add_field(name="> Язык ~~в жопе~~ программирования", value='\n'.join(about_bot_info), inline=False)
        emb.add_field(name="> А дальше нахуй иди", value='\n'.join(other_info), inline=False)
        emb.set_thumbnail(url=self.bot.user.avatar.url)
        emb.set_footer(text=random.choice(footer), icon_url=self.bot.user.avatar)
        await inter.send(embed=emb)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if (self.bot.user.mention) in message.content and 'order' not in message.content and 'fuck' not in message.content and 'suck' not in message.content:
            await message.reply(random.choice(replies))
            await message.add_reaction("🖕")
            await message.add_reaction("🅿️")
            await message.add_reaction("🇮")
            await message.add_reaction("🇩")
            await message.add_reaction("🇴")
            await message.add_reaction("🇷")
            return
        #self.bot.process_commands(message)

    @tasks.loop(seconds = 10)
    async def status(self):
        all_members = []
        for guild in self.bot.guilds:
            all_members.extend(guild.members)

        if all_members:
            member = random.choice(all_members)
            await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f'на аппарат {member.name}'))

    @status.before_loop
    async def before_status(self):
        await self.bot.wait_until_ready()

    def cog_unload(self):
        self.status.cancel()

def setup(bot: commands.Bot):
    bot.add_cog(PrikolsCog(bot))