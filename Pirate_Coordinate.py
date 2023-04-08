'''Assignment: Snake
Created on 13 October. 2020
Author: Ceyda Özgenç '''
from Pirate_DataInput import DataInputClass
ClassInput=DataInputClass()
ClassInput.DataFileInput()
class CoordinateRowClass():
    def __init__(self):
        self.coordinate_row=[]
        self.list=[]
        self.coordinate_weave=[]
    def CordinateRowPartition(self):
        for row in range(len(ClassInput.coordinate)):
            self.number=1
            self.list=ClassInput.coordinate[row]
            '''coordinate icindeki veriler list'e aktariyor '''
            self.list=self.list.split(" ")
            '''list icindeki veriler " " olan yerlerden parcalara ayrilip list'e aktariyor '''
            for count in range(len(self.list)):
                self.coordinate_row.insert(row,self.list)
                '''list ici liste yapilarak list'deki veriler coordinate_row aktariyor '''
                self.CoordinateWeave(row,count,self.number)
                self.number += 2
    def CoordinateWeave(self,index,count,number):
        if (index==0):
            self.coordinate_weave.insert(count,self.coordinate_row[index][count])
            '''eger birinci satirda isek coordinate_row icindeki veriler direk coordinate_weav'e eklenir'''
        else:
            self.coordinate_weave.insert(number,self.coordinate_row[index][count])
            '''degil isek coordinate_row icindeki weave yaparak coordinate_weav'e eklenir'''
ClassCoordinateRow=CoordinateRowClass()
ClassCoordinateRow.CordinateRowPartition()
class CoordinateClass:
    def __init__(self):
        self.x=[]
        self.y=[]
        self.x_shifted=[]
        self.y_shifted=[]
    def CoordinatePartition(self):
        for coordinate in range(len(ClassCoordinateRow.coordinate_weave)):
            self.x.insert(coordinate,ClassCoordinateRow.coordinate_weave[coordinate].split(",")[0])
            '''coordinate_weave icindeki cordinatlardan x cordinati x'e aktarilir'''
            self.y.insert(coordinate,ClassCoordinateRow.coordinate_weave[coordinate].split(",")[1])
            '''coordinate_weave icindeki cordinatlardan y cordinati y'e aktarilir'''
            self.CoordinateShifted(coordinate)

    def CoordinateShifted(self,coordinate):
        self.x_shifted.insert(coordinate,int(self.x[coordinate])+1)
        '''x icindeki cordinatlardan verilen deger kadar artirilir ve cordinati x_shifted'e aktarilir'''
        self.y_shifted.insert(coordinate, int(self.y[coordinate]) + 0)
        '''y icindeki cordinatlardan verilen deger kadar artirilir ve cordinati y_shifted'e aktarilir'''

