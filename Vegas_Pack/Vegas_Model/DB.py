
from typing import Type
from .Database.DBconfig import Session,Base,Engine
from .Database.models import TODO


class DataBase:
    '''
    This is the main database instance.
    It imports the configurations and creates a engine for connection when the 
    app is initialized.
    '''

    def __init__(self) -> None:
        self.Engine = Engine
        self.BASE = Base
        self.BASE.metadata.create_all(self.Engine)
        self.session = Session()
    

    def create(self,data:dict,*args,**kargs):
        '''
        Creates a instance of the todo object.
        '''
        
        t = TODO(task=data['TASK'])
        self.session.add(t)
        self.session.commit()


    @property
    def query(self)->list[TODO]:
        query = self.session.query(TODO)
        return query.all()



