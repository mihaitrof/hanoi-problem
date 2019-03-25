
from implementation import Implementation
from random import randint
import copy


class RandomHanoiSolver(Implementation):

    # n - number of towers
    # m - number of disks
    def __init__(self, n, m):
        super(RandomHanoiSolver, self).__init__(n, m)
        self.last_good = m
        self.strategy_name = "Random (Optimized)"

    def do_transition(self, tower_i, tower_j):
        try:
            top_from_tower_i = self.current_state[1:self.last_good + 1].index(tower_i) + 1
            self.current_state[top_from_tower_i] = tower_j
        except ValueError:
            pass
        self.tempsolutions.append((tower_i, tower_j))
        return self.current_state

    def strategy(self):
        while not self.is_in_final_state():
            tower_i, tower_j = self.get_random_towers()
            if self.is_valid_transition(tower_i, tower_j) is True:
                self.do_transition(tower_i, tower_j)

                if self.current_state[self.last_good] == self.n:
                    self.last_good -= 1

        self.run_on_final_state()

    def get_random_towers(self):
        tower_i = randint(1, self.n + 1)
        tower_j = randint(1, self.n + 1)
        return tower_i, tower_j