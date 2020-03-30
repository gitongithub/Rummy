'''pygame has been used for graphics
time is used for gameplay
random is used for generating deck
itertools is used for making combinations'''

import pygame
import os
import time
import random
import itertools

def showplayer():

    '''This function displays the cards present in the deck of the player.
    The cards are produced randomly. This function also displays the swap button'''
    for i in range(len(Lplayer)):
        gameDisplay.blit(pygame.transform.scale(Lplayer[i][0], (100, 150)), (Lplayer[i][1],0))
    font = pygame.font.Font('Pacifico.ttf', 28)
    text = font.render('Swap Cards', True, gray,red)
    gameDisplay.blit(text,(1050,0))    

def showcomp():

    '''This function shows the back of cards present in the deck of the computer.
    These cards are also generated randomly'''

    for i in range(10):
        gameDisplay.blit(pygame.transform.scale(cback, (100, 150)), ((i)*100,600))    

def showdeck():

    '''This functions displays the pile of cards present in deck.
    The cards are not visible unless you choose to pick one'''

    for i in range(len(Ldeck)):
        gameDisplay.blit(pygame.transform.scale(Ldeck[i][0], (100, 150)), (500,400)) 
    gameDisplay.blit(pygame.transform.scale(back, (100, 150)), (500,400))  
    font = pygame.font.Font('Pacifico.ttf', 22)
    text = font.render('Deck', True, gray,red)
    gameDisplay.blit(text,(530,550)) 

def showavl():

    '''This available deck function contains and shows the crads that the players throw 
    and are open to be chosen by the players till the next move'''

    gameDisplay.blit(pygame.transform.scale(empty, (100, 150)), (800,400))
    for i in range(len(Lavl)):
        gameDisplay.blit(pygame.transform.scale(Lavl[i][0], (100, 150)), (800,400))  
    font = pygame.font.Font('Pacifico.ttf', 15)
    text = font.render('Available Cards', True, gray,red)
    gameDisplay.blit(text,(800,550))             
def showchange():	

    '''This function displays the card that you have put on stake for your next move'''

    gameDisplay.blit(pygame.transform.scale(empty, (100, 150)), (1000,400))
    for i in range(len(Lchange)):
        gameDisplay.blit(pygame.transform.scale(Lchange[i][0], (100, 150)), (1000,400))
    font = pygame.font.Font('Pacifico.ttf', 17)
    text = font.render('Current Card', True, gray,red)
    gameDisplay.blit(text,(1000,550))     
def showchange1():	

    '''This function shows the card picked up from deck'''

    gameDisplay.blit(pygame.transform.scale(empty, (100, 150)), (100,400))
    for i in range(len(Lchange1)):
        gameDisplay.blit(pygame.transform.scale(Lchange1[i][0], (100, 150)), (100,400)) 
    font = pygame.font.Font('Pacifico.ttf', 15)
    text = font.render('Card From Deck', True, gray,red)
    gameDisplay.blit(text,(100,550))       
def clicked():

    '''This function identifies a click on the swap button and shows next below that'''

    font = pygame.font.Font('Pacifico.ttf', 15)
    text = font.render('Clicked', True, gray,red)
    gameDisplay.blit(text,(1100,50))    
def rulefunc():
	
    '''This function prints the rules and regulations of the game'''

    font = pygame.font.Font('mainfont.otf', 25)
    text = font.render('This is the famous 10 card rummy in which you have to make 3 sets or runs(1 of 4 card and', True, gray,red)
    text1 = font.render('other of 3 cards. A set is a collection of cards with same rank.A run is a collection of', True, gray,red)
    text2 = font.render('consecutive ranked cards of same suite.', True, gray,red)
    font = pygame.font.Font('mainfont.otf', 20)
    text3 = font.render('This is a very user friendly interface. In this game you play against the computer.', True, gray)
    text4 = font.render('Whenever you want to make your turn, you have two options. 1) You can pick a card', True, gray)
    text5 = font.render('present in available deck. when clicked on available deck the card will move towards', True, gray)
    text6 = font.render('Desired card holder, in next move you can click on the card that you want to discard', True, gray)
    text7 = font.render('from your set of cards. This card will move in current card holder, after that you can', True, gray)
    text8 = font.render('click on the card from deck and it will be included in your deck. 2) You can choose', True, gray)
    text9 = font.render('the topmost card from deck, on clicking it will be displayed on the desired card', True, gray)
    text10 = font.render('holder.You will choose any card from your deck which will go in your current card.', True, gray)
    text11 = font.render('holder. Now if you want to exchange the card click on the card from deck and if you', True, gray)
    text12 = font.render('dont want to exchange click on your current card.', True, gray)

    gameDisplay.blit(text,(0,0))   
    gameDisplay.blit(text1,(0,30))
    gameDisplay.blit(text2,(0,60))
    gameDisplay.blit(text3,(0,90))  
    gameDisplay.blit(text4,(0,110))   
    gameDisplay.blit(text5,(0,130))
    gameDisplay.blit(text6,(0,150))
    gameDisplay.blit(text7,(0,170))   
    gameDisplay.blit(text8,(0,190))   
    gameDisplay.blit(text9,(0,210))
    gameDisplay.blit(text10,(0,230))
    gameDisplay.blit(text11,(0,250))  
    gameDisplay.blit(text12,(0,270))

    gameDisplay.blit(pygame.transform.scale(sc1, (300, 200)), (900,100))
    gameDisplay.blit(pygame.transform.scale(sc2, (300, 200)), (0,350))
    gameDisplay.blit(pygame.transform.scale(sc3, (300, 200)), (320,350))
    gameDisplay.blit(pygame.transform.scale(sc4, (300, 200)), (640,350))
    gameDisplay.blit(pygame.transform.scale(sc5, (300, 200)), (960,350))
    gameDisplay.blit(pygame.transform.scale(sc6, (300, 200)), (0,560))

    text1 = font.render('You also have the option to swap your card. This can be achieved by clicking on swap', True, gray)
    text2 = font.render('the card button and then clicking the two cards from your deck which you want to', True, gray)
    text3 = font.render(' exchange.', True, gray)
    text4 = font.render('Alert!!You have to keep your deck in the order of', True, gray)
    text5 = font.render('4 3 3 to be considered for evaluation', True, gray)
    text6 = font.render('Alert!!Do not long press', True, gray)
    font = pygame.font.Font('mainfont.otf', 40)
    text7=font.render('Click Anywhere to Start',True,gray)

    gameDisplay.blit(text1,(310,560))
    gameDisplay.blit(text2,(310,580))
    gameDisplay.blit(text3,(310,600))  
    gameDisplay.blit(text4,(310,620))
    gameDisplay.blit(text5,(310,640))
    gameDisplay.blit(text6,(310,660))
    gameDisplay.blit(text7,(500,680))  

def checkPlayer():

    '''This function checks the win of the player. It accepts innput of 
    cards in the form of 4 3 3 i.e. a set or run of 4 cards first and then
    the other ones, in no specified order'''

    count=0
    c=0
    L1=LplayerD[:4]+[]
    L2=LplayerD[4:7]+[]
    L3=LplayerD[7:]+[]
    if (LplayerD[0][0]==LplayerD[1][0]==LplayerD[2][0]==LplayerD[3][0]):
       count+=1
    else:
        c=0
        L1t=L1+[]
        L1=[]
        for i in L1t:
           L1.append([int(i[0]),i[1]])
        i=0
        L1.sort()
        if (LplayerD[0][1]==LplayerD[1][1]==LplayerD[2][1]==LplayerD[3][1]):
           while(i<3):
              if(int(L1[i+1][0])==int(L1[i][0])+1):
                c+=1
              i+=1  
           if(c==3):      
              count+=1     
    if(LplayerD[4][0]==LplayerD[5][0]==LplayerD[6][0]):
        count+=1
    else:
        c=0
        L2t=L2+[]
        L2=[]
        for i in L2t:
           L2.append([int(i[0]),i[1]])
        L2.sort()
        i=0
        if (LplayerD[4][1]==LplayerD[5][1]==LplayerD[6][1]):
           while(i<2):
              if(int(L2[i+1][0])==int(L2[i][0])+1):
             
                c+=1
              i+=1 
           print(L2)    
           if(c==2):      
              count+=1
              print("1")   
    if(LplayerD[7][0]==LplayerD[8][0]==LplayerD[9][0]):
       count+=1
    else:
       
        c=0
        L3t=L3+[]
        L3=[]
        for i in L3t:
           L3.append([int(i[0]),i[1]])
        L3.sort()
        i=0
        if(LplayerD[7][1]==LplayerD[8][1]==LplayerD[9][1]):
           while(i<2):
              if(int(L3[i+1][0])==int(L3[i][0])+1):
                c+=1
              i+=1  
           if(c==2):      
             count+=1    
    if(count==3):
       win()  

def win():

       gameDisplay.blit(pygame.transform.scale(wini, (1000, 350)), (0,0))
       font = pygame.font.Font('Pacifico.ttf', 44)
       gameDisplay.blit(text,(450,650))   
def lost():

       gameDisplay.blit(pygame.transform.scale(losei, (1000, 350)), (0,0))
       font = pygame.font.Font('Pacifico.ttf', 44)
       gameDisplay.blit(text,(450,650))          
'''For generating the deck and cards for each player'''
Lsuite=['C','D','H','S']
Lrank=['1','2','3','4','5','6','7','8','9','10','11','12','13']
L= list(itertools.product(Lrank,Lsuite))
random.shuffle(L)
pygame.init()
display_width = 1200
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
white = (255,255,255)
red=(201, 10, 20)
gray=(207, 167, 167)
clock = pygame.time.Clock()
x = 0
y = 0
playgame=True
mouse_x,mouse_y,mouse_x1,mouse_y1=0,0,0,0

'''Images used have been loaded here'''

Limg=[]
background=pygame.image.load('background.jpg')
empty=pygame.image.load('capture.png')
start=pygame.image.load('start.jpg')
sc1=pygame.image.load('s1.png')
sc2=pygame.image.load('s2.png')
sc3=pygame.image.load('s3.png')
sc4=pygame.image.load('s4.png')
sc5=pygame.image.load('s5.png')
sc6=pygame.image.load('s6.png')
for i in range(52):
    Limg.append([pygame.image.load(L[i][0]+L[i][1]+".png"),x])   
    x+=100
    if(x>=1000):
       x=0	
back=pygame.image.load("gray_back.png")
cback=pygame.image.load("red_back.png")
wini=pygame.image.load("win.jpg")
losei=pygame.image.load("lost.jpg")
'''All the variables used in gameplay are declared below.
For maintaining the cards of the deck, we are simultaneously'''

change=0
var=[[],[]]
temp1,temp2=None ,None
Lplayer=Limg[:10]+[]
LplayerD=L[:10]+[]
Lcomp=Limg[10:20]+[]
LcompD=L[10:20]+[]
Lcompt=LcompD+[]
LcompD=[]
for i in Lcompt:
   LcompD.append([i[0],i[1]])
print(LcompD)
Ldeck=Limg[20:]+[]
LdeckD=L[20:]+[]
Lavl=[]
LavlD=[]
Lchange=[]
LchangeD=[]
Lchange1=[]
Lchange1D=[]
play=False
swap=False
swap1=False
ch=False
chDeck=False
ch1=False
ch2=False
rules=False
won=False
draw=False
lose=False
while playgame:
    mouse_x, mouse_y = None, None 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playgame = False
    gameDisplay.blit(pygame.transform.scale(background, (1200, 800)), (0,0))
    if play==False:
       gameDisplay.blit(pygame.transform.scale(start, (1200, 600)), (0,0))
       font = pygame.font.Font('Pacifico.ttf', 44)
       text = font.render('Start Playing!', True, gray,red)
       gameDisplay.blit(text,(450,650))
       if event.type == pygame.MOUSEBUTTONUP:
          play=True
          rules=True
          time.sleep(0.5)
    if rules==True:
       rulefunc()
       if pygame.mouse.get_pressed()[0]:
          play=True
          rules=False
    if win==True:
       win()
       if pygame.mouse.get_pressed()[0]:
          exit()
    if lose==True:
       lost() 
       if pygame.mouse.get_pressed()[0]:
          exit()   
    if draw==True:
       draw()
       if pygame.mouse.get_pressed()[0]:
          exit()                     
    if play==True and rules==False and won==False and lose==False:
        showplayer()
        showcomp()
        showdeck()
        showavl()
        showchange()
        showchange1()
        if ch2==True:
           a=Lcomp[5]
           d=LcompD[5]
           Lcomp.remove(Lcomp[5])
           LcompD.remove(LcompD[5])
           c=Lavl[len(Lavl)-1]
           b=LavlD[len(LavlD)-1]
           Lavl.remove(Lavl[len(Lavl)-1])
           LavlD.remove(LavlD[len(LavlD)-1])
           Lavl.append(a)
           LavlD.append(d)
           Lcomp.insert(4,c)
           LcompD.insert(4,b)
           ch2=False
           print(LcompD)
           time.sleep(0.2)
        if pygame.mouse.get_pressed()[0] and ch==False :
           mouse_x, mouse_y = pygame.mouse.get_pos()
           if len(Ldeck)==0:
             exit()
           if(mouse_x>500 and mouse_y>400 and mouse_x<600 and mouse_y<550 and ch2==False):
              Lchange1.append(Ldeck[len(Ldeck)-1])
              Lchange1D.append(LdeckD[len(LdeckD)-1])
              Ldeck.remove(Ldeck[len(Ldeck)-1])
              LdeckD.remove(LdeckD[len(LdeckD)-1])           
              #time.sleep(0.5)  
              ch=True
           elif(mouse_x>800 and mouse_y>400 and mouse_x<900 and mouse_y<550 and len(Lavl)>0 and ch2==False):   
              Lchange1.append(Lavl[len(Lavl)-1])
              Lchange1D.append(LavlD[len(LavlD)-1])             
              Lavl.remove(Lavl[len(Lavl)-1])
              LavlD.remove(LavlD[len(LavlD)-1])
              time.sleep(0.5)     
              ch=True
           elif(mouse_x>1050 and  mouse_y<50 ):
              swap=True
        if swap==True:
           clicked()      
        if(pygame.mouse.get_pressed()[0] and swap1==True and ch==False and ch2==False):
            mouse_x4, mouse_y4 = pygame.mouse.get_pos()
            if(mouse_y4<=150):
               i=0
               while i<len(Lplayer):
                 if(mouse_x4-100<=(int(Lplayer[i][1]))): 
                    print(Lplayer[i][1],Lplayer[tempvar][1])
                    Lplayer[i][1],Lplayer[tempvar][1]=Lplayer[tempvar][1],Lplayer[i][1]
  
                    LplayerD[i],LplayerD[tempvar]=LplayerD[tempvar],LplayerD[i]
                    Lplayer.sort(key = lambda x: x[1]) 
                    swap1=False
                    swap=False
                    break 
                 i+=1   
        if(pygame.mouse.get_pressed()[0] and swap==True):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if(mouse_y<=150):
               i=0
               while i<len(Lplayer):
                 if(mouse_x-100<=(int(Lplayer[i][1]))): 
                    tempvar=i
                    print(LplayerD)
                    ch1=True
                    swap1=True
                    break 
                 i+=1  
            time.sleep(0.5)
        if pygame.mouse.get_pressed()[0] and ch==True and swap==False and ch2==False:
           time.sleep(0.01)
           mouse_x1, mouse_y1 = pygame.mouse.get_pos()
           if(mouse_y1<=150):
               i=0
               while i<len(Lplayer):
                 if(mouse_x1-100<=(int(Lplayer[i][1]))): 
                    Lchange.append(Lplayer[i])
                    LchangeD.append(LplayerD[i])
                    val=Lplayer[i][1]
                    var=(i,val)
                    Lplayer.remove(Lplayer[i])
                    LplayerD.remove(LplayerD[i])
                    ch1=True
                    break 
                 i+=1
           time.sleep(0.5)   
           print(LplayerD) 
        if pygame.mouse.get_pressed()[0] and ch1==True and swap==False and ch2==False:
             mouse_x2, mouse_y2 = pygame.mouse.get_pos()    
             if mouse_x2>1000 and mouse_x2<1100 and mouse_y2>400 and mouse_y2<550:
                Lplayer.insert(var[0],[Lchange[len(Lchange)-1][0],var[1]])
                LplayerD.insert(var[0],LchangeD[len(LchangeD)-1])
                Lchange.remove(Lchange[len(Lchange)-1])
                LchangeD.remove(LchangeD[len(LchangeD)-1])
                Lavl.append(Lchange1[len(Lchange1)-1])
                LavlD.append(Lchange1D[len(Lchange1)-1])
                Lchange1.remove(Lchange1[len(Lchange1)-1])
                Lchange1D.remove(Lchange1D[len(Lchange1D)-1])
                ch1=False
                ch=False
                ch2=True
                
             elif mouse_x2>100 and mouse_x2<200 and mouse_y2>400 and mouse_y2<550:
                Lplayer.insert(var[0],[Lchange1[len(Lchange1)-1][0],var[1]])
                LplayerD.insert(var[0],Lchange1D[len(Lchange1D)-1])
                Lchange1.remove(Lchange1[len(Lchange1)-1])
                Lchange1D.remove(Lchange1D[len(Lchange1D)-1])
                if(len(Lchange)>0):
                   Lavl.append(Lchange[len(Lchange)-1])
                   LavlD.append(LchangeD[len(Lchange)-1])
                   Lchange.remove(Lchange[len(Lchange)-1])
                   LchangeD.remove(LchangeD[len(LchangeD)-1])
                ch1=False
                ch=False    
                ch2=True 
                

        '''When the deck of the players are complete, then they are gone for auto evaluation'''
        
        if(len(LplayerD)==10):        
           checkPlayer()             
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()