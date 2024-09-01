import os
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key=os.getenv('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'))

def get_gpt_response(prompt):
    try:
        # Create a chat completion
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # Get the response content
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chat():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = get_gpt_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
