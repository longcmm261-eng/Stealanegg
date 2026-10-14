import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ដាក់ Token របស់អ្នកនៅទីនេះ
TOKEN = os.environ.get('BOT_TOKEN', 'ដាក់_TOKEN_របស់អ្នកនៅទីនេះ')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # បង្កើត Reply Keyboard (resize_keyboard=True ដើម្បីឲ្យប៊ូតុងតូចល្មមស្អាត)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # បង្កើតប៊ូតុង
    btn1 = KeyboardButton("1 👨🏻‍💻គណនី")
    btn2 = KeyboardButton("2 🛍️ ហាងសេវា")
    btn3 = KeyboardButton("3 💬 អ្នកគ្រប់គ្រង")
    btn4 = KeyboardButton("4 ប្រវត្ដិទិញ")
    btn5 = KeyboardButton("5 របៀបប្រើ")
    
    # រៀបចំប៊ូតុង (2 ប៊ូតុងក្នុងមួយជួរ និងជួរចុងក្រោយមាន 1)
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    
    bot.send_message(message.chat.id, "សូមស្វាគមន៍! សូមជ្រើសរើសម៉ឺនុយខាងក្រោម៖", reply_markup=markup)

# ចាប់យកអត្ថបទនៅពេលអ្នកប្រើប្រាស់ចុចប៊ូតុង
@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    text = message.text
    
    if text == "1 👨🏻‍💻គណនី":
        bot.send_message(message.chat.id, "បង្ហាញព័ត៌មានគណនីរបស់អ្នកនៅទីនេះ...")
        
    elif text == "2 🛍️ ហាងសេវា":
        bot.send_message(message.chat.id, "សូមស្វាគមន៍មកកាន់ហាងសេវា! សូមរើសសេវាកម្ម...")
        
    elif text == "3 💬 អ្នកគ្រប់គ្រង":
        bot.send_message(message.chat.id, "ទំនាក់ទំនងអ្នកគ្រប់គ្រងតាមរយៈ៖ @AdminUsername")
        
    elif text == "4 ប្រវត្ដិទិញ":
        bot.send_message(message.chat.id, "នេះជាប្រវត្តិទិញរបស់អ្នក៖ \n- មិនទាន់មានទិន្នន័យ")
        
    elif text == "5 របៀបប្រើ":
        ៩bot.send_message(message.chat.id, "របៀបប្រើប្រាស់៖ \n១. ចុច... \n២. ជ្រើសរើស...")
        
    else:
        # ប្រសិនបើគេវាយអក្សរផ្សេងក្រៅពីប៊ូតុង
        bot.send_message(message.chat.id, "សូមជ្រើសរើសម៉ឺនុយណាមួយនៅខាងក្រោម។")

print("Bot កំពុងដំណើរការ...")
bot.polling()
