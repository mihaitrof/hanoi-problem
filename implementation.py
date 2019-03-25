from nice_timing import *

class Implementation(object):


    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.strategy_name = "None"

        self.initial_state = [n] + [1] * m
        self.current_state = list(self.initial_state)
        self.final_state = [n] * (m + 1)

        # Statistics
        self.solution_found = False
        self.number_of_solutions = 0
        self.solutions = []
        self.tempsolutions = []

    def get_current_state(self):
        return (self.current_state)

    def is_in_final_state(self):
        return self.current_state == self.final_state

    def is_valid_transition(self, tower_i, tower_j, state=None):
        if state is None:
            state = self.current_state
        # basic tests
        if not (1 <= tower_i <= self.n):
            return False
        if not (1 <= tower_j <= self.n):
            return False
        if tower_i == tower_j:
            return False

        try:
            top_from_tower_i = state[1:].index(tower_i) + 1
        except ValueError:  # Not found means tryin to move inexistent.
            return False

        try:
            top_from_tower_j = state[1:].index(tower_j) + 1
        except ValueError:  # Not found means empty.
            return True

        if (top_from_tower_i > top_from_tower_j):
            return False

        return True

    def run_on_final_state(self):
        self.solution_found = True
        self.number_of_solutions += 1
        self.solutions.append(list(self.tempsolutions))

    def run_solver(self):

        start_time = ctime_millis()

        print("I am trying to solve the problem.")
        print("Using strategy: {s}".format(s=self.strategy_name))
        print("Please wait....")
        self.strategy()
        print("Finished.")
        print("Nr. of solutions: {s}.".format(s=self.number_of_solutions))
        print("Details in file.")
        solution = []
        if len(self.solutions) > 0:
            solution = self.solutions[0]
        diff = ctime_millis() - start_time
        print("Time passed: {tt}".format(tt=nice_time(diff)))
        print (self.number_of_solutions)
        return (diff, self.number_of_solutions, solution)