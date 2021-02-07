class ListQueryError(Exception):
    def __init__(self):
        super().__init__('Serializer\'s argument must be the BaseQuery')