

from sqlalchemy import Column, Integer, String,DATETIME
from sqlalchemy.sql.operators import is_distinct_from
from sqlalchemy.sql.sqltypes import DateTime
import datetime
from .DBconfig import Base

class TODO(Base):
    '''
    Instance of a To-Do.

    '''
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    
    task = Column(String)
    date = Column(DATETIME)

    def __init__(self,task) -> None:
        super().__init__()
        
        self.task=task
        self.date = datetime.datetime.now()
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.task, self.date)
