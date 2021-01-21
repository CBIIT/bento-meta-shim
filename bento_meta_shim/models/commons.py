# -*- coding: utf-8 -*-
from bento_meta_shim.n4jdb import N4jdb
from bento_meta_shim.n4jdb_wcm import N4jdb_wcm

class Commons:
    """description"""

    def __init__(self, driver=None):
        """Commons

        :param driver:  the driver to connect to mdb neo4j database
        :type driver: a neo4j database driver
        """
        # style N4jdb
        if driver is None:
            n4jdb = N4jdb()
            driver = n4jdb.driver
        
        # style N4jdb_wcm
        #if driver is None:
        #    with N4jdb_wcm() as n:
        #        driver = n
        
        self.driver = driver

    def get_list_of_all_models(self, model=None):  # noqa: E501
        """List all models

        Returns a collection of models
        :rtype: Model
        """

    @staticmethod
    def _get_models_query(tx):
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
            models = session.read_transaction(self._get_models_query)
        return models




