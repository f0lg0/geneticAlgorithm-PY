import random
import time
from displayBanner import displayBanner, choice


TARGET = "genetic algorithm"
INDIVIDUAL_SIZE = len(TARGET)
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
TOURNAMENT_SELECTION_SIZE = 40

KEYS = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Individual:
	def __init__(self):
		self._dna = random.choices(KEYS, k=INDIVIDUAL_SIZE)
		self._fitness = 0

	def getDNA(self):
		return self._dna

	def calculateFitness(self):
		self._score = 0
		for own_letter, target_letter in zip(self._dna, TARGET):
			if own_letter == target_letter:
				self._score += 1

		self._fitness = self._score / len(TARGET)
		return self._fitness

	def __str__(self):
		return str(self._dna)

class Population:
	def __init__(self, size):
		self._population = []

		for i in range(size):
			self._population.append(Individual())

	def getPopulation(self):
		return self._population

class GeneticAlgorithm:
	def selectTournamentPopulation(self, pop):
		tournament_pop = Population(0)
		tournament_pop.getPopulation().extend(random.choices(pop.getPopulation(), k=TOURNAMENT_SELECTION_SIZE))
		tournament_pop.getPopulation().sort(key = lambda x: x.calculateFitness(), reverse = True)
		return tournament_pop

	def reproduction(self, pop):
		for i in range(len(pop.getPopulation())):
			partnerA = self.selectTournamentPopulation(pop).getPopulation()[0]	
			partnerB = self.selectTournamentPopulation(pop).getPopulation()[1]	

			child = self.crossover(partnerA, partnerB)
			self.mutate(pop)

			pop.getPopulation()[i] = child
		
	def crossover(self, parentA, parentB):
		child = Individual()
		midpoint = random.randrange(0, INDIVIDUAL_SIZE)
		
		for i in range(midpoint):
			child.getDNA()[i] = parentA.getDNA()[i]
		for i in range(midpoint, len(TARGET)):
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
	print("Generation #", genNumber, "| Fittest individual fitness: ", pop.getPopulation()[0].calculateFitness())
	print("Target phrase:", TARGET)
	print("==========================================================")
	for i, x in enumerate(pop.getPopulation()):
		print("Individual #", i, ":", ''.join(x.getDNA()), "| Fitness: ", x.calculateFitness())
	print()

def main():
	displayBanner()
	time.sleep(2)
	choice()

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

	print("Simulation terminated, target reached")

if __name__ == "__main__":
	main()
