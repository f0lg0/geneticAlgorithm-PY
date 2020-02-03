Introduction
------------
This is an application of a genetic algorithm to the *Infinite monkey theorem*.

Open this [link](https://en.wikipedia.org/wiki/Infinite_monkey_theorem) for more information about the theorem.


## Concepts:
* Fitness 
* Selection
* Reproduction
* Crossover
* Mutation

I recommend you to check "The Nature of Code" chapter 9 as I am not describing these concepts in this file.


The Algorithm
=============

Individual class
----------------
This class creates a list populated with random keys coming from a defined range of characters and calculates the fitness of each list. A list is called an Individual.

Population
----------------
This class creates a list containing a defined number (POPULATION_SIZE) of Individual objects.

The Algorithm itself
--------------------
`def selectTournamentPopulation(self, pop):`

This function consists of making a tournament (a race) between Individuals based on their fitness. The winners will be chosen for reproduction.


`def reproduction(self, pop):`
This function generates new Individuals from 2 parents


`def crossover(self, parentA, parentB):`
This function is related to reproduction. It is indeed a crossover of genes between 2 parents to generate a child with genetic material coming from the parents. 


`def mutate(self, pop):`
This function changes randomly the genetic material of an Individual

`def evolve(self, pop):`
It evolves the population calling the previous functions

## Info
Written by: **Leonardo Folgoni**



