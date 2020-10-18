import random

class WordGenerator():
  def __init__(self):
    self.__dict_words = {'country': ['Argentina', 'Alemanha', 'Venezuela', 'Colombia', 'Espanha', 'Italia'],
'food': ['Pizza', 'Lasanha', 'Brigadeiro', 'Feijoada', 'Nhoque'],
'technology': ['computador', 'notebook', 'celular', 'tablet'],
'brand': ['apple', 'samsung', 'dell', 'lg', 'asus', 'positivo']
}
  
  def get_theme(self):
    theme = random.choice(list(self.__dict_words.keys()))
    return (theme, self.__get_word(theme))

  def __get_word(self,theme):
    word = random.choice(self.__dict_words[theme]).lower()
    return word
