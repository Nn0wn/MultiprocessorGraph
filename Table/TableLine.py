class TableLine:

    def __init__(self, time=None, availableTasks=None, processors=None):
        self.__time = time
        self.__availableTasks = availableTasks
        self.__processors = processors
        # self.__fieldWidth = [0, 0]

    def time(self):
        return self.__time

    def setTime(self, val):
        self.__time = val

    def availableTasks(self):
        return self.__availableTasks

    def setAvailableTasks(self, val):
        self.__availableTasks = val

    def processors(self):
        return self.__processors

    def setProcessors(self, val):
        self.__processors = val

    def print(self):
        print(str('| {:10s} | {:15s} |' + ''.join(' {:15s} |'
                                                  for _ in self.__processors)).format(str(self.__time),
                                                                                      str(self.__availableTasks),
                                                                                      *self.__processors))
