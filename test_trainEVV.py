import unittest
import neat
from trainEVNN import *

class Test_TrainEVNN(unittest.TestCase):

    checkpoints = "NEAT_Files\\neat-checkpoint-"
    config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction
    ,neat.DefaultSpeciesSet,neat.DefaultStagnation
    ,config_location)
    test_object = Neat_Train(1,1)

    def test_store_fitnessValue(self):
        pass

    def test_run(self):
        self.test_object.start("neat-config.txt")

    def test_continue_training(self):
        self.test_object.continue_training(self.checkpoints+str(0))


if __name__ == '__main__': 
    unittest.main()