from Graph.Graph import Graph
from Table.Processor import Processor
from Table.TableLine import TableLine


class ProcessorTable:

    def __init__(self, graph: Graph, log=False):
        self.__processors = [Processor() for _ in range(graph.getProcessors())]
        self.__edges = graph.edges().copy()
        self.__availableTasks = [node for layer in graph.layers() for node in layer
                                 if node.id() not in [edge.idTo() for edge in self.__edges]
                                 and node.id() != 0]
        self.__notAvailableTasks = [node for layer in graph.layers() for node in layer
                                    if node.id() in [edge.idTo() for edge in self.__edges]
                                    and node.id() != 0]
        self.__processedTasks = []
        self.__time = 0
        self.__log = log
        self.__logLines = [TableLine('Time', 'Available tasks',
                                     ['Processor ' + str(i + 1) for i in range(len(self.__processors))]),
                           TableLine('-' * 10, '-' * 15, ['-' * 15 for _ in range(len(self.__processors))])]

    def process(self):
        while len(self.__availableTasks) > 0 or True in [proc.isProcessing() for proc in self.__processors]:
            self.__logLines.append(TableLine())
            self.__setProcessorTasks()
            self.__finishNearestTask()
            self.__updateAvailableTasks()

    def print(self):
        title = ' Processor loading table '
        width = (len(self.__processors) * 18 + 15 + 10 + 7 - 2)
        print(' ' + '-' * width + ' ')
        print('|' + ' ' * int((width - (len(title))) / 2) + title + ' ' * (width - (len(title)) - int((width - (len(title))) / 2)) + '|')
        print('| ' + '-' * (len(self.__processors) * 18 + 15 + 10 + 7 - 4) + ' |')
        for line in self.__logLines:
            line.print()
        print(' ' + '-' * (len(self.__processors) * 18 + 15 + 10 + 7 - 2) + ' ')

    def __setProcessorTasks(self):
        self.__logLines[-1].setAvailableTasks([task.id() for task in self.__availableTasks])
        for index, proc in enumerate(self.__processors):
            if not proc.isProcessing() and len(self.__availableTasks) > 0:
                task = min(self.__availableTasks, key=lambda node: node.weight())
                proc.setTask(task, self.__time)
                proc.setProcessing(True)
                self.__availableTasks.pop(self.__availableTasks.index(task))
                if self.__log:
                    print('<===== Setting task [', task.id(), '] on processor [', index + 1, '] at time [',
                          self.__time, '] =====>')
        self.__logLines[-1].setProcessors([str(proc.task().id()) if proc.isProcessing() else 'Not processed'
                                           for proc in self.__processors])

    def __finishNearestTask(self):
        chosenProc = min([proc for proc in self.__processors if proc.isProcessing()],
                         key=lambda proc: proc.finishTime())
        nearestTask = chosenProc.task()
        self.__edges = [edge for edge in self.__edges if edge.idFrom() != nearestTask.id()]
        self.__processedTasks.append(nearestTask)
        if self.__time == chosenProc.finishTime():
            self.__logLines.pop(-1)
        else:
            self.__logLines[-1].setTime('{} - {}'.format(str(self.__time), str(chosenProc.finishTime())))
        self.__time = chosenProc.finishTime()
        chosenProc.setTask(None, None)
        chosenProc.setProcessing(False)
        if self.__log:
            print('<===== Finished task [', nearestTask.id(), '] on processor [',
                  self.__processors.index(chosenProc) + 1, '] at time [', self.__time, '] =====>')

    def __updateAvailableTasks(self):
        updatedTasks = [task for task in self.__notAvailableTasks
                        if task.id() not in [edge.idTo() for edge in self.__edges]]
        self.__availableTasks.extend(updatedTasks)
        self.__notAvailableTasks = [task for task in self.__notAvailableTasks if task not in updatedTasks]
        if self.__log:
            print('<===== Updated tasks - available:', [task.id() for task in self.__availableTasks],
                  '- not available:', [task.id() for task in self.__notAvailableTasks], '=====>')
