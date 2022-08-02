from redbot.core import commands

class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        if message.content.startswith('https://discord.gg'):
      await message.delete()
      await message.author.send("This Is What Is Will DM The User That Sent The Link")
        await ctx.send("I can do stuff!")
        
