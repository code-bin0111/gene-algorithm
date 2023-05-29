import random

answer= int(input('원하는 실행을 선택하세요(1:초기화or시작/2:다음 세대/3:종료)'))

while answer!=3:
  
 if answer==1: #초기화
     gene1=[] #부모유전자1
     gene2=[] #부모유전자2
     while len(gene1)<4 and len(gene2)<4:
         Onum1 = random.randint(0,1) #부모유전자1의 형질1    #gene1=[Onum1,Onum2,Onum3,Onum4]
         gene1.append(Onum1)
         Onum2 = random.randint(0,1) #부모유전자1의 형질2
         gene1.append(Onum2)
         Onum3 = random.randint(0,1) #부모유전자1의 형질3
         gene1.append(Onum3)
         Onum4 = random.randint(0,1) #부모유전자1의 형질4
         gene1.append(Onum4)

         Tnum1 = random.randint(0,1) #부모유전자2의 형질1    #gene2=[Tnum1,Tnum2,Tnum3,Tnum4]
         gene2.append(Tnum1)
         Tnum2 = random.randint(0,1) #부모유전자2의 형질2
         gene2.append(Tnum2)
         Tnum3 = random.randint(0,1) #부모유전자2의 형질3
         gene2.append(Tnum3)
         Tnum4 = random.randint(0,1) #부모유전자2의 형질4
         gene2.append(Tnum4)


     print('gene1:' , gene1,'gene2:' , gene2)
     answer= int(input('원하는 실행을 선택하세요(1:초기화/2:다음 세대/3:종료)'))
     if answer==2:
         while answer==2: #자손유전자  
             Nnum1=random.choice([Onum1 , Tnum1])
             Nnum2=random.choice([Onum2 , Tnum2])
             Nnum3=random.choice([Onum3 , Tnum3])
             Nnum4=random.choice([Onum4 , Tnum4])
             gene3=[Nnum1 , Nnum2 , Nnum3 , Nnum4]
             print(gene3)
             answer=int(input('원하는 실행을 선택하세요(1:초기화or시작/2:다음 세대/3:종료)'))
         answer=int(input('원하는 실행을 선택하세요(1:초기화or시작/2:다음 세대/3:종료)'))
     
print('종료')