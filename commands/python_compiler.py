import os
from discord.ext import commands
from apis.py_code_compiler import compiler


class PythonCompiler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def run_python(self, ctx, *, arg):
        code = [(item+'\n') for item in (''.join(list(arg))).split('\n')]
        code_file = open('files/py_source_code.py', 'w')
        code_file.writelines(code[1:-1])
        code_file.close()
        os.system('black ./files/py_source_code.py')
        code_file = open('files/py_source_code.py', 'r')
        await ctx.send(f"**Output:**\n```yaml\n{compiler(code=code_file.read())['output']}```")
        code_file.close()


def setup(bot):
    bot.add_cog(PythonCompiler(bot))
