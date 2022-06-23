

class Automaton:
    """Class representing an Elementary Cellular Automaton, which can be updated to follow any of the 256 rules"""

    def __init__(self, num_rows, num_cols, cell_side):
        self._rule = 0
        self._rule_bits = [0] * 8

        self._num_rows = num_rows + 1
        self._num_cols = num_cols + 2

        self._matrix = [[0 for i in range(self._num_cols)] for j in range(self._num_rows)]
        self._matrix[0][num_rows] = 1

        self._cell_size = cell_side

    def update_rule(self, new_rule):
        """
        Updates the current rule to new_rule and generates pattern
        :param new_rule: int, represents a new rule for the generator
        """

        self._rule = new_rule
        self._rule_bits = [int(x) for x in format(new_rule, '08b')]

        self._update_pattern_matrix()

    def _update_pattern_matrix(self):
        """
        Generates the pattern produced by this automaton and updates matrix
        """

        rows = self._num_rows
        cols = self._num_cols
        rule_bits = self._rule_bits
        mat = self._matrix

        for row_ind in range(rows - 1):
            this_row = mat[row_ind]
            next_row = mat[row_ind + 1]
            for col_ind in range(cols):
                if col_ind == 0:
                    rule_case = self.cell_seq_case([this_row[1], this_row[0], this_row[1]])
                elif col_ind == cols - 1:
                    rule_case = self.cell_seq_case([this_row[cols - 2], this_row[cols - 1], this_row[cols - 2]])
                else:
                    rule_case = self.cell_seq_case(this_row[col_ind - 1:col_ind + 2])

                next_row[col_ind] = rule_bits[rule_case]

    def draw(self, canvas):
        """
        Draws the pattern produced by this automaton on the given canvas
        :param canvas: Canvas passed from main on which the pattern will be drawn
        """

        rows = self._num_rows
        cols = self._num_cols
        mat = self._matrix
        size = self._cell_size

        for row_ind in range(rows - 1):
            this_row = mat[row_ind]
            for col_ind in range(cols - 2):
                cell_is_alive = this_row[col_ind + 1]
                canvas.TKCanvas.create_rectangle(col_ind * size, row_ind * size,
                                                 (col_ind + 1) * size, (row_ind + 1) * size,
                                                 fill=("black" if cell_is_alive else "white"),
                                                 outline=("black" if cell_is_alive else "white"))

    @staticmethod
    def cell_seq_case(binary):
        return 7 - sum(val * (2 ** i) for i, val in enumerate(reversed(binary)))
