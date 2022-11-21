from datetime import datetime
import pytz
import discord
from discord.ext import commands
import asyncio


intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def wait_for(message):
    send_message = await message.send('알고싶은 나라:')

    def check(m):
        return m.author == message.author and m.channel == message.channel
    
    try:
        message = await client.wait_for('message', check=check)
    except asyncio.TimeoutError:
        await message.send('시간 초과 다시 써주세요')
    else:
        await message.send('축하함')



"""
@client.event
async def Ctime(k):
    await message.channel.send('알고싶은 나라:')
    #나라를 받는다
    while country_n != str:
        #if구문 실행한다
        country_n = None
        if message.content == '한국':
            country_n = 'Asia/Seoul'
        elif message.content == '빅토리아':
            country_n = 'Australia/Victoria'
        elif message.content == '미국':
            country_n = 'US/Eastern'
        elif message.content == '캐나다':
            country_n = 'Canada/Eastern'   
        else:
            message.channel.send('그런 나라는 없습니다. 한국, 빅토리아, 미국, 캐나다 중 선택하세요\n')
            break
        country_t = pytz.timezone(country_n)
        cur_time = datetime.now(country_t)
        simple_cur_time = cur_time.strftime("현재시간: %H시 %M분 %S초")
        return simple_cur_time
"""