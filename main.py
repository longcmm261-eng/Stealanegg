import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ដាក់ Token របស់អ្នកនៅទីនេះ ឬប្រើ Environment Variable នៅលើ Railway
TOKEN = os.environ.get('BOT_TOKEN', 'ដាក់_TOKEN_របស់អ្នកនៅទីនេះ')
bot = telebot.TeleBot(TOKEN)

# បញ្ជីកូដដែលអនុញ្ញាត និងកូដដែលបានប្រើរួច
VALID_CODES = {"ST27QX", "ST28QX", "ST31QX"}
USED_CODES = set()

# ចងចាំស្ថានភាពរបស់អ្នកប្រើប្រាស់ (កំពុងរង់ចាំបញ្ចូលកូដ)
user_states = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Unlock 🔓", callback_data="unlock"))
    bot.send_message(message.chat.id, "សូមស្វាគមន៍! សូមចុចប៊ូតុងខាងក្រោមដើម្បី Unlock:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "unlock":
        user_states[call.from_user.id] = 'waiting_for_code'
        bot.send_message(call.message.chat.id, "សូមបញ្ចូលកូដសម្ងាត់របស់អ្នក:")

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'waiting_for_code')
def verify_code(message):
    code = message.text.strip()
    
    if code in VALID_CODES:
        if code not in USED_CODES:
            USED_CODES.add(code) # កត់ត្រាថាកូដនេះត្រូវបានប្រើហើយ
            bot.send_message(message.chat.id, f"✅ ជោគជ័យ! កូដ {code} ត្រូវបាន Unlock។")
            user_states[message.from_user.id] = None # បញ្ចប់ការរង់ចាំ
        else:
            bot.send_message(message.chat.id, "❌ កូដនេះត្រូវបានប្រើប្រាស់រួចហើយ! សូមព្យាយាមម្ដងទៀត។")
    else:
        bot.send_message(message.chat.id, "❌ កូដមិនត្រឹមត្រូវទេ! សូមព្យាយាមម្ដងទៀត។")

print("Bot កំពុងដំណើរការ...")
bot.polling()
