from bento_meta_shim.n4jdb import N4jdb
from bento_meta_shim.models.commons import Commons

def main():

    metadb = N4jdb()
    commons = Commons(metadb.driver)    # ick

    modellist = commons.get_list_of_models()
    print(modellist)

    

if __name__ == '__main__':
    main()
