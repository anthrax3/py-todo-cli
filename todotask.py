from datetime import datetime
import time

from member_repo import BaseRepository, TextFileRepository, SqliteRepository, ArrayRepository

class ToDoTask:
    def __init__(self, title_task, desc_task):
        """
            flag_done   - признак сделана/не сделана задача (True/False)
            title_task  - заголовок задачи
            desc_task   - подробное описание задачи
            time_create - время создания задачи
        """
        #self._repo = repository # репозиторий данных
        #if not isinstance(self._repo, BaseRepository):
        #    raise Exception()
        self._title_task = title_task
        self._desc_task = desc_task
        self._time_create = datetime.now()
        self._flag_done = False

    def done(self):
        """
            Make Task is Done        
        """
        self._flag_done = True

    def undone(self):
        """
            Make Task is UnDone        
        """
        self._flag_done = False

    def __str__(self):
        if self._flag_done:
            flag_done = '[x]'
        else:
            flag_done = '[ ]'
        result = "{0} : {1} - {2} - {3}".format(flag_done, self._title_task, self._desc_task, self._time_create )
        return result

    def __repr__(self):
        if self._flag_done:
            flag_done = '[x]'
        else:
            flag_done = '[ ]'
        result = "{0}  {1} - {2} - {3}".format(flag_done, self._title_task, self._desc_task, self._time_create )

        return result

class ToDoList:    
    def __init__(self, repository=TextFileRepository):
        self._repo = repository
        self._list = []

    def add(task):
        if not isinstance(ToDoTask, task):
            raise Exception()
        self._list.add(task)
    
        

# ---------------------
t1 = ToDoTask("первая задача заголовок", "описание задачи 1")
#time.sleep(10)
t2 = ToDoTask("вторая задача заголовок", "описание задачи 2")

list_task = [t1, t2]
print(list_task)



"""
print(t1)
print(t2)
t2.done()
print(t2)
t2.undone()
print(t2)
"""