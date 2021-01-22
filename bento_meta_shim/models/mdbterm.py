from bento_meta.objects import Term

class MDBterm():
    __term = None
    """give proper life"""

    def __init__(self, term):
        self.__term = term
        self.kind = term.mapspec_['label']
        self.name = term.value
        self.handle = term.value
        self.nanoid = term.nanoid
        
    def old(self):
        return self.__term
        
    def __str__(self):
        return 'a {}: {} called {}'.format(self.kind, self.nanoid, self.name)
    
    def __repr__(self):
        return '{}:{}:{}'.format(self.kind, self.nanoid, self.name)