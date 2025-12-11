movies = {
    "Inception": ["Sci-Fi", "Action"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Shrek": ["Animation", "Comedy"],
    "Toy Story": ["Animation", "Family"],
    "Interstellar": ["Sci-Fi", "Drama"]
}
def searcher(genres):
    result = {}
    for movie, genre in genres.items():
        for gen in genre:
            if gen not in result:
                result[gen] = []
            result[gen].append(movie)
    
    return result

    
print(searcher(movies))