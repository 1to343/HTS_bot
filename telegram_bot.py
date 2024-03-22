from flask import Flask, request
import telegram
import telebot
from telebot import types

# Create a new bot instance
bot = telebot.TeleBot("6279655479:AAGS-mulMsfFyvOPdw4BK7OFVSfUQdoceW4")

# Handle the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello! Welcome to your Telegram bot.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "I'm here to help you. How can I assist you today?")

@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.reply_to(message, "This is telegram bot of DiscoverEd. It is a platform for students to learn and grow.")


courses = {
    "Course1": {
        "description": "Description for Course1",
        "teacher": "Teacher for Course1"
    },
    "Course2": {
        "description": "Description for Course2",
        "teacher": "Teacher for Course2"
    }
    # Add more courses as needed
}

FAQ = {
    "How do I enroll in a course?": "You can enroll in a course by clicking on the 'Enroll' button on the course page.",
    "How do I contact my teacher?" : "You can contact your teacher by sending them a message through the platform.",
    "Would there be other courses in the future?" : "Yes, we are constantly adding new courses to the platform. Keep an eye out for updates!"
}

@bot.message_handler(commands=['courses'])
def send_courses(message):
    markup = types.InlineKeyboardMarkup()
    for course in courses:
        markup.add(types.InlineKeyboardButton(text=course, callback_data=course))
    bot.send_message(message.chat.id, "Here are the available courses:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    course_info = courses[call.data]
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Course: {call.data}\nDescription: {course_info['description']}\nTeacher: {course_info['teacher']}")

@bot.message_handler(commands=['FAQ'])
def send_faq(message):
    bot.send_message(message.chat.id, "Here are some frequently asked questions:\n." + "\n".join(f"{k}. {v}" for k, v in FAQ.items()))

# Handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "You said: " + message.text)

# Start the bot
bot.polling()
