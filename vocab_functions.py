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
  words_to_test = 0
  words_to_test_tomorrow = 0
  words_to_test_the_day_after = 0
  one_day = 60 * 60 * 24

  # Get summary
  for entry in local_copy:
    for definition in local_copy[entry]:
      if definition[3] not in day_dict:
        day_dict[definition[3]] = 0

      # Get actual words to test right now
      if int(float(definition[2])) + (one_day * int(definition[3])) < time.time():
        words_to_test += 1

      # Get actual words to test tomorrow (Not actually this simple.)
      if int(float(definition[2])) + (one_day * int(definition[3])) < time.time() + one_day:
        words_to_test_tomorrow += 1

      # Get actual words to test tomorrow (Not actually this simple.)
      if int(float(definition[2])) + (one_day * int(definition[3])) < time.time() + one_day * 2:
        words_to_test_the_day_after += 1

      day_dict[definition[3]] += 1

  # Get total number
  total_number = 0
  for day in day_dict:
    total_number += day_dict[day]

  # Get average words tested per day
  average_words_tested_per_day = 0.0
  for day in day_dict:
    denominator = (float(day) if int(day) != 0 else 1.0)
    average_words_tested_per_day += float(day_dict[day])/denominator

  # Print summary
  print('\n------------------------------------')
  print('The total number of words is ' + str(total_number) + '.')
  print('Average words tested per day is ' + str(int(round(average_words_tested_per_day, 0))) + '.')
  print('Actual words to test is ' + str(words_to_test) + '.')
  print('Actual words to test tomorrow is ' + str(words_to_test_tomorrow) + '.')
  print('Actual words to test the day after is ' + str(words_to_test_the_day_after) + '.\n')

  print('Days','\t', '# of words')

  for day in sorted(day_dict):
    print (day, '\t', day_dict[day])
  print('------------------------------------')
