#public version invite link:
#https://discord.com/api/oauth2/authorize?client_id=1159384275532132423&permissions=9882683571440&scope=bot

#Thanks to JT.0 for supporting this project

#基本解釋
#@bot.slash_command(name = "名稱", description = "描述")    //宣告一個新的指令
#async def 定義名字(定義名字, a: str, b: str):              //定義指令動作，給名字，a / b為輸入框
#await wmemo.response.send_message('傳送訊息')             //當指令被呼叫時，回覆字串
    
'''
please pip install listed down below:
discord
python-dotenv
py-cord
pycord
requests
'''
import discord
import os
import random
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")

def bot_start():
    intents = discord.Intents.all()
    bot = discord.Bot(intents = intents)
    discord.Intents.all = True

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}\n")
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("HDNX ver 1.10.6"))

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        username = str(message.author)
        if message.attachments:
            print(f"{username}傳送了一個或多個附件")
            return
        
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username[:-2]} said '{user_message}' ({channel})")
        with open(f"{message.guild.id}.msglog.txt", 'a', encoding="utf-8") as x:
            await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Saving Logs..."))
            if x.tell() >= 3000:
                open(f"{message.guild.id}.msglog.txt", 'w', encoding="utf-8")
                x.write("")
                x.close()
            else:
                time = str(datetime.now())
                x.write(f"**{username[:-2]}** 於 **{time[:19]}** 在**[{channel}]**說：**'{user_message}'**\n")
                x.close()
                await bot.change_presence(status=discord.Status.online, activity=discord.Game("HDNX ver 1.10.6"))

        if user_message == '操':
            await message.channel.send(f'{message.author.mention} 你有躁鬱症')
        if user_message == '幹你娘':
            await message.channel.send(f'{message.author.mention} chill bruv')


    bsc = bot.slash_command
    dice = [1,2,3,4,5,6]

    @bsc(name = "狀態", description = "Bot Info")
    async def status(ctx):
            with open(f"{ctx.guild.id}.msglog.txt", 'a', encoding = "utf-8") as x:
                xl = x.tell()
                x.close()
            with open(f"{ctx.author.id}.txt", 'a', encoding = "utf-8") as mx:
                mxl = mx.tell()
                mx.close()
                await ctx.response.send_message(f"```Version Date : 2023/11/12\nCode Name: HDNX (HydrodynamicX) / ver.1.10.6 / Rose.\n本伺服器訊息Log大小：{xl}\n您的備忘錄大小：{mxl}```")
    @bsc(name = "操", description = "操")
    async def fuk(fuk, 訊息: str):
        await fuk.response.send_message(f"操！{訊息}")
    
    @bsc(name = '中二直播', description = "中二直播")
    async def chunithm(chunithm):
        await chunithm.response.send_message("https://bit.ly/46eJHWb")
    

    @bsc(name = "隨機本子random_hentai", description="隨機開啟nhentai本子(注意使用)")
    async def fuk(fuk):
        await fuk.response.send_message("本子內容不保證安全：<https://shorturl.at/jlY79>")
    @bsc(name = "編寫備忘錄write_memo", description = "輸入備忘錄")
    async def wmemo(wmemo, 標題: str, 內容: str):
        author = str(wmemo.author)
        await wmemo.response.send_message(f'**{標題}** 已被新增到備忘錄')
        with open(f"{wmemo.author.id}.txt", 'a',encoding="utf-8") as f:
            f.write(f'**[{標題}] {內容}**\n')
    
    @bsc(name = "閱讀備忘錄read_memo", description = "閱讀備忘錄")
    async def rmemo(rmemo):
        author = str(rmemo.author)
        with open(f"{rmemo.author.id}.txt", 'a+',encoding="utf-8") as f:
            with open(f"{rmemo.author.id}.txt", "r", encoding="utf-8") as t:
                await rmemo.response.send_message(f"{author[:-2]} 的筆記本：\n- - -\n{t.read()}\n**(沒了)**")
        
    @bsc(name = "清空備忘錄_clear_memo", description = "清除備忘錄")
    async def clrmem(clrmem):
        with open(f"{clrmem.author.id}.txt", 'a+',encoding="utf-8") as f:
            with open(f"{clrmem.author.id}.txt", 'w', encoding="utf-8") as x:
                x.write("")
                await clrmem.response.send_message("已清空備忘錄")

    @bsc(name = "訊息紀錄msg_log", description = "讀取伺服器聊天紀錄")
    async def log(log):
        id = log.guild.id
        with open(f"{id}.msglog.txt", "a+",encoding="utf-8") as logmes:
            with open(f"{id}.msglog.txt", "r", encoding="utf-8") as xx:
                await log.response.send_message(f'此伺服器的聊天紀錄：\n{xx.read()}')
    
    @bsc(name = "禁尻月倒數", description = "準備勝利")
    async def nnn(nnn):
        time = str(datetime.now())
        print(time)
        passhur = int((int(time[8:10]) - 1) * 24 + int(time[11:13]))
        passmin = int(passhur * 60 + int(time[14:16]))
        passsec = int(passmin * 60 + int(time[17:19]))
        remainhur = int(720 - passhur)
        remainmin = int(43200 - passmin)
        remainsec = int(2592000 - passsec)

        await nnn.response.send_message(f"> 經過時間：\n> **{passhur}**小時 或 **{passsec}**秒\n> 距離NNN結束還剩下：\n> **{remainhur}**小時\n> **{remainmin}**分鐘\n> **{remainsec}**秒\n\n`註：單位之間不是僅換算，而是取各項之整數減去經過時間，並非四捨五入`")
    @bsc(name = "骰骰子roll_a_dice" , description = "骰骰子")
    async def roll(roll):
        random.shuffle(dice)
        await roll.response.send_message(f"{dice[0]}")
        await roll.send(f"本次隨機取數結果：{dice}")

    @bsc(name = "俄羅斯轉盤_russian_roulette", description = "緊張刺激好遊戲")
    async def rr(rr,  轉多大力: int):
        locbullet = 0
        location = 0
        random.shuffle(dice)
        power = int(轉多大力)
        if abs(power) <= 30:
            power = power % 6
            for i in range(6):
                if dice[i] == 5:
                    locbullet = i+1
            location = power + 1
            absans = abs(locbullet - location)
            if locbullet == location:
                await rr.response.send_message(f"{rr.author.mention}你中槍了 :skull: (abs = {absans}) 子彈位置：{locbullet} 彈艙位置：{location}")
            else:
                await rr.response.send_message(f"{rr.author.mention}安全下庄 :baby: (abs = {absans}) 子彈位置：{locbullet} 彈艙位置：{location}")
            await rr.send(f"本次dice結果：{dice}")
        else:
            await rr.response.send_message("請輸入正確數值(最大:30)")
        

    @bsc(name = "獲得伺服器_get_id", description = "get a server id")
    async def gsid(gsid):
        await gsid.response.send_message(f"此伺服器ID: {gsid.guild.id}")
        await gsid.send(f'你的ID: {gsid.author.id}')

    @bsc(name = "香香圖片get_waifu_pics", description = "要查看NSFW內容，請在NSFW頻道使用")
    async def gw(gw):
        if gw.channel.nsfw:
            catg = 'nsfw'
        else:
            catg = 'sfw'
        pic = requests.get(f"https://api.waifu.pics/{catg}/waifu")
        picj = pic.json()
        embed = discord.Embed()
        embed.set_image(url = picj['url'])
        await gw.response.send_message(embed=embed)

    @bsc(name = "neko貓貓香箱", description = "得到貓貓圖片")
    async def gneko(gneko):
        pic = requests.get("https://api.waifu.pics/sfw/neko")
        picj = pic.json()
        embed = discord.Embed()
        embed.set_image(url=picj['url'])
        await gneko.response.send_message(embed=embed)

    @bsc(name = "pog", description = "use it or lose it")
    async def pog(pog):
        await pog.response.send_message(":nerd:")
        await pog.send("[POG按鍵](<https://shorturl.at/fgBMX>)")

    bot.run(TOKEN)


if __name__ == "__main__":
    bot_start()

