from __future__ import print_function
import os
import neat
import visualize
import random
from TicTacToe import *


class Neat_Train():
    gameTTT = TTT()
    averageFitness=0

    def __init__(self,
    generations=101,gen_intervall = 97,dir="NEAT_Files\\",showGraphics=False):
        self.generations = generations
        self.gen_intervall = gen_intervall
        self.dir = dir
        self.showGraphics = showGraphics
        
    @staticmethod
    def get_NNMove_func(net): ## needs improvement!
        def func(field):
            inputVector = TTT.fieldToVector(field)
            moveVector = net.activate(tuple(inputVector)) # STUPID IMPLEMENTATION!!!!!!!
            m = TTT.vectorToMove( list(moveVector))
            while not TTT.moveLegal(field,m):
                moveVector[m] = -99999999.0
                m = TTT.vectorToMove( moveVector)
            return m      
        return func   

    def calc_AVGFitness(self,genomes):
        self.averageFitness = 0
        for genome_id, genome in genomes:
            self.averageFitness += genome.fitness
        self.averageFitness = self.averageFitness / len(genomes)

    def fitness(self,genomes,config):
        for genome_id, genome in genomes:
            genome.fitness = 0
        for genome_id, genome in genomes:
            net = neat.nn.FeedForwardNetwork.create(genome,config)
            for opponent_id, opponent_genome in genomes:
                if not opponent_id == genome_id:
                    opp_net = neat.nn.FeedForwardNetwork.create(genome,config)
                    for i in range(10):
                        f = Neat_Train.get_NNMove_func
                        winner = self.gameTTT._match([f(net),f(opp_net)])
                        if winner ==  'X':
                            genome.fitness+=1
                        elif winner == 'O':
                            opponent_genome.fitness+=1
        self.calc_AVGFitness(genomes)


    def genome_vs_Supervised(self,genome_net,total=100):
        losses = 0
        for i in range(total):
            winner = self.gameTTT._match([self.gameTTT.get_NNMove,Neat_Train.get_NNMove_func(genome_net)],startRandom=True)
            if winner ==  'X':
                losses+=1
        print("genome lost: ",losses," matches out of", 
        total," against the supervised model")
            
    def show_Winner(self,winner,p):
        print('\nBest genome:\n{!s}'.format(winner))
        
        print("Winner Fitness is ", winner.fitness, "\n average fitness ist:", self.averageFitness,
        "\n winner is", winner.fitness/self.averageFitness,"times as fit as the average")

        winner_net = neat.nn.FeedForwardNetwork.create(winner, p.config)
        self.genome_vs_Supervised(winner_net)
        
        node_names = {}
        for index in range(-27,9):
            node_names[index] = str(index)
        if self.showGraphics:
            visualize.draw_net(p.config, winner, True, node_names=node_names,filename=self.dir+"winner.svg")

    def train_population(self,p):
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(self.gen_intervall,filename_prefix=self.dir+"neat-checkpoint-"))

        winner = p.run(self.fitness,self.generations)

        self.show_Winner(winner,p)
        if  self.showGraphics:
            visualize.plot_stats(stats, ylog=False, view=True,filename=self.dir+"avg_fitness.svg")
            visualize.plot_species(stats, view=True,filename=self.dir+"speciation.svg")

    def run(self,configName):
        config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction
        ,neat.DefaultSpeciesSet,neat.DefaultStagnation
        ,self.dir+configName)
        p = neat.population.Population(config)
        self.train_population(p)

    def check_out_population(self,p):  
        winner = p.run(fitness,1)
        self.show_Winner(winner,p)

    def continue_training(self,check_point_path):
        populus = neat.Checkpointer.restore_checkpoint(check_point_path)
        self.train_population(populus)
