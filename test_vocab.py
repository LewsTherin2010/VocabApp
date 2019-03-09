import sys

sys.path.append('.\\')

from vocab_functions import *
from grammar_functions import *

# *******************************************************************
# *************************** MENU FUNCTIONS ************************
# *******************************************************************

def test_grammar():
  grammar_test_input = -1
  while grammar_test_input != '99':

    print('******************** TEST GRAMMAR MENU *********************')
    print('0. Adjectives')
    print('1. Definite article')
    print('2. Indefinite article')
    print('3. Weak Verbs')
    print('4. "sein"')
    print('5. "haben"')
    print('6. "werden"')
    print('7. Personal pronoun')
    print('99. Go back')
    print('************************************************************')
      
    grammar_test_input = input()

    if grammar_test_input == '0':
      test_adjectives()
    if grammar_test_input == '1':
      test_definite_article()
    if grammar_test_input == '2':
      test_indefinite_article()
    if grammar_test_input == '3':
      test_weak_verbs()
    if grammar_test_input == '4':
      test_sein()
    if grammar_test_input == '5':
      test_haben()
    if grammar_test_input == '6':
      test_werden()
    if grammar_test_input == '7':
      test_personal_pronoun()

def test_weak_verbs():
  test_weak_verbs_input = -1
  while test_weak_verbs_input != '99':

    print('****************** TEST WEAK VERBS MENU *******************')
    print('0. Present tense')
    print('1. Past tense')
    print('99. Go back')
    print('***********************************************************')
  
    test_weak_verbs_input = input()

    if test_weak_verbs_input == '0':
      test_weak_verb_present_tense()
    if test_weak_verbs_input == '1':
      test_weak_verb_past_tense()

def test_personal_pronoun():
  test_personal_pronoun_input = -1
  while test_personal_pronoun_input != '99':
    print('******************* TEST ADJECTIVES MENU *******************')
    print('1. First person')
    print('2. Second person')
    print('3. Third person')
    print('99. Go back')
    print('************************************************************')
    test_personal_pronoun_input = input()

    if test_personal_pronoun_input == '1':
      test_first_person_personal_pronoun()
    if test_personal_pronoun_input == '2':
      test_second_person_personal_pronoun()
    if test_personal_pronoun_input == '3':
      test_third_person_personal_pronoun()

def test_adjectives():
  test_adjectives_input = -1
  while test_adjectives_input != '99':
    print('******************* TEST ADJECTIVES MENU *******************')
    print('1. Strong endings')
    print('2. Weak endings')
    print('99. Go back')
    print('************************************************************')

    test_adjectives_input = input()

    if test_adjectives_input == '1':
      test_adjective_strong_endings()
    if test_adjectives_input == '2':
      test_adjective_weak_endings()      

def test_sein():
  test_sein_input = -1
  while test_sein_input != '99':
    print('******************** TEST "SEIN" MENU *********************')
    print('1. Present tense')
    print('2. Past tense')
    print('99. Go back')
    print('************************************************************')
    
    test_sein_input = input()

    if test_sein_input == '1':
      test_present_tense_sein()
    if test_sein_input == '2':
      test_past_tense_sein()

def test_haben():
  test_haben_input = -1
  while test_haben_input != '99':
    print('******************** TEST "HABEN" MENU *********************')
    print('1. Present tense')
    print('2. Past tense')
    print('99. Go back')
    print('************************************************************')
    
    test_haben_input = input()

    if test_haben_input == '1':
      test_present_tense_haben()
    if test_haben_input == '2':
      test_past_tense_haben()

def test_werden():
  test_werden_input = -1
  while test_werden_input != '99':
    print('******************** TEST "WERDEN" MENU *********************')
    print('1. Present tense')
    print('2. Past tense')
    print('99. Go back')
    print('*************************************************************')
    
    test_werden_input = input()

    if test_werden_input == '1':
      test_present_tense_werden()
    if test_werden_input == '2':
      test_past_tense_werden()

# *******************************************************************
# *************************** MAIN LOOP *****************************
# *******************************************************************

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
    words_to_test = int(input('How many words would you like to test? '))
    
    test_words(words_to_test)
  elif user_input == '3':
    summarize_vocabulary()
  elif user_input == '4':
    test_grammar()
