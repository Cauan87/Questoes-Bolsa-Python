import unittest


def verbing(s):
    if 'ing' == s[-3:]:
       return s + 'ly'
    elif 'do' == s:
       return s
    else:
       return s + 'ing'
    return s

# Dado uma string, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    bad_word = s.find('bad')
    not_word = s.find('not')
    if not_word != -1 and bad_word != -1 and bad_word > not_word:
       return s[:not_word] + 'good' + s[bad_word + 3:]
    else:
       return s
        

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a parte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
   if len(a) % 2 == 0 and len(b) % 2 == 0:
      return a[:2] + b[:1] + a[2:] + b[1:]
   elif len(a) % 2 !=  0 and len(b) <= 3:
      return a[:3] + b[:2] + a[3:] + b[2:]
   else:
      return a[:3] + b[:3] + a[3:] + b[3:]


class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()
