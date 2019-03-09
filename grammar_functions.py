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

def test_weak_verb_present_tense():

  first_singular = input('Enter the first person singular form of "leben": ')
  second_singular = input('... the second person singular form of "leben": ')
  third_singular = input('... third person singular ...: ')
  first_plural = input('first person plural: ')
  second_plural = input('second person plural: ')
  third_plural = input('third person plural: ')  
  second_formal = input('second person formal: ')

  score = 7.0

  if first_singular != 'lebe':
    print('The first person singular past of "leben" is "lebe". You entered "' + first_singular + '".')
    score -= 1

  if second_singular != 'lebst':
    print('The second person singular past of "leben" is "lebst". You entered "' + second_singular + '".')
    score -= 1

  if third_singular != 'lebt':
    print('The third person singular past of "leben" is "lebt". You entered "' + third_singular + '".')
    score -= 1

  if first_plural != 'leben':
    print('The first person plural past of "leben" is "leben". You entered "' + first_plural + '".')
    score -= 1

  if second_plural != 'lebt':
    print('The second person plural past of "leben" is "lebt". You entered "' + second_plural + '".')
    score -= 1

  if third_plural != 'leben':
    print('The third person plural past of "leben" is "leben". You entered "' + third_plural + '".')
    score -= 1

  if second_formal != 'leben':
    print('The second person formal past of "leben" is "leben". You entered "' + second_formal + '".')
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

def test_adjective_strong_endings():
  masculine_nominative = input('Enter the strong masculine nominative form of the adjective "viel-": ')
  masculine_genitive = input('. . . strong masculine genitive form of the adjective "viel-": ')
  masculine_dative = input('. . . strong masculine dative form . . . "viel-": ')
  masculine_accusative = input('. . . masculine accusative form . . . "viel-": ')
  feminine_nominative = input('. . . feminine nominative . . . "viel-": ')
  feminine_genitive = input('. . . feminine genitive . . .: ')
  feminine_dative = input('feminine dative: ')
  feminine_accusative = input('feminine accusative: ')
  neuter_nominative = input('neuter nominative: ')
  neuter_genitive = input('neuter genitive: ')
  neuter_dative = input('neuter dative: ')
  neuter_accusative = input('neuter accusative: ')
  plural_nominative = input('plural nominative: ')
  plural_genitive = input('plural genitive: ')
  plural_dative = input('plural dative: ')
  plural_accusative = input('plural accusative: ')

  score = 16.0

  if masculine_nominative != 'vieler':
    print('The strong masculine nominative form of "viel-" is "vieler". You entered "' + masculine_nominative + '".')
    score -= 1

  if masculine_genitive != 'vielen':
    print('The strong masculine genitive form of "viel-" is "vielen". You entered "' + masculine_genitive + '".')
    score -= 1

  if masculine_dative != 'vielem':
    print('The strong masculine dative form of "viel-" is "vielem". You entered "' + masculine_dative + '".')
    score -= 1

  if masculine_accusative != 'vielen':
    print('The strong masculine accusative form of "viel-" is "vielen". You entered "' + masculine_accusative + '".')
    score -= 1

  if feminine_nominative != 'viele':
    print('The strong feminine nominative form of "viel-" is "viele". You entered "' + feminine_nominative + '".')
    score -= 1

  if feminine_genitive != 'vieler':
    print('The strong feminine genitive form of "viel-" is "vieler". You entered "' + feminine_genitive + '".')
    score -= 1

  if feminine_dative != 'vieler':
    print('The strong feminine dative form of "viel-" is "vieler". You entered "' + feminine_dative + '".')
    score -= 1

  if feminine_accusative != 'viele':
    print('The strong feminine accusative form of "viel-" is "viele". You entered "' + feminine_accusative + '".')
    score -= 1

  if neuter_nominative != 'vieles':
    print('The strong neuter nominative form of "viel-" is "vieles". You entered "' + neuter_nominative + '".')
    score -= 1

  if neuter_genitive != 'vielen':
    print('The strong neuter genitive form of "viel-" is "vielen". You entered "' + neuter_genitive + '".')
    score -= 1

  if neuter_dative != 'vielem':
    print('The strong neuter dative form of "viel-" is "vielem". You entered "' + neuter_dative + '".')
    score -= 1

  if neuter_accusative != 'vieles':
    print('The strong neuter accusative form of "viel-" is "vieles". You entered "' + neuter_accusative + '".')
    score -= 1

  if plural_nominative != 'viele':
    print('The strong plural nominative form of "viel-" is "viele". You entered "' + plural_nominative + '".')
    score -= 1

  if plural_genitive != 'vieler':
    print('The strong plural genitive form of "viel-" is "vieler". You entered "' + plural_genitive + '".')
    score -= 1

  if plural_dative != 'vielen':
    print('The strong plural dative form of "viel-" is "vielen". You entered "' + plural_dative + '".')
    score -= 1

  if plural_accusative != 'viele':
    print('The strong plural accusative form of "viel-" is "viele". You entered "' + plural_accusative + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 16, for a score of ' + str(int(score/16.0 * 100)) + '%.')

def test_adjective_weak_endings():
  masculine_nominative = input('Enter the weak masculine nominative form of the adjective "viel-": ')
  masculine_genitive = input('. . . weak masculine genitive form of the adjective "viel-": ')
  masculine_dative = input('. . . weak masculine dative form . . . "viel-": ')
  masculine_accusative = input('. . . masculine accusative form . . . "viel-": ')
  feminine_nominative = input('. . . feminine nominative . . . "viel-": ')
  feminine_genitive = input('. . . feminine genitive . . .: ')
  feminine_dative = input('feminine dative: ')
  feminine_accusative = input('feminine accusative: ')
  neuter_nominative = input('neuter nominative: ')
  neuter_genitive = input('neuter genitive: ')
  neuter_dative = input('neuter dative: ')
  neuter_accusative = input('neuter accusative: ')
  plural_nominative = input('plural nominative: ')
  plural_genitive = input('plural genitive: ')
  plural_dative = input('plural dative: ')
  plural_accusative = input('plural accusative: ')

  score = 16.0

  if masculine_nominative != 'viele':
    print('The weak masculine nominative form of "viel-" is "viele". You entered "' + masculine_nominative + '".')
    score -= 1

  if masculine_genitive != 'vielen':
    print('The weak masculine genitive form of "viel-" is "vielen". You entered "' + masculine_genitive + '".')
    score -= 1

  if masculine_dative != 'vielen':
    print('The weak masculine dative form of "viel-" is "vielen". You entered "' + masculine_dative + '".')
    score -= 1

  if masculine_accusative != 'vielen':
    print('The weak masculine accusative form of "viel-" is "vielen". You entered "' + masculine_accusative + '".')
    score -= 1

  if feminine_nominative != 'viele':
    print('The weak feminine nominative form of "viel-" is "viele". You entered "' + feminine_nominative + '".')
    score -= 1

  if feminine_genitive != 'vielen':
    print('The weak feminine genitive form of "viel-" is "vielen". You entered "' + feminine_genitive + '".')
    score -= 1

  if feminine_dative != 'vielen':
    print('The weak feminine dative form of "viel-" is "vielen". You entered "' + feminine_dative + '".')
    score -= 1

  if feminine_accusative != 'viele':
    print('The weak feminine accusative form of "viel-" is "viele". You entered "' + feminine_accusative + '".')
    score -= 1

  if neuter_nominative != 'viele':
    print('The weak neuter nominative form of "viel-" is "viele". You entered "' + neuter_nominative + '".')
    score -= 1

  if neuter_genitive != 'vielen':
    print('The weak neuter genitive form of "viel-" is "vielen". You entered "' + neuter_genitive + '".')
    score -= 1

  if neuter_dative != 'vielen':
    print('The weak neuter dative form of "viel-" is "vielen". You entered "' + neuter_dative + '".')
    score -= 1

  if neuter_accusative != 'viele':
    print('The weak neuter accusative form of "viel-" is "viele". You entered "' + neuter_accusative + '".')
    score -= 1

  if plural_nominative != 'vielen':
    print('The weak plural nominative form of "viel-" is "vielen". You entered "' + plural_nominative + '".')
    score -= 1

  if plural_genitive != 'vielen':
    print('The weak plural genitive form of "viel-" is "vielen". You entered "' + plural_genitive + '".')
    score -= 1

  if plural_dative != 'vielen':
    print('The weak plural dative form of "viel-" is "vielen". You entered "' + plural_dative + '".')
    score -= 1

  if plural_accusative != 'vielen':
    print('The weak plural accusative form of "viel-" is "vielen". You entered "' + plural_accusative + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 16, for a score of ' + str(int(score/16.0 * 100)) + '%.')

def test_first_person_personal_pronoun():
  nominative_singular = input('Enter the first person nominative singular personal pronoun: ')
  genitive_singular = input('Enter the first person genitive singular . . .: ')
  dative_singular = input('. . . first person dative singular . . .: ')
  accusative_singular = input('First person accusative singular: ')
  nominative_plural = input('First person nominative plural: ')
  genitive_plural = input('First person genitive plural: ')
  dative_plural = input('First person dative plural: ')
  accusative_plural = input('First person accusative plural: ')

  score = 8.0

  if nominative_singular != 'ich':
    print('The first person nominative singular personal pronoun is "ich". You entered "' + nominative_singular + '".')
    score -= 1

  if genitive_singular != 'meiner':
    print('The first person genitive singular personal pronoun is "meiner". You entered "' + genitive_singular + '".')
    score -= 1

  if dative_singular != 'mir':
    print('The first person dative singular personal pronoun is "mir". You entered "' + dative_singular + '".')
    score -= 1

  if accusative_singular != 'mich':
    print('The first person accusative singular personal pronoun is "mich". You entered "' + accusative_singular + '".')
    score -= 1

  if nominative_plural != 'wir':
    print('The first person nominative plural personal pronoun is "wir". You entered "' + nominative_plural + '".')
    score -= 1

  if genitive_plural != 'unser':
    print('The first person genitive plural personal pronoun is "unser". You entered "' + genitive_plural + '".')
    score -= 1

  if dative_plural != 'uns':
    print('The first person dative plural personal pronoun is "uns". You entered "' + dative_plural + '".')
    score -= 1

  if accusative_plural != 'uns':
    print('The first person accusative plural personal pronoun is "uns". You entered "' + accusative_plural + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 8, for a score of ' + str(int(score/8.0 * 100)) + '%.')

def test_second_person_personal_pronoun():
  nominative_singular = input('Enter the second person nominative singular personal pronoun: ')
  genitive_singular = input('Enter the second person genitive singular . . .: ')
  dative_singular = input('. . . second person dative singular . . .: ')
  accusative_singular = input('Second person accusative singular: ')
  nominative_plural = input('Second person nominative plural: ')
  genitive_plural = input('Second person genitive plural: ')
  dative_plural = input('Second person dative plural: ')
  accusative_plural = input('Second person accusative plural: ')
  nominative_formal = input('Second person nominative formal: ')
  genitive_formal = input('Second person genitive formal: ')
  dative_formal = input('Second person dative formal: ')
  accusative_formal = input('Second person accusative formal: ')

  score = 12.0

  if nominative_singular != 'du':
    print('The second person nominative singular personal pronoun is "du". You entered "' + nominative_singular + '".')
    score -= 1

  if genitive_singular != 'deiner':
    print('The second person genitive singular personal pronoun is "deiner". You entered "' + genitive_singular + '".')
    score -= 1

  if dative_singular != 'dir':
    print('The second person dative singular personal pronoun is "dir". You entered "' + dative_singular + '".')
    score -= 1

  if accusative_singular != 'dich':
    print('The second person accusative singular personal pronoun is "dich". You entered "' + accusative_singular + '".')
    score -= 1

  if nominative_plural != 'ihr':
    print('The second person nominative plural personal pronoun is "ihr". You entered "' + nominative_plural + '".')
    score -= 1

  if genitive_plural != 'euer':
    print('The second person genitive plural personal pronoun is "euer". You entered "' + genitive_plural + '".')
    score -= 1

  if dative_plural != 'euch':
    print('The second person dative plural personal pronoun is "euch". You entered "' + dative_plural + '".')
    score -= 1

  if accusative_plural != 'euch':
    print('The second person accusative plural personal pronoun is "euch". You entered "' + accusative_plural + '".')
    score -= 1

  if nominative_formal != 'Sie':
    print('The second person nominative formal personal pronoun is "Sie". You entered "' + nominative_formal + '".')
    score -= 1

  if genitive_formal != 'Ihrer':
    print('The second person genitive formal personal pronoun is "Ihrer". You entered "' + genitive_formal + '".')
    score -= 1

  if dative_formal != 'Ihnen':
    print('The second person dative formal personal pronoun is "Ihnen". You entered "' + dative_formal + '".')
    score -= 1

  if accusative_formal != 'Sie':
    print('The second person accusative formal personal pronoun is "Sie". You entered "' + accusative_formal + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 12, for a score of ' + str(int(score/12.0 * 100)) + '%.')

def test_third_person_personal_pronoun():
  masculine_nominative = input('Enter the third person masculine nominative personal pronoun: ')
  masculine_genitive = input('Enter the third person masculine genitive . . .: ')
  masculine_dative = input('. . . third person masculine dative . . .: ')
  masculine_accusative = input('Third person masculine accusative: ')
  feminine_nominative = input('Third person feminine nominative: ')
  feminine_genitive = input('Third person feminine genitive: ')
  feminine_dative = input('Third person feminine dative: ')
  feminine_accusative = input('Third person feminine accusative: ')
  neuter_nominative = input('Third person neuter nominative: ')
  neuter_genitive = input('Third person neuter genitive: ')
  neuter_dative = input('Third person neuter dative: ')
  neuter_accusative = input('Third person neuter accusative: ')
  plural_nominative = input('Third person plural nominative: ')
  plural_genitive = input('Third person plural genitive: ')
  plural_dative = input('Third person plural dative: ')
  plural_accusative = input('Third person plural accusative: ')

  score = 16.0

  if masculine_nominative != 'er':
    print('The third person masculine nominative personal pronoun is "er". You entered "' + masculine_nominative + '".')
    score -= 1

  if masculine_genitive != 'seiner':
    print('The third person masculine genitive personal pronoun is "seiner". You entered "' + masculine_genitive + '".')
    score -= 1

  if masculine_dative != 'ihm':
    print('The third person masculine dative personal pronoun is "ihm". You entered "' + masculine_dative + '".')
    score -= 1

  if masculine_accusative != 'ihn':
    print('The third person masculine accusative personal pronoun is "ihn". You entered "' + masculine_accusative + '".')
    score -= 1

  if feminine_nominative != 'sie':
    print('The third person feminine nominative personal pronoun is "sie". You entered "' + feminine_nominative + '".')
    score -= 1

  if feminine_genitive != 'ihrer':
    print('The third person feminine genitive personal pronoun is "ihrer". You entered "' + feminine_genitive + '".')
    score -= 1

  if feminine_dative != 'ihr':
    print('The third person feminine dative personal pronoun is "ihr". You entered "' + feminine_dative + '".')
    score -= 1

  if feminine_accusative != 'sie':
    print('The third person feminine accusative personal pronoun is "sie". You entered "' + feminine_accusative + '".')
    score -= 1

  if neuter_nominative != 'es':
    print('The third person neuter nominative personal pronoun is "es". You entered "' + neuter_nominative + '".')
    score -= 1

  if neuter_genitive != 'seiner':
    print('The third person neuter genitive personal pronoun is "seiner". You entered "' + neuter_genitive + '".')
    score -= 1

  if neuter_dative != 'ihm':
    print('The third person neuter dative personal pronoun is "ihm". You entered "' + neuter_dative + '".')
    score -= 1

  if neuter_accusative != 'es':
    print('The third person neuter accusative personal pronoun is "es". You entered "' + neuter_accusative + '".')
    score -= 1

  if plural_nominative != 'sie':
    print('The third person plural nominative personal pronoun is "sie". You entered "' + plural_nominative + '".')
    score -= 1

  if plural_genitive != 'ihrer':
    print('The third person plural genitive personal pronoun is "ihrer". You entered "' + plural_genitive + '".')
    score -= 1

  if plural_dative != 'ihnen':
    print('The third person plural dative personal pronoun is "ihnen". You entered "' + plural_dative + '".')
    score -= 1

  if plural_accusative != 'sie':
    print('The third person plural accusative personal pronoun is "sie". You entered "' + plural_accusative + '".')
    score -= 1

  print ('\n')
  print('You got ' + str(int(score)) + ' correct out of 16, for a score of ' + str(int(score/16.0 * 100)) + '%.')
