def is_sentence(string):
    if not(is_capital(string[0])):
        return False
    if not(is_sentence_terminator(string[-1])):
        return False

    quotation_mark_count = 0
    previous_character = string[0]
    digit_run = ""
    for character in string[1:-2]:
        if character == '.':
            return False
        
        if character == '"':
            quotation_mark_count += 1

        # Check that numbers less than 13 are spelled out
        if digit_run != "" and is_digit(character):
            digit_run += character
        elif digit_run != "" and is_less_than_thirteen(digit_run):
            return False
        else:
            digit_run = ""
        if digit_run == "" and is_digit(character):
            digit_run = character
            
        previous_character = character

    if quotation_mark_count % 2 != 0:
        return False
    
    return True
        

def is_capital(character):
    return (character >= 'A' and character <= 'Z')

def is_digit(character):
    return (character >= '0' and character <= '9')

def is_sentence_terminator(character):
    return (character == '.' or character == '!' or character == '?')

def is_less_than_thirteen(digit_run):
    numeric_value = int(digit_run)
    return numeric_value < 13

def test_is_sentence(string):
    print(string)
    print(is_sentence(string))
    
def main():
    test_is_sentence("A valid sentence.")
    test_is_sentence("an invalid sentence.")
    test_is_sentence("An invalid sentence")
    test_is_sentence("A \"valid\" sentence?")
    test_is_sentence("An \"invalid\"\" sentence.")
    test_is_sentence("A 12 invalid sentence.")
    test_is_sentence("A 13 valid sentence!")
    test_is_sentence("A 2 invalid sentence.")
    test_is_sentence("A 103 valid sentence.")

main()
