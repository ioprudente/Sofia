import  wikipedia

def searchOnWikipedia(user_search):
    response = wikipedia.summary(user_search,  sentences = 1)
    return response
