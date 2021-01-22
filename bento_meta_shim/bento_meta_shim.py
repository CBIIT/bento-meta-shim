"""Main module."""
from bento_meta_shim.n4jdb_wcm import N4jdb_wcm
from bento_meta_shim.n4jdb import N4jdb
from .user import User
from .models.commons import MDBCommons
import pprint
    

def main():

    print('using default env-based configuration....')
    local_mdb = MDBCommons()

    nodes = local_mdb.get_nodes('ICDC')
    print("nodes are {}".format(nodes))

    # test out more
    for n in nodes:
        print('n is {}'.format(n))

    n = local_mdb.get_node('KoWtYN')
    #n = local_mdb.get_node('KoWtYNasasasa')    
    if n:
        print('found: {}'.format(n))
    else:
        print('no joy')

    ps = local_mdb.get_properties()
    for p in ps:
        print('.. {} -> {}'.format(p.model, p.nanoid))
    print('=====')

    p = local_mdb.get_property('KNKAaP')
    #p = local_mdb.get_property('KJzaMwasdfadsf')
    if p:
        print('found property {}'.format(p))
    else:
        print('no joy')

    rs = local_mdb.get_relationships()
    for r in rs:
        print('++ {} -> {}'.format(r.model, r.nanoid))
    print(' - - - -')

    p2 = local_mdb.get_property('shUKsa')
    print('found property {}'.format(p2.handle))

    vss = local_mdb.get_valuesets()
    for vs in vss:
        if (vs):
            print('++ {}'.format(vs.nanoid))
    print(' - - - -')


if __name__ == '__main__':
    main()
