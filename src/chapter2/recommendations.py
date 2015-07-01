'''
Created on 2015. 7. 1.

@author: jtj
'''
critics = {}
def getUser(name):
    global critics
    if name not in critics :
        critics[name] = {}
    return critics[name]
def setMovieScore(user, movie, score):
    user[movie] = score

ladyInTheWater = 'Lady in the Water'    
snakesOnAPlane = 'Snakes on a Plane'
justMyLuck = 'Just My Luck'
supermanReturns = 'Superman Returns'
youMeAndDupree = 'You, Me and Dupree'
theNightListener = 'The Night Listener'
user = getUser('Lisa Rose')
setMovieScore(user, ladyInTheWater, 2.5 )
setMovieScore(user, snakesOnAPlane, 3.5 )
setMovieScore(user, justMyLuck, 3.0 )
setMovieScore(user, supermanReturns, 3.5 )
setMovieScore(user, youMeAndDupree, 2.5 )
setMovieScore(user, theNightListener, 3.0 )
user = getUser('Gene Seymour')
setMovieScore(user, ladyInTheWater, 3.0 )
setMovieScore(user, snakesOnAPlane, 3.5 )
setMovieScore(user, justMyLuck, 1.5 )
setMovieScore(user, supermanReturns, 5.0 )
setMovieScore(user, youMeAndDupree, 3.5 )
setMovieScore(user, theNightListener, 3.0 )
user = getUser('Micheal Phillips')
setMovieScore(user, ladyInTheWater, 2.5 )
setMovieScore(user, snakesOnAPlane, 3.0 )
setMovieScore(user, supermanReturns, 3.5 )
setMovieScore(user, theNightListener, 4.0 )
user = getUser('Claudia Puig')
setMovieScore(user, snakesOnAPlane, 3.5 )
setMovieScore(user, justMyLuck, 3.0 )
setMovieScore(user, supermanReturns, 4.0 )
setMovieScore(user, youMeAndDupree, 2.5 )
setMovieScore(user, theNightListener, 4.5 )
user = getUser('Mick LaSalle')
setMovieScore(user, ladyInTheWater, 3.0 )
setMovieScore(user, snakesOnAPlane, 4.0 )
setMovieScore(user, justMyLuck, 2.0 )
setMovieScore(user, supermanReturns, 3.0 )
setMovieScore(user, theNightListener, 3.0 )
setMovieScore(user, youMeAndDupree, 2.0 )
user = getUser('Jack Matthews')
setMovieScore(user, ladyInTheWater, 3.0 )
setMovieScore(user, snakesOnAPlane, 4.0 )
setMovieScore(user, theNightListener, 3.0 )
setMovieScore(user, supermanReturns, 5.0 )
setMovieScore(user, youMeAndDupree, 3.5 )
user = getUser('Toby')
setMovieScore(user, snakesOnAPlane, 4.5 )
setMovieScore(user, youMeAndDupree, 1.0 )
setMovieScore(user, supermanReturns, 4.0 )
print(critics)


