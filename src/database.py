from neo4j import GraphDatabase


class Neo4jConnection:
    def __init__(
        self,
        uri: str = "bolt://localhost:7687",
        username: str = "neo4j",
        password: str = "password",
    ):
        self.uri = uri
        self.username = username
        self.password = password
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def query(self, query, parameters=None, db=None):
        with self.driver.session(database=db) as session:
            result = session.write_transaction(_execute_query, query, parameters)
            return result


def _execute_query(tx, query, parameters):
    result = tx.run(query, parameters)
    try:
        return [record for record in result]
    except Exception as e:
        print("Query failed:", e)
        return None
