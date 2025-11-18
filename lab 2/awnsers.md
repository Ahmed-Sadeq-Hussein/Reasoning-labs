1. An ontology describes the concepts, and relationships between them, that can formally exist for some model. It is explicit, meaning the descriptions are clearly defined and unambiguous.

2.

* OWl 2 DL is an extension of SROIQ, it is decidable and it has several quality resoners that cover OW2 DL language. It is very expressive too.
Complex and reliable for ontologies

* OWL 2 FULL is based on the RDF compatible semantics, however unlike DL it is undecidable and there are no reasoners for WOL2 FULL.
Nax freedom and good for theoretical testing and integratin messy RDF data.

* OWL 2 EL is based on a description logic family called EL++ . It's optimized for efficient classification of large ontology's with a lot of classes and or properties.

* OWL 2 QL is a language optimized for ontology based query awnsering , that is to say that the Ontology schema is used to rewrite and enrich queries over a large instance data stored in a data base in that ontology.

* OWL 2 RL is aimed at applications that require scalable reasoning without sacrifising too much expressiveness

4.  

1)

* HappyPerson
DL: Person ⊓ ∀hasChild.happy ⊓ ∃hasChild.happy                                    ∃hasChild.happy ⊓ ∀hasChild.happy
Natural: a happy person is a person and has only happy children                    A HappyPerson is anything that has some childen and all those children are happy.

* JohnsChildren
DL: hasparent.john
Natural: johnsChildren have john as their parent                                   JohnsChildren are anything that has John as their parent.

* NarcisticPerson
DL: Loves.Self
Natural: Narsistic person love themself                                             NarcisticPerson loves themselves.

* Orphan
DL : ¬∀hasParent                                                                    ∀hasParent.Dead
Natural : anyone that had them as their child is dead                               An Orphan is anything of which all its parents are dead (or anything that doesn't have any parents in the first place).

2)

* hasSpouse
Natural langauge : person that has a spouse whom has no other spouse, is

HasSpouse is a symmetric object property. This means that if the property is applied in one direction (from individual a to individual b, for example), then it is also applied in the opposite direction (from individual b to individual a).
It is also disjoint with object property hasParent. This means that an individual cannot have another individual as spouse and parent simultaneously.

HasWife is a subproperty of hasSpouse. This means that if some individual has a wife, then that individual also has a spouse.
The domain of hasWife is Man, and the Range is Woman. This means that if indivudual a has individual b as wife, a must be a man and b must be a woman.

* hasWife
Natural langauge :a person that has a spouse who is female

3)

* Teenager
A teenager is anyone between the ages 13 and 19

A Teenager is anything that has some age between 13 and 19.

* hasAge
hasage queries

HasAge is a datatype property.
Its Domain is Person, and its Range is a non-negative integer. This means that if individual a has age x, a must be a person and x must be a non-negative integer.

4)

* John
John is a father and has exactly 5 children, 3 of which are parents and john can not have more than 4 children that are parents and less than 2 children that are parents.
He has a wife who is Mary.
He is 51 years of age.
And he is diffrent from the individual Bill. Ergo he is not Bill

5)

* Grandfather
Superclasses (6):
Father
Human
Man
Parent
Person
owl:Thing

This means that if something is a Grandfather, then it must also be a Father, a Human, a Man, a Parent, a Person and owl:Thing. owl:Thing is the top-most class in the class hierarchy.

Subclasses (1):
owl:Nothing

This means that there are no subclasses of Grandparent in this ontology. There exists no single class, from which we can infer that an individual in that class must also be a Grandfather.

Instances (0):

This means that there are no Grandparents in this ontology.

* ChildlessPerson
Superclasses (3):
Human
Person
owl:Thing

This means that if something is a ChildlessPerson, then it must also be a Human, a Person and owl:Thing.

Subclasses (1):
owl:Nothing

This means that there are no subclasses of ChildlessPerson in this ontology. There exists no single class, from which we can infer that an individual in that class must also be a ChildlessPerson.

Instances (1):
Jack

This means that there exists one individual that is a ChildlessPerson. Jack is a Childless Person.

* Person and (hasChild min 2 Person)
Superclasses (4):
Human
Parent
Person
owl:Thing

This means that if an individual is a Person and has 2 or more children that are also Persons, then that individual must also be a Human, a Person, a Parent and owl:Thing.

Subclasses (1):
owl:Nothing

This means that This means that there are no subclasses of Person that has 2 or more person children in this ontology. There exists no single class, from which we can infer that an individual in that class must also be a Person that has 2 or more person children.

6)

The reasoner inferred that the object property hasSpouse is the inverse of hasSpouse. This is true, since hasSpouse is symmetric.

The reasoner also inferred that the individual Mary hasSpouse the individual John.

Known information: John hasWife Mary
Inferred information: John hasSpouse Mary => Mary hasSpouse John.

5.

1)

Entities:
{University, Faculty, Student, Course, Program, Prerequisite, Teacher, teachesCourse, ProgramDirector, directsProgram, CourseExaminer, examinesCourse}

* Things is the foundation for anything concrete (Not including programs/courses ) . subclass (people, equipment, universities)
* People can be seperated into 4 distinct sections. Students, faculty, program directors and guests .
* Universities Employ faculty exlusivly . Guests can attend/teach in any university .
* To be a student to a univesity you have to be in a course or in a program. Also a student has to have prerequisite courses to take a course or program and must not have taken that same course/program before as a prerequisite.
*

Competency Questions:

1. Which universities offer 3 or more programs?
2. Which universities offer some program with some course in mathematics?
3. Which programs are 5 years long?
4. Which courses are worth 7.5 hp?
5. Which courses are exclusively in Swedish?
6. Which students are part of a given university?
7. Which countries have 2 or more universities?
8. In what country is a given university located?
9. Which persons are both teachers and course examiners?
10. Which courses have no prerequisites?

Key Terms from CQ:
{offersProgram, includesCourse, isYearsLong, isWorthPoints, isInLanguage, Language, locatedInCountry, Country, hasUniversity, Person}

Classes:
{University, Faculty, Student, Course, Program, Prerequisite, Teacher, ProgramDirector, CourseExaminer, Language, Country, Person}

6

 ⨅  ¬ ⊔ ∃ ∀ ⊑ ≡
