import telebot
from telebot import types

name = 'Jiniret'
energy = 70
satiety = 10
happiness = 100
balance = 0

bot = telebot.TeleBot('')


def feed():
  global satiety, energy

  satiety += 10
  energy += 5


def play():
  global satiety, happiness, energy

  satiety -= 5
  energy -= 10
  happiness += 10


def sleep():
  global satiety, happiness, energy

  satiety -= 5
  happiness += 10
  energy = 70


def send():
  global balance, happiness
  balance += 10
  happiness += 5


@bot.message_handler(commands=['feed'])
def feed_handler(message):
  global satiety, happiness
  feed()
  bot.send_message(
      message.chat.id, 'чем ты хочешь его покормить:'
      'брауни, острые чипсы, баклажаны')
  check(message)
  bot.register_next_step_handler(message, feed_handler)
  if message.text == 'брауни':
    satiety += 15
    happiness += 17
  if message.text == 'острые чипсы':
    satiety += 20
    happiness += 20
  if message.text == 'баклажаны':
    satiety += 2
    happiness -= 15


@bot.message_handler(commands=['play'])
def play_handler(message):
  play()
  bot.send_message(message.chat.id,
                   f'{name} поиграл, теперь его счастье {happiness}')
  check(message)


@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
  sleep()
  bot.send_message(message.chat.id,
                   f'{name} поспал, теперь его энергия {happiness}')
  check(message)


@bot.message_handler(commands=['send'])
def send_handler(message):
  send()
  bot.send_message(message.chat.id, f'{name} получил деньги, его баланс {balance}')
  check(message)


def check(message):
  global satiety, happiness, energy
  if satiety <= 0:
    bot.send_message(message.chat.id, f'{name} умер от голода...( не забывай его кормить!')
  elif satiety >= 10:
    bot.send_message(message.chat.id, f'{name} наелся и счастлив!')
  if happiness < 0:
    bot.send_message(message.chat.id, f'{name} умер от тоски...( не забывай с ним играть!')
  elif happiness > 100:
    bot.send_message(message.chat.id, f'{name} счастлив как никогда')
  if energy < 70:
    bot.send_message(message.chat.id, f'{name} умер от истощения...( ’')
  elif energy > 70:
    bot.send_message(message.chat.id, f'{name} полон сил и энергии!!')
    
bot.polling()
