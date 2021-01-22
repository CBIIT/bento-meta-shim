from bento_meta.objects import Node

class MDBnode():
    __node = None
    """give proper life"""

    def __init__(self, node):
        self.__node = node
        self.kind = node.mapspec_['label']
        self.name = node.handle
        self.model = node.model
        
    def yup(self):
        return self.__node
    
    def get_nanoid(self):
        pass
        
    def __str__(self):
        return 'a {} called {}'.format(self.kind, self.name)
    
    def __repr__(self):
        return '{}:{}'.format(self.kind, self.name)