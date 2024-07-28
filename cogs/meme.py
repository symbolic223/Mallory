import disnake
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io
class MemeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.slash_command(name="meme", description="Сгенерировать мем")
    async def memegen(self, inter: disnake.ApplicationCommandInteraction, img: disnake.Attachment, *, toptext: str, bottomtext: str = None):
        if bottomtext is None:
            bottomtext = toptext

        image = Image.open(io.BytesIO(await img.read()))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("impact.ttf", 100)

        top_text_bbox = draw.textbbox((0, 0), toptext, font=font)
        top_text_width = top_text_bbox[2] - top_text_bbox[0]
        top_text_height = top_text_bbox[3] - top_text_bbox[1]
        top_x = (image.width - top_text_width) / 2
        top_y = 10
        draw.text((top_x, top_y), toptext, font=font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
        bottom_text_bbox = draw.textbbox((0, 0), bottomtext, font=font)
        bottom_text_width = bottom_text_bbox[2] - bottom_text_bbox[0]
        bottom_text_height = bottom_text_bbox[3] - bottom_text_bbox[1]
        bottom_x = (image.width - bottom_text_width) / 2
        bottom_y = image.height - bottom_text_height - 35
        draw.text((bottom_x, bottom_y), bottomtext, font=font, fill=(255, 255, 255), stroke_width=2,
                  stroke_fill=(0, 0, 0))

        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)

        await inter.send(file=disnake.File(buffered, filename="meme.png"))


def setup(bot: commands.Bot):
    bot.add_cog(MemeCog(bot))