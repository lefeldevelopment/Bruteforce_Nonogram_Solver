from itertools import combinations

class Nonogram_solver():
    SYMBOLS = {
        "fill": "■",
        "false": "x",
        "empty": " "
    }

    def __init__(self,size: tuple[int, int], preset: list[list, list]):
        self.size = size
        self.preset = preset

        self.field = [[self.SYMBOLS["empty"]]*size[0]]*size[1]
            
        self.row_comb = self.get_all_combinations(preset[0], size[1])
        self.col_comb = self.get_all_combinations(preset[1], size[0])   


    def get_all_combinations(self,values, remain):
        possibilities = []
        for v in values:
            groups = len(v)
            no_empty = remain-sum(v)-groups+1
            ones = [[1]*x for x in v]
            res = self._create_possibilities(no_empty, groups, ones)
            possibilities.append(res)
        return possibilities


    def _create_possibilities(self,n_empty, groups, ones):
        res_opts = []
        for p in combinations(range(groups+n_empty), groups):
            selected = [-1]*(groups+n_empty)
            ones_idx = 0
            for val in p:
                selected[val] = ones_idx
                ones_idx += 1
            res_opt = [ones[val]+[-1] if val > -1 else [-1] for val in selected]
            res_opt = [item for sublist in res_opt for item in sublist][:-1]
            res_opts.append(
                [self.SYMBOLS["fill"] if x == 1 else self.SYMBOLS["false"] for x in res_opt])
        return res_opts


    def find_matches(self,combo, size):
        empty = [self.SYMBOLS["empty"]]*size
        for i in range(size):
            all_poss = [x[i] for x in combo]
            if len(set(all_poss)) == 1:
                empty[i] = all_poss[0]
        return empty


    def filter_combos(self, current_line, combos):
        new_combos = []
        for combo in combos:
            match = True
            for current, c in zip(current_line, combo):
                if current != self.SYMBOLS["empty"] and current != c:
                    match = False
                    break
            if match:
                new_combos.append(combo)
        return new_combos


    def solve(self):
        while self.SYMBOLS["empty"] in [cell for row in self.field for cell in row]:
            check_field = self.field.copy()
            # row
            for i, line in enumerate(self.row_comb):
                self.row_comb[i] = self.filter_combos(self.field[i], line)
                self.field[i] = self.find_matches(self.row_comb[i], self.size[1])
            # column
            for j in range(self.size[1]):
                col = [self.field[i][j] for i in range(self.size[0])]
                self.col_comb[j] = self.filter_combos(col, self.col_comb[j])
                matches = self.find_matches(self.col_comb[j], self.size[0])
                for i in range(self.size[0]):
                    self.field[i][j] = matches[i]
            if check_field == self.field:
                break
        return self.field

    @staticmethod
    def from_input():
        while True:
            try:
                size_str = input("Enter the size of the Nonogram in the format 'width x height': ")
                width, height = size_str.split("x")
                size = (int(height), int(width))
                break
            except ValueError:
                print("Invalid input. Please enter the size in the format 'width x height' (e.g '10x10').")

        preset_rows = []
        for i in range(size[1]):
            while True:
                try:
                    inp_row = input(f"Enter preset for row {i+1} (comma separated): ")
                    if not inp_row:
                        preset_row = []
                    else:
                        preset_row = list(map(int, inp_row.split(",")))
                    break
                except ValueError:
                    print("Invalid input. Please the row preset comma separated (e.g '1,4,2').")
            preset_rows.append(preset_row)

        preset_cols = []
        for i in range(size[0]):
            while True:
                try:
                    inp_col = input(f"Enter preset for col {i+1} (comma separated): ")
                    if not inp_col:
                        preset_col = []
                    else:
                        preset_col = list(map(int, inp_col.split(",")))
                    break
                except ValueError:
                    print("Invalid input. Please the column preset comma separated (e.g '1,4,2').")
            preset_cols.append(preset_col)

        preset = (preset_rows, preset_cols)

        return Nonogram_solver(size, preset)

    def __repr__(self):
        return '\n'.join([' '.join(map(str, sublist)) for sublist in self.field])


if __name__ == "__main__":
    example_object = Nonogram_solver.from_input()
    example_object.solve()
    print(example_object)
