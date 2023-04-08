'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from Pirate_Coordinate import CoordinateClass
ClassCoordinate=CoordinateClass()
ClassCoordinate.CoordinatePartition()
class WriteClass:
    def CoordinateOutput(self):
        for row in range(len(ClassCoordinate.x_shifted)):
            print (str(ClassCoordinate.x_shifted[row])+","+str(ClassCoordinate.y_shifted[row]))
            '''Cordinatlar ekrana yazdirilir'''
ClassWrite=WriteClass()
ClassWrite.CoordinateOutput()