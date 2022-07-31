print(" "*22, "Игра Крестики-нолики ")

board = list(range(1,10))

def board1(board):
   print(" "* 25,"-" * 13)
   for i in range(3):
      print(" "* 25,"|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print(" "* 25,"-" * 13)

def take_input(token):
   valid = False
   while not valid:
      answer = input(" "* 25 + "Куда поставим " + token+"? ")
      try:
         answer = int(answer)
      except:
         print(" "* 25,"Вы ввели не число?")
         continue
      if answer >= 1 and answer <= 9:
         if(str(board[answer-1]) not in "XO"):
            board[answer-1] = token
            valid = True
         else:
            print(" "* 25,"здесь занято!")
      else:
        print(" "* 25,"Введите число от 1 до 9.")

def check_win(board):
   coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        board1(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp," "* 25 ,"ПОЗДРАВЛЯЮ!")
              win = True
              break
        if counter == 9:
            print(" "*25,"Ничья!")
            break
    board1(board)
main(board)

input("Нажмите Enter для выхода!")