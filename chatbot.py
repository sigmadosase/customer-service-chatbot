# chatbot.py

import random
import nltk
from nltk.tokenize import word_tokenize

responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm a bot, but I'm functioning perfectly!", "All good!"],
    "help": ["Sure, I'm here to help. Ask me anything."],
    "price": ["Our pricing depends on your needs. Can you be more specific?"],
    "bye": ["Goodbye!", "Have a nice day!", "See you again!"],
        "good mornig": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "good night": ["I'm a bot, but I'm functioning perfectly!", "All good!"],

}

def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    for word in tokens:
        if word in responses:
            return random.choice(responses[word])
    return "I'm sorry, I didn't understand that."
