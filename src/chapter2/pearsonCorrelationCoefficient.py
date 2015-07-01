'''
Created on 2015. 7. 1.
Pearson’s product moment correlation coefficient
@author: jtj
'''
from chapter2.recommendations import critics
from math import sqrt
from chapter2.movieScore import MovieScore

class PearsonCorrelationCoefficient(MovieScore):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def getCorrelationCoefficient(self, person1, person2):
        movies = self.intersection(person1, person2)
        scores1 = critics[person1];
        scores2 = critics[person2];
        score = 0;
        if not movies:
            return score    
        sum1 = sum([scores1[movie] for movie in movies])
        sum2 = sum([scores2[movie] for movie in movies])
        
        sum1Sq = sum([pow(scores1[movie],2) for movie in movies])
        sum2Sq = sum([pow(scores2[movie],2) for movie in movies])
        
        pSum = sum([scores1[movie] * scores2[movie] for movie in movies])
        n = len(movies);
        num = pSum - (sum1*sum2/n)
        den = sqrt((sum1Sq-pow(sum1, 2)/n) * (sum2Sq-pow(sum2,2)/n))
        if den == 0: return 0;
        r = num/den
        return r;