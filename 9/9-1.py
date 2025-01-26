import sys,re
class State():
    BASE = 0
    FIRSTNUM = 1
    SECONDNUM = 2
input = sys.stdin.read()
built = ''
subsection = ''
idx = -1
state = State.BASE
while idx < len(input) - 1:
    idx += 1
    match state:
        case State.BASE:
            if input[idx] != '(':
                built += input[idx]
                continue
            state = State.FIRSTNUM
            subsection = input[idx]
        case State.FIRSTNUM:
            if input[idx] == 'x':
                if len(subsection) == 1:
                    # Input was '(x', which doesn't make a marker
                    built += subsection
                    built += input[idx]
                    state = State.BASE
                    print('asdfasdfeeeeee')
                    continue
                subsection += input[idx]
                state = State.SECONDNUM
                continue
            if not input[idx].isdigit():
                #Input was '(12ax' or similar
                built += subsection
                built += input[idx]
                state = State.BASE
                continue
            subsection += input[idx]
        case State.SECONDNUM:
            if input[idx] == ')':
                if subsection[-1] == 'x':
                    # Input was '(12x)', which doesn't make a marker
                    built += subsection
                    built += input[idx]
                    state = State.BASE
                    continue
                subsection += input[idx]
                #Mutliply here
                _, ln, tm, _ = re.split(r'\(|\)|x', subsection)
                ln = int(ln)
                tm = int(tm)
                toMult = ''
                for _ in range(ln):
                    idx += 1
                    toMult += input[idx]
                for _ in range(tm):
                    built += toMult
                state = State.BASE
                continue
            if not input[idx].isdigit():
                #Input was '(12xdd' or similar
                built += subsection
                built += input[idx]
                state = State.BASE
                continue
            subsection += input[idx]
print(len(built))