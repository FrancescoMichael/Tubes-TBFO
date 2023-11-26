class Run:
    def __init__(self, tokenized, rules):
        self.tokenized = tokenized
        self.rules = rules
        self.pointer = 0
        self.states = [("_Qstart", "Z0")]

    def unify(self, state, char):
        res = []
        for rule in self.rules:
            if state[0] == rule[0] and char == rule[1] and state[1] == rule[2]:
                curstack = state[1]
                for nxt in range(0, len(rule[3]), 1):
                    res.append((rule[3][nxt][0], curstack.replace(rule[2], rule[3][nxt][1])))
        return res

    def find_expected(self, end_state):
        res = []
        for rule in self.rules:
            if end_state[0] == rule[0] and end_state[1] == rule[2]:
                res.append(rule[1])
        return res

    def fun(self):
        while self.pointer < len(self.tokenized):
            all_pos_states = []
            for state in self.states:
                all_pos_states = self.unify(state, self.tokenized[self.pointer][0])
            self.states = all_pos_states
            if not self.states:
                print(f'Unknown character in line {self.tokenized[self.pointer][1]}: {self.tokenized[self.pointer][0]}')
                return
            self.pointer += 1
        for endState in self.states:
            if endState[1] == "eps":
                print('Accepted!')
                return
        expected_symbols = []
        for endState in self.states:
            expected_symbols.extend(self.find_expected(endState))
        print('Expected:')
        print(expected_symbols)
