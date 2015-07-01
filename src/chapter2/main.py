'''
Created on 2015. 7. 1.

@author: jtj
'''
from chapter2.euclideanDistance import EuclideanDistance
from chapter2.pearsonCorrelationCoefficient import PearsonCorrelationCoefficient

if __name__ == '__main__':
    euclidean = EuclideanDistance()
    print(euclidean.getDistance('Lisa Rose', 'Gene Seymour'))  
    
    pearson = PearsonCorrelationCoefficient()
    print(pearson.getCorrelationCoefficient('Lisa Rose', 'Gene Seymour'))