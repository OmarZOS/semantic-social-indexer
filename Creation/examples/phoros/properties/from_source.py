from classes.static.links.link import link
from classes.static.nodes.node import node
from ontology_loader import TARGET_ONTOLOGY
from owlready2 import *


with TARGET_ONTOLOGY:
    class from_source(link>>node,FunctionalProperty):
        pass

