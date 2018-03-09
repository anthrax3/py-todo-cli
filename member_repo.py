import os

class BaseRepository:
    """
     Общий интерфейс для работы с репозиторием
    """
    def save(self, member):
        pass

    def getAll(self):
        pass
    
    def findById(self, memberid):
        pass


class TextFileRepository(BaseRepository):
    """
        репозиторий в виде обычного txt файла
        Репозиторий должен знать структуру данных которую сохраняет/ищет
    """

    def __init__(self, title, namefile="example.txt"):
        self._namefile = namefile #  файла
        self._f = None            # дескриптор  файла репозитория
        self._title = title  # заголовок таблицы
        self._create()


    def _create(self):
        if not os.path.exists(self._namefile):
            self._f = open(self._namefile, 'w+')
            # записать заголовок таблицы
            self._f.write(self._ziplist(self._title))
        else:
            self._f = open(self._namefile, 'a+')
            # проверить корректность заголовка таблицы

    def _ziplist(self, tlist):
        """
        """
        result = ""
        for el in tlist:
            result = result + el+";"
        result = result + "\n"
        return result

    def save(self, member):    
        #self._f.seek(0,2)  # переход на конец файла
        if member is None:
            return False
        self._f.write(self._ziplist(member))
        return True

    def getAll(self):
        self._f.seek(0) # переход на начала файла
        result = self._f.readlines()
        return result[1:]
    
    def getTitle(self):
        self._f.seek(0) # переход на начала файла
        result = self._f.readline()
        return result
    
    def findById(self, memberid):
        pass    
    

class SqliteRepository(BaseRepository):
    pass

class ArrayRepository(BaseRepository):
    pass


if __name__ == "__main__":
    print("Run as main programm")
    t1 = "Task number one;1;-2\n"
    t2 = ["Task number one;1;-2" , "Task number two;1;-2"]
    title = ["первый","второй"]
    export_txt = TextFileRepository(title)
    export_txt.save(t2)
    print(export_txt.getAll())
