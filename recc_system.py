# Movie Recommendation System

movies = {
    "inception": ["sci-fi", "thriller"],
    "interstellar": ["sci-fi", "drama"],
    "avatar": ["sci-fi", "adventure"],
    "titanic": ["romance", "drama"],
    "the godfather": ["crime", "drama"],
    "the dark knight": ["action", "crime", "drama"],
    "parasite": ["thriller", "drama"],
    "the matrix": ["sci-fi", "action"],
    "frozen": ["animation", "adventure", "family"],
    "joker": ["crime", "drama", "thriller"],
    "finding nemo": ["animation", "adventure", "family"],
    "gladiator": ["action", "drama"],
    "la la land": ["musical", "romance", "drama"],
    "avengers": ["action", "sci-fi", "adventure"],
    "harry potter": ["fantasy", "adventure"],
}

print("Bot: Hi! Type the name of a movie to see its genres, or type 'exit' to quit.")

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input == "exit":
        print("Bot: Goodbye!")
        break
    
    if user_input in movies:
        print("Bot: Recommended genres are:", movies[user_input])
    else:
        print("Bot: Sorry, I don't understand that. Try typing just the movie title or type 'exit' to quit.")
