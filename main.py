class Printer():
    def __init__(self, nr_of_iterations, strategies):
        self.solvers = list(strategies)
        self.nr_iterations = nr_of_iterations
        self.inputs = []
        self.outputs = {}

    def generate_cases(self):
        from random import randint
        inputs = []
        f = open("inputs.txt", 'w')
        f.write("Nr   Towers    Disks\n")
        for i in range(0, self.nr_iterations):
            number_of_towers = randint(3, 9)
            number_of_disks = randint(2, 9)
            inputs.append(tuple([number_of_towers, number_of_disks]))
            f.write("%d     %d          %d\n" % (i, number_of_towers, number_of_disks))
        f.close()
        return inputs

    def run_tests(self):
        from random_strategy import RandomHanoiSolver

        self.inputs = self.generate_cases()
        for solver in self.solvers:
            self.outputs[solver] = []

        for strategy in self.solvers:
            nr_test = 0
            for input in self.inputs:
                hanoi_solver = None
                print ("Running Test " + str(nr_test))
                nr_test += 1
                if strategy == "random":
                    hanoi_solver = RandomHanoiSolver(input[0], input[1])

                solver_response = hanoi_solver.run_solver()
                self.outputs[strategy].append(solver_response)
        return (self.outputs)
        # print("Time passed: {tt}".format(tt=nice_time(diff)))

    def get_summary(self):
        solvers_info = []
        for solver in self.solvers:
            all_results = self.outputs[solver]
            total_time = sum([result[0] for result in all_results])
            total_passed = sum([result[1] for result in all_results])
            total_fail = self.nr_iterations - total_passed
            total_moves = sum([len(result[2]) for result in all_results])
            avg_moves = 0
            if total_passed != 0:
                avg_moves = total_moves / total_passed
            solver_summary = {"name":solver,
                              "nr fails": total_fail,
                              "nr successes": total_passed,
                              "average time": total_time / self.nr_iterations,
                              "average moves": avg_moves
                              }
            solvers_info.append(solver_summary)
        return solvers_info

    def write_to_file(self, file_name):
        from nice_timing import nice_time
        f = open(file_name, 'w')
        dates = self.get_summary()

        for data in dates:
            txt_result = """
The result for %(name)s strategy, after running %(nr_iteration)d  inputs from inputs.txt are:
        *Nr Fails: %(fails)d
        *Nr Success: %(success)d
        *Average Solution Length: %(moves)d
        *Average Time: %(time)s

            """ % ({"name": data['name'],
                    "nr_iteration": self.nr_iterations,
                    "fails": data["nr fails"],
                    "success": data["nr successes"],
                    "moves": data["average moves"],
                    "time": nice_time(data["average time"])
                    })
            f.write(txt_result)
        f.close()


if __name__ == "__main__":
    print("Starting...")
    printer = Printer(100, ['random'])
    outputs = printer.run_tests()
    printer.write_to_file("output_summary.txt")
    print("Done")