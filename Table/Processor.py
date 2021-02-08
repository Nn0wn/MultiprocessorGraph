from typing import Optional

from Graph.Node import Node


class Processor:

    def __init__(self):
        self.__task = None
        self.__processing = False
        self.__finishTime = None

    def task(self):
        return self.__task

    def setTask(self, val: Optional[Node], time: Optional):
        self.__task = val
        if val:
            self.__finishTime = time + val.weight()
        else:
            self.__finishTime = None

    def isProcessing(self):
        return self.__processing

    def setProcessing(self, val: bool):
        self.__processing = val

    def finishTime(self):
        return self.__finishTime
