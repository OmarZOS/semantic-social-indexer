
from classes.static.social_network.social_network import social_network
from classes.static.links.link import link
from classes.static.nodes.node import node
from ontology_loader import TARGET_ONTOLOGY
from owlready2 import *


with TARGET_ONTOLOGY:
    class part_of(Or([node,link])>>social_network,FunctionalProperty):
        pass

