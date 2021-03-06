import os, time

class Game():
  def __init__(self, theme, secret_word):
    self.theme = theme
    self.secret_word = secret_word
    self.word = ['_'] * len(secret_word)
    self.mistakes = []
    self.tries = 4
    self.tried_letters = []
    self.guess = False

  def draw(self):
    time.sleep(0.1)
    os.system('clear')
    print(f'The subject is {self.theme}')
    for l in self.word:
      print(f'{l}', end=' ')
    print(f'\nThe secret word has {len(self.secret_word)} letters!')
    if self.tried_letters:
      print('\nYou\'ve already tried letter(s)')
      if len(self.tried_letters) > 1:
        for idx, l in enumerate(self.tried_letters):
          if self.tried_letters[idx] == self.tried_letters[-1]:
            print(l)
          else:
            print(l, end=',')
      else:
        print(self.tried_letters[0])
      
      if self.mistakes:
        print(f'\nYou\'ve done {len(self.mistakes)} mistake(s)\n')


  def __check_guess(self, letter):
    while len(letter) > 1 or not letter:
      if letter == 'guess':
        break
      else:
        print('Invalid character.')
        letter = input('Please type a letter again:\n')
        return letter
    return letter
  
  def __compare(self, letter):
    count = 0
    if letter in self.secret_word:
      while count < len(self.secret_word):
        if letter == self.secret_word[count]:
          self.word[count] = letter
        count += 1
    else:
      print(f'\nThe letter {letter} is not in secret word!\n')
      self.mistakes.append(letter)
      time.sleep(1.5)

  def get_guess(self):
    letter = self.__check_guess(input('\nType a letter or type \'guess\' if you think you already know the entire word and want to try to guess:\n'))

    if letter == 'guess':
      self.try_guess()
    else:

      if letter in self.tried_letters:
        print(f'Letter {letter} was already typed')
        time.sleep(1.5)
      else:
        self.tried_letters.append(letter)
        self.__compare(letter)

  def try_guess(self):
    self.draw()
    guessed_word = input('All right! Try to guess. Type the entire word. Be careful. You have only one chance:\n')
    if guessed_word == self.secret_word:
      self.guess = True
    else:
      self.guess = False
      self.tries = 0
    
  def play(self):
    while (len(self.mistakes) < self.tries and '_' in self.word) and not self.guess:
      self.draw()
      self.get_guess()
  
    if self.guess:
      for idx, w in enumerate(self.secret_word):
        self.word[idx] = self.secret_word[idx]
    
    self.draw()

    if not '_' in self.word:
      os.system('clear')
      print('Congratulations!!! You Win!!!')
    else:
      os.system('clear')
      print('You lose. The word was...', end=' ')
      for l in self.secret_word:
        print(l, end='')

      
    


  

    