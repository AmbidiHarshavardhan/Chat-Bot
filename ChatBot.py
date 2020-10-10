import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot=ChatBot('Bot')

bot.set_trainer(ListTrainer)

langFile = os.listdir('chatterbot-corpus-master/chatterbot_corpus/data/english/')

for file in langFile:
  print(file)
for file in langFile:
  data=open('chatterbot-corpus-master/chatterbot_corpus/data/english/'+file,'r',encoding='utf-8').readlines()
  bot.train(data)
while True:
  ip=input("Chat with Bot : ")
  if (ip.strip()!='bye' or ip.strip()!='Bye'):
    reply=bot.get_response(ip)
    print("Bot : ",reply)
  if (ip.strip()=='bye' or ip.strip()=='Bye'):
    print("Missing you so much......")
    break