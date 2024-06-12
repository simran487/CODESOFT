import re
import random
import nltk
import pandas as pd

# Download NLTK data 
nltk.download('punkt')

# Load the dataset of conversations
df = pd.read_csv('conversations.csv')

# Define rule-based patterns and responses
patterns_responses = [
    (r'hello|hi|hey', ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r'how are you', ["I'm just a bot, but I'm doing great!", "I'm here to assist you. How can I help?"]),
    (r'what is your name', ["I am a rule-based chatbot."]),
    (r'bye|goodbye', ["Goodbye!", "See you later!", "Take care!"])
]

def match_rule_based_response(user_input):
    for pattern, responses in patterns_responses:
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return None

def find_response_in_dataset(user_input):
    # Tokenize user input
    tokens = nltk.word_tokenize(user_input.lower())
    # Search for a matching response in the dataset
    for i, row in df.iterrows():
        if all(token in nltk.word_tokenize(row['input'].lower()) for token in tokens):
            return row['response']
    return None

def chatbot():
    print("Chatbot: Hi! I am a rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye!")
            break
        
        # Try to match a rule-based response
        response = match_rule_based_response(user_input)
        
        if response is None:
            # If no rule-based response is found, look for a response in the dataset
            response = find_response_in_dataset(user_input)
        
        if response is None:
            response = "I'm sorry, I don't understand that."
        
        print(f"Chatbot: {response}")

# Start the chatbot
chatbot()
