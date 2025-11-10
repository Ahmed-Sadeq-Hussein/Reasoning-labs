1. It is the definition used for defining ontology in AI terms by Tom Gruber 

2. 
* OWl 2 DL is an extension of SROIQ, it is decidable and it has several quality resoners that cover OW2 DL language. It is very expressive too.
Complex and reliable for ontologies

* OWL 2 FULL is based on the RDF compatible semantics, however unlike DL it is undecidable and there are no reasoners for WOL2 FULL.
Nax freedom and good for theoretical testing and integratin messy RDF data.

* OWL 2 EL is based on a description logic family called EL++ . It's optimized for efficient classification of large ontology's .

* OWL 2 QL is a language optimized for ontology based query awnsering , that is to say that the Ontology schema is used to rewrite and enrich queries over a large instance data sored in a data base in that ontology.

4.  
1) 
* HappyPerson 
DL : Person ⊓  ∀hasChild.happy ⊓ ∃hasChild.happy
Natural : a happy person is a person and has only happy children 
* JohnsChildren
DL : hasparent.john
Natural : johns children have john as their parent
* NarcisticPerson
DL : Loves.Self
Natural :Narsistic person love themself
* Orphan
DL : ¬∀hasParent
Natural : anyone that had them as their child is dead 
2) 
* hasSpouse 
Natural langauge : person that has a spouse whom has no other spouse, is 
* hasWife
Natural langauge :a person that has a spouse who is female 
3) 
* Teenager 
A teenager is anyone between the ages 13 and 19 
* hasAge
hasage queries
4) 
* John 
John is a father and has exactly 5 children, 3 of which are parents and john can not have more than 4 children that are parents and less than 2 children that are parents .
5) 
1. 
{universities, faculties, students, courses, programs, prerequisites,
etc.}
* Things is the foundation for anything concrete (Not including programs/courses ) . subclass (people, equipment, universities)
* People can be seperated into 4 distinct sections. Students, faculty, program directors and guests . 
* Universities Employ faculty exlusivly . Guests can attend/teach in any university . 
* To be a student to a univesity you have to be in a course or in a program. Also a student has to have prerequisite courses to take a course or program and must not have taken that same course/program before as a prerequisite.
* 

 ⨅  ¬ ⊔ ∃ ∀ ⊑ ≡