import random

b='rock'
c='paper'
d='scissors'
f='quit'
g=int(0)
score=int(0)
print('Welcome to Rock, Paper, Scissors!')
while g==0:
    print('Please choose rock, paper or scissors or type quit to quit')
    e=random.randrange(3)
    print('score:', score)
    a=input()
    if a==f:
        g+=1
        print('final score:', score)
    #computer chose rock
    elif e==0:
        if a==b:
            print('Draw, you both chose rock')
        elif a==c:
            print('you win, paper beats rock')
            score+=1
        elif a==d:
            print('you lose, rock beats scissors')
            score-=1
        else:
            print('make sure you type rock, paper or scissors')
    #computer chose paper
    elif e==1:
        if a==b:
            print('You lose, paper beats rock')
            score-=1
        elif a==c:
            print('Draw,you both chose paper')
        elif a==d:
            print('You win, scissors beats paper')
            score+=1
        else:
            print('make sure you type rock, paper or scissors')
        
    #computer chose scissors    elif e==2:
        if a==b:
            print('You win, rock beats scissors')
            score+=1
        elif a==c:
            print('You lose, scissors beats paper')
            score-=1
        elif a==d:
            print('draw, ypu both chose scissors')
        else:
            print('make sure you type rock, paper or scissors')
    else:
        print('make sure you typenoooooo rock, paper or scissors')
