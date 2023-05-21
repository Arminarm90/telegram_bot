import telebot

# Initialize your bot with the bot token
bot = telebot.TeleBot('6040505891:AAHxsbKZfAWbyiFczwoLYb_Y6ibzR_ibKnM')

# Dictionary to map button titles to user IDs
user_ids = {
    
    'آرمین': 1324005362,
    'پشتیبان 1': 5568959797# Replace with the desired user ID
      # Replace with the desired user ID
    # Add more buttons and user IDs as needed
}

@bot.message_handler(commands=['start'])
def start(message):
    # Create a keyboard with buttons representing user IDs
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    buttons = [telebot.types.KeyboardButton(title) for title in user_ids.keys()]
    keyboard.add(*buttons)

    # Send a welcome message with the keyboard
    bot.send_message(message.chat.id, 'به ربات پشتیبانی کدلرن خوش آمدید. با کدام بخش میخواهید در ارتباط باشید؟:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in user_ids.keys())
def handle_button(message):
    # Get the selected button title
    selected_button = message.text

    # Prompt the user to enter a message
    bot.send_message(message.chat.id, f'  ارسال پیام به :{selected_button} ، لطفا پیام خود را بهمراه شماره تلفن و یا یوزرنیم تلگرام را به همراه @ بگذارید تا در اسرع وقت به آن پاسخ داده شود :')

    # Register a handler to wait for the user's message
    bot.register_next_step_handler(message, lambda m: send_message_to_user(m, selected_button))

def send_message_to_user(message, button):
    # Get the user's message
    user_message = message.text

    # Get the corresponding user ID for the selected button
    user_id = user_ids.get(button)

    if user_id:
        # Send the user's message to the specified user ID
        bot.send_message(user_id, f'پیام دریافتی : {user_message}')

        # Reply to the user with a confirmation message
        bot.send_message(message.chat.id, f'پیام شما به  {button} با موفقیت انجام شد .')
    else:
        # Reply to the user with an error message if the button is not associated with a user ID
        bot.send_message(message.chat.id, f'خطا: دستور اشتباه .')


# Start the bot
bot.polling(timeout=15)
