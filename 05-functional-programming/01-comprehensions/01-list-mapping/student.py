def titles(lijst):
    return [
        movie.title for movie in lijst
    ]

def titles_and_years(lijst):
    return [
        (movie.title, movie.year) for movie in lijst
    ]

def titles_and_actor_counts(lijst):
    return [
        (movie.title, len(movie.actors)) for movie in lijst
    ]

def reverse_words(sentence):
    return " ".join([word[::-1] for word in sentence.split(' ')])