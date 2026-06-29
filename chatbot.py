print("AI Chat Assistant")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    if "hello" in user_input.lower():
        response = "Hello! How can I help you today?"

    elif "name" in user_input.lower():
        response = "I am an AI Chat Assistant built in Python."

    elif "ai" in user_input.lower():
        response = "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."

    else:
        response = "That's interesting. Tell me more."

    print("Assistant:", response)
