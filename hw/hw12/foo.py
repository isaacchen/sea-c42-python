def main_menu():
    text = ('\nWelcome to Mailroom Madness\n\n' +
            'Choose from the following:\n\n' +
            'T - Send a (T)hank you\n\n' +
            'R - Create a (R)eport\n\n' +
            "L - Generate letter for all donations\n\n"
            'quit - Quit the program\n\n> ')
    choice = input(text)
    if choice.lower() not in dispatch:
        return True
    else:
        result = dispatch[choice.lower()]()
        return result

#        report(D_DONERS)
#        letterForAll(D_ORGS, D_SENDERS, D_LETTERS, D_DONERS, ORG)


def thankyou():
    print('thank you sir')
    return True

foo = 'run a report'
bar = 'save all letters'


def report(foo):
    print(foo)


def do_report():
    print(foo)
    return True


def do_letterForAll(bar):
    print(bar)
    return True


def quit():
    return False


# define this after all callables are defined
dispatch = {'t': thankyou,
            'r': do_report,
            'l': do_letterForAll,
            'q': quit,
            'quit': quit
            }

ANSWER = True

while ANSWER:
    ANSWER = main_menu()
    if not ANSWER:
        # exit the program
        break
