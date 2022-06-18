class Automaton:
    def __init__(self, num_rows, num_cols, cell_side):
        self._rule = 0
        self._rule_bits = [0] * 8

        self._num_rows = num_rows
        self._num_cols = num_cols

        self._base_row = [0] * self._num_cols
        self._base_row[self._num_cols // 2] = 1

        self.size = cell_side

    def update_rule(self, new_rule):
        """
        Updates the current rule to new_rule
        :param new_rule: int, represents a new rule for the generator
        """

        self._rule = new_rule
        self._rule_bits = [int(x) for x in format(new_rule, '08b')]

    def draw(self, canvas):
        """
        Draws the pattern on the given graph
        :param canvas: Canvas passed from main on which the pattern will be drawn
        """

        this_row = self._base_row
        next_row = self._base_row

        for row_ind in range(self._num_rows):
            for col_ind in range(self._num_cols):
                if col_ind == 0:
                    rule_case = self.get_deci([0, this_row[0], this_row[1]])
                elif col_ind == self._num_cols - 1:
                    rule_case = self.get_deci([this_row[self._num_cols-2], this_row[self._num_cols-1], 0])
                else:
                    rule_case = self.get_deci(this_row[col_ind-1:col_ind+2])

                next_row[col_ind] = self._rule_bits[rule_case]
                canvas.TKCanvas.create_rectangle(col_ind * self.size, row_ind * self.size,
                                                 (col_ind + 1) * self.size, (row_ind + 1) * self.size,
                                                 fill=("black" if this_row[col_ind] else "white"),
                                                 outline=("black" if this_row[col_ind] else "white"))

                this_row = next_row

    @staticmethod
    def get_deci(binary):
        return sum(val * (2 ** i) for i, val in enumerate(reversed(binary)))
