# He Tan, 2024-10
#
#
from SPARQLWrapper import SPARQLWrapper, JSON


# Connect to the DBpedia SPARQL endpoint.
sparql = SPARQLWrapper("https://yago-knowledge.org/sparql/query")
sparql.setReturnFormat(JSON)

# Select the query. [1-4]
query = 3


def prequery(q):
    sparql.setQuery(q)


prefix = """PREFIX schema: <http://schema.org/>
            PREFIX yago: <http://yago-knowledge.org/resource/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            
            """

query_1_who_influenced_the_beatles = prefix + """SELECT DISTINCT ?artist WHERE {
                                                ?artist ^schema:influencedBy yago:The_Beatles .
                                                ?artist a ?class .
                                                ?class rdfs:subClassOf+ yago:Creator .
                                            } 
                                            LIMIT 10"""

query_2_influenced_by_the_beatles = prefix + """SELECT DISTINCT ?artist ?nationality WHERE {
                                                ?artist (schema:influencedBy)+ yago:The_Beatles .
                                                ?artist a ?class .
                                                ?class rdfs:subClassOf+ yago:Creator .
                                                OPTIONAL { ?artist schema:nationality ?nationality . }
                                                FILTER (?artist != yago:The_Beatles)
                                            } 
                                            LIMIT 10"""

query_3_movies_1960_1970 = prefix + """SELECT DISTINCT ?movie ?year ?director  WHERE {
                                                yago:The_Beatles schema:award/^schema:award ?director .
                                                ?movie schema:director ?director ;
                                                            schema:dateCreated ?date
                                                BIND (year(?date) AS ?year)
 											    FILTER (?year >= 1960 && ?year < 1970)
                                            } 
                                            LIMIT 10"""

query_4_the_beatles_family_members = prefix + """SELECT ?person WHERE {
                                                { yago:The_Beatles ^schema:memberOf/schema:children ?person }
                                                UNION
                                                { yago:The_Beatles ^schema:memberOf/schema:spouse ?person }
                                                UNION
                                                {?person schema:memberOf yago:The_Beatles }
                                            } 
                                            LIMIT 10"""

match query:
    case 1:
        prequery(query_1_who_influenced_the_beatles)
        print("Query 1: Everyone who influenced The Beatles.")
    case 2:
        prequery(query_2_influenced_by_the_beatles)
        print("Query 2: Everyone influenced by The Beatles. (This one might take a while)")
    case 3:
        prequery(query_3_movies_1960_1970)
        print("Query 3: Movies (from 1960 to 1970) directed by people who have won the same award as The Beatles.")
    case _:
        prequery(query_4_the_beatles_family_members)
        print("Query 4: Members of The Beatles and their family members.")

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        for var in ret["head"]["vars"]:
            print(f"{var}: ", r[var]["value"].replace(
                "http://yago-knowledge.org/resource/", "").replace("_", " "))
        print("")

except Exception as e:
    print(e)
