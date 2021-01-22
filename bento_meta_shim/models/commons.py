# -*- coding: utf-8 -*-
from bento_meta_shim.n4jdb import N4jdb
from bento_meta_shim.n4jdb_wcm import N4jdb_wcm
from bento_meta.model import Model, ArgError

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

    @staticmethod
    def __models_query(tx):
        list_of_models = []
        result = tx.run("MATCH (n:node) WHERE n._to IS NULL RETURN DISTINCT n.model as model")
        for record in result:
            list_of_models.append(record['model'])
        return list_of_models

    """
    In [5]: m.get_list_of_models()
    Out[5]: ['ICDC', 'CTDC']
    """
    def get_list_of_models(self):
        with self.driver.session() as session:
            models = session.read_transaction(self.__models_query)
        return models


    def get_list_of_nodes(self, model=None):  # noqa: E501
        """List nodes

        Returns a list of models
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
            print(' iterating over model: {}'.format(_m))
            _model = Model(_m, self.driver)
            _model.dget()

            _m_node_dict = _model.nodes            
            for _name, _type in _m_node_dict.items():
                #print('name {}'.format(_name))
                nodes.append(_name)
                
        return nodes

            
