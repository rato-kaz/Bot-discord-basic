from discord.ext import commands

def is_owner():
    def predicate(ctx):
        return ctx.author.id == int(os.getenv("OWNER_ID"))
    return commands.check(predicate)
