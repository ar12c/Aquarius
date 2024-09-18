from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from flask import Flask, render_template

app = Flask(__name__)

chatbot = ChatBot('Aquarius')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)
# Train the chatbot based on the english corpus

trainer2.train([
    "What is your name?",
    "I am Aquarius",
])

trainer2.train([
    "Goodbye",
    "It was nice talking to you!",
])

trainer2.train([
    "Hello",
    "hi",
    "Hello",
    ":3c",
    "Hi, how may I help you",
])

trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
print('Aquarius has started.')

# The following loop will execute each time the user enters input
while True:
        user_input = input("You:")

        bot_response = chatbot.get_response(user_input)

        print("Aquarius: ", bot_response)
        

@app.route("/")
def main():
    return render_template("index.html")
#bleh

if __name__ == "__main__":
    app.run(debug=True)