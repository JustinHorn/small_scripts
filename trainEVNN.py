from __future__ import print_function
import os
import neat
import visualize
import random
from TicTacToe import *
from model import TicTacToefield_ToInputList,outputVectorToMove

game_TTT = TTT()

averageFitness=0

def fieldToInputVector(field):
    vector = []
    for char in field:
        x = [0.01]*3
        if char == game_TTT.EMPTY:
            x[0] = 0.99
        elif char == game_TTT.PLAYER_SIGNS[1]:
            x[1] = 0.99
        else:
            x[2] = 0.99
        for e in x:
            vector.append(e)
    return vector

def outputVectorToMove(vector):
    return np.argmax(vector)


def get_NNMove(game,model): ## needs improvement!
    field_as_inputVector = fieldToInputVector(game_TTT.field)
    move_as_vector = model.activate(tuple(field_as_inputVector)) # STUPID IMPLEMENTATION!!!!!!!
    m = outputVectorToMove( list(move_as_vector))
    while not game.is_moveLegal(m):
        move_as_vector[m] = -99999999.0
        m = outputVectorToMove( move_as_vector)
    return m         

def match(model_function,model):
    g = game_TTT
    g.reset()
    while not g.game_over:
        m = model_function[g.current_player](g,model[g.current_player])
        if g.is_moveLegal(m):
            g.make_move(m)
            (g.game_over ,WINNER) = g.is_gameOver_whoWon()
            if not g.game_over:
                g.swap_player()
        else:
            print("Illegal move!")
    return WINNER

int_actual_generations = 0


def fitness(genomes,config):
    for genome_id, genome in genomes:
        genome.fitness = 0
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        for opponent_id, opponent_genome in genomes:
            if not opponent_id == genome_id:
                opp_net = neat.nn.FeedForwardNetwork.create(genome,config)
                for i in range(10):
                    winner = match([get_NNMove,get_NNMove],[net,opp_net])
                    if winner ==  'X':
                        genome.fitness+=1
                    elif winner == 'O':
                        opponent_genome.fitness+=1
    global averageFitness
    averageFitness = 0
    for genome_id, genome in genomes:
        averageFitness += genome.fitness
    averageFitness = averageFitness / len(genomes)
    global int_actual_generations
    int_actual_generations+=1

def score_match(model):
    g = game_TTT
    g.reset()
    g.field[random.randrange(0,9)] = [g.PLAYER_SIGNS[0]]
    g.current_player = 1
    while not g.game_over:
        if g.current_player == 0:
            m = g.get_NNMove()
        else:
            m = get_NNMove(g,model)
        if g.is_moveLegal(m):
            g.make_move(m)
            (g.game_over ,WINNER) = g.is_gameOver_whoWon()
            if not g.game_over:
                g.swap_player()
        else:
            print("Illegal move!")
    return WINNER

def genome_vs_SupervisedTTTFedForward(genome_net,total=100):
    losses = 0
    for i in range(total):
        winner = score_match(genome_net)
        if winner ==  'X':
            losses+=1
    print("genome lost: ",losses," matches out of", 
    total," against the supervised model")
        


def show_winner_build_and_score(winner,p):
    print('\nBest genome:\n{!s}'.format(winner))
    
    print("Winner Fitness is ", winner.fitness, "\n average fitness ist:", averageFitness, "\n winner is", winner.fitness/averageFitness," as fit as the average")
    winner_net = neat.nn.FeedForwardNetwork.create(winner, p.config)
    genome_vs_SupervisedTTTFedForward(winner_net)
    print("actual_generations: ",int_actual_generations)
    node_names = {}
    for index in range(-27,9):
        node_names[index] = str(index)
    #node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    visualize.draw_net(p.config, winner, True, node_names=node_names)

def train_population(p,generations=101,checkpoint=97):
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(checkpoint))

    winner = p.run(fitness,generations)

    show_winner_build_and_score(winner,p)

    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)


def run(file_path):
    config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction
    ,neat.DefaultSpeciesSet,neat.DefaultStagnation
    ,file_path)

    p = neat.population.Population(config)
    train_population(p)


# filename = 'neat-config.txt'
# local_dir = os.path.dirname(__file__)
# config_path = os.path.join(local_dir,'neat-config.txt')

# run(config_path)

def restore_checkpoint(check_point):
    return neat.Checkpointer.restore_checkpoint(check_point)


def check_out_population(p):  
    winner = p.run(fitness,1)
    show_winner_build_and_score(winner,p)


# p = restore_checkpoint("neat-checkpoint-99")
# train_population(p,generations=100,checkpoint=97)
check_out_population(restore_checkpoint("neat-checkpoint-196"))