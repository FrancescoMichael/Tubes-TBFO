class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Run:
    def __init__(self, tokenized, rules):
        #print(tokenized)
        new_rule = []
        for Rule in rules:
            Rule1 = Rule[0].replace("eps", "")
            Rule2 = Rule[1].replace("eps", "")
            Rule3 = Rule[2].replace("eps", "")
            Rule4 = Rule[3][0][0].replace("eps", "")
            Rule5 = Rule[3][0][1].replace("eps", "")
            new_rule.append((Rule1, Rule2, Rule3, [(Rule4, Rule5)]))
        self.tokenized = tokenized
        self.rules = new_rule
        self.pointer = 0
        self.states = [("_Qstart", "_Z0")]
        self.allowed_texts = ["GET", "POST", "text", "password", "email", "number", "checkbox", "submit", "reset",
                              "button"]
        self.allowed_stack = ["_getpost", "_valinput", "_subresbut"]

    def is_prefix(self, str1, str2):
        if str1 == str2:
            return True
        if len(str2) > len(str1):
            return False
        #print(str1, str2)
        if len(str1) > 8:
            if "_anyText" ==  str1[:8] and str2 in self.allowed_stack:
                return True
        i = 0
        while i < len(str2):
            if str2[i] != str1[i]:
                return False
            i = i + 1
        if i == len(str1):
            return True
        if str1[i] == '_':
            return True
        #print(str1, str2)
        return False
    
    def isTheSame(self, str1, str2):
        if str1 == "anyText" and str2 in self.allowed_texts:
            return True
        return False

    def unify(self, state, char):
        res = []
        for rule in self.rules:
            if state[0] == rule[0] and (self.isTheSame(char, rule[1]) or char == rule[1]) and self.is_prefix(state[1], rule[2]):
                #print(state[0], state[1], rule[0], rule[1], rule[2])
                curstack = state[1]
                for nxt in range(0, len(rule[3]), 1):
                    res.append((rule[3][nxt][0], curstack.replace(rule[2], rule[3][nxt][1], 1)))
        return res

    def find_expected(self, end_state):
        res = []
        for rule in self.rules:
            if end_state[0] == rule[0] and end_state[1] == rule[2]:
                res.append(rule[1])
        return res

    def fun(self):
        stack_trace = []
        #print("here")
        while self.pointer < len(self.tokenized):
            all_pos_states = []
            for state in self.states:
                all_pos_states = self.unify(state, self.tokenized[self.pointer])
            stack_trace.extend(all_pos_states)
            self.states = all_pos_states
            if not self.states:
                #print(stack_trace)
                #print(self.pointer)
                print(f'{bcolors.FAIL}Syntax Error!\nUnknown character: {self.tokenized[self.pointer]} {bcolors.ENDC}')
                return
            self.pointer += 1
        #print(stack_trace)
        #print("END: ")
        #print(self.states[0])
        for endState in self.states:
            if not endState[1] :
                print(f'{bcolors.OKGREEN}Accepted! {bcolors.ENDC}')
                return
        expected_symbols = []
        for endState in self.states:
            expected_symbols.extend(self.find_expected(endState))
        print('Expected:')
        print(expected_symbols)
