class Edge:

    def __init__(self, idFrom: int, idTo: int):
        self.__idFrom = idFrom
        self.__idTo = idTo

    def idFrom(self):
        return self.__idFrom

    def idTo(self):
        return self.__idTo
