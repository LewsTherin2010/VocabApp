import sys

sys.path.append('.\\')

from vocab_functions import *

user_input = -1
while user_input != '9':
  print('*************************** MENU ***************************')
  print('1. Add new word')
  print('2. Test words')
  print('3. See summary of vocabulary')
  print('4. Test grammar')
  print('9. Exit program')
  print('************************************************************')
  user_input = input()

  if user_input == '1':
    prompt_user_for_new_entry()
  elif user_input == '2':
    test_words()
  elif user_input == '3':
    summarize_vocabulary()
  elif user_input == '4':
    print('******************** TEST GRAMMAR MENU *********************')
    print('1. Declension of definite article')
    print('************************************************************')
      
    grammar_test_input = input()

    if grammar_test_input == '1':
      test_definite_article()
