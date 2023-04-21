def directors(movies):
    return {
        movie.director
        for movie in movies
    }

def common_elements(elements,list):
    return {
        element
        for element in elements
        if element in list
    }