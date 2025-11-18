from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import Namespace, XSD

FAMILY = Namespace("http://example.com/owl/families/")
BASE = Namespace("http://example.com/rdf/family#")

g = Graph()

# Individuals
eragon = URIRef(BASE + "eragon")
murtagh = URIRef(BASE + "murtagh")
roran = URIRef(BASE + "roran")
garrow = URIRef(BASE + "garrow")
selena = URIRef(BASE + "selena")
brom = URIRef(BASE + "brom")
morzan = URIRef(BASE + "morzan")
katrina = URIRef(BASE + "katrina")
sloan = URIRef(BASE + "sloan")
ismira = URIRef(BASE + "ismira")

# Everyone is a Person (Man or Woman)
g.add((eragon, RDF.type, FAMILY.Man))
g.add((murtagh, RDF.type, FAMILY.Man))
g.add((roran, RDF.type, FAMILY.Man))
g.add((garrow, RDF.type, FAMILY.Man))
g.add((selena, RDF.type, FAMILY.Woman))
g.add((brom, RDF.type, FAMILY.Man))
g.add((morzan, RDF.type, FAMILY.Man))
g.add((katrina, RDF.type, FAMILY.Woman))
g.add((sloan, RDF.type, FAMILY.Man))
g.add((ismira, RDF.type, FAMILY.Woman))

# Adults
g.add((murtagh, RDF.type, FAMILY.Adult))
g.add((roran, RDF.type, FAMILY.Adult))
g.add((garrow, RDF.type, FAMILY.Adult))
g.add((selena, RDF.type, FAMILY.Adult))
g.add((brom, RDF.type, FAMILY.Adult))
g.add((morzan, RDF.type, FAMILY.Adult))
g.add((katrina, RDF.type, FAMILY.Adult))
g.add((sloan, RDF.type, FAMILY.Adult))

# Dead
g.add((selena, RDF.type, FAMILY.Dead))
g.add((brom, RDF.type, FAMILY.Dead))
g.add((morzan, RDF.type, FAMILY.Dead))

# Females
g.add((selena, RDF.type, FAMILY.Female))
g.add((katrina, RDF.type, FAMILY.Female))
g.add((ismira, RDF.type, FAMILY.Female))

# Happy
g.add((roran, RDF.type, FAMILY.Happy))
g.add((katrina, RDF.type, FAMILY.Happy))
g.add((ismira, RDF.type, FAMILY.Happy))

# Young Children
g.add((ismira, RDF.type, FAMILY.YoungChild))


# Eragon's close relations:
g.add((eragon, FAMILY.hasAncestor, brom))
g.add((eragon, FAMILY.hasAncestor, selena))
g.add((eragon, FAMILY.hasParent, selena))
g.add((eragon, FAMILY.hasFather, brom))
g.add((eragon, FAMILY.loves, brom))
g.add((eragon, FAMILY.loves, roran))
g.add((eragon, FAMILY.loves, garrow))

# Murtagh's close relations:
g.add((murtagh, FAMILY.hasAncestor, morzan))
g.add((murtagh, FAMILY.hasAncestor, selena))
g.add((murtagh, FAMILY.hasParent, selena))
g.add((murtagh, FAMILY.hasFather, morzan))

# Roran's close relations:
g.add((roran, FAMILY.hasAncestor, garrow))
g.add((roran, FAMILY.hasChild, ismira))
g.add((roran, FAMILY.hasDuaghter, ismira))
g.add((roran, FAMILY.hasFather, garrow))
g.add((roran, FAMILY.hasWife, katrina))
g.add((roran, FAMILY.loves, katrina))
g.add((roran, FAMILY.loves, ismira))
g.add((roran, FAMILY.loves, garrow))
g.add((roran, FAMILY.loves, eragon))
g.add((roran, FAMILY.parentOf, ismira))

# Garrow's close relations:
g.add((garrow, FAMILY.hasChild, roran))
g.add((garrow, FAMILY.hasSon, roran))
g.add((garrow, FAMILY.parentOf, roran))
g.add((garrow, FAMILY.loves, roran))
g.add((garrow, FAMILY.loves, eragon))

# Selena's close relations:
g.add((selena, FAMILY.hasBrother, garrow))
g.add((selena, FAMILY.hasChild, eragon))
g.add((selena, FAMILY.hasSon, eragon))
g.add((selena, FAMILY.loves, brom))
g.add((selena, FAMILY.parentOf, eragon))

# Brom's close relations:
g.add((brom, FAMILY.hasChild, eragon))
g.add((brom, FAMILY.hasSon, eragon))
g.add((brom, FAMILY.loves, selena))
g.add((brom, FAMILY.loves, eragon))
g.add((brom, FAMILY.parentOf, eragon))

# Morzan's close relations:
g.add((morzan, FAMILY.hasChild, murtagh))
g.add((morzan, FAMILY.hasSon, murtagh))
g.add((morzan, FAMILY.loves, selena))
g.add((morzan, FAMILY.parentOf, murtagh))

# Katrina's close relations:
g.add((katrina, FAMILY.hasAncestor, sloan))
g.add((katrina, FAMILY.hasChild, ismira))
g.add((katrina, FAMILY.hasDaughter, ismira))
g.add((katrina, FAMILY.hasFather, sloan))
g.add((katrina, FAMILY.hasSposue, roran))
g.add((katrina, FAMILY.loves, roran))
g.add((katrina, FAMILY.loves, ismira))
g.add((katrina, FAMILY.parentOf, ismira))

# Sloan's close relations:
g.add((sloan, FAMILY.hasChild, katrina))
g.add((sloan, FAMILY.hasDaughter, katrina))
g.add((sloan, FAMILY.loves, katrina))
g.add((sloan, FAMILY.parentOf, katrina))

# Ismira's close relations:
g.add((ismira, FAMILY.hasAncestor, roran))
g.add((ismira, FAMILY.hasAncestor, katrina))
g.add((ismira, FAMILY.hasParent, katrina))
g.add((ismira, FAMILY.hasFather, roran))
g.add((ismira, FAMILY.loves, roran))
g.add((ismira, FAMILY.loves, katrina))

# Ages
g.add((eragon, FAMILY.hasAge, Literal("17", datatype=XSD.nonNegativeInteger)))
g.add((murtagh, FAMILY.hasAge, Literal("20", datatype=XSD.nonNegativeInteger)))
g.add((roran, FAMILY.hasAge, Literal("20", datatype=XSD.nonNegativeInteger)))
g.add((garrow, FAMILY.hasAge, Literal("43", datatype=XSD.nonNegativeInteger)))
g.add((selena, FAMILY.hasAge, Literal("27", datatype=XSD.nonNegativeInteger)))
g.add((brom, FAMILY.hasAge, Literal("120", datatype=XSD.nonNegativeInteger)))
g.add((morzan, FAMILY.hasAge, Literal("50", datatype=XSD.nonNegativeInteger)))
g.add((katrina, FAMILY.hasAge, Literal("20", datatype=XSD.nonNegativeInteger)))
g.add((sloan, FAMILY.hasAge, Literal("48", datatype=XSD.nonNegativeInteger)))
g.add((ismira, FAMILY.hasAge, Literal("0", datatype=XSD.nonNegativeInteger)))

# Bind each namespace to a prefix
g.bind("fm", FAMILY)
g.bind("", BASE)

# print all the data in the Turtl format
print(g.serialize(destination="the_inheritance_cycle_family.ttl"))
