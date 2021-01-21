import os
from neo4j import GraphDatabase

class N4jdb:

    def __init__(self, uri=None, user=None, password=None):
        if uri is None:
            # uri = 'bolt://localhost:7687'
            uri = os.environ.get("NEO4J_MDB_URI")
        self.uri = uri

        if user is None:
            # user = 'neo4j'
            user = os.environ.get("NEO4J_MDB_USER")
        self.user = user

        if password is None:
            password = os.environ.get("NEO4J_MDB_PASS")
        self.password = password

        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    greeter = N4jdb("bolt://localhost:7687", "neo4j", "test")
    greeter.print_greeting("hello, world")
    greeter.close()
