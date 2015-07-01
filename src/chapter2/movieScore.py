'''
Created on 2015. 7. 1.

@author: jtj
'''
from chapter2.recommendations import critics
class MovieScore(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
    def intersection(self, person1, person2): 
        movies = []
        scores1 = critics[person1];
        scores2 = critics[person2];
        for movie in scores1:
            if movie in scores2:
                movies.append(movie); 
        return movies;        