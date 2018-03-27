import time
import os.path
from shutil import copyfile

def get_local_copy_of_dictionary():
  # Declare variable
  local_copy = dict()
  
  # Make sure dictionary exists.
  if os.path.isfile('./dictionary/dictionary.csv'):
    f = open('./dictionary/dictionary.csv', 'r')
  else:
    f = open('./dictionary/dictionary.csv', 'w+')

  # Read in all info in dictionary
  for line in f.readlines():
    line_elements = line.split(',')
    line_elements[4] = line_elements[4][:-1] # get rid of newline

    # There may be more than one definition for a word
    if line_elements[0].replace('*^*', ',') not in local_copy:
      local_copy[line_elements[0].replace('*^*', ',')] = [] # Initialize entry
    
    local_copy[line_elements[0].replace('*^*', ',')].append([line_elements[1].replace('*^*', ','), line_elements[2].replace('*^*', ','), line_elements[3], line_elements[4]])

  # Close file
  f.close()

  # Return dict
  return local_copy

def add_entry_to_dict(dictionary, word, definition, example_phrase, record_time = time.time(), successful_attempts = 0):
  if word not in dictionary:
    dictionary[word] = []
    dictionary[word].append([definition, example_phrase, record_time, successful_attempts])

  else: # make sure the definition is unique
    definition_exists = False

    for entry in dictionary[word]:
      if entry[0] == definition:
        definition_exists = True

    if not definition_exists:
      dictionary[word].append([definition, example_phrase, record_time, successful_attempts])

# ***********************************************************************************
# This function inserts a new line in the dictionary, with the following format:
# [WORD], [DEFINITION], [EXAMPLE PHRASE], [TIMESTAMP], [# OF SUCCESSFUL TESTS]NEWLINE
# ***********************************************************************************
def insert_new_word (word, definition, example_phrase):

  # Get local copy
  local_copy = get_local_copy_of_dictionary()

  # Add new item to local copy
  add_entry_to_dict(local_copy, word, definition, example_phrase)

  # Make a backup of the original dictionary
  copyfile('./dictionary/dictionary.csv', './backups/dictionary_backup.csv')

  # Rewrite the file with the new entry
  f = open('./dictionary/dictionary.csv', 'w')
  
  for entry in sorted(local_copy):
    for definition in local_copy[entry]:
      # Comma handling occurs here.
      f.write(entry.replace(',', '*^*') + ',' + definition[0].replace(',', '*^*') + ',' + definition[1].replace(',', '*^*') + ',' + str(definition[2]) + ',' + str(definition[3]) + '\n') # START HERE

  f.close()

# ********************************************************************************
# This function expects two parameters. 'Word' is just the word being tested.
# 'Entry' is a dict of the following format:
#
# { word : 
#   [
#     [definition1, sample_phrase1, # of successful tests, timestamp]
#     ,[definition2, sample_phrase1, # of successful tests, timestamp]
#     ...
#   ]
# }
#
# It will conduct a mini-exam, edit the dict based on the user's response, and 
# return the edited dict.
# ********************************************************************************
def test_word(word, entry):

  number_of_definitions = len(entry)

  if len(entry) == 1:
    print('The word is \'' + word + '\' and 1 definition will be tested.' + '\n')
  else:
    print('The word is \'' + word + '\' and ' + str(number_of_definitions) + ' definitions will be tested.' + '\n\n')

  for definition in entry:
    input('Define \'' + word + '\', as in \'' + definition[1] + '\'. Press enter to read the answer.')

    print('****\'' + word + '\' means \'' + definition[0] + '\'.****')
    result = input('Did you get it right? Be honest. Enter \'y\' if you did, or \'n\' if you didn\'t.')

    if result == 'y':
      definition[3] = str(int(definition[3]) + 1)
    elif result == 'n':
      definition[3] = 0
    else:
      result = input('I didn\'t understand your input. Please type \'y\' or \'n\'.')

      if result == 'y':
        definition[3] = str(int(definition[3]) + 1)
      elif result == 'n':
        definition[3] = 0
      else:
        print('If you have Parkinson\'s and your hands shake, please find another app. Otherwise, learn to read English. You fail this entry.')
        definition[3] = 0

    definition[2] = time.time()
    print('-----------------------------------------------')

  return entry

def test_words(number_to_test = -1):
  local_copy = get_local_copy_of_dictionary()
  words_to_test = {}  

  one_day = 60 * 60 * 24

  # Compile a list of words to test.
  i = 0
  for word in local_copy:
    for entry in local_copy[word]:
      if number_to_test == -1 or i < number_to_test:
        if int(float(entry[2])) + (one_day * int(entry[3])) < time.time():
          add_entry_to_dict(words_to_test, word, entry[0], entry[1], entry[2], entry[3])
          i += 1

  # Test every word
  for word in words_to_test:
    # Test every word
    tested_entry = test_word(word, words_to_test[word])
    
    # Edit the local copy of the dictionary.
    i = 0
    for definition in tested_entry:
      j = 0
      for original_entry in local_copy[word]:
        if definition[0] == original_entry[0]: # If the definitions match
          local_copy[word][j][2] = definition[2]
          local_copy[word][j][3] = definition[3]
        j += 1
      i += 1

  # Make a backup of the original dictionary
  copyfile('./dictionary/dictionary.csv', './backups/dictionary_backup.csv')

  # Rewrite the file with the new entry
  f = open('./dictionary/dictionary.csv', 'w')
  
  for entry in sorted(local_copy):
    for definition in local_copy[entry]:
      f.write(entry.replace(',', '*^*') + ',' + definition[0].replace(',', '*^*') + ',' + definition[1].replace(',', '*^*') + ',' + str(definition[2]) + ',' + str(definition[3]) + '\n') # START HERE

  f.close()

def prompt_user_for_new_entry():
  word = input('Please enter the German word.')
  definition = input('Please enter its definition.')
  example_phrase = input('Please enter an example phrase.')

  insert_new_word(word, definition, example_phrase)

def summarize_vocabulary():
  local_copy = get_local_copy_of_dictionary()

  day_dict = {}

  # Get summary
  for entry in local_copy:
    for definition in local_copy[entry]:
      if definition[3] not in day_dict:
        day_dict[definition[3]] = 0
      day_dict[definition[3]] += 1

  # Print summary
  print('\n------------------------')
  print ('Days','\t', '# of words')

  for day in sorted(day_dict):
    print (day, '\t', day_dict[day])
  print('------------------------')

def test_definite_article():
  masculine_nominative = input('Enter the masculine nominative form: ')
  masculine_genitive = input('... masculine genitive form: ')
  masculine_dative = input('... masculine dative ...: ')
  masculine_accusative = input('Masculine accusative: ')
  
  feminine_nominative = input('Feminine nominative: ')
  feminine_genitive = input('Feminine genitive: ')
  feminine_dative = input('Feminine dative: ')
  feminine_accusative = input('Feminine accusative: ')

  neuter_nominative = input('Neuter nominative: ')
  neuter_genitive = input('Neuter genitive: ')
  neuter_dative = input('Neuter dative: ')
  neuter_accusative = input('Neuter accusative: ')

  plural_nominative = input('Plural nominative: ')
  plural_genitive = input('Plural genitive: ')
  plural_dative = input('Plural dative: ')
  plural_accusative = input('Plural accusative: ')

  score = 16.0

  if masculine_nominative != 'der':
    print('The masculine nominative form is "der". You entered "' + masculine_nominative + '".')
    score -= 1.0

  if masculine_genitive != 'des':
    print('The masculine genitive form is "des". You entered "' + masculine_genitive + '".')
    score -= 1.0

  if masculine_dative != 'dem':
    print('The masculine dative form is "dem". You entered "' + masculine_dative + '".')
    score -= 1.0

  if masculine_accusative != 'den':
    print('The masculine accusative form is "den". You entered "' + masculine_accusative + '".')
    score -= 1.0

  if feminine_nominative != 'die':
    print('The feminine nominative form is "die". You entered "' + feminine_nominative + '".')
    score -= 1.0

  if feminine_genitive != 'der':
    print('The feminine genitive form is "der". You entered "' + feminine_genitive + '".')
    score -= 1.0

  if feminine_dative != 'der':
    print('The feminine dative form is "der". You entered "' + feminine_dative + '".')
    score -= 1.0

  if feminine_accusative != 'die':
    print('The feminine accusative form is "die". You entered "' + feminine_accusative + '".')
    score -= 1.0

  if neuter_nominative != 'das':
    print('The neuter nominative form is "das". You entered "' + neuter_nominative + '".')
    score -= 1.0

  if neuter_genitive != 'des':
    print('The neuter genitive form is "des". You entered "' + neuter_genitive + '".')
    score -= 1.0

  if neuter_dative != 'dem':
    print('The neuter dative form is "dem". You entered "' + neuter_dative + '".')
    score -= 1.0

  if neuter_accusative != 'das':
    print('The neuter accusative form is "das". You entered "' + neuter_accusative + '".')
    score -= 1.0

  if plural_nominative != 'die':
    print('The plural nominative form is "die". You entered "' + plural_nominative + '".')
    score -= 1.0

  if plural_genitive != 'der':
    print('The plural genitive form is "der". You entered "' + plural_genitive + '".')
    score -= 1.0

  if plural_dative != 'den':
    print('The plural dative form is "den". You entered "' + plural_dative + '".')
    score -= 1.0

  if plural_accusative != 'die':
    print('The plural accusative form is "die". You entered "' + plural_accusative + '".')
    score -= 1.0

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 16, for a score of ' + str(int(score/16.0 * 100)) + '%.')
