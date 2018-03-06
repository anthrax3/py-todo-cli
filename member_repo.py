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

    def __init__(self, namefile="example.txt"):
        self._namefile = namefile #  файла
        self._f = None            # дескриптор  файла репозитория
        self._create()


    def _create(self):
        if not os.path.exists(self._namefile):
            self._f = open(self._namefile, 'w+')
        else:
            self._f = open(self._namefile, 'a+')
        
    def save(self, member):    
        self._f.seek(2)  # переход на конец файла
        self._f.write(member)

    def getAll(self):
        self._f.seek(0) # переход на начала файла
        result = self._f.readlines()
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
    t2 = "Task number t;1;-2\n"
    export_txt = TextFileRepository()
    export_txt.save(t2)
    print(export_txt.getAll())

