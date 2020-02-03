import random

TARGET = "genetic algorithm"
INDIVIDUAL_SIZE = TARGET.__len__()
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
TOURNAMENT_SELECTION_SIZE = 40

KEYS = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Individual:
	def __init__(self):
		self._dna = []
		self._fitness = 0

		i = 0
		while i < INDIVIDUAL_SIZE:
			self._dna.append(random.choice(KEYS))
			i += 1

	def getDNA(self):
		return self._dna

	def calculateFitness(self):
		self._score = 0
		for i in range(self._dna.__len__()):
			if self._dna[i] == TARGET[i]:
				self._score += 1

		self._fitness = self._score / TARGET.__len__()
		return self._fitness

	def __str__(self):
		return self._dna.__str__()

class Population:
	def __init__(self, size):
		self._population = []

		i = 0
		while i < size:
			self._population.append(Individual())
			i += 1

	def getPopulation(self):
		return self._population

class GeneticAlgorithm:
	def selectTournamentPopulation(self, pop):
		tournament_pop = Population(0)

		i = 0
		while i < TOURNAMENT_SELECTION_SIZE:
			tournament_pop.getPopulation().append(pop.getPopulation()[random.randrange(0, POPULATION_SIZE)])
			i += 1
			tournament_pop.getPopulation().sort(key = lambda x: x.calculateFitness(), reverse = True)
		return tournament_pop

	def reproduction(self, pop):
		for i in range(pop.getPopulation().__len__()):
			self._partnerA = self.selectTournamentPopulation(pop).getPopulation()[0]	
			self._partnerB = self.selectTournamentPopulation(pop).getPopulation()[1]	

			self._child = self.crossover(self._partnerA, self._partnerB)
			self.mutate(pop)

			pop.getPopulation()[i] = self._child
		
	def crossover(self, parentA, parentB):
		self._child = Individual()
		self._midpoint = random.randrange(0, INDIVIDUAL_SIZE)

		for i in range(TARGET.__len__()):
			if i < self._midpoint:
				self._child.getDNA()[i] = parentA.getDNA()[i]
			else:
				self._child.getDNA()[i] = parentB.getDNA()[i]

		return self._child

	def mutate(self, pop):
		for x in pop.getPopulation():
			if random.random() <= MUTATION_RATE:
				x.getDNA()[random.randrange(0, INDIVIDUAL_SIZE)] = random.choice(KEYS)

	def evolve(self, pop):
		self.selectTournamentPopulation(pop)
		self.reproduction(pop)

# =============================================
def printPopulation(pop, genNumber):
	print("==========================================================")
	print("Generation #", genNumber, "| Fittest individual fitness: ", pop.getPopulation()[0].calculateFitness())
	print("Target phrase:", TARGET)
	print("==========================================================")
	i = 0
	for x in pop.getPopulation():
		print("Individual #", i, ":", ''.join(x.getDNA()), "| Fitness: ", x.calculateFitness())
		i += 1
	print()

population = Population(POPULATION_SIZE)
population.getPopulation().sort(key = lambda x: x.calculateFitness(), reverse = True)
printPopulation(population, 0)

algo = GeneticAlgorithm()

generationNumber = 1
while population.getPopulation()[0].calculateFitness() < 1:
	algo.evolve(population)
	population.getPopulation().sort(key = lambda x: x.calculateFitness(), reverse = True)
	printPopulation(population, generationNumber)
	generationNumber += 1