from words import WordGenerator
from game import Game

theme, word = WordGenerator().get_theme()

game = Game(theme, word)

game.play()



