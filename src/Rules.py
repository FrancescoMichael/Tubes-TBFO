def readrulesFile(path):
    try:
        with open(path, "rt") as file:
            States, Terminal, StackSymbol, StartState, StartStack, AcceptingState, Acceptby, Rules = "", "", "", "", "", "", "", ""
            States = list(file.readline().split())
            Terminal = list(file.readline().split())
            StackSymbol = list(file.readline().split())
            StartState = file.readline()
            StartStack = file.readline()
            AcceptingState = list(file.readline().split())
            Acceptby = file.readline()
            Rules = []
            line = file.readline()
            while (line):
                split = tuple(line.split())
                transition = []
                for i in range(2, 1 + (len(split)//2)):
                    transition.append((split[2 * i - 1], split[2*i]))
                rule = (split[0], split[1], split[2], transition)
                Rules.append(rule)
                del split
                del transition
                del rule
                line = file.readline()
        file.close()
        return States, Terminal, StackSymbol, StartState, StartStack, AcceptingState, Acceptby, Rules
    except Exception as e:
        print(f"Unexpected error while reading PDA file - {e}")