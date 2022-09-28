import telebot

token = "5660578069:AAFJiUV4FznwSyGZT99Wd664qUnbQUSzPuw"

bot=telebot.TeleBot(token)

@bot.message_handler(content_types='text')
def message_reply(message):
    print(f"[{message.chat.first_name} {message.chat.last_name}| @{message.from_user.username}] : {message.text}")
bot.infinity_polling()