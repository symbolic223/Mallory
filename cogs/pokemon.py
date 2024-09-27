import disnake
from disnake.ext import commands
import pokebase as pb
import random
class PokemonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pok(self, ctx, number: int):
        male_percentage = 0
        female_percentage = 0
        if number >= 1026:
            j = disnake.Embed(
                title="Информация о покемоне: Danil Demin",
                color=0x00f3ff
            )
            j.add_field(name="Имя:", value="Данил Дёмин", inline=True)
            j.add_field(name="Ориентация:", value="Пидорок", inline=True)
            j.add_field(name="Типы:", value="Гений, миллиардер, плейбой, филантроп", inline=True)
            j.add_field(name="Можно ебать?", value="Нужно", inline=True)
            j.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1221283286710485113/1289138530244886548/0320b707c4a05dc7.png?ex=66f7bb50&is=66f669d0&hm=c17e667ecd5adebb90d56109471f37c71a0ca03705d60359a4470034c0cbda50&")
            await ctx.send(embed = j)
            return

        try:
            pokemon = pb.pokemon(number)
            name = pokemon.name.capitalize()
            gender_rate = pb.pokemon_species(number).gender_rate
            if gender_rate == -1:
                gender = "Пол не определен"
            else:
                male_percentage = (8 - gender_rate) * 12.5
                female_percentage = gender_rate * 12.5
                gender = f"Мужской: {male_percentage}%, Женский: {female_percentage}%"


            types = ", ".join([t.type.name.capitalize() for t in pokemon.types])


            sprite_url = pokemon.sprites.front_default


            embed = disnake.Embed(
                title=f"Информация о покемоне: {name}",
                color=disnake.Color.blue() if male_percentage > female_percentage else 0xff00c1 if male_percentage < female_percentage else 0x8000ff
            )

            embed.add_field(name="Имя", value=name, inline=True)
            embed.add_field(name="Пол", value=gender, inline=True)
            embed.add_field(name="Типы", value=types, inline=True)
            embed.add_field(name="Можно ебать?", value = "Да" if female_percentage > male_percentage else "Возможно" if female_percentage == male_percentage else "Нет", inline=True)


            if sprite_url:
                embed.set_thumbnail(url=sprite_url)
            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"Произошла ошибка: {str(e)}")


def setup(bot: commands.Bot):
    bot.add_cog(PokemonCog(bot))
