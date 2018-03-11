from datetime import datetime
# import time

from member_repo import BaseRepository, TextFileRepository, SqliteRepository, ArrayRepository


class ToDoTask:

    def __init__(self, title_task, desc_task="", flag_done=False, time_create=datetime.now()):
        """
            flag_done   - признак сделана/не сделана задача (True/False)
            title_task  - заголовок задачи
            desc_task   - подробное описание задачи
            time_create - время создания задачи
        """
        self._title_task = title_task
        self._desc_task = desc_task
        self._time_create = time_create
        self._flag_done = flag_done

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

    def getlist(self):
        """
            привести объект к списку, удобно для сохранения в репозиторий
        """
        if self._flag_done:
            flag_done = '1'
        else:
            flag_done = '0'
        strs = [flag_done, self._title_task, self._desc_task, str(self._time_create)]
        return strs

    def __str__(self):
        if self._flag_done:
            flag_done = '[x]'
        else:
            flag_done = '[ ]'
        result = "{0} : {1} - {2} - {3}".format(flag_done, self._title_task, self._desc_task, self._time_create)
        return result

    def __repr__(self):
        if self._flag_done:
            flag_done = '[x]'
        else:
            flag_done = '[ ]'
        result = "{0}  {1} - {2} - {3}".format(flag_done, self._title_task, self._desc_task, self._time_create)

        return result


class ToDoList:    
    def __init__(self, title_task, title, desc_task="", flag_done=False, time_create=datetime.now(), namefile="mylist_todo.txt"):
        self._repo = TextFileRepository(title, namefile)  # модель для сохранения списка дел на физическом уровне
        self._title = self._getTitle()        # заголовок таблицы
        self._list = self._getAll()         # список дел
        # здесь нужно проверить на наличие файла 
        self._todo = self._setInfoList(title_task, desc_task, flag_done, time_create)  # описание и служебная информация списка задач
    
    def _setInfoList(self, title_task, desc_task="", flag_done=False, time_create=datetime.now()):

        all_todo = self._getAll()
        if len(all_todo) == 0:
            result = ToDoTask(title_task, desc_task, flag_done, time_create)
            self._repo.save(result.getlist())
        else:
            result = all_todo[0]  # первая строка после заголовка это информация о самом списке задач
        return result     

    def add(self, task):
        if not isinstance(task, ToDoTask):
            raise Exception()
        self._list.append(task)
        self._repo.save(task.getlist())
    
    def getAll(self):
        return self._list[1:]

    def getTitle(self):
        """
            получить заголовок хранилища
        """
        return self._title

    def getInfoList(self):
        return self._todo

    # ----------- служебные функции
    def _getFlagDone(self, fl):
        if fl == "0":
            return False
        return True

    def _getAll(self):
        """
            
        """
        result = []
        list_all = self._repo.getAll()
        # list_all = list_all[1:]
        for el in list_all:
            elm = el.split(";")
            result.append(ToDoTask(elm[1], elm[2], self._getFlagDone(elm[0]), elm[3]))
        return result

    def _getTitle(self):

        str_title = self._repo.getTitle()
        if str_title is None:
            return None
        result = str_title.split(";")
        return result[:-1]
    # ----------- END служебные функции
    """
    чеклист в описании можно разделять пункты чеклиста с помощью табуляции \t :
    например, ToDoTask("купить", "молоко\tхлеб\tчай")
    """
# ---------------------

if __name__ == "__main__":
    t1 = ToDoTask("купить", "молоко")
    t2 = ToDoTask("прочитать Война и Мир")
    t3 = ToDoTask("заплатить за сервер 5$")
    t4 = ToDoTask("Заплатить за стоянку", "1500 рублей")

    title = ["сделано", "заголовок", "описание", "время создания"]

    list_task = ToDoList("Важный список задач", title)

    """
    list_task.add(t1)
    time.sleep(1)
    list_task.add(t2)
    time.sleep(1)
    list_task.add(t3)
    time.sleep(1)
    list_task.add(t4)
    """
    """
    #t2.done()
    #list_task.add(t2)
    """
    print(list_task.getAll())
    print(list_task.getTitle())
    print(list_task.getInfoList())