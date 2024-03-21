from neo4j import GraphDatabase


class Database:

    def __init__(self) -> None:
        self.URI = "bolt://localhost:7687"
        self.AUTH = ("neo4j", "password")
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                print(session.run("RETURN datetime()").single()[0])
