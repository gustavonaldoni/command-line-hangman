def print_meanings(word, meanings):
    print()
    print(f' == "{word.upper()}" DEFINITION ==')
    print()
    
    all_values = ''

    for key, values in meanings.items():
        for value in values:
            all_values += f'{value} - '

        print(f'{key.title()} : {all_values}')
        print()

    print()
