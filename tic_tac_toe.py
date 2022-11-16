import random as rp

class Game:
    def board(self):            #to print the board
        for _ in range(9):
            if _ == 3 or _ == 6 :
                print()
                print(f"---|---|---")
            if _ == 2 or _ == 5 or _ == 8:
                print(f" {_}", end="")
            else:
                print(f" {_} |", end="")
        print()

    def choosing_turn(self, player_choice):
        computer_val = ""
        self.player_choice = player_choice
        if player_choice == 'x':
            computer_val = 'o'
            return computer_val
        if player_choice == 'o':
            computer_val = 'x'
            return computer_val
        
    def turn(self, computer_val):
        turn = 165145         #garbage value
        if computer_val == 'x':
            turn = 1
        elif computer_val == 'o':
            turn = 0
        return turn

    def computer_chance(self, list1, list2):
        if len(list2) == 9:
            com_move = rp.choice(list2)
            at_index = list1.index(com_move)
            list1.pop(com_move)
            list1.insert(at_index, computer_val)
            list2.remove(com_move)
            return list1
        elif len(list2) >= 0:
            com_move = rp.choice(list2)
            at_index = list1.index(com_move)
            list1.pop(com_move)
            list1.insert(at_index, computer_val)
            list2.remove(com_move)
            return list1

    def player_chance(self, list1, list2):
        player_move = int(input("Please choose a box between 0 to 8: "))
        if player_move in list1:
            at_index = list1.index(player_move)
            list1.pop(player_move)
            list1.insert(at_index, self.player_choice)
            list2.remove(player_move)
            return list1

    def return_list(self):
        l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.list1= l1

    def change_board(self, l1):            #other way to print changing board
        print(f"{l1[0]} | {l1[1]} | {l1[2]}")
        print(f"{l1[3]} | {l1[4]} | {l1[5]}")
        print(f"{l1[6]} | {l1[7]} | {l1[8]}")

    def checkWinner(self, l1):
        if l1[0] == l1[1] == l1[2]: #checking winner in a straight first line
            return l1[0]
        elif l1[3] == l1[4] == l1[5]: #checking winner in a straight second line
            return l1[3]
        elif l1[6] == l1[7] == l1[8]: #checking winner in a straight third line
            return l1[6]
        elif l1[0] == l1[4] == l1[8]:   #checking winner in a diagonally left to right
            return l1[4]
        elif l1[2] == l1[4] == l1[6]:   #checking winner in a diagonally right to left
            return l1[2]
        elif l1[0] == l1[3] == l1[6]:   #checking winner in a up to down 1st line
            return l1[3]
        elif l1[1] == l1[4] == l1[7]:   #checking winner in a up to down 2nd line
            return l1[7]
        elif l1[2] == l1[5] == l1[8]:   #checking winner in a up to down 3rd line
            return l1[2]
        else:
            return -1

if __name__=="__main__":
    g = Game()
    g.board()
    user_input = input("Please choose any characer from X or O: ")
    computer_val = g.choosing_turn(user_input)
    turn = g.turn(computer_val)
    list_available_move = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while len(list2) != 0:
        if turn == 1:
            print("Computer's Chance")
            list_available_move = g.computer_chance(list_available_move, list2)
            g.change_board(list_available_move)
            turn = 0
        elif turn == 0:
            print("Player's Chance")
            list_available_move = g.player_chance(list_available_move, list2)
            g.change_board(list_available_move)
            turn = 1
        winner = g.checkWinner(list_available_move)
        if winner == 'x':
            print("X won")
            break
        elif winner == 'o':
            print("O won")
            break
        elif len(list2) == 0:
            print("It's a tie..!")
            break