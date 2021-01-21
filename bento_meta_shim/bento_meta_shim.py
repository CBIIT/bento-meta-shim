"""Main module."""
from bento_meta_shim.n4jdb_wcm import N4jdb_wcm
from bento_meta_shim.n4jdb import N4jdb
from .user import User
from .models.commons import Commons

def stub_user():
    umlaut = User()
    response = umlaut.grunt()
    print('{}'.format(response))

def stub_n():
    n = N4jdb()
    n.print_greeting('bah')

def stub_models():
    c = Commons()
    m = c.get_list_of_models()
    print('{}'.format(m))

#def stub_unmodels():
#    c = Uncommons()
#    m = c.get_list_of_models()
#    print('{}'.format(m))

def stub_models_direct():
    n = N4jdb()
    c = Commons(n.driver)
    m = c.get_list_of_models()
    print('{}'.format(m))

def stub_unmodels():
    with N4jdb_wcm() as n:
        c = Commons(n)
        m = c.get_list_of_models()
        print('{}'.format(m))


def main():
    print('calling user')
    stub_user()

    print('calling N4jdb directly')
    stub_n()
    
    print('trying to call via commons()')
    stub_models()

    print('trying to call via commons() by passing')
    stub_models_direct()

    print('trying to call via uncommons() by passing wcm')
    stub_unmodels()


if __name__ == '__main__':
    main()
