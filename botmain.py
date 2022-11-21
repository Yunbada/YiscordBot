# -*- coding:utf-8 -*- 
import roullette
import rank
import pytz
from datetime import datetime

import discord
from discord.ext import commands
import asyncio

discord_token = 'DiscordToken'

#디스코드 클라이언트 클래스
intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


#event decorator 설정 후 on_ready function 추가
@client.event
async def on_ready():
    print('\n{}로그인 완료\n'.format(client))
    print('{}온라인\n'.format(client.user.name))


#event decorator 설정 후 on_message function 추가
#message는 디스코드 내 모든 메세지
@client.event
async def on_message(message):

    #간단히 단어 줄이기
    channel = message.channel
    author = message.author
    content = message.content

    #embed로 깔끔하게 정리
    embed=discord.Embed(title= "봇 도움말", color=0x832121)
    embed.add_field(name="1.공지 :handshake: ", value="중요", inline=True)
    embed.add_field(name="2.게임 :video_game: ", value="룰렛, 주사위 등", inline=False)
    embed.add_field(name="3.순위 :trophy: ", value="채팅, 게임 등", inline=True)
    embed.add_field(name="4.시간 :alarm_clock: ", value="현재 시간", inline=False)
    
    #prefix 설정
    if content.startswith('봇 '):
        msg = content[2:]
    else:
        return None
    #message author이 client.user(봇)이면 무시
    if author == client.user:
     return

    #message 보낸 사람이 bot이 아니면 message가 특정 글자를 받으면 글자를 보내라
    elif msg == "도움말":
        await channel.send(embed=embed)
    elif msg == "시간":
        await channel.send('알고싶은 나라를 적으세요')
        ctx = await client.wait_for('message')
        if ctx == '한국':
            country_n = 'Asia/Seoul'
        elif ctx == '빅토리아':
            country_n = 'Australia/Victoria'
        elif ctx == '미국':
            country_n = 'US/Eastern'
        elif ctx == '캐나다':
            country_n = 'Canada/Eastern'
        else:
            await channel.send('그런 나라는 없습니다. 한국, 빅토리아, 미국, 캐나다 중 선택하세요\n')            
        country_t = pytz.timezone(country_n)
        cur_time = datetime.now(country_t)
        simple_cur_time = cur_time.strftime("현재시간: %H시 %M분 %S초")
        await channel.send(simple_cur_time)
        

        


#client class를 token으로 인증하여 실행
client.run(discord_token)
