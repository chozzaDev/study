'''
Created on 2015. 7. 1.

@author: jtj
'''
from chapter2.recommendations import critics
from math import sqrt
from chapter2.movieScore import MovieScore
class EuclideanDistance(MovieScore):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def getDistance(self, person1, person2):
        movies = self.intersection(person1, person2)
        scores1 = critics[person1];
        scores2 = critics[person2];
        score = 0;
        if not movies:
            return score
        for movie in movies:
            score = score + pow(scores1[movie] - scores2[movie],2);
        return 1/(1 + sqrt(score))    