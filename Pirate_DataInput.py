'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda ÖZgenç '''
class DataInputClass:
    def __init__(self):
        self.coordinate = open("PirateInput.txt").read()
        ''' PirateInput.txt icindeki veriler, coordinate degerine aktariyor '''
    def DataFileInput(self):
        self.coordinate= self.coordinate.split("=")
        '''coordinate icindeki veriler = olan yerlerden parcalara ayrilip coordinate'e aktariyor '''
