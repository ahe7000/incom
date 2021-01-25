import discord
from discord.ext import commands
import random
 
app = commands.Bot(command_prefix='/')

############################################### 인콤

list2 = ['마음에 드나?', '여기 있네.', '가져가게.',
    '이게 원하던 물건인가?', '현명한 선택이야.', '좋지.',
    '아무렴, 가져가게나.', '얼마든지.',
    '후회 없는 선택이었길 바라지.', '요즘 플레이어들은 이런 것도 사나?',
    '음, 이건 내가 아끼는 건데.', '원하는 게 나왔나?',
    '자네라면 이게 마음에 들 거야.', '아마도 이게 최선인 것 같구나.',
    '필요한 곳에 사용하길 바라지.', '가져가.', '도박에 꽤 관심이 있는 모양이야.',
    '옛다.', '자네에게 주고 싶던 것이 있어.', '이 정도면 충분한가?',
    '안될 거 있나.']

list = ['혈액', '링거', '루페', '에너지 드링크',
    '우주선 사탕', '에일리언 젤리', '민첩한 하루',
    '흰색 곰돌이 인형', '리코더', '빨간 약', '어쩐지 화면이나 유리창이 잘 닦일 것만 같은 청정 물티슈',
    '한때 관에서 유행했던 랜덤박스 모양의 박스', 'TV 모양 쿠키',
    '눈부시게 빛나는 요요', '탈부착 콧수염', '링거… 모양 링거 피규어',
    '카메라', '깜찍한 검은색 곰돌이 인형', '반만 채워진 링거',
    '21세기 직장인의 성공 신화가 담긴 감동 서적', '겁나 멋진 선글라스',
    '백열전구', '마법의 운세책', '메추라기 알(무정란)',
    '링거를 닮은 혈액', '회색 곰돌이 인형', '손거울',
    'Incomi Mask', '돋보기', '농담 치는 곰인형', '회색 담요', '흰색 담요',
    '검은색 담요', '리시키톤 조화', '해바라기 조화', '찔레꽃 조화',
    '에델바이스 조화', '무화과', '노송나무 조화', '잿빛 장미 조화',
    '칼세올라리아 조화', '능소화 조화', '크레파스', '스케치북',
    '수선화 조화', '아마꽃 조화 꽃다발', '프리지아 조화',
    '레위시아 조화', '치즈 팝콘', '기프트의 양말', '기프트의 안경',
    '흰 카네이션', '목련 가지', '칼림바', '극세사 담요',
    '메리골드', '은방울꽃', '컵라면', '방울뱀 인형', '첼로 모양 링거',
    '첼로', '하이포시스 오리어', '안젤로니아', '기생꽃',
    '당국화', '팔레놉시스', '백합', '메꽃', '라스피', '제충국',

    '҉황҉금҉빛҉ ҉꽃҉ ҉한҉ ҉송҉이҉,҉ ҉행҉복҉', '½ÀÚ ±', '푸҈̧̣̘̯͈̣̣͕͙͖른҉̧̟̙̩̆͆͠빛҈̢̥͇͔̤̞̣̘̤͈̫̯̱͕ 꽃҉͚̝̘̗̜̣͔̯̞̩͈̲͇͎͗̂̆̄͆̌͑̓ͅ 한҉̠̮̫͕̯̝͉̗̆͗͐̌̀̋̐̓̀͋̄̎̄ 송҈̧̰͔͇̤̙̟͙̝͖͔̬̞̖이҈͇̰̳̯̜͙͇̲͕͈̤̳̣͕̞͑̓͐̒̆̋̒͌́̀͗̂͑',
    '҉4҉절҉ ҉도҉화҉지҉', '҉4҉B҉ ҉연҉필҉', '҉2҉4҉색҉의҉ ҉물҉감҉ ҉튜҉브҉',
    '흰҈͎̲̯̬̞̣̞̊͊̀͒͒̈́̽̚̚ 국҉̖̫͚̜̙̆́̽̐화҉̱̦̝̪̮̞͍̝͍͉͈͐͛̒̊͌̇͂', '파҉̤̮̲͚̲̫̈́̿̈̃̈́우҈͙̩̙̞̯̅̎̌̽̂͌͊̂̒̊́́스҉̯̲̖̱̱͚̙̱͎̖̜͈̈̋̓̎̓́̍̒̏̚타҈̤̮̰̤̙̫̜̓͛͑̽̓ͅ이҈̰̙͉͈̖̫̲̝͖̟͛̍͆̈트҈̟̬̦̰̣̙̽̀́͐͑͛̈͊̿͆ 원҉͔̩̬̣̒̆̓̓̔̈͌̀̈́͗̾ͅ석҈͍̣͈̱̰͕͔̙̓̑͒̓̐̈̏͛́̾̔̚', '금҈̘̩̗͚̣̊̉̾̌̊잔҈̳̟̯̳̮̝̟̤̟͐͗̔̊̀̒͂͊̑͐҉화҉']


jewel = ['가넷', '아메시스트', '아쿠아마린', '다이아몬드',
    '에메랄드', '펄', '루비', '페리도트',
    '사파이어', '오팔', '토파즈', '터쿼이즈']

num_item = len(list) + 2*len(jewel)

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)
    await app.change_presence(activity=discord.Game("랜덤박스 판매"))

#@app.event
#async def on_command_error():
#    list = ['무슨 소리를 하는 겐가?', '이봐, 난 바쁜 몸일세.', '그 명령어에 대한 스크립트는 짜여 있지 않다는군.']
#    await ctx.send(random.choice(list))

@app.command(aliases = ['자기소개', '소개', '설명', '설명해'])
async def intro(ctx):
    introduce = discord.Embed(title = f"쓸데없는 곳에 시간을 허비하지 말자고.",
    description = f"오로지 랜덤박스만 판매하는 인콤 봇입니다.\n현재 테스트 중. 허봉국 코딩 못함.\n\n")
    introduce.add_field(name = f"맨 앞에 \'/\'를 붙인 뒤 용건을 말하세요.",
    value = f"현재 가능한 것:\n1. /설명\n2. /안녕(응답 패턴 2가지)\n3. /랜덤박스\n4. /매점",
    inline = False)
    introduce.add_field(name = f"인콤은 총 {num_item}개의 물품을 취급하고 있습니다. 그 중 절반은 꽃입니다.\n곤듀는 총 {num_item_gondu}개의 물품을 취급하고 있습니다.",
    value = f"추후 물품 추가나 매입 같은 기능을 만들 수도 있고 아닐 수도 있고…\n", inline = False)
    await ctx.send(embed = introduce)

@app.command()
async def 테스트(ctx):
    await ctx.send(ctx.message.author.id)

@app.command(aliases = ['안녕', 'ㅎㅇ'])
async def hello(ctx):
    list = ['Hello, World.', '또 보는군.', '또 보는군, <@{}>'.format(ctx.message.author.id) + '. 이런 걸 원하나?']

    #if(ctx.message.author.id == 798592840102969354):
    #    await ctx.send('또 보는군, 준철. 이런 걸 원하나?')
    #elif(ctx.message.author.id == 377497338492747778):
    #    await ctx.send('또 보는군, 허봉국. 이런 걸 원하나?')
    #else:
    #    await ctx.send(random.choice(list))
    await ctx.send(random.choice(list))

@app.command()
async def 따라해(ctx, *, text = None):
    if(text != None):
        await ctx.send(text)

@app.command(aliases = ['랜덤박스', '랜박'])
async def ranbox(ctx):
    item = random.choice(list) # 보석이 아닌 것으로 item 초기화

    if(random.choice([True, False])):
        item = random.choice(jewel) # 50% 확률로 item을 보석으로 선언
        if(random.choice([True, False])):
            item = 'incompresibleare의 얼굴 모양 ' + item # item이 보석일 때 50% 확률로 인콤 얼굴 모양임
    
    #item = 

    await ctx.send(random.choice(list2) + '\n※ ' + '<@{}>'.format(ctx.message.author.id) + ', ' + item + ' 구매 완료.')
    # await ctx.send('73시간 기다리게나.')


############################################### 곤듀

list_gondu = ['어어 그래 여기 있다', '한창 클 나이에 랜덤박스라니, 쯧.',
'북두가 합숙 끝나고 너 한 번 보자 그러던데.', '어어 여기',
'곤듀 바쁘다', '바쁘다니깐', '어어 곤듀님 여기 있어']

list_gwaza = ['어어 그래 여기 있다', '한창 클 나이에 랜덤박스라니, 쯧.',
'북두가 합숙 끝나고 너 한 번 보자 그러던데.', '어어 여기',
'곤듀 바쁘다', '바쁘다니깐', '어어 곤듀님 여기 있어',
'맛있게 먹으렴…', '많이 먹으면 이 썩는다 조심해']

cafeteria = ['사이다', '매점빵', '새*깡', '새*우깡',
'감자칩', '치킨 닭다리', '뿌*클 치킨', '즉석 떡볶이',
'퍼런 떡볶이', '로제 떡볶이', '크림 떡볶이']

cafeteria2 = ['편지지', '등산 선글라스', '새마을 모자',
'수*의 정석', '프로틴', '도토리묵', 'KF94', '선글라스',
'길리슈트', '루돌프 탈', '도토리 모양 선글라스',
'도토리 자수 스웨터']

num_item_gondu = len(cafeteria) + len(cafeteria2)

@app.command(aliases = ['곤듀랜박', '곤듀랜덤박스', '매점', '곤듀매점'])
async def ranbox_gondu(ctx):
    item = random.choice(cafeteria2) # 음식이 아닌 것으로 item 초기화

    if(random.choice([True, False])):
        item = random.choice(cafeteria) # 50% 확률로 item을 음식으로 선언
        await ctx.send(random.choice(list_gwaza) + '\n※ ' + '<@{}>'.format(ctx.message.author.id) + ', ' + item + ' 구매 완료.')
    else:
        await ctx.send(random.choice(list_gondu) + '\n※ ' + '<@{}>'.format(ctx.message.author.id) + ', ' + item + ' 구매 완료.')
     
app.run('token')