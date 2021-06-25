import os
from discord.ext import commands
from apis.cpp_code_compiler import compiler


class CppCompiler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def run_cpp(self, ctx, *, arg):
        code = [(item+'\n') for item in (''.join(list(arg))).split('\n')]
        code_file = open('files/cpp_source_code.cpp', 'w')
        code_file.writelines(code[1:-1])
        code_file.close()
        os.system('astyle --style=allman ./files/cpp_source_code.cpp')
        code_file = open('files/cpp_source_code.cpp', 'r')
        await ctx.send(f"**Output:**\n```yaml\n{compiler(code=code_file.read())['output']}```")
        code_file.close()


def setup(bot):
    bot.add_cog(CppCompiler(bot))
