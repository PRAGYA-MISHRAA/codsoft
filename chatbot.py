def simple_chatbot():
    print("Hello! I'm your chatbot. Type 'exit' to leave.")

    while True:
        message = input("You: ").lower()

        if message == "exit":
            print("Bot: Bye! Take care.")
            break
        elif message == "hi":
            print("Bot: Hi there!")
        elif message == "who are you":
            print("Bot: I'm just a simple chatbot.")
        elif "help" in message:
            print("Bot: Sure, how can I help you?")
        else:
            print("Bot: Sorry, I don’t understand that.")

simple_chatbot()
