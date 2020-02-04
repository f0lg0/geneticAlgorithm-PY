import random
import time
from displayBanner import displayBanner, choice


TARGET = "genetic algorithm"
INDIVIDUAL_SIZE = len(TARGET)
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
TOURNAMENT_SELECTION_SIZE = 40

KEYS = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Individual:
	def __init__(self):
		self._dna = random.choices(KEYS, k=INDIVIDUAL_SIZE)
		self._fitness = -1
		self._score = -1

	def getDNA(self):
		self._fitness = -1
		self._score = -1
		return self._dna
	
	@property
	def fitness(self):
		if self._score == -1:
			self._score = 0
			for own_letter, target_letter in zip(self._dna, TARGET):
				if own_letter == target_letter:
					self._score += 1

			self._fitness = self._score / len(TARGET)
		return self._fitness

	def __str__(self):
		return "".join(self._dna)

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
			
		tournament_pop.getPopulation().sort(key = lambda x: x.fitness, reverse = True)
		return tournament_pop

	def reproduction(self, pop):
		for i in range(len(pop.getPopulation())):
			partnerA = self.selectTournamentPopulation(pop).getPopulation()[0]	
			partnerB = self.selectTournamentPopulation(pop).getPopulation()[1]	

			child = self.crossover(partnerA, partnerB)
			

			pop.getPopulation()[i] = child
		self.mutate(pop)
		
	def crossover(self, parentA, parentB):
		child = Individual()
		midpoint = random.randrange(0, INDIVIDUAL_SIZE)

		for i in range(len(TARGET)):
			if i < midpoint:
				child.getDNA()[i] = parentA.getDNA()[i]
			else:
				child.getDNA()[i] = parentB.getDNA()[i]

		return child

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
	print("Generation #", genNumber, "| Fittest individual fitness: ", pop.getPopulation()[0].fitness)
	print("Target phrase:", TARGET)
	print("==========================================================")
	for i, x in enumerate(pop.getPopulation()):
		print("Individual #", i, ":", ''.join(x.getDNA()), "| Fitness: ", x.fitness)
	print()

def main():
	displayBanner()
	time.sleep(2)
	choice()

	population = Population(POPULATION_SIZE)
	population.getPopulation().sort(key = lambda x: x.fitness, reverse = True)
	printPopulation(population, 0)

	algo = GeneticAlgorithm()

	generationNumber = 1
	while population.getPopulation()[0].fitness < 1:
		algo.evolve(population)
		population.getPopulation().sort(key = lambda x: x.fitness, reverse = True)
		printPopulation(population, generationNumber)
		generationNumber += 1

	print("Simulation terminated, target reached")

if __name__ == "__main__":
	main()
