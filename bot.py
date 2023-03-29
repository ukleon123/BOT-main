import discord
from searched import Searched, StockUp
from stateping import StatusPing
from servercheck import port_Check
from discord.ext import commands
import config


app = commands.Bot(command_prefix='?')
server = port_Check(config.ip, 25565)     
@app.command()
async def 멘션(ctx, *args):
        
        user = config.userId[args[0]]

        num = 30
        for i in range(num):
                await ctx.send(user)       

@app.command()
async def 실검(ctx):
        searched = Searched()
        data, link = searched.getData()
        embed = discord.Embed(title= "실시간 검색어(Naver)", color = 0xFF6F61)
        for idx in range(10):
                embed.add_field(name= str(idx + 1), value = '['+ data[idx] +'](<' + link[idx] + '>)', inline = True)
        await ctx.send(embed = embed)
@app.command()
async def 주식(ctx):
        stockup = StockUp()
        data, links = stockup.getData()
        embed = discord.Embed(title = "많이 오른 주식", color = 0xFF6F61)
        for i in range(10):
                temp = ' 가격: ' + data[i][0] +'변동룰: ' + data[i][1] + '%' + '[링크](<' + links[i] + '>)'
                embed.add_field(name = data[i][2], value = temp, inline = False)
        await ctx.send(embed = embed)



@app.command()
async def 서버확인(ctx):
        state = server.check_port()
        name = config.name
        if state == 1:
                status = StatusPing()
                data = status.get_status()
                if data.get('players').get('online') == 0:
                        await ctx.send("열렸는데 아무도 안하네...")
                else:
                        await ctx.send("서버 열려있고!")
                        for player in data.get('players').get('sample'):
                                await ctx.send(name[player.get('name')])
                        if data.get('players').get('online') == 1:
                                await ctx.send("얘가 들어있네")
                        else:
                                await ctx.send("얘네가 들어있네")
        else:
                await ctx.send("서버 안열림..")
@app.command()
async def 모드확인(ctx):
        msg = ''
        state = server.check_port()
        if state == 1:
                status = StatusPing()
                data = status.get_status()
                for mod in data.get('modinfo').get('modList') :
                        msg += '모드이름: ' + mod.get('modid') + ' 모드 버전: ' + mod.get('version') + '\n'
                await ctx.send(msg)
        else:
                await ctx.send("서버 안열려서 확인 못함 ㅠ..")
app.run(config.token)