"""Main module."""
from bento_meta_shim.n4jdb_wcm import N4jdb_wcm
from bento_meta_shim.n4jdb import N4jdb
from .user import User
from .models.commons import MDBCommons
import pprint
    

def main():

    print('using default configuration....')
    local_mdb = MDBCommons()

    nodes = local_mdb.get_list_of_nodes()
    print("nodes are {}".format(nodes))

if __name__ == '__main__':
    main()
