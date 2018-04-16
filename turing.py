class Tape(object):
    empty_symbol = ' '

    def __init__(self, tape_string=''):
        self.__tape = dict((enumerate(tape_string)))

        # self.__tape = {}
        # for i in range(len(tape_string)):
        #     self.__tape[i] = input[i]

    def __str__(self):
        s = ''
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s

    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.empty_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char


class TuringMachine(object):
    def __init__(self,
                 tape='',
                 empty_symbol=' ',
                 inital_state='',
                 final_states=None,
                 transition_function=None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__empty_symbol = empty_symbol
        self.__current_state = inital_state
        if transition_function == None:
            self.transition_function = {}
        else:
            self.transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return(str(self.__tape))

    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.transition_function:
            y = self.transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == 'R':
                self.__head_position += 1
            elif y[2] == 'L':
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False
