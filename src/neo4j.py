from neo4j import GraphDatabase

class Database:
    
    def __init__(self) -> None:
        self.URI = "neo4j://localhost"
        self.AUTH = ("neo4j", "password")
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            print(driver.verify_connectivity())