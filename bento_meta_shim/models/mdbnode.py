from bento_meta.objects import Node
from bento_meta_shim.models.mdbproperty import MDBproperty

class MDBnode():
    __node = None
    """give proper life"""

    def __init__(self, node):
        self.__node = node
        self.kind = node.mapspec_['label']
        self.name = node.handle
        self.handle = node.handle
        self.model = node.model
        self.nanoid = node.nanoid
        self.props = self.__convert_props()

        
    def old(self):
        return self.__node

    def __convert_props(self):
        mdbprops = []
        for tuple_key in self.__node.props:
            _prop = self.__node.props[tuple_key]
            mdbprops.append(MDBproperty(property=_prop, key=tuple_key))
        return mdbprops
        
    def __str__(self):
        return 'a {}: {} called {}'.format(self.kind, self.nanoid, self.name)
    
    def __repr__(self):
        return '{}:{}:{}'.format(self.kind, self.nanoid, self.name)