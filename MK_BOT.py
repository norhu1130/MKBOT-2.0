import asyncio, discord ,setting
from activity_log import log_actvity, log_start_actvity
from msg_log import log_msg, log_start_msg


client = discord.Client()
app = discord.Client()
Setting = setting.Settings()

@client.event
async def on_ready():
    print("로그인완료!")
    print(client.user.name)
    print(client.user.id)
    print("-----------")
    await client.change_presence(game=discord.Game(name='MK 도움말 MK BOT2.0정상작동', type=1))




@client.event
async def on_message(message):
                if "MK 공지 " in message.content:
                    if message.author.id == Setting.owner_id:
                        # DPNK 사용 구문 시점
                        embed=discord.Embed(title="MK BOT 전체공지 시스템", color=0xb2ebf4)
                        embed.add_field(name="공지 발신을 준비하고 있습니다!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        mssg = await client.send_message(message.channel, embed=embed)
                        a = []
                        b = []
                        e = []
                        ec = {}
                        embed=discord.Embed(title="MK BOT 전체공지 시스템", color=0xb2ebf4)
                        embed.add_field(name="공지 발신중 입니다!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        await client.edit_message(mssg, embed=embed)
                        for server in client.servers:
                            for channel in server.channels:
                                for tag in ["notice", "공지", "알림", "Alarm"]:
                                    if tag in channel.name:
                                        dtat = True
                                        for distag in ["밴", "경고", "제재", "길드", "ban", "worry", "warn", "guild"]:
                                            if distag in channel.name:
                                                dtat = False
                                        if dtat:
                                            if not server.id in a:
                                                try:
                                                    await client.send_message(channel, message.content)
                                                except discord.HTTPException:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "HTTPException"
                                                except app.Forbidden:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "Forbidden"
                                                except app.NotFound:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "NotFound"
                                                except discord.InvalidArgument:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "InvalidArgument"
                                                else:
                                                    a.append(str(server.id))
                                                    b.append(str(channel.id))
                        asdf = "```\n"
                        for server in client.servers:
                            if not server.id in a:
                                try:
                                    ch = await client.create_channel(server, "MK-BOT공지")
                                    await client.send_message(ch, "공지채널찾을수없어채널을생성했습니다. DM을주세요. 컴퓨터의모든팁들#6225")
                                    await client.send_message(ch, message.content)
                                except:
                                    asdf = asdf + str(server.name) + "[채널 생성에 실패하였습니다. (서버 관리자와 연락 요망)]\n"
                                else:
                                    asdf = asdf + str(server.name) + "[채널 생성 및 재발송에 성공하였습니다.]\n"
                        asdf = asdf + "```"
                        embed=discord.Embed(title="MK BOT 전체공지 시스템", color=0xb2ebf4)
                        embed.add_field(name="공지 발신이 완료되었습니다!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        bs = "```\n"
                        es = "```\n"
                        for bf in b:
                            bn = client.get_channel(bf).name
                            bs = bs + str(bn) + "\n"
                        for ef in e:
                            en = client.get_channel(ef).name
                            es = es + str(client.get_channel(ef).server.name) + "(#" + str(en) + ") : " + ec[ef] + "\n"
                        bs = bs + "```"
                        es = es + "```"
                        if bs == "``````":
                            bs = "``` ```"
                        if es == "``````":
                            es = "``` ```"
                        if asdf == "``````":
                            asdf = "``` ```"
                        sucess = bs
                        missing = es
                        notfound = asdf
                        embed.add_field(name="공지 발신에 성공한 채널은 다음과 같습니다 :", value=sucess, inline=False)
                        embed.add_field(name="공지 발신에 실패한 채널은 다음과 같습니다 :", value=missing, inline=False)
                        embed.add_field(name="키워드가 발견되지 않은 서버는 다음과 같습니다 :", value=notfound, inline=False)
                        await client.edit_message(mssg, embed=embed)
                        # DPNK 사용 구문 종점
                        log_actvity("I send Notice for all Server. (content : %s\nSuccess : %s\nFail : %s\nNotfound : %s)." % (message.content, sucess, missing, notfound))
                    else:
                        await client.send_message(message.channel, "<@%s>, 봇 관리자로 등록되어 있지 않습니다." % (message.author.id))
    
     
                if "MK 종료" == message.content:
                    if message.author.id == Setting.owner_id:
                        await client.send_message(message.channel, "<@%s>, 봇의 가동을 중지합니다. 5분 이내로 오프라인으로 전환됩니다(디스코드 API 딜레이)." % (message.author.id))
                        await client.change_presence(game=discord.Game(name="Offline", type=0))
                        log_actvity("Change status to offline (Request by. %s)." % (message.author.id))
                        quit() # 왜왜애왜 애러나
                    else:
                        await client.send_message(message.channel, "<@%s>, 봇 관리자로 등록되어 있지 않습니다." % (message.author.id))

    
     
                if message.content.startswith('MK 개발자의말'):
                  await client.send_message(message.channel, "안녕하세요. 이번 MKBOT2.0프로젝트담당자 컴퓨터의모든팁들입니다. 이메시지가 모든MineKorea에있던분께전달돼면좋겠네요. 저희 MineKorea삭제와MK BOT삭제")
                  await client.send_message(message.channel, "그모든유저분께죄송하다는말밖에는못하겠네요 저희 MineKorea는로봇플린과통합했습니다. 여기로와주세요. https://discord.gg/utW2X3q")
                if message.content.startswith('MK 봇프사'):
                  await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/518429267298877460/520534040269422612/2117d4628437cdf3.jpg")
                if message.content.startswith("MK 마크사이트"):
                  await client.send_message(message.channel, "https://minecraft.net/ko-kr/?ref=m")
                if message.content.startswith('MK 하이픽셀'):
                  await client.send_message(message.channel, "마크 최대의 서버입니다. 서버주소 MC.hypixel.net") 
                if message.content.startswith("MK 온라인"):
                  await client.send_message(message.channel, "저는 온라인 입니다.만약 이 메세지가 출력이 안 된다면 오프라인입니다.")  
                if message.content.startswith("MK 마인코리아"):
                  await client.send_message(message.channel, "마인코리아는 디스코드에게 편의를 제공하기 위한 커뮤니티입니다.")
                if message.content.startswith("MK 초대"):
                   await client.send_message(message.channel, "https://discordapp.com/oauth2/authorize?client_id=533202743532191747&scope=bot&permissions=124992")
                if message.content.startswith('MK 패치노트'):
                   await client.send_message(message.channel, "**<MK BOT 2.0.0 패치노트>**")
                   await client.send_message(message.channel, "**`MK 개발자의말`**")
                if message.content.startswith('MK 도움말'):
                   embed=discord.Embed()
                   embed.add_field(name='MK 봇프사', value='봇의 프로필 사진을 출력합니다.')
                   embed.add_field(name='MK 프사', value='당신의 프로필 사진을 출력합니다.')
                   embed.add_field(name='MK 마크사이트', value='마인크래프트 공식 사이트를 출력합니다.')
                   embed.add_field(name='MK 온라인', value='봇이 온라인인지 확인합니다.메세지가 출력이 되지 않을 경우 오프라인입니다.')
                   embed.add_field(name='MK 봇정보', value='봇의 정보를 출력합니다.')
                   embed.add_field(name='MK 마인코리아', value='MineKorea에 대한 정보를 출력합니다.단,서버 초대 링크는 출력하지 않습니다.')
                   embed.add_field(name='MK 도움말', value='MK BOT의 명령어 전체를 출력합니다.')
                   embed.add_field(name='MK 초대', value='MK BOT의 초대링크를 출력합니다.')
                   embed.add_field(name='MK 패치노트', value='MK BOT의 패치 내역을 확인합니다.')
                   embed.add_field(name='MK 개발자의말', value='개발자의메시지를확인합니다.')
                   embed.add_field(name='MK BOT 개발자와 도움을 주신 분들', value='MineKorea 대표 :large_blue_circle: Amo :large_blue_circle: #4899 / 컴퓨터의모든팁들 #6225 / The_Adminator #4074 / 블맨 #5969')
                   await client.send_message(message.channel, embed=embed)
                if message.content.startswith('MK 프사'):
                   memberid = message.content[5:]
                   memberid = memberid.replace("<", "")
                   memberid = memberid.replace("@", "")
                   memberid = memberid.replace("!", "")
                   memberid = memberid.replace(">", "")
                   memberid = str(memberid)
                if memberid == "":
                   memberid = message.author.id
                   member = message.server.get_member(memberid)
                   a = member.avatar_url
                if a == "":
                   a = member.default_avatar_url
                   embed = discord.Embed(title="", description="", color=0x62bf42)
                   embed.set_author(name="당신의 프로필입니다.")
                   embed.set_footer(text="만든이 컴퓨터의모든팁들")

                   embed.set_thumbnail(url=a)
                   await client.send_message(message.channel, embed=embed)
    
    
    
client.run('token')    
