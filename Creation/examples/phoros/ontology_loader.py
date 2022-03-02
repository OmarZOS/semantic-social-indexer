

from owlready2 import *
from constants import PATH_TO_ONTOLOGY

TARGET_ONTOLOGY = get_ontology(PATH_TO_ONTOLOGY).load(reload=True)






# parse classes using generator..
# for c in onto.classes(): 
#     print(c.name)

# print(onto.sister.is_a)

