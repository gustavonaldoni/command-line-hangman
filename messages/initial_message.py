def calculate_spaces_to_put_string_on_center(base_string, string_to_calculate):
    result = (len(base_string) - len(string_to_calculate)) / 2

    return int(result)

def format_string_to_center(base_string, string_to_center):
    amount_of_spaces_needed = calculate_spaces_to_put_string_on_center(base_string, string_to_center)
    formatted_spaces_needed = ' ' * amount_of_spaces_needed

    resulted_string = f'{formatted_spaces_needed}{string_to_center}{formatted_spaces_needed}'

    return resulted_string

def show_inital_message(creator_name, company_name):
    initial_text = "==== WELCOME TO HANGMAN ===="
    middle_text = f'Created by {creator_name}'
    final_text = f'Powered by {company_name}'

    print()
    print(initial_text)
    print(format_string_to_center(initial_text, middle_text))
    print(format_string_to_center(initial_text, final_text))
    

if __name__ == '__main__':
    base_string_example = 'This is just a test string'
    string_to_calculate_example = 'AAAAAAA'

    print(base_string_example)
    print(format_string_to_center(base_string_example, string_to_calculate_example))