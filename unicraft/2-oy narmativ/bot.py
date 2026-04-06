from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import json

TOKEN = "6886201566:AAHJM3qn7P7iHt3InEdR9p34G7sZ7JTUTT4"



def start(update: Update, context: CallbackContext):
    name =
    update.message.reply_text(f'salom {name} men sizning botingizman\n nima kamandala bor /info /menu /anketa\n /infoda siz oz malumotingizni olasiz\n /menuda knopalar  \n /anketada anketa toldirasiz 3ta mosqich \n 1.bosqich ismingiz\n 2.bosqich familya \n3.bosqich telifon raqm')

def info(update: Update, context: CallbackContext):
    user = update.message.from_user
    id1 = user.id
    first_name = user.first_name
    user_name = user.username or "yo‘q"
    last_name = user.last_name or "yo‘q"
    language_cod = user.language_code
    update.message.reply_text(f"sizning malumotingiz \nId: {id1} \nFirst_name: <b>{first_name}</b> \nLast_name: <b>{last_name}</b> \nuser_name: @{user_name}\n language_code: <b>{language_cod}</b> taishganimdan hursandman")

    new_user = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "language": user.language_code
    }

    try:
        with open("tg_data.json", "r", encoding="utf-8") as f:
            users = json.load(f)
    except:
        users = []

    for u in users:
        if u["id"] == user.id:
            update.message.reply_text("ℹ️ Siz allaqachon ro‘yxatga qoshilgan ekansiz")
            return

    users.append(new_user)

    with open("tg_data.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


    print("user malumoti saqlandi")
    update.message.reply_text("✅ Ma'lumotlaringiz saqlandi!")


updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
# dp.add_handler(CommandHandler('menu', menu))
dp.add_handler(CommandHandler('info', info))
# dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
# dp.add_handler(CallbackQueryHandler(button_handler))
updater.start_polling()
updater.idle()
