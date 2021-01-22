from bento_meta.objects import Property

class MDBproperty():
    __prop = None
    """give proper life"""

    def __init__(self, property, key):
        self.__prop = property
        self.parent = key
        self.kind = property.mapspec_['label']
        self.name = property.handle
        self.handle = property.handle
        self.model = property.model
        self.nanoid = property.nanoid
        self.value_set = property.value_set
        self.on_type = self.__get_type_from_parent()
        
    def old(self):
        return self.__prop
    
    def __get_type_from_parent(self):
        """key is a tuple, and it describes the parents of the property
        For properties, the key is a tuple that depends on whether the 
        property belongs to a node or an edge:

        node_prop = model.props[ (node.handle, prop.handle) ]
        edge_prop = model.props[ (edge.handle, edge.src.handle, edge.dst.handle, prop.handle) ]

        so unpack the tuple...
        """
        on_type = None
        if len(self.parent) == 4:
            on_type = 'relationship'
        elif len(self.parent) == 2:
            on_type = 'node'
        return on_type
        
    def __str__(self):
        return 'a {}: {} called {}'.format(self.kind, self.nanoid, self.name)
    
    def __repr__(self):
        return '{}:{}:{}'.format(self.kind, self.nanoid, self.name)