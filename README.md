# semantic-social-indexer

This repository will contain the code of a semantic way to index social data.


## owlready2 library:

After loading your ontology, here is what you can get:

Method | Description |
---         | --- |
individuals()    |   All individuals 
classes()    |   All classes 
properties()    |   All properties  
object_properties()    |   All object properties   
properties()    |   All data properties 
annotation_properties()    |   All annotation properties   
disjoints()    |   All pairwise disjoints (including pairwise  distinct individuals and disjoint/distinct pairs) 
disjoint_classes()  |   All pairwise disjoint classes (including disjoint pairs of classes) 
disjoint_properties()   |   All pairwise disjoint properties (including disjoint pairs of properties) 
different_individuals() |   All pairwise distinct individuals (including distinct pairs of individuals) 
rules ()    |   All SWRL rules 
variables() |   All SWRL variables 
general_axioms()    |   All general axioms 


 ## Progress


  - [ ] Ontology creation. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/33)
    - [ ] Fill and generate template.
    - [ ] The phoros project's data ontology.

  - [ ] Index generation. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/5)
    - [ ] Concept extraction.
      - Load ontology.
    - [ ] Build from hierarchy.
    - [ ] Relocation of index.

  - [ ] Packages. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/5)
    - [Ontology maker by template](). (noch nicht verfugbar)
    - [Semantic indexer](). (noch nicht verfugbar)



### Packaging:
Please follow these instructions:
    
    # Enter the target directory (make sure to have __init__.py file if it was for python scripts)
    zip -r packageName.zip



