from bento_meta.objects import Edge

class MDBrelationship():
    __relationship = None
    """give proper life"""

    def __init__(self, relationship, key):
        self.__relationship = relationship
        self.parent = key
        self.kind = relationship.mapspec_['label']
        self.name = relationship.handle
        self.handle = relationship.handle
        self.model = relationship.model
        self.nanoid = relationship.nanoid
        self._from_node = None
        self._to_node = None
        
    def old(self):
        return self.__relationship
        
    def __str__(self):
        return 'a {}: {} called {}'.format(self.kind, self.nanoid, self.name)
    
    def __repr__(self):
        return '{}:{}:{}'.format(self.kind, self.nanoid, self.name)