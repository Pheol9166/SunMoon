from gamepack import *

class SunMoon(Gamepack):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def intro(self) -> None:
        scene = """
옛날 옛적 깊은 산 속에 가난한 오누이와 그 홀어머니 가족이 살고 있었다. 
오누이의 어머니는 혼자 몇 고개를 넘어가야 하는 장터에 떡을 내다 팔며 생계를 유지하고 있었다.
그날도 오누이는 하염없이 돌아오는 어머니를 기다리고 있었다.

여동생:『오빠, 엄마는 언제 올까?』
오빠: 『걱정마, 금방 오실거야.』

하지만 날이 점점 어두워져도 어머니는 오지 않았고, 오누이는 점점 불안해져 갔다.

오빠:『어머니가 안 오시네... 내가 밖에 나가서 모시고 올게.』

A. 나도 같이 가! 오빠.
B. 조심해서 갔다 와! 오빠.
C. 아니야! 무서우니까 같이 있어줘..
"""
        SunMoon.read(scene) # read scene
        print("-" * 60)
        
        # get user's selection
        while(1):
            answer = input("당신의 선택은: ")
            if answer.upper() == 'A':
                self.route_A()
            elif answer.upper() == 'B':
                self.leave_ending()
            elif answer.upper() == 'C':
                self.route_C()
            else:
                print("다시 입력해주세요!")
                print()

    def route_A(self) -> None:
        scene = """
여동생: 『나도 같이 가! 오빠』

오빠: 『안돼, 위험할 수도 있으니까 집에 있어.』
여동생: 『나, 버리고 가는거야?』
오빠: 『아니...』
여동생: 『혼자 있기 싫어. 부탁이야, 응?』
오빠: 『알았어.. 대신에 조심해야해?』

오누이는 집을 나서 고개로 향했다. 날은 점점 저물고 있었다.

여동생: 『춥네... 엄마는 무사하시겠지?』
오빠: 『그럼, 분명 집에 오시고 있을거야.』

여동생은 그 말에 안심하며 오빠와 함께 고개를 넘고 있었다. 
세 번째 고개를 넘었을 때쯤, 저 멀리 있는 어머니의 모습이 오빠의 눈에 보였다.

오빠: 『봐! 엄마야!!』
여동생: 『정말?』
오빠: 『엄마 짐 무겁겠다. 먼저 도와주러 갈게.』

오빠는 어머니를 향해 뛰어갔다.

여동생:『같이 가!』

여동생은 오빠의 모습을 따라갔으나, 아무리 달려도 오빠는 멀어지기만 했다. 그러다 어느 순간 오빠의 모습이 점점 가까워지고 있었다.

여동생:『오빠, 왜 그래?』
오빠:『....저건... 엄마가 아니야.......』

여동생은 어렴풋이 어머니의 형상을 한 것과 눈이 마주쳤다. 그것은 자애로운 모성애의 눈빛이 아닌 먹잇감을 바라보는 눈빛이었다.

A. 오빠에게 간다.
B. 도망친다.
"""
        SunMoon.read(scene)
        print("-" * 60)

        while(1):
            answer = input("당신의 선택은: ")
            if answer.upper() == "A":
                self.tree_ending()
            elif answer.upper() == "B":
                self.guity_ending()
            else:
                print("다시 입력해주세요.")
                print()

    def tree_ending(self) -> None:
        scene = """
여동생: 『오빠!』

여동생이 오빠에게 다가갔다. 어머니의 형상을 한 것도 오빠를 향해 다가가고 있었다.
오빠는 공포에 질린 채로 얼어 아무것도 할 수 없었다. 여동생 또한 무서웠지만, 오빠마저 죽는다는 생각에 전력으로 뛰었다.
그녀는 오빠의 손을 잡고 말했다.

여동생: 『저기 나무로! 빨리!!』
오빠: 『...』

오빠는 대답이 없었지만, 동생과 함께 나무에 올라갔다. 오누이가 나무 위로 올라간 동시에 호랑이도 나무에 왔었다.
호랑이는 어머니의 옷을 입고 있었다.

호랑이:『너희가 이 옷 주인의 자식들이구나. 맛있겠는걸.』
여동생: 『우리 엄마는 어딨어?』
호랑이: 『걱정하지 마렴. 곧 만나게 될테니까.』

오빠는 사시나무처럼 떨고 있었다. 그리고 같은 말을 계속 반복하면서 고개를 숙이고 있었다.

오빠:『죽고 싶지 않아.... 살고 싶어.....』

호랑이는 나무 위의 오누이에게 말했다. 

호랑이:『얘들아, 거긴 어떻게 올라갔니? 알려주는 한 명만 살려줄게.』
여동생: 『도끼로 나무를 찍어서... 헉!』

호랑이는 여동생을 향해 웃음을 지었다.

호랑이: 『그렇구나. 넌 살려줄게.』

오빠는 울면서 더욱이 떨기 시작했다.

오빠: 『왜 말한거야... 난 죽을 거야. 죽을 거라고 엄마처럼.... 죽기 싫어.』
여동생: 『오..오빠. 잘못했.. 어?』

여동생은 자신의 몸이 붕 뜨며 세상이 옆으로 기울어지는 것을 느낀다.
희미하게 오빠의 목소리가 들린다.

오빠:『난.. 살고 싶어... 미안해.』

여동생은 자신의 오빠에게 무언가 말하려고 했지만, 그보다 더 빨리 지면에 부딫혔다.
그녀의 시야가 어두워졌다. 
--------------The END--------------
"""
        SunMoon.read(scene)
        exit()

    def guity_ending(self) -> None:
        import time

        scene = """
여동생은 오빠를 뒤로 한 채 도망갔다. 곧이어 오빠의 비명소리와 호랑이의 울음소리가 들렸다.
그녀는 그 소리들이 더 이상 들리지 않을 정도로 걸었고, 어느덧 시간은 밤이 되었다.
넘어지고 다치며 수많은 고개를 넘은 여동생. 그녀는 결국 길을 잃은 채로 땅바닥에 주저앉게 되었다.
오빠가 보고 싶었다. 자신이 힘들 때마다 옆에서 도와주었던 오빠가 그 누구보다도 보고 싶었다.
하지만 오빠는 더 이상 없다. 자신이 나약해서 도망쳤기 때문이다. 

여동생 : 『전부 나 때문이야...』

그녀의 몸이 서서히 차가워지자 오빠의 모습이 눈앞에 보였다. 
여동생은 반가운 나머지 오빠를 불러보았지만, 돌아오는 대답은 한 마디였다.

오빠:『왜 도망갔어?』
"""
        SunMoon.read(scene)

        for i in range(1, 101):
            print("왜 도망갔어?", end = ' ', flush= True)
            if i % 10 == 0:
                print()
                time.sleep(0.4)

        ending = "><><><><><><>>tHe EnD<><><<><><>><<>"
    
        for i in ending:
            print(i, end='', flush=True)
            time.sleep(0.1)
    
        exit()

    def leave_ending(self) -> None:
        scene = """
여동생: 『조심해서 갔다 와! 오빠.』

오빠: 『그래, 빨리 엄마 모시고 올게.』
여동생: 『응!』

그렇게 오빠는 집을 나섰다.
여동생은 또다시 기다림의 시간을 보냈다. 하지만 마찬가지로 오빠는 돌아오지 않았다.
    
여동생: 『추워, 엄마랑 오빠는 어딨는거야...』

문 밖의 발소리가 들렸다. 사람의 발소리치고는 제법 컸다.
여동생은 가족이 왔다는 기쁨에 달려 나가 문을 열었다.

여동생: 『오빠, 엄마! 기다렸...』

그러나 문 앞에 있는 것은 오빠나 엄마가 아니었다. 입가에 피가 묻어 있었다. 

호랑이:『안녕.』
    
그것이 세 가족의 마지막이었다.
--------------The END--------------
"""
        SunMoon.read(scene)
        exit()

    def route_C(self) -> None:
        scene = """
여동생:『아니야! 무서우니까 같이 있어줘..』
여동생:『부탁이야, 응?』
오빠:『참.. 그러면 조금만 더 기다려보자.』

남매는 또다시 기다렸다. 언제쯤 기다렸을까, 문 앞에서 발소리가 들렸다.

여동생:『엄마인가봐! 나가보자!』

쿵. 쿵. 쿵. 사람의 발소리라기에는 너무나 컸다.

오빠:『잠깐만, 엄마가 아닌 것 같아.』
여동생:『응?』
오빠:『확인해보자.』

오누이는 문 앞에 다가가 물었다.

오빠:『누구세요?』

문 밖에서는 걸걸한 목소리가 들렸다.

호랑이:『엄마란다. 문 좀 열어 주렴.』
오빠:『엄마 목소리가 아닌데요.』
호랑이:『감기에 걸려서 그래. 콜록콜록』
여동생:『엄마가 많이 아픈 것 같아. 빨리 열어주자!』

A. 열어준다
B. 열어주지 않는다
"""
        SunMoon.read(scene)
        print("-" * 60)

        while(1):
            answer = input("당신의 선택은: ")
            if answer.upper() == "A":
                self.hug_ending()
            elif answer.upper() == "B":
                self.route_C2()
            else:
                print("다시 입력해주세요.")
                print()   

    def hug_ending(self) -> None:
        scene = """
오빠:『그래, 엄마가 많이 아프신가봐. 엄마!』

그가 문을 열면서 기대했던 것은 어머니의 자애로운 포옹이었지만, 돌아온 것은 뼈가 으스러지는 아픔이었다.

오빠:『아아아아아아아아악!』
여동생:『오빠!!!』

여동생의 눈에 들어온 것은 호랑이에게 안겨 압축된 오빠의 모습이었다. 오빠의 팔은 축 늘어져 있었고, 눈은 이미 생기를 잃었다.
생기를 잃은 그의 눈이 그녀와 마주쳤다.

여동생:『아아.... 으아아......』

충격으로 주저 앉아버린 여동생 앞에 큰 그림자가 드리운다.

호랑이:『엄마 왔다.』

--------------The END--------------
"""
        SunMoon.read(scene)
        exit()
        
    def route_C2(self) -> None:
        scene = """
오빠:『그럼 문구멍으로 손을 내밀어봐요.』

그러자 사람의 손이 문구멍으로 들어왔다. 하얀 핏기 없는 손이었다.
여동생은 손을 만지면 말했다.

여동생:『정말 엄마인가봐! 손이 하얘!』
오빠:『근데 손이 너무 차가워. 우리 엄마 손은 따뜻한데...』

호랑이:『밖이 추워서 그렇단다. 어서 열어주겠니?』
오빠:『알았어요. 엄...』

오빠는 문을 열어주려고 다가간 순간, 문구멍을 통해 바깥을 보았다.
구멍 바깥에는 잘린 손을 든 채, 입맛을 다시고 있는 호랑이가 있었던 것이다.
그리고 그 호랑이와 눈이 마주쳤다.

호랑이:『봤구나?』
오빠:『도망쳐!, 저건 엄마가 아니야!!』

호랑이가 문을 찢고 방 안으로 들어왔다. 오빠는 동생의 손을 잡고 밖으로 도망쳤다.
밖에는 우물과 한 그루의 나무가 보였다.

A. 우물에 숨는다
B. 나무에 올라간다
"""
        SunMoon.read(scene)
        print("-" * 60)
        
        while(1):
            answer = input("당신의 선택은: ")
            if answer.upper() == "A":
                self.well_ending()
            elif answer.upper() == "B":
                self.dream_ending()
            else:
                print("다시 입력해주세요.")
                print()    

    def well_ending(self) -> None:
        scene = """
오빠:『우물로, 빨리!』

오누이는 우물로 들어갔다. 우물은 깊었으나, 물은 채워져 있었기에 .
여동생은 우물 안에서 허우적대면서, 호랑이가 못 알아채기를 빌었다.

여동생:『제발, 하늘이시여. 도와주세요.』
오빠:『쉿!, 그러다 들킬라.』

그러나 바램과는 달리, 우물 위에서 내려다 보는 호랑이의 모습이 나왔다.

오누이:『살려주세요...』
호랑이:『괜찮아, 안 잡아먹어. 우물이 너무 깊거든.』

그 말에 오누이는 안도의 한숨을 쉬었다.

오누이:『휴...』
호랑이:『그치만 너네는 살 수 없을거야. 마찬가지 이유로.』

오누이는 그제서야 자신들이 무슨 짓을 벌였는지 알게 되었다.

호랑이는 그렇게 갔지만, 그들에게 남은 것은 살았다는 안도감이 아닌 다가올 결과에 대한 공포였다.

오빠는 우물의 벽을 타고 올라가려 했지만, 그럴수록 힘만 빠질 뿐이었다.

오빠:『아냐.. 그럴리가 없어. 그럴리가 없다고. 그럴리가 없다고!!!!!!』
여동생:『오빠, 나 다리 아파..』
오빠:『오빠한테 업혀. 빨리 나가서 구해줄게.』
여동생:『응..』

오빠는 나갈 수 없다는 것은 알고 있었다. 하지만 여동생을 위해서라도 시도해봐야 한다고 생각했다.

오빠:『미안해...』

우물 안에는 물 속에 가라앉은 남매와 수많은 손톱 자국만이 남아있었다.
--------------The END--------------
"""
        SunMoon.read(scene)
        exit()

    def dream_ending(self) -> None:
        scene = """
오빠:『나무에 올라가! 빨리!!』

오누이는 제빨리 나무에 올라갔다. 호랑이는 나무 밑에서 오누이들에게 말했다.

호랑이:『얘들아, 어떻게 올라갔니?』
여동생:『혹시 나무를 못 오르는거야?』
오빠:『손에 참기름을 바르면 올라갈 수 있어!』

호랑이가 웃으면서 말했다.

호랑이:『아니, 그냥 장난쳐본거야.』

호랑이는 나무를 오르기 시작했다. 마치 오누이들을 압박하듯, 서서히 나무를 올라오고 있었다.
오누이는 무서운 나머지 벌벌 떨며, 두손을 모아 하늘에 빌었다.

오누이:『하느님, 우리를 살리시려거든 새 동아줄을 내려 주시고 우리를 버리시려거든 헌 동아줄을 내려 주세요.』

그러자 하늘이 열리면서 새 동아줄이 내려왔다. 

여동생:『와! 정말 동아줄이 왔어!!』

오누이는 동아줄을 타고 올라가기 시작했다.

눈 앞에서 먹잇감을 놓친 호랑이도 두 발을 모으며 똑같이 빌었다.

호랑이:『저게도 동아줄을 내려주세요.』

그러자 이번에도 하늘이 열리면서 동아줄이 내려왔다.

호랑이:『흐흐흐, 기다... 앗』

그러나 그것은 헌 동아줄이었고, 호랑이는 눈앞에 오누이를 둔 채 수수밭으로 떨어졌다.
오빠는 떨어진 호랑이를 보면서 말했다.

오빠:『쌤통이다.』

그렇게 계속 올라가려는 찰나, 그의 정신이 흐릿해지고, 동아줄에서 떨어졌다.

여동생:『오빠!!!』


오누이의 집 뒷편 나무, 호랑이가 나무 밑에서 먹이를 먹고 있다. 
마지막까지 하늘에서 동아줄이 내려올 것이라고 믿고 있던 아이들이었다.

수수밭이 그들의 피로 붉게 물들었다.
--------------The END--------------
"""
        SunMoon.read(scene)
        exit()


