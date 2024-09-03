class Game ():
  
  def __init__(self, turn = 'x', tie = False, winner = None, board = {
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
  }):
    
    self.turn = turn
    self.tie = tie
    self.winner = winner
    self.board = board

  def print_message(self):
    if self.tie:
      print("The game ended in a tie")
    elif self.winner:
      print(f"{self.winner} wins the game!")
    else:
      print(f"It's player {self.turn}'s turn!")


  def print_board(self):
    b = self.board
    print(f"""
          A   B   C
      1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
      2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
      3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
    """)

  def switch_turn(self):
    self.turn = 'o' if self.turn == 'x' else 'x'


  def check_winner(self):
    winning_combinations = [
        ('a1', 'b1', 'c1'),
        ('a2', 'b2', 'c2'),
        ('a3', 'b3', 'c3'),
        ('a1', 'a2', 'a3'),
        ('b1', 'b2', 'b3'),
        ('c1', 'c2', 'c3'),
        ('a1', 'b2', 'c3'),
        ('a3', 'b2', 'c1'),
    ]
    
    for combo in winning_combinations:
      if self.board[combo[0]] and self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
        self.winner = self.turn
        return self.winner
    return None  


  def check_for_tie(self):
    if all(value is not None for value in self.board.values()) and self.winner is None:
      self.tie = True


  def get_move(self):
    move = input(f"Enter a valid move (example: A1): ").lower().strip()
    
    if move in self.board:
      if self.board[move] is None:
        self.board[move] = self.turn
        self.print_board()
        if self.check_winner():
          self.print_message()
          return
        self.check_for_tie()
        if self.tie:
          self.print_message()
          return
        self.switch_turn()
        self.print_message()
      else:
        self.print_message()
    self.get_move()


  def play_game(self):   
    print("Welcome to tic-tac-toe")   
    self.print_board()
    self.print_message()
    self.get_move()
  
  
game_instance = Game()
game_instance.play_game()