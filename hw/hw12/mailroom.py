# Revision Goals:
# done: more descriptive variable names
# done: fix idle print statement
# make clean pull request
# done: all-cap global variables, no need for my_local_variable
# done: full name with space for keys
# done: new data structure
# done: fixed extra loop bug by calling back main_menu()
# done: check for integer and negative number
#
# HW12 Goals:
# done: use dicts where appropriate
# done: write a full set of letters to everyone to individual files on disk
# see if you can use a dict to switch between the users selections
# done: Try to use a dict and the .format() method to do the letters

D_DONERS = {'John Smith': [320],
            'Mary Simpson': [100, 150, 200],
            'Chris Finch': [400],
            'Larry Bookman': [150, 200],
            'Victoria Black': [60]
            }

D_LETTERS = {'dear': 'Dear {},\n\n',
             'amount': 'Thank you so much for your kind donation of ${:.2f}. ',
             'org': 'We here at {} greatly appreciate it. ',
             'mission': 'Your money will go towards {}.\n\n',
             'finally': 'Thanks again,\n\n',
             'sender': '{}\n',
             'title': '{}\n'
             }

D_SENDERS = {'FHW': ['Jim Grant', 'Director, F.H.W.'],
             'HAP': ['Harry Johnson', 'Treasurer, H.A.P.']
             }

D_ORGS = {'FHW': ['the Foundation for Homeless Whales',
                  'creating new oceans on the moon for whales to live in'],
          'HAP': ['the Home of Abandoned Pennies',
                  'restoring the coins back to their original shine']
          }

# for now, only support one organization, by acronym
ORG = 'FHW'


def main_menu():
    text = ('\nWelcome to Mailroom Madness\n\n' +
            'Choose from the following:\n\n' +
            'T - Send a (T)hank you\n\n' +
            'R - Create a (R)eport\n\n' +
            "L - Generate letter for all donations\n\n"
            'quit - Quit the program\n\n> ')
    choice = input(text)
    if (choice == 'T') or (choice == 't'):
        thankyou()
        return True
    elif (choice == 'R') or (choice == 'r'):
        report(D_DONERS)
        return True
    elif (choice == 'L') or (choice == 'l'):
        letterForAll(D_ORGS, D_SENDERS, D_LETTERS, D_DONERS, ORG)
        return True
    elif (choice == 'quit'):
        return False
    else:
        return True


def thankyou():
    text = ('\nPlease enter a name, or choose from the following:\n\n' +
            'list - Print a list of previous donors\n\n' +
            'quit - Return to main menu\n\n> ')
    choice = input(text)
    if (choice == 'list'):
        list_name_pretty(D_DONERS)
    elif (choice == 'quit'):
        return
    else:
        names = list_name(D_DONERS)
        if (choice not in names):
            D_DONERS[choice] = []

        amount = take_donation()
        if (amount != 'quit'):
            D_DONERS[choice].append(amount)
            display_letter(D_ORGS, D_SENDERS, D_LETTERS, choice, amount, ORG)
    # always return to the main menu
    return True


def countall(d_doner):
    totals = {}
    counts = {}
    for doner, donations in d_doner.items():
        totals[doner] = sum(donations)
        counts[doner] = len(donations)
    return totals, counts


def report(d_doner):
    (totals, counts) = countall(d_doner)
    names = list_name(d_doner)
    header = '%s|%s |%s |%s\n\n%s\n' % ('Name'.center(20), 'Total'.rjust(10),
                                        '#'.rjust(3), 'Average'.rjust(10),
                                        '_' * 60)
    print(header)
    for doner in names:
        count = counts[doner]
        total = totals[doner]
        avg = total / count
        line = '{:<20}|{:>10} |{:3d} |{:>10}'.format(doner,
                                                     '${:.2f}'.format(total),
                                                     count,
                                                     '${:.2f}'.format(avg))
        print(line)
    input('\nPress Enter to Continue...\n\n> ')


def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def take_donation():
    while True:
        amount = input("\nPlease enter a donation amount or 'quit':\n\n> ")
        if (amount == 'quit'):
            return amount
        elif (is_number(amount) and int(amount) > 0):
            return int(amount)
        else:
            print('\nIncorrect number. Press try again')


def list_name(d_doner):
    names = set()
    for doner in d_doner:
        if doner not in names:
            names.add(doner)
    return names


def list_name_pretty(d_doner):
    """print doner names one per line"""
    for doner in list_name(d_doner):
        print(doner)
    input('\nPress Enter to Continue...\n\n> ')


def gen_letter(d_org, d_sender, d_letter, name, amount, org):
    sender = d_sender[org][0]
    title = d_sender[org][1]
    org_fullname = d_org[org][0]
    mission = d_org[org][1]
    text = (d_letter['dear'].format(name) +
            d_letter['amount'].format(float(amount)) +
            d_letter['org'].format(org_fullname) +
            d_letter['mission'].format(mission) +
            d_letter['finally'] +
            d_letter['sender'].format(sender) +
            d_letter['title'].format(title)
            )
    return(text)


def display_letter(d_org, d_sender, d_letter, name, amount, org):
    org = ORG
    text = gen_letter(d_org, d_sender, d_letter, name, amount, org)
    print(text)
    input('Press Enter to Continue...\n\n> ')


def save_letter(d_org, d_sender, d_letter, name, amount, seq, org):
    org = ORG
    text = gen_letter(d_org, d_sender, d_letter, name, amount, org)

    filename = '%s_%d.txt' % (name.replace(' ', '_'), seq)
    dir = 'letters'
    try:
        f = open((dir + '/' + filename), 'w')
    except IOError:
        return False
    else:
        f.write(text)
        f.close
        return True


def letterForAll(d_org, d_sender, d_letter, d_doner, org):
    for doner, donations in d_doner.items():
        seq = 0
        for amount in donations:
            save_letter(d_org, d_sender, d_letter, doner, amount, seq, org)
            seq += 1
    print("\n***Please find saved letters in 'letters' directory***")

ANSWER = True

if (__name__ == '__main__'):
    while ANSWER:
        ANSWER = main_menu()
        if not ANSWER:
            # exit the program
            break
