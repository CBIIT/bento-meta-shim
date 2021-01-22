# -*- coding: utf-8 -*-
from bento_meta_shim.models.mdbvalueset import MDBvalueset
from bento_meta_shim.n4jdb import N4jdb
from bento_meta_shim.n4jdb_wcm import N4jdb_wcm
from bento_meta_shim.models.mdbnode import MDBnode
from bento_meta_shim.models.mdbproperty import MDBproperty
from bento_meta_shim.models.mdbrelationship import MDBrelationship
from bento_meta.model import Model
from bento_meta.objects import Property


class MDBCommons:
    """description"""

    def __init__(self, driver=None):
        """Commons

        :param driver:  the driver to connect to mdb neo4j database
        :type driver: a neo4j database driver
        """
        # style N4jdb
        #if driver is None:
        #    n4jdb = N4jdb()
        #    driver = n4jdb.driver
        
        # style N4jdb_wcm
        if driver is None:
            with N4jdb_wcm() as n:
                driver = n
        
        self.driver = driver

    def get_models(self, model=None):  # noqa: E501
        """List all models

        Returns a list of models
        :rtype: list
        """
        models = self.__get_list_of_models()
        return models

    def clean_model_names(self, models):
        """some models e.g. need to be removed... as they are not production data"""
        test = 'test'
        if test in models:
            models.remove(test)
        return models

    @staticmethod
    def __models_query(tx):
        list_of_models = []
        result = tx.run("MATCH (n:node) WHERE n._to IS NULL RETURN DISTINCT n.model as model")
        for record in result:
            list_of_models.append(record['model'])
        return list_of_models

    def get_list_of_models(self):
        """
        In [5]: m.get_list_of_models()
        Out[5]: ['ICDC', 'CTDC']
        """
        with self.driver.session() as session:
            models = session.read_transaction(self.__models_query)

        # remove any smoke test model data
        self.clean_model_names(models)
        return models

    def get_nodes(self, model=None):  # noqa: E501
        """get nodes, by model if provided

        Returns a list of mdb-style nodes
        :rtype: list
        """
        nodes = []

        __models = self.get_list_of_models()
        
        if model:
            if model not in __models:
                """todo: better error handling for non-existing model"""
                __models = []
            __models = [model]

        for _m in __models:
            _model = Model(_m, self.driver)
            _model.dget()
            
            for _node in _model.nodes.values():
                # convert to mdb-style node
                nodes.append(MDBnode(_node))
                
        return nodes

    def get_node(self, nanoid):  # noqa: E501
        """get node, by nanoid 
        Returns a mdb-style node
        :rtype: mdbnode
        """
        node = None

        __models = self.get_list_of_models()

        for _m in __models:
            _model = Model(_m, self.driver)
            _model.dget()
            
            for _n in _model.nodes.values():
                if (_n.nanoid) and _n.nanoid == nanoid:
                    # convert to mdb-style node
                    node = MDBnode(_n)
                    break
            else:
                continue
            break
                
        return node
            

    def get_properties(self, model=None):  # noqa: E501
        """get nodes, by model if provided

        Returns a list of mdb-style nodes
        :rtype: list
        """
        properties = []

        __models = self.get_list_of_models()
        
        if model:
            if model not in __models:
                """todo: better error handling for non-existing model"""
                __models = []
            __models = [model]

        for _m in __models:
            _model = Model(_m, self.driver)
            _model.dget()
            
            for tuple_key in _model.props:
                _prop = _model.props[tuple_key]
                properties.append(MDBproperty(property=_prop, key=tuple_key))
                
        return properties

    def get_property(self, nanoid):  # noqa: E501
        """get property, by nanoid 
        Returns a mdb-style property
        :rtype: mdbproperty
        """
        property = None

        __models = self.get_list_of_models()

        for _m in __models:
            _model = Model(_m, self.driver)
            _model.dget()
            
            for tuple_key in _model.props:
                _prop = _model.props[tuple_key]
                if (_prop.nanoid) and _prop.nanoid == nanoid:
                    # convert to mdb-style property
                    property = MDBproperty(property=_prop, key=tuple_key)
                    break
            else:
                continue
            break
                
        return property

    def get_relationships(self, model=None):  # noqa: E501
        """get relationships, by model if provided

        Returns a list of mdb-style relationships
        :rtype: list
        """
        relationships = []

        __models = self.get_list_of_models()
        
        if model:
            if model not in __models:
                """todo: better error handling for non-existing model"""
                __models = []
            __models = [model]

        for _m in __models:
            _model = Model(_m, self.driver)
            _model.dget()

            for tuple_key in _model.edges:
                _rel = _model.edges[tuple_key]
                relationships.append(MDBrelationship(relationship=_rel, key=tuple_key))
                
        return relationships

    def get_relationship(self, nanoid):  # noqa: E501
        """get relationship, by nanoid 
        Returns a mdb-style relationship
        :rtype: mdbrelationship
        """
        relationship = None

        __models = self.get_list_of_models()

        for _m in __models:
            _model = Model(_m, self.driver)
            _model.dget()
            
            for tuple_key in _model.edges:
                _rel = _model.edges[tuple_key]
                if (_rel.nanoid) and _rel.nanoid == nanoid:
                    # convert to mdb-style relationship
                    relationship = MDBrelationship(relationship=_rel, key=tuple_key)
                    break
            else:
                continue
            break
                
        return relationship        


    def get_valuesets(self, model=None):  # noqa: E501
        """get valuesets, by model if provided

        Returns a list of mdb-style valuesets
        :rtype: list of mdbvaluesets
        """
        valuesets = []

        __models = self.get_list_of_models()
        
        if model:
            if model not in __models:
                """todo: better error handling for non-existing model"""
                __models = []
            __models = [model]

        for _m in __models:
            _model = Model(_m, self.driver)
            _model.dget()
            
            # county = 0
            for tuple_key in _model.props:
                _prop = _model.props[tuple_key]
                
                #_prop.dget()
                if (_prop.value_domain) and _prop.value_domain == 'value_set':
                    #county += 1
                    #print('{} {}'.format(county, _prop.handle))
                    _prop.dget()
                    #print(' .')

                    if (_prop.value_set) and _prop.value_set is not None:
                        #print(' {} '.format(_prop.value_set.nanoid))
                        valuesets.append(MDBvalueset(_prop.value_set))
                    #print('   .')
                else:
                    #print('skip')
                    pass
                
        return valuesets