from datetime import date
import turtle
import urllib.request as urllib2
import random
gamestate = 50
numberletterwords=[]
guesslist=[]
x = 0
win = 0
amount = 0

today = date.today()
date1= date(2022,1,20)
delta = date1 - today
daynumber=(delta.days)


# start game
while gamestate==50:
  print("Choose the number of letters you want the word to be. INPUT NUMBER AS THE NUMBER ITS SELF NOT SPREAD OUT.")
  numberchoice = input()
  gamestate=51


# getting words
word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
response = urllib2.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()

# choosenumber of letters
def numberofletters(x):
  for element in WORDS:
        if len(element)==x:
          numberletterwords.append(str(element))
  return(numberletterwords)
numberofletters(int(numberchoice))

def cleanup(sentence):
  return [x[1:] for x in sentence]

while gamestate==51:
  prewordbank = cleanup(numberletterwords)
  wordbank = [i.replace('"','') for i in prewordbank] 
  # 
  print("If you want to play the daily puzzle type 1, if you want to play random type 2")
  dorr=input()
  for i in wordbank:
    amount=amount+1
  if int(dorr) == 1:
    gamestate=60
  if int(dorr) == 2:
    gamestate=52


# print(wordbank)
# wordbank=[x[1:] for string in numberletterwords ]
while gamestate==60:
  if daynumber%50 == 0:
    preguessword=wordbank[((int(amount/100))*36)+daynumber]
  if daynumber%50 == 1:
    preguessword=wordbank[((int(amount/100))*2)+daynumber]
  if daynumber%50 == 2:
    preguessword=wordbank[((int(amount/100))*20)+daynumber]
  if daynumber%50 == 3:
    preguessword=wordbank[((int(amount/100))*26)+daynumber]
  if daynumber%50 == 4:
    preguessword=wordbank[((int(amount/100))*66)+daynumber]
  if daynumber%50 == 5:
    preguessword=wordbank[((int(amount/100))*98)+daynumber]
  if daynumber%50 == 6:
    preguessword=wordbank[((int(amount/100))*28)+daynumber]
  if daynumber%50 == 7:
    preguessword=wordbank[((int(amount/100))*96)+daynumber]
  if daynumber%50 == 8:
    preguessword=wordbank[((int(amount/100))*18)+daynumber]
  if daynumber%50 == 9:
    preguessword=wordbank[((int(amount/100))*48)+daynumber]
  if daynumber%50 == 10:
    preguessword=wordbank[((int(amount/100))*30)+daynumber]
  if daynumber%50 == 11:
    preguessword=wordbank[((int(amount/100))*50)+daynumber]
  if daynumber%50 == 12:
    preguessword=wordbank[((int(amount/100))*56)+daynumber]
  if daynumber%50 == 13:
    preguessword=wordbank[((int(amount/100))*72)+daynumber]
  if daynumber%50 == 14:
    preguessword=wordbank[((int(amount/100))*38)+daynumber]
  if daynumber%50 == 15:
    preguessword=wordbank[((int(amount/100))*76)+daynumber]
  if daynumber%50 == 16:
    preguessword=wordbank[((int(amount/100))*6)+daynumber]
  if daynumber%50 == 17:
    preguessword=wordbank[((int(amount/100))*42)+daynumber]
  if daynumber%50 == 18:
    preguessword=wordbank[((int(amount/100))*32)+daynumber]
  if daynumber%50 == 19:
    preguessword=wordbank[((int(amount/100))*74)+daynumber]
  if daynumber%50 == 20:
    preguessword=wordbank[((int(amount/100))*4)+daynumber]
  if daynumber%50 == 21:
    preguessword=wordbank[((int(amount/100))*94)+daynumber]
  if daynumber%50 == 22:
    preguessword=wordbank[((int(amount/100))*34)+daynumber]
  if daynumber%50 == 23:
    preguessword=wordbank[((int(amount/100))*52)+daynumber]
  if daynumber%50 == 24:
    preguessword=wordbank[((int(amount/100))*56)+daynumber]
  if daynumber%50 == 25:
    preguessword=wordbank[((int(amount/100))*88)+daynumber]
  if daynumber%50 == 26:
    preguessword=wordbank[((int(amount/100))*40)+daynumber]
  if daynumber%50 == 27:
    preguessword=wordbank[((int(amount/100))*90)+daynumber]
  if daynumber%50 == 28:
    preguessword=wordbank[((int(amount/100))*68)+daynumber]
  if daynumber%50 == 29:
    preguessword=wordbank[((int(amount/100))*44)+daynumber]
  if daynumber%50 == 30:
    preguessword=wordbank[((int(amount/100))*16)+daynumber]
  if daynumber%50 == 31:
    preguessword=wordbank[((int(amount/100))*82)+daynumber]
  if daynumber%50 == 32:
    preguessword=wordbank[((int(amount/100))*54)+daynumber]
  if daynumber%50 == 33:
    preguessword=wordbank[((int(amount/100))*60)+daynumber]
  if daynumber%50 == 34:
    preguessword=wordbank[((int(amount/100))*84)+daynumber]
  if daynumber%50 == 35:
    preguessword=wordbank[((int(amount/100))*76)+daynumber]
  if daynumber%50 == 36:
    preguessword=wordbank[((int(amount/100))*8)+daynumber]
  if daynumber%50 == 37:
    preguessword=wordbank[((int(amount/100))*80)+daynumber]
  if daynumber%50 == 38:
    preguessword=wordbank[((int(amount/100))*86)+daynumber]
  if daynumber%50 == 39:
    preguessword=wordbank[((int(amount/100))*66)+daynumber]
  if daynumber%50 == 40:
    preguessword=wordbank[((int(amount/100))*78)+daynumber]
  if daynumber%50 == 41:
    preguessword=wordbank[((int(amount/100))*10)+daynumber]
  if daynumber%50 == 42:
    preguessword=wordbank[((int(amount/100))*62)+daynumber]
  if daynumber%50 == 43:
    preguessword=wordbank[((int(amount/100))*14)+daynumber]
  if daynumber%50 == 44:
    preguessword=wordbank[((int(amount/100))*96)+daynumber]
  if daynumber%50 == 45:
    preguessword=wordbank[((int(amount/100))*24)+daynumber]
  if daynumber%50 == 46:
    preguessword=wordbank[((int(amount/100))*64)+daynumber]
  if daynumber%50 == 47:
    preguessword=wordbank[((int(amount/100))*92)+daynumber]
  if daynumber%50 == 48:
    preguessword=wordbank[((int(amount/100))*22)+daynumber]
  if daynumber%50 == 49:
    preguessword=wordbank[((int(amount/100))*86)+daynumber]
  if daynumber%50 == 50:
    preguessword=wordbank[((int(amount/100))*12)+daynumber]
  guessword= preguessword.replace("'", "")
  gamestate = 53

# choose word to guess
while gamestate==52:
  preguessword=random.choice(wordbank)
  guessword= preguessword.replace("'", "")
  gamestate=53


# turtle set up and boxes
while gamestate == 53:
  turtle.speed(9999999999)
  turtle.ht()
  turtle.penup()
  turtle.goto(-150,150)
  turtle.pensize(3)
  turtle.pendown()
  turtle.forward(300)
  turtle.right(90)
  turtle.forward(300)
  turtle.right(90)
  turtle.forward(300)
  turtle.right(90)
  turtle.forward(300)

  turtle.penup()
  turtle.goto(-150,100)
  turtle.pendown()
  turtle.right(90)
  turtle.forward(300)
  turtle.penup()
  turtle.goto(-150,50)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.goto(-150,0)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.goto(-150,-50)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.goto(-150,-100)
  turtle.pendown()
  turtle.forward(300)
  turtle.right(90)

  while int(numberchoice) > x:
    x=x+1
    turtle.penup()
    turtle.goto(-150+(300*x)/int(numberchoice),150)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
  gamestate=1


# First guess of the word
while gamestate == 1:
  print("What is your first guess")
  guess = str(input())
  guess1= "'"+ guess+"'"
  print (guess1)

  for i in wordbank:
    if guess1==i:
      gamestate = 2
  else:
    print("word is not in word bank")

n = int(numberchoice)
while gamestate == 2: 
  print("WORD IS IN WORD BANK")
  guess1a=guess[0:1]
  guess1b=guess[1:2]
  guess1c=guess[2:3]
  guess1d=guess[3:4]
  guess1e=guess[4:5]
  guess1f=guess[5:6]
  guess1g=guess[6:7]
  guess1h=guess[7:8]
  guess1i=guess[8:9]
  guess1j=guess[9:9]
  guess1k=guess[10:11]
  guess1l=guess[11:12]
  guess1m=guess[12:13]
  guess1o=guess[13:14]
  
  guessworda=guessword[0:1]
  guesswordb=guessword[1:2]
  guesswordc=guessword[2:3]
  guesswordd=guessword[3:4]
  guessworde=guessword[4:5]
  guesswordf=guessword[5:6]
  guesswordg=guessword[6:7]
  guesswordh=guessword[7:8]
  guesswordi=guessword[8:9]
  guesswordj=guessword[9:9]
  guesswordk=guessword[10:11]
  guesswordl=guessword[11:12]
  guesswordm=guessword[12:13]
  guesswordo=guessword[13:14]
  guesswordletters1=[guessworda,guesswordb,guesswordc,guesswordd,guessworde,guesswordf,guesswordg,guesswordh,guesswordi,guesswordj,guesswordk,guesswordl,guesswordm,guesswordo]
  
  
  if guess1a == guessworda:
    turtle.color("green")
    win = win+1
  elif guess1a in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(0*(300/n)+(300/n)/3),110)
  turtle.write(guess1a, font=('arial',20,'bold'))
  
  if guess1b == guesswordb:
    turtle.color("green")
    win=win+1
  elif guess1b in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(1*(300/n)+(300/n)/3),110)
  turtle.write(guess1b, font=('arial',20,'bold'))
 
  if guess1c == guesswordc:
    turtle.color("green")
    win=win+1
  elif guess1c in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(2*(300/n)+(300/n)/3),110)
  turtle.write(guess1c, font=('arial',20,'bold'))

  if guess1d == guesswordd:
    turtle.color("green")
    win=win+1
  elif guess1d in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(3*(300/n)+(300/n)/3),110)
  turtle.write(guess1d, font=('arial',20,'bold'))
  
  if guess1e == guessworde:
    turtle.color("green")
    win=win+1
  elif guess1e in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(4*(300/n)+(300/n)/3),110)
  turtle.write(guess1e, font=('arial',20,'bold'))
 
  if guess1f == guesswordf:
    turtle.color("green")
    win=win+1
  elif guess1f in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(5*(300/n)+(300/n)/3),110)
  turtle.write(guess1f, font=('arial',20,'bold'))

  if guess1g == guesswordg:
    turtle.color("green")
    win=win+1
  elif guess1g in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(6*(300/n)+(300/n)/3),110)
  turtle.write(guess1g, font=('arial',20,'bold'))
 
  if guess1h == guesswordh:
    turtle.color("green")
    win=win+1
  elif guess1h in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(7*(300/n)+(300/n)/3),110)
  turtle.write(guess1h, font=('arial',20,'bold'))
  
  if guess1i == guesswordi:
    turtle.color("green")
    win=win+1
  elif guess1i in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(8*(300/n)+(300/n)/3),110)
  turtle.write(guess1i, font=('arial',20,'bold'))
 
  if guess1j == guesswordj:
    turtle.color("green")
    win=win+1
  elif guess1j in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(9*(300/n)+(300/n)/3),110)
  turtle.write(guess1j, font=('arial',20,'bold'))
  
  if guess1k == guesswordk:
    turtle.color("green")
    win=win+1
  elif guess1k in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(10*(300/n)+(300/n)/3),110)
  turtle.write(guess1k, font=('arial',20,'bold'))
 
  if guess1l == guesswordl:
    turtle.color("green")
    win=win+1
  elif guess1l in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(11*(300/n)+(300/n)/3),110)
  turtle.write(guess1l, font=('arial',20,'bold'))

  if guess1m == guesswordm:
    turtle.color("green")
    win=win+1
  elif guess1m in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(12*(300/n)+(300/n)/3),110)
  turtle.write(guess1m, font=('arial',20,'bold'))
 
  if guess1o == guesswordo:
    turtle.color("green")
    win=win+1
  elif guess1o in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(13*(300/n)+(300/n)/3),110)
  turtle.write(guess1o, font=('arial',20,'bold'))
  if guessword==guess1:
    gamestate=10
  else:
    gamestate=3


while guessword==guess1:
  gamestate=10

while gamestate == 3:
  print("What is your second guess")
  guess = str(input())
  guess2= "'"+ guess+"'"
  print (guess2)

  for i in wordbank:
    if guess2==i:
      gamestate = 4
  else:
    print("word is not in word bank")

while gamestate ==4:
  win=0
  print("WORD IS IN WORD BANK")
  guess2a=guess[0:1]
  guess2b=guess[1:2]
  guess2c=guess[2:3]
  guess2d=guess[3:4]
  guess2e=guess[4:5]
  guess2f=guess[5:6]
  guess2g=guess[6:7]
  guess2h=guess[7:8]
  guess2i=guess[8:9]
  guess2j=guess[9:9]
  guess2k=guess[10:11]
  guess2l=guess[11:12]
  guess2m=guess[12:13]
  guess2o=guess[13:14]
  
  if guess2a == guessworda:
    turtle.color("green")
    win = win+1
  elif guess2a in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(0*(300/n)+(300/n)/3),60)
  turtle.write(guess2a, font=('arial',20,'bold'))
  
  if guess2b == guesswordb:
    turtle.color("green")
    win = win+1
  elif guess2b in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(1*(300/n)+(300/n)/3),60)
  turtle.write(guess2b, font=('arial',20,'bold'))
 
  if guess2c == guesswordc:
    turtle.color("green")
    win = win+1
  elif guess2c in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(2*(300/n)+(300/n)/3),60)
  turtle.write(guess2c, font=('arial',20,'bold'))

  if guess2d == guesswordd:
    turtle.color("green")
    win = win+1
  elif guess2d in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(3*(300/n)+(300/n)/3),60)
  turtle.write(guess2d, font=('arial',20,'bold'))
  
  if guess2e == guessworde:
    turtle.color("green")
    win = win+1
  elif guess2e in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(4*(300/n)+(300/n)/3),60)
  turtle.write(guess2e, font=('arial',20,'bold'))
 
  if guess2f == guesswordf:
    turtle.color("green")
    win = win+1
  elif guess2f in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(5*(300/n)+(300/n)/3),60)
  turtle.write(guess2f, font=('arial',20,'bold'))

  if guess2g == guesswordg:
    turtle.color("green")
    win = win+1
  elif guess2g in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(6*(300/n)+(300/n)/3),60)
  turtle.write(guess2g, font=('arial',20,'bold'))
 
  if guess2h == guesswordh:
    turtle.color("green")
    win = win+1
  elif guess2h in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(7*(300/n)+(300/n)/3),60)
  turtle.write(guess2h, font=('arial',20,'bold'))
  
  if guess2i == guesswordi:
    turtle.color("green")
    win = win+1
  elif guess2i in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(8*(300/n)+(300/n)/3),60)
  turtle.write(guess2i, font=('arial',20,'bold'))
 
  if guess2j == guesswordj:
    turtle.color("green")
    win = win+1
  elif guess2j in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(9*(300/n)+(300/n)/3),60)
  turtle.write(guess2j, font=('arial',20,'bold'))
  
  if guess2k == guesswordk:
    turtle.color("green")
    win = win+1
  elif guess2k in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(10*(300/n)+(300/n)/3),60)
  turtle.write(guess2k, font=('arial',20,'bold'))
 
  if guess2l == guesswordl:
    turtle.color("green")
    win = win+1
  elif guess2l in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(11*(300/n)+(300/n)/3),60)
  turtle.write(guess2l, font=('arial',20,'bold'))

  if guess2m == guesswordm:
    turtle.color("green")
    win = win+1
  elif guess2m in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(12*(300/n)+(300/n)/3),60)
  turtle.write(guess2m, font=('arial',20,'bold'))
 
  if guess2o == guesswordo:
    turtle.color("green")
    win = win+1
  elif guess2o in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(13*(300/n)+(300/n)/3),60)
  turtle.write(guess2o, font=('arial',20,'bold'))
  if guessword==guess2:
    gamestate=10
  else:
    gamestate=5

while guessword==guess2:
  gamestate=10
while guessword==guess1:
  gamestate=10

while gamestate == 5:
  print("What is your third guess")
  guess = str(input())
  guess2= "'"+ guess+"'"
  print (guess2)

  for i in wordbank:
    if guess2==i:
      gamestate = 6
  else:
    print("word is not in word bank")

while gamestate ==6:
  win=0
  print("WORD IS IN WORD BANK")
  guess2a=guess[0:1]
  guess2b=guess[1:2]
  guess2c=guess[2:3]
  guess2d=guess[3:4]
  guess2e=guess[4:5]
  guess2f=guess[5:6]
  guess2g=guess[6:7]
  guess2h=guess[7:8]
  guess2i=guess[8:9]
  guess2j=guess[9:9]
  guess2k=guess[10:11]
  guess2l=guess[11:12]
  guess2m=guess[12:13]
  guess2o=guess[13:14]
  
  if guess2a == guessworda:
    turtle.color("green")
  elif guess2a in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(0*(300/n)+(300/n)/3),10)
  turtle.write(guess2a, font=('arial',20,'bold'))
  
  if guess2b == guesswordb:
    turtle.color("green")
    win = win+1
  elif guess2b in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(1*(300/n)+(300/n)/3),10)
  turtle.write(guess2b, font=('arial',20,'bold'))
 
  if guess2c == guesswordc:
    turtle.color("green")
    win = win+1
  elif guess2c in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(2*(300/n)+(300/n)/3),10)
  turtle.write(guess2c, font=('arial',20,'bold'))

  if guess2d == guesswordd:
    turtle.color("green")
    win = win+1
  elif guess2d in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(3*(300/n)+(300/n)/3),10)
  turtle.write(guess2d, font=('arial',20,'bold'))
  
  if guess2e == guessworde:
    turtle.color("green")
    win = win+1
  elif guess2e in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(4*(300/n)+(300/n)/3),10)
  turtle.write(guess2e, font=('arial',20,'bold'))
 
  if guess2f == guesswordf:
    turtle.color("green")
    win = win+1
  elif guess2f in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(5*(300/n)+(300/n)/3),10)
  turtle.write(guess2f, font=('arial',20,'bold'))

  if guess2g == guesswordg:
    turtle.color("green")
    win = win+1
  elif guess2g in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(6*(300/n)+(300/n)/3),10)
  turtle.write(guess2g, font=('arial',20,'bold'))
 
  if guess2h == guesswordh:
    turtle.color("green")
    win = win+1
  elif guess2h in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(7*(300/n)+(300/n)/3),10)
  turtle.write(guess2h, font=('arial',20,'bold'))
  
  if guess2i == guesswordi:
    turtle.color("green")
    win = win+1
  elif guess2i in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(8*(300/n)+(300/n)/3),10)
  turtle.write(guess2i, font=('arial',20,'bold'))
 
  if guess2j == guesswordj:
    turtle.color("green")
    win = win+1
  elif guess2j in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(9*(300/n)+(300/n)/3),10)
  turtle.write(guess2j, font=('arial',20,'bold'))
  
  if guess2k == guesswordk:
    turtle.color("green")
    win = win+1
  elif guess2k in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(10*(300/n)+(300/n)/3),10)
  turtle.write(guess2k, font=('arial',20,'bold'))
 
  if guess2l == guesswordl:
    turtle.color("green")
    win = win+1
  elif guess2l in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(11*(300/n)+(300/n)/3),10)
  turtle.write(guess2l, font=('arial',20,'bold'))

  if guess2m == guesswordm:
    turtle.color("green")
    win = win+1
  elif guess2m in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(12*(300/n)+(300/n)/3),10)
  turtle.write(guess2m, font=('arial',20,'bold'))
 
  if guess2o == guesswordo:
    turtle.color("green")
    win = win+1
  elif guess2o in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(13*(300/n)+(300/n)/3),10)
  turtle.write(guess2o, font=('arial',20,'bold'))
  if guessword==guess2:
    gamestate=10
  else:
    gamestate=7

while guessword==guess2:
  gamestate=10
while guessword==guess1:
  gamestate=10

while gamestate == 7:
  print("What is your fourth guess")
  guess = str(input())
  guess2= "'"+ guess+"'"
  print (guess2)

  for i in wordbank:
    if guess2==i:
      gamestate = 8
  else:
    print("word is not in word bank")

while gamestate ==8:
  win=0
  print("WORD IS IN WORD BANK")
  guess2a=guess[0:1]
  guess2b=guess[1:2]
  guess2c=guess[2:3]
  guess2d=guess[3:4]
  guess2e=guess[4:5]
  guess2f=guess[5:6]
  guess2g=guess[6:7]
  guess2h=guess[7:8]
  guess2i=guess[8:9]
  guess2j=guess[9:9]
  guess2k=guess[10:11]
  guess2l=guess[11:12]
  guess2m=guess[12:13]
  guess2o=guess[13:14]
  
  if guess2a == guessworda:
    turtle.color("green")
    win = win+1
  elif guess2a in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(0*(300/n)+(300/n)/3),-40)
  turtle.write(guess2a, font=('arial',20,'bold'))
  
  if guess2b == guesswordb:
    turtle.color("green")
    win = win+1
  elif guess2b in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(1*(300/n)+(300/n)/3),-40)
  turtle.write(guess2b, font=('arial',20,'bold'))
 
  if guess2c == guesswordc:
    turtle.color("green")
    win = win+1
  elif guess2c in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(2*(300/n)+(300/n)/3),-40)
  turtle.write(guess2c, font=('arial',20,'bold'))

  if guess2d == guesswordd:
    turtle.color("green")
    win = win+1
  elif guess2d in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(3*(300/n)+(300/n)/3),-40)
  turtle.write(guess2d, font=('arial',20,'bold'))
  
  if guess2e == guessworde:
    turtle.color("green")
    win = win+1
  elif guess2e in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(4*(300/n)+(300/n)/3),-40)
  turtle.write(guess2e, font=('arial',20,'bold'))
 
  if guess2f == guesswordf:
    turtle.color("green")
    win = win+1
  elif guess2f in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(5*(300/n)+(300/n)/3),-40)
  turtle.write(guess2f, font=('arial',20,'bold'))

  if guess2g == guesswordg:
    turtle.color("green")
    win = win+1
  elif guess2g in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(6*(300/n)+(300/n)/3),-40)
  turtle.write(guess2g, font=('arial',20,'bold'))
 
  if guess2h == guesswordh:
    turtle.color("green")
    win = win+1
  elif guess2h in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(7*(300/n)+(300/n)/3),-40)
  turtle.write(guess2h, font=('arial',20,'bold'))
  
  if guess2i == guesswordi:
    turtle.color("green")
    win = win+1
  elif guess2i in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(8*(300/n)+(300/n)/3),-40)
  turtle.write(guess2i, font=('arial',20,'bold'))
 
  if guess2j == guesswordj:
    turtle.color("green")
    win = win+1
  elif guess2j in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(9*(300/n)+(300/n)/3),-40)
  turtle.write(guess2j, font=('arial',20,'bold'))
  
  if guess2k == guesswordk:
    turtle.color("green")
    win = win+1
  elif guess2k in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(10*(300/n)+(300/n)/3),-40)
  turtle.write(guess2k, font=('arial',20,'bold'))
 
  if guess2l == guesswordl:
    turtle.color("green")
    win = win+1
  elif guess2l in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(11*(300/n)+(300/n)/3),-40)
  turtle.write(guess2l, font=('arial',20,'bold'))

  if guess2m == guesswordm:
    turtle.color("green")
    win = win+1
  elif guess2m in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(12*(300/n)+(300/n)/3),-40)
  turtle.write(guess2m, font=('arial',20,'bold'))
 
  if guess2o == guesswordo:
    turtle.color("green")
    win = win+1
  elif guess2o in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(13*(300/n)+(300/n)/3),-40)
  turtle.write(guess2o, font=('arial',20,'bold'))
  if guessword==guess2:
    gamestate=10
  else:
    gamestate=9

while guessword==guess2:
  gamestate=10
while guessword==guess1:
  gamestate=10

while gamestate == 9:
  print("What is your fifth guess")
  guess = str(input())
  guess2= "'"+ guess+"'"
  print (guess2)

  for i in wordbank:
    if guess2==i:
      gamestate = 12
  else:
    print("word is not in word bank")

while gamestate ==12:
  win=0
  print("WORD IS IN WORD BANK")
  guess2a=guess[0:1]
  guess2b=guess[1:2]
  guess2c=guess[2:3]
  guess2d=guess[3:4]
  guess2e=guess[4:5]
  guess2f=guess[5:6]
  guess2g=guess[6:7]
  guess2h=guess[7:8]
  guess2i=guess[8:9]
  guess2j=guess[9:9]
  guess2k=guess[10:11]
  guess2l=guess[11:12]
  guess2m=guess[12:13]
  guess2o=guess[13:14]
  
  if guess2a == guessworda:
    turtle.color("green")
    win = win+1
  elif guess2a in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(0*(300/n)+(300/n)/3),-90)
  turtle.write(guess2a, font=('arial',20,'bold'))
  
  if guess2b == guesswordb:
    turtle.color("green")
    win = win+1
  elif guess2b in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(1*(300/n)+(300/n)/3),-90)
  turtle.write(guess2b, font=('arial',20,'bold'))
 
  if guess2c == guesswordc:
    turtle.color("green")
    win = win+1
  elif guess2c in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(2*(300/n)+(300/n)/3),-90)
  turtle.write(guess2c, font=('arial',20,'bold'))

  if guess2d == guesswordd:
    turtle.color("green")
    win = win+1
  elif guess2d in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(3*(300/n)+(300/n)/3),-90)
  turtle.write(guess2d, font=('arial',20,'bold'))
  
  if guess2e == guessworde:
    turtle.color("green")
    win = win+1
  elif guess2e in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(4*(300/n)+(300/n)/3),-90)
  turtle.write(guess2e, font=('arial',20,'bold'))
 
  if guess2f == guesswordf:
    turtle.color("green")
    win = win+1
  elif guess2f in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(5*(300/n)+(300/n)/3),-90)
  turtle.write(guess2f, font=('arial',20,'bold'))

  if guess2g == guesswordg:
    turtle.color("green")
    win = win+1
  elif guess2g in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(6*(300/n)+(300/n)/3),-90)
  turtle.write(guess2g, font=('arial',20,'bold'))
 
  if guess2h == guesswordh:
    turtle.color("green")
    win = win+1
  elif guess2h in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(7*(300/n)+(300/n)/3),-90)
  turtle.write(guess2h, font=('arial',20,'bold'))
  
  if guess2i == guesswordi:
    turtle.color("green")
    win = win+1
  elif guess2i in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(8*(300/n)+(300/n)/3),-90)
  turtle.write(guess2i, font=('arial',20,'bold'))
 
  if guess2j == guesswordj:
    turtle.color("green")
    win = win+1
  elif guess2j in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(9*(300/n)+(300/n)/3),-90)
  turtle.write(guess2j, font=('arial',20,'bold'))
  
  if guess2k == guesswordk:
    turtle.color("green")
    win = win+1
  elif guess2k in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(10*(300/n)+(300/n)/3),-90)
  turtle.write(guess2k, font=('arial',20,'bold'))
 
  if guess2l == guesswordl:
    turtle.color("green")
    win = win+1
  elif guess2l in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(11*(300/n)+(300/n)/3),-90)
  turtle.write(guess2l, font=('arial',20,'bold'))

  if guess2m == guesswordm:
    turtle.color("green")
    win = win+1
  elif guess2m in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(12*(300/n)+(300/n)/3),-90)
  turtle.write(guess2m, font=('arial',20,'bold'))
 
  if guess2o == guesswordo:
    turtle.color("green")
    win = win+1
  elif guess2o in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(13*(300/n)+(300/n)/3),-90)
  turtle.write(guess2o, font=('arial',20,'bold'))
  if guessword==guess2:
    gamestate=10
  else:
    gamestate=13

while guessword==guess2:
  gamestate=10
while guessword==guess1:
  gamestate=10

while gamestate == 13:
  print("What is your sixth and final guess")
  guess = str(input())
  guess2= "'"+ guess+"'"
  print (guess2)

  for i in wordbank:
    if guess2==i:
      gamestate = 14
  else:
    print("word is not in word bank")

while gamestate ==14:
  win=0
  print("WORD IS IN WORD BANK")
  guess2a=guess[0:1]
  guess2b=guess[1:2]
  guess2c=guess[2:3]
  guess2d=guess[3:4]
  guess2e=guess[4:5]
  guess2f=guess[5:6]
  guess2g=guess[6:7]
  guess2h=guess[7:8]
  guess2i=guess[8:9]
  guess2j=guess[9:9]
  guess2k=guess[10:11]
  guess2l=guess[11:12]
  guess2m=guess[12:13]
  guess2o=guess[13:14]
  
  if guess2a == guessworda:
    turtle.color("green")
    win = win+1
  elif guess2a in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(0*(300/n)+(300/n)/3),-140)
  turtle.write(guess2a, font=('arial',20,'bold'))
  
  if guess2b == guesswordb:
    turtle.color("green")
    win = win+1
  elif guess2b in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(1*(300/n)+(300/n)/3),-140)
  turtle.write(guess2b, font=('arial',20,'bold'))
 
  if guess2c == guesswordc:
    turtle.color("green")
    win = win+1
  elif guess2c in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(2*(300/n)+(300/n)/3),-140)
  turtle.write(guess2c, font=('arial',20,'bold'))

  if guess2d == guesswordd:
    turtle.color("green")
    win = win+1
  elif guess2d in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(3*(300/n)+(300/n)/3),-140)
  turtle.write(guess2d, font=('arial',20,'bold'))
  
  if guess2e == guessworde:
    turtle.color("green")
    win = win+1
  elif guess2e in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(4*(300/n)+(300/n)/3),-140)
  turtle.write(guess2e, font=('arial',20,'bold'))
 
  if guess2f == guesswordf:
    turtle.color("green")
    win = win+1
  elif guess2f in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(5*(300/n)+(300/n)/3),-140)
  turtle.write(guess2f, font=('arial',20,'bold'))

  if guess2g == guesswordg:
    turtle.color("green")
    win = win+1
  elif guess2g in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(6*(300/n)+(300/n)/3),-140)
  turtle.write(guess2g, font=('arial',20,'bold'))
 
  if guess2h == guesswordh:
    turtle.color("green")
    win = win+1
  elif guess2h in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(7*(300/n)+(300/n)/3),-140)
  turtle.write(guess2h, font=('arial',20,'bold'))
  
  if guess2i == guesswordi:
    turtle.color("green")
    win = win+1
  elif guess2i in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(8*(300/n)+(300/n)/3),-140)
  turtle.write(guess2i, font=('arial',20,'bold'))
 
  if guess2j == guesswordj:
    turtle.color("green")
    win = win+1
  elif guess2j in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(9*(300/n)+(300/n)/3),-140)
  turtle.write(guess2j, font=('arial',20,'bold'))
  
  if guess2k == guesswordk:
    turtle.color("green")
    win = win+1
  elif guess2k in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(10*(300/n)+(300/n)/3),-140)
  turtle.write(guess2k, font=('arial',20,'bold'))
 
  if guess2l == guesswordl:
    turtle.color("green")
    win = win+1
  elif guess2l in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(11*(300/n)+(300/n)/3),-140)
  turtle.write(guess2l, font=('arial',20,'bold'))

  if guess2m == guesswordm:
    turtle.color("green")
    win = win+1
  elif guess2m in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(12*(300/n)+(300/n)/3),-140)
  turtle.write(guess2m, font=('arial',20,'bold'))
 
  if guess2o == guesswordo:
    turtle.color("green")
    win = win+1
  elif guess2o in guesswordletters1:
    turtle.color("yellow")
  else:
    turtle.color("black")
  turtle.penup()
  turtle.goto(-150+(13*(300/n)+(300/n)/3),-140)
  turtle.write(guess2o, font=('arial',20,'bold'))
  if guessword==guess2:
    gamestate=10
  else:
    gamestate=15


if guessword==guess2:
  gamestate=10
if guessword==guess1:
  gamestate=10


while gamestate==15:
  print("You did not guess the word.  The word was "+ guessword)
  print("To play again type 1")
  restart=int(input())
  if restart == 1:
    turtle.clear()
    print("restarting...")
    gamestate=50


while gamestate==10:
  print("Congrats You Guessed The Word!!!")
  print("To play again type 1")
  restart=int(input())
  if restart == 1:
    turtle.clear()
    gamestate=50