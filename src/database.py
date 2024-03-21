from neo4j import GraphDatabase


class Database:

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

    def verify_connection(self):
        """Verify that we can connect to Neo4j"""

        def get_datetime(driver):
            with driver.session() as session:
                return session.run("RETURN datetime()").single()[0]

        try:
            current_datetime = get_datetime(self.driver)
            print(f"Connection verified, current datetime in Neo4j: {current_datetime}")
        except Exception as e:
            print(f"Failed to verify connection: {e}")
