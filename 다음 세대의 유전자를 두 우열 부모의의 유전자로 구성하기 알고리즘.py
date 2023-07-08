import random


gene1=[]
gene2=[]
gene3=[]
gene4=[]

while len(gene1) <8:
  gene1.append(random.randint(0,1))

while len(gene2) <8:
  gene2.append(random.randint(0,1))

while len(gene3) <8:
  gene3.append(random.randint(0,1))

while len(gene4) <8:
  gene4.append(random.randint(0,1))



print('gene1:',gene1)#부모유전자1
print('gene2:',gene2)#부모유전자2
print('gene3:',gene3)#부모유전자3
print('gene4:',gene4)#부모유전자4

parent1=random.choice([gene1,gene2,gene3,gene4])
parent2=random.choice([parent1,gene2,gene3,gene4])
print('parent1:',parent1)
print('parent2:',parent2)
ngene=[]

ngene.append(random.choice([parent1[0],parent2[0]]))
ngene.append(random.choice([parent1[1],parent2[1]]))
ngene.append(random.choice([parent1[2],parent2[2]]))
ngene.append(random.choice([parent1[3],parent2[3]]))
ngene.append(random.choice([parent1[4],parent2[4]]))
ngene.append(random.choice([parent1[5],parent2[5]]))
ngene.append(random.choice([parent1[6],parent2[6]]))
ngene.append(random.choice([parent1[7],parent2[7]]))

print('ngene:',ngene)

