from typing import List, Union


class Node:

    def __init__(self, id: int, weight: Union[int, float]):
        self.__id = id
        self.__weight = weight
        self.__critical = 0
        self.__criticalPath = []

    def id(self):
        return self.__id

    def weight(self):
        return self.__weight

    def critical(self):
        return self.__critical

    def setCritical(self, val: int):
        self.__critical = val

    def criticalPath(self):
        return self.__criticalPath

    def setCriticalPath(self, val: List[int]):
        self.__criticalPath = val
