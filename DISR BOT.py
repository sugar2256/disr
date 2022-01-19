from pydoc import cli
import discord, asyncio, datetime, pytz
import os
client = discord.Client() 

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("Bot Ready.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("대구국제사격장 : https://discord.gg/S2HAvYtvv3"))

@client.event
async def on_message(message):
    if message.content == ".디버그": # 메세지 감지
        await message.channel.send ("{} | {}, Welcome".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Welcome".format(message.author, message.author.mention))

    if message.content == ".정보": # 메세지 감지
        embed = discord.Embed(title="[KR:RP] 대구국제사격장 V3 정보", description="대구국제사격장에 오신 것을 환영합니다!\n대구국제사격장 서비스 상태를 확인해보십시오.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="인게임 오픈", value="데이터 없음", inline=False)
        embed.add_field(name="인게임 개발", value="진행 중", inline=False)

        embed.add_field(name="디스코드 서버 관리", value="진행 중", inline=True)
        embed.add_field(name="디스코드 서버 전용 봇", value="진행 중", inline=True)

        embed.set_footer(text="Bot Made by CHICKEN#8878", icon_url="https://media.discordapp.net/attachments/933204637123751939/933213213951135754/1df8a049f88e9074.jpg?width=657&height=657")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/933204637123751939/933213213951135754/1df8a049f88e9074.jpg?width=657&height=657")
        await message.channel.send (embed=embed)     

    if message.content.startswith (".삭제"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by CHICKEN#8878", icon_url="https://media.discordapp.net/attachments/933204637123751939/933213213951135754/1df8a049f88e9074.jpg?width=657&height=657")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

    if message.content == (".명령어"):
     await message.channel.send ("\n**대구국제사격장 | [KR RP] DISR V3 봇 명령어 목록입니다.** \n > 일반 명령어 \n > .디버그 : 봇이 작동중인지 확인 할 수 있는 테스트 명령어입니다. \n > .정보 : 현재 대구국제사격장 서비스 정보를 표시합니다. \n > .봇 정보 : 봇의 현재 버전과 업데이트 일시, 수정 내용등을 표시합니다. \n > 관리자 명령어 \n > .삭제 (삭제할 메세지 개수) : 메세지를 (삭제할 메세지 개수)만큼 삭제시킵니다. \n > .공지 (내용) : (내용)을 지정된 채널 (사격장 공지)에 전송합니다. \n > .모집 (내용) : (내용)을 지정된 채널 (모집)에 전송합니다.")
    
    if message.content == (".봇 정보"):
        await message.channel.send ("[대구국제사격장 | [KR RP] DISR V3 봇 버전\nV 1.0.1 (2022년 01월 19일 20시 50분 업데이트)\n업데이트 내용 : 명령어 수정 (.버전 -> .봇 정보, .도움말 -> .명령어)\n봇 오류는 CHICKEN#8878로 문의주시면 수정하겠습니다.")
    
    if message.content == ("무야호"):
        await message.channel.send ("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wikitree.co.kr%2Farticles%2F624278&psig=AOvVaw0DsiEiMYNVFRh5GpyXke7B&ust=1642681056470000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLiO-fnlvfUCFQAAAAAdAAAAABAf")
    
    if message.content.startswith (".공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(837285551903342612)
            embed = discord.Embed(title="**[KR:RP] 대구국제사격장 V3 공지**", description="\n――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made By CHICKEN#8878 | 담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/933204637123751939/933213213951135754/1df8a049f88e9074.jpg?width=657&height=657")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/933204637123751939/933213213951135754/1df8a049f88e9074.jpg?width=657&height=657")
            await channel.send ("", embed=embed)
            await message.author.send("**[BOT 자동 알림]**\n정상적으로 공지가 채널에 작성이 완료되었습니다.\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if message.content.startswith (".모집"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(868093638301868062)
            embed = discord.Embed(title="**[KR:RP] 대구국제사격장 V3 직원모집**", description="\n――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made By CHICKEN#8878 | 담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/933204637123751939/933213213951135754/1df8a049f88e9074.jpg?width=657&height=657")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/933204637123751939/933213213951135754/1df8a049f88e9074.jpg?width=657&height=657")
            await channel.send ("", embed=embed)
            await message.author.send("**[BOT 자동 알림]**\n정상적으로 모집공지가 채널에 작성이 완료되었습니다.\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
