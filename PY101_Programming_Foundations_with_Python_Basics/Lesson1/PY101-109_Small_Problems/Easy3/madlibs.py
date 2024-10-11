def mad_lib():
    noun = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    adj = input('Enter an adjective: ')
    adverb = input('Enter an adverb: ')
    if isinstance(noun, str) and isinstance(verb, str) and isinstance(adj, str) and isinstance(adverb, str):
            print(f'Do you {verb} your {adj} {noun} {adverb}? That\'s hilarious!\n'+
                  f'The {adj} {noun} {verb} {adverb} over the lazy {noun}.\n'+
                  f'The {noun} {adverb} {verb} up to Joe\'s {adj} turtle.')
    else:
        print('Please use string values inputs')        
    return
mad_lib()