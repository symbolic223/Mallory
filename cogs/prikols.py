import asyncio
import platform
import random
import disnake
from disnake.ext import tasks, commands

replies = ['Нахуй иди', 'Хули орешь?', 'Купи мою подписку на ютубе! Будешь смотреть мои сюжеты первым!', 'Я тебя забаню, падла']
class PrikolsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.status.start()

    
    @commands.command()
    @commands.is_nsfw()
    async def services(self, ctx, action: str = commands.Param(choices=['Минет', 'Анал', 'Дрочка', '69'])):
        if action.lower() == 'минет':
            await ctx.send(f'**Меллори**: Ну... приступаю')
            await asyncio.sleep(3)
            await ctx.send(f'**Меллори**: *снимает штаны {ctx.author.name}*')
            await asyncio.sleep(3)
            await ctx.send(f'**Меллори**: *жестко облизывает хуй и яйца*')
            await asyncio.sleep(3)
            await ctx.send(f'**Меллори**: _Ну что, нравится?_')
            await asyncio.sleep(3)
            await ctx.send(f'**Меллори**: *жестко заглатывет и трогает яйца*')
            await asyncio.sleep(3)
            await ctx.send('*проходит 5 минут*')
            await ctx.send(f'**Меллори**: *надрачивает*')
            await asyncio.sleep(3)
            await ctx.send(f'**Меллори**: _Обосперми мне лицо!_')
            await asyncio.sleep(3)
            await ctx.send(f'**{ctx.author.name}**: *кончил на еблет*')
            await asyncio.sleep(1)
            await ctx.send(f'**Меллори**: *еблет в сперме*')
            await asyncio.sleep(3)
            await ctx.send(f'**Меллори**: Всё, с тебя 300 бачей, сучка')
            
        elif action.lower() == 'анал':
            await ctx.send(f'> **Меллори**: Ммм... Ну давай, хули')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: *раздевается*')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: *трясет жопой*')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: _Чего ждем, ковбой?_')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *надевает гандон*')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *водит хуем по очку*')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *вставляет и начинает трахать*')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: **АХ! ДАВАЙ, ТРАХАЙ МЕНЯ!**')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: _Ну че, сука, нравится?_')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: _О, да, продолжай...._')
            await asyncio.sleep(3)
            await ctx.send('*прошло полчаса, Меллори вся потекла*')
            await ctx.send(f'- **{ctx.author.name}**: *достает хуй и начинает дрочить*')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: *открыла рот и ждет спермы*')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *жестко кончает в рот Меллори*')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: *весь рот и лицо в сперме*')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: _Неплохой у тебя револьвер, ковбой, а теперь гони 900 бачей нахуй_')
            
        elif action.lower() == 'дрочка':
            await ctx.send('> **Меллори**: Тебя это так заводит? Окей..')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: *встаёт на колени*')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: *снимает штаны с {ctx.author.name}*')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: *люто надрачивает хуёк {ctx.author.name}*')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: Да... Продолжай в том же духе, шлюшка.')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: _Да, мой господин!~_')
            await asyncio.sleep(3)
            await ctx.send(f'*проходит 20 минут, {ctx.author.name} на грани завершения*')
            await ctx.send('> **Меллори**: _Кончи мне в носяру, ты же так этого хочешь!_')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *кончил в носяру*')
            await asyncio.sleep(1)
            await ctx.send('> **Меллори**: *захлёбывается в сперме*')
            await asyncio.sleep(3)
            await ctx.send('> **Меллори**: Не забываемые *откашливается* ощущения... С тебя 1400 бачей за такой крутой мув, сынок')
            
        elif action == '69':
            await ctx.send('> **Меллори**: Ну, давай, раздевайся...')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори и {ctx.author.name}**: *раздеваются и сосутся*')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: *ложится на {ctx.author.name} и начинает сосать писюнчик*')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *активно лижет пиздёнку Меллори*')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: Давай... лижи мою пизду, сучка!')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *подходит к вальгалле*')
            await ctx.send(f'> **Меллори**: *чувствует это и начинает активно дрочить, насаживаясь пиздой на еблет {ctx.author.name}*')
            await asyncio.sleep(3)
            await ctx.send(f'- **{ctx.author.name}**: *обкончал весь еблет Меллори*')
            await asyncio.sleep(1)
            await ctx.send('> **Меллори**: *проглотила все до единой капли*')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: *ебейше сквиртанула на еблет {ctx.author.name}*')
            await asyncio.sleep(3)
            await ctx.send(f'> **Меллори**: *Как же я ебейше тебя намочила, {ctx.author.name}, давай свои 2200 бачей, а то после этого мне нужно идти жестко гантели 20 кг поднимать.*')
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
        
        if (self.bot.user.mention) in message.content:
            await message.reply(random.choice(replies))
            await message.add_reaction("🖕")
            await message.add_reaction("🅿️")
            await message.add_reaction("🇮")
            await message.add_reaction("🇩")
            await message.add_reaction("🇴")
            await message.add_reaction("🇷")
            return

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


















