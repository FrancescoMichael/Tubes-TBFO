states, terminal, stackSymbol, startState, startStack, acceptingState, acceptby, rules = "", "", "", "", "", "", "", "",

def readrulesFile(path):
    try:
        with open(path, "rt") as file:
            global states, terminal, stackSymbol, startState, startStack, acceptingState, acceptby, rules
            states = list(file.readline().split())
            terminal = list(file.readline().split())
            stackSymbol = list(file.readline().split())
            startState = file.readline()
            startStack = file.readline()
            acceptingState = list(file.readline().split())
            acceptby = file.readline()
            rules = []
            line = file.readline()
            while (line):
                split = tuple(line.split())
                transition = []
                for i in range(2, 1 + (len(split)//2)):
                    transition.append((split[2 * i - 1], split[2*i]))
                rule = (split[0], split[1], split[2], transition)
                rules.append(rule)
                del split
                del transition
                del rule
                line = file.readline()
        file.close()
    except FileNotFoundError:
        print("PDA file is not found")
    except Exception as e:
        print(f"Unexpected error while reading PDA file - {e}")