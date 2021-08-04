import praw

markings = [" ", "O", "X"]
playField = "   A B C\n  -------\n1 |{}|{}|{}|\n  -------\n2 |{}|{}|{}|\n  -------\n3 |{}|{}|{}|\n  -------"

# print(playField.format(fieldState[0],fieldState[1],fieldState[2],fieldState[3],fieldState[4],fieldState[5],fieldState[6],fieldState[7],fieldState[8]))


class TicTacToe:
    def __init__(self) -> None:

        '''
            Players are identified by numbers 1 and 2.
            1 corresponds to "O"
            0 corresponds to "X"
        '''

        self.fieldState = [0,0,0,0,0,0,0,0,0,0]
        self.currentPlayer = 1

        print(self.getUserInput(input("Select where you would place your cell -> ")))

    def drawPlayingField(self):
        return playField.format(markings[self.fieldState[0]],
                                markings[self.fieldState[1]],
                                markings[self.fieldState[2]],
                                markings[self.fieldState[3]],
                                markings[self.fieldState[4]],
                                markings[self.fieldState[5]],
                                markings[self.fieldState[6]],
                                markings[self.fieldState[7]],
                                markings[self.fieldState[8]],)

    def getUserInput(self, input: str):
        if len(input) > 2 :
            return None
        else :
            pos = 0
            if input[1].upper() == "A" :
                pos = 3 * (int(input[0]) - 1) + 0
            elif input[1].upper() == "B" :
                pos = 3 * (int(input[0]) - 1) + 1
            elif input[1].upper() == "C" :
                pos = 3 * (int(input[0]) - 1) + 2
            return pos

    def turn(self, inp):
        if inp != None :
            self.fieldState[inp] = self.currentPlayer
            self.currentPlayer = not(self.currentPlayer - 1) + 1

game = TicTacToe()
        