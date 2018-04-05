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

def test_indefinite_article():
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

  score = 12.0

  if masculine_nominative != 'ein':
    print('The masculine nominative form is "ein". You entered "' + masculine_nominative + '".')
    score -= 1.0

  if masculine_genitive != 'eines':
    print('The masculine genitive form is "eines". You entered "' + masculine_genitive + '".')
    score -= 1.0

  if masculine_dative != 'einem':
    print('The masculine dative form is "einem". You entered "' + masculine_dative + '".')
    score -= 1.0

  if masculine_accusative != 'einen':
    print('The masculine accusative form is "einen". You entered "' + masculine_accusative + '".')
    score -= 1.0

  if feminine_nominative != 'eine':
    print('The feminine nominative form is "eine". You entered "' + feminine_nominative + '".')
    score -= 1.0

  if feminine_genitive != 'einer':
    print('The feminine genitive form is "einer". You entered "' + feminine_genitive + '".')
    score -= 1.0

  if feminine_dative != 'einer':
    print('The feminine dative form is "einer". You entered "' + feminine_dative + '".')
    score -= 1.0

  if feminine_accusative != 'eine':
    print('The feminine accusative form is "eine". You entered "' + feminine_accusative + '".')
    score -= 1.0

  if neuter_nominative != 'ein':
    print('The neuter nominative form is "ein". You entered "' + neuter_nominative + '".')
    score -= 1.0

  if neuter_genitive != 'eines':
    print('The neuter genitive form is "eines". You entered "' + neuter_genitive + '".')
    score -= 1.0

  if neuter_dative != 'einem':
    print('The neuter dative form is "einem". You entered "' + neuter_dative + '".')
    score -= 1.0

  if neuter_accusative != 'ein':
    print('The neuter accusative form is "ein". You entered "' + neuter_accusative + '".')
    score -= 1.0

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 12, for a score of ' + str(int(score/12.0 * 100)) + '%.')

def test_weak_verb_past_tense():

  first_singular = input('Enter the first person singular form of "leben": ')
  second_singular = input('... the second person singular form of "leben": ')
  third_singular = input('... third person singular ...: ')
  first_plural = input('first person plural: ')
  second_plural = input('second person plural: ')
  third_plural = input('third person plural: ')  
  second_formal = input('second person formal: ')

  score = 7.0

  if first_singular != 'lebte':
    print('The first person singular past of "leben" is "lebte". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'lebtest':
    print('The second person singular past of "leben" is "lebtest". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'lebte':
    print('The third person singular past of "leben" is "lebte". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'lebten':
    print('The first person plural past of "leben" is "lebten". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'lebtet':
    print('The second person plural past of "leben" is "lebtet". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'lebten':
    print('The third person plural past of "leben" is "lebten". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'lebten':
    print('The second person formal past of "leben" is "lebten". You entered "' + second_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 7, for a score of ' + str(int(score/7.0 * 100)) + '%.')

def test_past_tense_sein():
  first_singular = input('Enter the first person singular past form of "sein": ')
  second_singular = input('... the second person singular past form of "sein": ')
  third_singular = input('... third person singular past ...: ')
  first_plural = input('first person plural past: ')
  second_plural = input('second person plural past: ')
  third_plural = input('third person plural past: ')  
  second_formal = input('second person formal past: ')

  score = 7.0

  if first_singular != 'war':
    print('The first person singular past of "sein" is "war". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'warst':
    print('The second person singular past of "sein" is "warst". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'war':
    print('The third person singular past of "sein" is "war". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'waren':
    print('The first person plural past of "sein" is "waren". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'wart':
    print('The second person plural past of "sein" is "wart". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'waren':
    print('The third person plural past of "sein" is "waren". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'waren':
    print('The second person formal past of "sein" is "waren". You entered "' + second_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 7, for a score of ' + str(int(score/7.0 * 100)) + '%.')

def test_present_tense_sein():
  first_singular = input('Enter the first person singular present form of "sein": ')
  second_singular = input('... the second person singular present form of "sein": ')
  third_singular = input('... third person singular present ...: ')
  first_plural = input('first person plural present: ')
  second_plural = input('second person plural present: ')
  third_plural = input('third person plural present: ')  
  second_formal = input('second person formal present: ')

  score = 7.0

  if first_singular != 'bin':
    print('The first person singular present of "sein" is "bin". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'bist':
    print('The second person singular present of "sein" is "bist". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'ist':
    print('The third person singular present of "sein" is "ist". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'sind':
    print('The first person plural present of "sein" is "sind". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'seid':
    print('The second person plural present of "sein" is "seid". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'sind':
    print('The third person plural present of "sein" is "sind". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'sind':
    print('The second person formal present of "sein" is "sind". You entered "' + second_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 7, for a score of ' + str(int(score/7.0 * 100)) + '%.')

def test_past_tense_haben():
  first_singular = input('Enter the first person singular past form of "haben": ')
  second_singular = input('... the second person singular past form of "haben": ')
  third_singular = input('... third person singular past...: ')
  first_plural = input('first person plural past: ')
  second_plural = input('second person plural past: ')
  third_plural = input('third person plural past: ')  
  second_formal = input('second person formal past: ')

  score = 7.0

  if first_singular != 'hatte':
    print('The first person singular past of "haben" is "hatte". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'hattest':
    print('The second person singular past of "haben" is "hattest". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'hatte':
    print('The third person singular past of "haben" is "hatte". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'hatten':
    print('The first person plural past of "haben" is "hatten". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'hattet':
    print('The second person plural past of "haben" is "hattet". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'hatten':
    print('The third person plural past of "haben" is "hatten". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'hatten':
    print('The second person formal past of "haben" is "hatten". You entered "' + second_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 7, for a score of ' + str(int(score/7.0 * 100)) + '%.')

def test_present_tense_haben():

  first_singular = input('Enter the first person singular present form of "haben": ')
  second_singular = input('... the second person singular present form of "haben": ')
  third_singular = input('... third person singular present...: ')
  first_plural = input('first person plural present: ')
  second_plural = input('second person plural present: ')
  third_plural = input('third person plural present: ')  
  second_formal = input('second person formal present: ')

  score = 7.0

  if first_singular != 'habe':
    print('The first person singular present of "haben" is "habe". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'hast':
    print('The second person singular present of "haben" is "hast". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'hat':
    print('The third person singular present of "haben" is "hat". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'haben':
    print('The first person plural present of "haben" is "haben". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'habt':
    print('The second person plural present of "haben" is "habt". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'haben':
    print('The third person plural present of "haben" is "haben". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'haben':
    print('The second person formal present of "haben" is "haben". You entered "' + second_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 7, for a score of ' + str(int(score/7.0 * 100)) + '%.')

def test_past_tense_werden():
  first_singular = input('Enter the first person singular past form of "werden": ')
  second_singular = input('... the second person singular past form of "werden": ')
  third_singular = input('... third person singular past...: ')
  first_plural = input('first person plural past: ')
  second_plural = input('second person plural past: ')
  third_plural = input('third person plural past: ')  
  second_formal = input('second person formal past: ')

  score = 7.0

  if first_singular != 'wurde':
    print('The first person singular past of "werden" is "wurde". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'wurdest':
    print('The second person singular past of "werden" is "wurdest". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'wurde':
    print('The third person singular past of "werden" is "wurde". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'wurden':
    print('The first person plural past of "werden" is "wurden". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'wurdet':
    print('The second person plural past of "werden" is "wurdet". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'wurden':
    print('The third person plural past of "werden" is "wurden". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'wurden':
    print('The second person formal past of "werden" is "wurden". You entered "' + second_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 7, for a score of ' + str(int(score/7.0 * 100)) + '%.')

def test_present_tense_werden():
  first_singular = input('Enter the first person singular present form of "werden": ')
  second_singular = input('... the second person singular present form of "werden": ')
  third_singular = input('... third person singular present...: ')
  first_plural = input('first person plural present: ')
  second_plural = input('second person plural present: ')
  third_plural = input('third person plural present: ')  
  second_formal = input('second person formal present: ')

  score = 7.0

  if first_singular != 'werde':
    print('The first person singular present of "werden" is "werde". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'wirst':
    print('The second person singular present of "werden" is "wirst". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'wird':
    print('The third person singular present of "werden" is "wird". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'werden':
    print('The first person plural present of "werden" is "werden". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'werdet':
    print('The second person plural present of "werden" is "werdet". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'werden':
    print('The third person plural present of "werden" is "werden". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'werden':
    print('The second person formal present of "werden" is "werden". You entered "' + second_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 7, for a score of ' + str(int(score/7.0 * 100)) + '%.')
