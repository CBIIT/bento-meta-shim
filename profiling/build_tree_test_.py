# pip install line-profiler
# kernprof -l build_tree_test.py
# python -m line_profiler tree.py.lprof
import os
from neo4j import GraphDatabase
import bento_meta
from bento_meta.object_map import ObjectMap
from bento_meta.entity import *
from bento_meta.objects import *
from bento_meta.model import Model, ArgError
from bento_meta.objects import Node, Property, Edge, Term, ValueSet, Concept, Origin
import pprint

def get_neo4j_db():
    uri = os.environ.get("NEO4J_MDB_URI")
    user = os.environ.get("NEO4J_MDB_USER")
    password = os.environ.get("NEO4J_MDB_PASS")
    ndbr = GraphDatabase.driver(uri, auth=(user, password))
    return ndbr

@profile
def build_tree():
    drv = get_neo4j_db()
    model_list = ['CTDC', 'ICDC', 'Bento']
    for m in model_list:
        _model = Model(m, drv)
        _model.dget()
        print('model: {}'.format(_model.handle))
        for _node in _model.nodes.values():
            print('  node:{} {}'.format(_node.nanoid, _node.handle))
            for tuple_key in _node.props:
                _prop = _node.props[tuple_key]
                print('    prop:{} {}'.format(_prop.nanoid, _prop.handle))
                if (_prop.value_domain) and _prop.value_domain == 'value_set':
                    #_prop.dget()
                    if (_prop.value_set) and _prop.value_set is not None:
                        # vs
                        _vset = _prop.value_set
                        print('      vset:{} {}'.format(_vset.nanoid, _vset.handle))
                        for term_key in _vset.terms:
                            _term = _vset.terms[term_key]
                            print('        term:{} {}'.format(_term.nanoid, _term.value))

def main():
    print('Start')
    build_tree()
    print('Done')

if __name__ == '__main__':
    main()

main()
