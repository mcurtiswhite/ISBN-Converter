# Import function modules.
import isbn_format

# The convert10 function converts the ISBN-10 to an ISBN-13.
def convert10(num):
    # Declare local variables.
    num_list = [9, 7, 8]
    check_digit = 0
    weight = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    weighted_sum = 0
    converting_to = '13'
    isbn = ''

    # Loop to convert ISBN-10 string into an integer list, excluding the
    # check digit.
    for i in num[:-1]:
        # Append each character as an integer to the list so they can be
        # calculated.
        num_list.append(int(i))

    # Loop to calculate weighted sum.
    for value in range(len(num_list)):
        # Multiply value by value in each list and add to accumulator.  
        weighted_sum += num_list[value] * weight[value]

    # Calculate the check digit.
    remainder = weighted_sum % 10
    if remainder != 0:
        check_digit = 10 - remainder
    else:
        check_digit = remainder

    check_digit, num, num_list, isbn, converting_to = \
                 conversion(check_digit, num, num_list, isbn, converting_to)

    # Return the ISBN-13.
    return isbn

# The convert13 function converts the ISBN-13 to an ISBN-10.
def convert13(num):
    # Declare local variables.
    num_list = []
    new_list = []
    check_digit = 0
    weight = 0
    weighted_sum = 0
    converting_to = '10'
    isbn = ''

    # Loop to convert ISBN-13 string into an integer list, excluding the
    # first 3 digits and the check digit check digit.
    for i in num[3:-1]:
        # Append each character as an integer to the list so they can be
        # calculated.
        num_list.append(int(i))

    # Loop to calculate weighted sum.
    for value in num_list:
        # Add one to weight for each iteration.
        weight += 1
        # Multiply value and weight and add to accumulator.
        weighted_sum += value * weight

    # Calculate the check digit from weighted sum.
    check_digit = weighted_sum % 11
    # Convert check digit to Romun numeral X if equal to 10.
    if check_digit == 10:
        check_digit = 'X'

    check_digit, num, num_list, isbn, converting_to = \
                 conversion(check_digit, num, num_list, isbn, converting_to)

    # Return the ISBN-13.
    return isbn

# Conversion function for formatting and displaying the conversion.
def conversion(check, orig, lst, new, ver):
    # Append the check digit to the list.
    lst.append(check)
    
    # Loop to convert the list to a string.
    for x in lst:
        new += ''.join(str(x))

    # Call the isbn_format function to format ISBN numbers for display.
    if ver == '10':
        new_pr, orig_pr = isbn_format.hyphenate(new, orig)
    elif ver == '13':
        orig_pr, new_pr = isbn_format.hyphenate(orig, new)
    
    # Display the conversion.
    print()
    print('******** CONVERSION RESULTS *********')
    print('The ISBN-' + ver + ' for ' + orig_pr + ' is ' + new_pr + '.')
    print()
    print()

    # Return variables.
    return check, orig, lst, new, ver
