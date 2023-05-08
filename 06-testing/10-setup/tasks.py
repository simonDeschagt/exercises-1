import datetime


class Task:
    def __init__(self, description, due_date, finished = False):
        self.__description = description
        self.__due_date = due_date
        self.finished = finished

    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def description(self):
        return self.__description
    
    # @finished.setter
    # def finished(self):
    #     self.finished = not self.finished


class TaskList():
    def __init__(self, calendar):
        self.tasklist = list()
        self.__calendar = calendar

    def __len__(self):
        return len(self.tasklist)

    def add_task(self, task):
        if task.due_date < self.__calendar.today:
            raise RuntimeError()
        self.tasklist.append(task)

    @property
    def finished_tasks(self):
        return [x for x in self.tasklist if x.finished]

    @property
    def due_tasks(self):
        return [x for x in self.tasklist if x.finished == False]
    
    @property
    def overdue_tasks(self):
        return [x for x in self.tasklist if not x.finished and x.due_date < self.__calendar.today]