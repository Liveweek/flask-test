from typing import List


from .base.exceptions import ListQueryError


class ListSerializer:
    def __init__(self, query_set: List):
        if type(query_set) is not list:
            raise ListQueryError
        
        self.query_set = query_set
        
        
    @property
    def data(self) -> list:
        return [item.serialize for item in self.query_set]
        
        

        
        
    