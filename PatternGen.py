CELLS_PER_ROW = 201


class PatternGen:
    def __init__(self):
        self.rule_num = 0
        self.rule = [0] * 8
        self.row = [0] * CELLS_PER_ROW
        self.row[CELLS_PER_ROW // 2] = 1

    def update_rule(self, new_rule):
        """
        Updates the current rule to new_rule
        :param new_rule: int, represents a new rule for the generator
        """

        self.rule_num = new_rule
        self.rule = [int(x) for x in format(new_rule, '08b')]
        print(self.rule)

    def draw(self, graph):
        """
        Draws the pattern on the given graph
        :param graph: Graph passed from main on which the pattern will be drawn
        """

        pass
