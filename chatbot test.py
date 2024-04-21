import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m fine, thanks. How about you?']),
    (r'(.*) your name?', ['My name is ALEXZIAIX.']),
    (r'(.*) help (.*)', ['Sure, I can help you. What do you need assistance with?']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

def main():
    print("Welcome to the Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
