#!/usr/bin/python
# -*- encoding: utf8 -*-

import csv


class weight:
    def __init__(self):
        self.dict_weight = []
        self.load()
        
    def load(self):
        """
         Load parameters includes in the *weight.csv* file
        """
        f = open('weight.csv', 'r')
        reader = csv.reader(f, delimiter=',')
        for line in reader :
            if len(line)==3 :
                self.dict_weight.append({
                    'class' : line[0],
                    'type' : line[1],
                    'weight' : line[2]
                })
        f.close()

    def search(self,class_,typ) :
        """
            Returns a weight
        """
        for line in self.dict_weight :
            if line['class']==class_ and line['type']== typ :
                return line['weight']
        
        # Default value
        return 100


if __name__ == '__main__':
    p = weight()
    print p.dict_weight
    print p.search("highway","secondary")
    print p.search("highway","path")
    print p.search("highway","track")
    print p.search("highway","toto")
    print p.search("place","town")
    
