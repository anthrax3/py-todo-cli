class BaseRepository:
    """
     Общий интерфейс для работы с репозиторием
    """
    def save(member):
        pass

    def getAll():
        pass
    
    def findById(memberid):
        pass


class TextFileRepository(BaseRepository):
    def save(member):
        pass

    def getAll():
        pass
    
    def findById(memberid):
        pass

class SqliteRepository(BaseRepository):
    pass

class ArrayRepository(BaseRepository):
    pass