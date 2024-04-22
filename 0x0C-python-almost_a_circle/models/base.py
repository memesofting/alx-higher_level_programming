#!/usr/bin/python3

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        self.__id = id

        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.__id = Base.__nb_objects
