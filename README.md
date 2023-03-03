# py4owl

A Python packages for OWL ontology development.


**py4owl** is a Python package for ontology development. It is based on the OWL 2 Web Ontology Language and the RDFLib library.

It is highly inspired by [**owlready2**](http://github.com/pwin/owlready2) and [**EMMOntoPy**](https://github.com/emmo-repo/EMMOntoPy)
and tries to overcome some of their architectural shortcomings.

## Features

  * easy to use OWL based ontology development
  * strong modularisation
    - separation of RDF import, export and ontology development
    - standard interface to common reasoners (like FaCT++, HermiT, Pellet, ELK, RacerPro, etc.)
    - standard interface to common triple stores (e.g. Virtuoso) and SPARQL endpoints
  * OSM - object semantic mapping (analogue to ORM, like Django or SQLAlchemy)
  * import and export of common RDF formats (RDF/XML, Turtle, N3, NTriples, NQuads, TriG, RDFa, JSON-LD)
  * tested for speed and memory usage

## Documentation

The Documentation can be found here: [openlab.gitlab.io/py4owl](openlab.gitlab.io/py4owl) or [py4owl.gitlab.io](py4owl.gitlab.io/)


## Credits

This package was created with Cookiecutter* and the `opensource/templates/cookiecutter-pypackage`* project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter )
[opensource/templates/cookiecutter-pypackage](https://gitlab.com/opensourcelab/software-dev/cookiecutter-pypackage) 
