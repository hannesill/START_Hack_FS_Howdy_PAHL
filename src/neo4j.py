from neo4j import GraphDatabase


def create_startup(tx, startup_name, description):
    query = (
        "CREATE (s:Startup {name: $startup_name, description: $description}) "
        "RETURN s"
    )
    return tx.run(query, startup_name=startup_name, description=description)


def create_name_and_link_to_startup(tx, startup_name, name):
    query = (
        "MATCH (s:Startup {name: $startup_name}) "
        "CREATE (n:Name {name: $name}) "
        "CREATE (s)-[:HAS_NAME]->(n)"
    )
    tx.run(query, startup_name=startup_name, name=name)


class Database:

    def __init__(self) -> None:
        self.URI = "bolt://localhost:7687"
        self.AUTH = ("neo4j", "password")
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            with driver.session() as session:
                # Create the startup node
                startup_name = "OurStartup"  # Example startup name
                description = "We offer innovative solutions to common problems."
                session.write_transaction(create_startup, startup_name, description)

                # Now link the startup to a name node
                name = "Innovative Tech Solutions"  # Example name to link
                session.write_transaction(
                    create_name_and_link_to_startup, startup_name, name
                )
