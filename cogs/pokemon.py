import disnake
from disnake.ext import commands
import pokebase as pb

class PokemonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pok(self, ctx, number: int):
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
                color=disnake.Color.green()
            )

            embed.add_field(name="Имя", value=name, inline=True)
            embed.add_field(name="Пол", value=gender, inline=True)
            embed.add_field(name="Типы", value=types, inline=True)

            if sprite_url:
                embed.set_thumbnail(url=sprite_url)
            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"Произошла ошибка: {str(e)}")


def setup(bot: commands.Bot):
    bot.add_cog(PokemonCog(bot))
