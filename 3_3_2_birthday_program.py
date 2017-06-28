birth={}
while(True): #무한 반복 (True=참)
    print('당신의 생일정보를 알려드립니다.')
    print('Q를 입력하면 프로그램이 종료됩니다.')
    name=input('당신의이름은?')#데이터입력후 name변수에 저장
    if name=='Q' or name=='q':
        print('프로그램이 종료됩니다.')
        break #반복문 종료
    #입력된 이름 key로 저장이 되어있으면 True 아니면 False
    if name in birth.keys():
        print(birth[name])
    else:
        print('당신의 정보가 없습니다.')
        print('당신의 생일을 입력해주세요(예9-15) :')
        b=input()
        birth[name]=b
    
