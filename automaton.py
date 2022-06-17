
class Automaton:
    def __init__(self, num_rows):
        self._rule_num = 0
        self._rule = [0] * 8
        self._rule_unpacked = [[int(x) for x in format(x, '03b')] for x in range(8)]

        self._num_rows = num_rows
        self._num_cols = self._num_rows * 2 - 1

        self._row = [0] * self._num_cols
        self._row[self._num_cols // 2] = 1

    def update_rule(self, new_rule):
        """
        Updates the current rule to new_rule
        :param new_rule: int, represents a new rule for the generator
        """

        self._rule_num = new_rule
        self._rule = [int(x) for x in format(new_rule, '08b')]

    def draw(self, graph):
        """
        Draws the pattern on the given graph
        :param graph: Graph passed from main on which the pattern will be drawn
        """

        next_row = self._row

        for row_ind in range(self._num_rows):
            for col_ind in range(self._num_cols):
                pass
