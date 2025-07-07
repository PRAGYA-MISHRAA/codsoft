movies = {
    "inception": ["sci-fi", "thriller"],
    "interstellar": ["sci-fi", "drama"],
    "avatar": ["sci-fi", "adventure"],
}

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input == "exit":
        print("Bot: Goodbye!")
        break
    
    if user_input in movies:
        print("Bot: Recommended genres are:", movies[user_input])
    else:
        print("Bot: Sorry, I don’t understand that. Try typing just the movie title or type 'exit' to quit.")
