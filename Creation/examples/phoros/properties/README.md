You should write your property scripts inside *Creation/properties*, you can multiple-inherit from these classes:

- FunctionalProperty
- InverseFunctionalProperty
- TransitiveProperty
- SymmetricProperty
- AsymmetricProperty
- ReflexiveProperty
- IrreflexiveProperty

###### Specifying [domain,range]
Example-1:
    
    with onto:
        class some-property(Bacterium >> Shape, FunctionalProperty):
             pass

Example-2:
    
    with onto:
        class some-property(ObjectProperty, FunctionalProperty):
            domain = [some_Object]
            range  = [some_Property]

P.S: DataProperty (bool, int, decimal...) or ObjectProperty, is automatically deduced from the range.
