from bento_meta.objects import ValueSet
from bento_meta_shim.models.mdbterm import MDBterm

class MDBvalueset():
    __vs = None
    """give proper life"""

    def __init__(self, vs):
        self.__vs = vs
        self.parent = None
        self.kind = vs.mapspec_['label']
        self.name = vs.handle
        self.handle = vs.handle
        self.nanoid = vs.nanoid
        self.terms = self.__convert_terms()
        self.size = len(self.terms)
        
    def old(self):
        return self.__vs

    def __convert_terms(self):
        mdbterms = []
        for term_key in self.__vs.terms:
            _term = self.__vs.terms[term_key]
            #print(' lookin at {}'.format(_term))
            mdbterms.append(MDBterm(_term))
        return mdbterms 
        
    def __str__(self):
        return 'a {}: {} called {}'.format(self.kind, self.nanoid, self.name)
    
    def __repr__(self):
        return '{}:{}:{}'.format(self.kind, self.nanoid, self.name)