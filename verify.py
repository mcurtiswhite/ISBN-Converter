# The verify10 function verifies the check digit of an ISBN-10.
def verify10(num):
    # Declare local variables.
    num_list = []
    check_digit = 0
    correct_digit = 0
    weight = 0
    weighted_sum = 0
    isbn = ''

    # Loop to convert ISBN-10 string into an integer list, excluding the
    # check digit.
    for i in num[:-1]:
        # Append each character as an integer to the list so they can be
        # calculated.
        num_list.append(int(i))
    # Get the ISBN-10 check digit..
    check_digit = num[9]

    # Loop to calculate weighted sum.
    for value in num_list:
        # Add one to weight for each iteration.
        weight += 1
        # Multiply value and weight and add to accumulator.
        weighted_sum += value * weight

    # Calculate the remainder from the weighted sum.
    correct_digit = str(weighted_sum % 11)
    
    # If the correct digit is 10, change it to Roman numeral X.
    if correct_digit == '10':
        correct_digit = 'X'

    # Call the verification function to display and update the correct
    # check digit.
    check_digit, correct_digit, num_list, isbn = \
                 verification(check_digit, correct_digit, num_list, isbn)
    
    # Return the ISBN-10.
    return isbn

# The verify13 function verifies the check digit of an ISBN-13.
def verify13(num):
    # Declare local variables.
    num_list = []
    check_digit = 0
    correct_digit = 0
    weight = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    weighted_sum = 0
    isbn = ''

    # Loop to convert ISBN-13 string into an integer list, excluding the
    # check digit.
    for i in num[:-1]:
        # Append each character as an integer to the list so they can be
        # calculated.
        num_list.append(int(i))
    # Get the ISBN-13 check digit.
    check_digit = num[12]

    # Loop to calculate weighted sum.
    for value in range(len(num_list)):
        # Multiply value by value in each list and add to accumulator.  
        weighted_sum += num_list[value] * weight[value]

    # Calculate the remainder from the weighted sum.
    remainder = weighted_sum % 10

    # Calculate the correct check digit from the remainder.
    if remainder != 0:
        correct_digit = str(10 - remainder)
    else:
        correct_digit = str(remainder)

    # Call the verification function to display and update the correct
    # check digit.
    check_digit, correct_digit, num_list, isbn = \
                 verification(check_digit, correct_digit, num_list, isbn)

    # Return the ISBN-13.
    return isbn

# Verification function for verifying, displaying and updating the correct
# check digit.
def verification(check, correct, lst, number):
    print()
    print('******** CHECK DIGIT VERIFICATION *********')

    # Verify if check if check digit is correct and display result.        
    if check == correct:
        print('The check digit is correct!')
        print()
        print()
    else:
        print('The check digit is incorrect. Instead of ' + check +
              ', it should be ' + correct + '.')
        print('Updating ISBN with the correct check digit...')
        print()
        print()
        # Change check digit to correct digit.
        check = correct

    # Append the check digit to the list.
    lst.append(check)
        
    # Loop to convert list to string for return.
    for x in lst:
        number += ''.join(str(x))

    # Return variables.
    return check, correct, lst, number
