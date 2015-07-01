'''
Created on 2015. 7. 1.

@author: jtj
'''
from chapter2.recommendations import critics
from math import sqrt
class EuclideanDistance(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def distance(self, person1, person2):
        movies = []
        scores1 = critics[person1];
        scores2 = critics[person2];
        for movie in scores1:
            if movie in scores2:
                movies.append(movie);
        score = 0;
        if not movies:
            return score
        for movie in movies:
            score = score + pow(scores1[movie] - scores2[movie],2);
        return 1/(1 + sqrt(score))    

euclidean = EuclideanDistance();
print(euclidean.distance('Lisa Rose', 'Gene Seymour'))            