# The hyphenate function formats the ISBN numbers for display.
def hyphenate(ten, thirteen):
    # Format ISBN numbers for display.
    if ten[1] != '-':
        ten = ten[0] + '-' + ten[1:3] + '-' + ten[3:9] + '-' + ten[9]
    if thirteen[3] != '-':
        thirteen = thirteen[0:3] + '-' + thirteen[3] + '-' + thirteen[4:6] + \
        '-' + thirteen[6:12] + '-' + thirteen[12]

    # Return variables.
    return ten, thirteen
