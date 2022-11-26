tic_tac_toe = {
  'top-l': ' ',
  'top-m': ' ',
  'top-r': ' ',
  'mid-l': ' ',
  'mid-m': ' ',
  'mid-r': ' ',
  'bottom-l': ' ',
  'bottom-m': ' ',
  'bottom-r': ' '
}


def print_board(tic_tac_toe):
  print(tic_tac_toe['top-l'] + '|' + tic_tac_toe['top-m'] + '|' +
        tic_tac_toe['top-r'])
  print('------')
  print(tic_tac_toe['mid-l'] + '|' + tic_tac_toe['mid-m'] + '|' +
        tic_tac_toe['mid-r'])
  print('------')
  print(tic_tac_toe['bottom-l'] + '|' + tic_tac_toe['bottom-m'] + '|' +
        tic_tac_toe['bottom-r'])


def gameplay(tic_tac_toe):
  turn = 'X'
  gamewin = 0
  for i in range(9):
    print_board(tic_tac_toe)

    move = input("Turn for " + turn + " .Move on which space?")
    tic_tac_toe[move] = turn

    if (tic_tac_toe['top-l'] == tic_tac_toe['top-m'] == tic_tac_toe['top-r'] ==
        turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()
    elif (tic_tac_toe['mid-l'] == tic_tac_toe['mid-m'] == tic_tac_toe['mid-r']
          == turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()
    elif (tic_tac_toe['bottom-l'] == tic_tac_toe['bottom-m'] ==
          tic_tac_toe['bottom-r'] == turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()
    elif (tic_tac_toe['top-l'] == tic_tac_toe['mid-m'] ==
          tic_tac_toe['bottom-r'] == turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()
    elif (tic_tac_toe['top-r'] == tic_tac_toe['mid-m'] ==
          tic_tac_toe['bottom-l'] == turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()
    elif (tic_tac_toe['top-l'] == tic_tac_toe['mid-l'] ==
          tic_tac_toe['bottom-l'] == turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()

    elif (tic_tac_toe['top-m'] == tic_tac_toe['mid-m'] ==
          tic_tac_toe['bottom-m'] == turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()

    elif (tic_tac_toe['top-r'] == tic_tac_toe['mid-r'] ==
          tic_tac_toe['bottom-r'] == turn):
      print_board(tic_tac_toe)
      print("Player " + turn + " is the winner")
      gamewin = 1
      quit()

    if turn == 'X':
      turn = 'O'
    else:
      turn = 'X'

  if gamewin == 0:
    print_board(tic_tac_toe)
    print("The game is draw")


gameplay(tic_tac_toe)
