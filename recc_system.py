movies = {
    "Mad Max": ["action", "adventure"],
    "Die Hard": ["action", "thriller"],
    "Titanic": ["romance", "drama"],
    "Notebook": ["romance", "drama"],
    "Inception": ["sci-fi", "thriller"],
    "Interstellar": ["sci-fi", "drama"]
}

likes = input("Which genres do you like ? (comma separated) ").lower().split(",")

# Clean up spaces
likes = [g.strip() for g in likes]

print("\nRecommended for you:")

found = False
for movie, genres in movies.items():
    if any(g in genres for g in likes):
        print("-", movie)
        found = True

if not found:
    print("Sorry, no matches found.")
