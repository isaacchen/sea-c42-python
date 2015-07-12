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
# write a full set of letters to everyone to individual files on disk
# see if you can use a dict to switch between the users selections
# done: Try to use a dict and the .format() method to do the letters


doners = [['John Smith', 320],
          ['Mary Simpson', 100],
          ['Chris Finch', 400],
          ['Larry Bookman', 150],
          ['Victoria Black', 60],
          ['Mary Simpson', 150],
          ['Mary Simpson', 200],
          ['Larry Bookman', 200]]

# HW12 data structure
D_DONERS = {'John Smith': [320],
            'Mary Simpson': [100, 150, 200],
            'Chris Finch': [400],
            'Larry Bookman': [150, 200],
            'Victoria Black': [60]
            }


def main_menu():
    text = ('\nWelcome to Mailroom Madness\n\n' +
            'Choose from the following:\n\n' +
            'T - Send a (T)hank you\n\n' +
            'R - Create a (R)eport\n\n' +
            'quit - Quit the program\n\n> ')
    choice = input(text)
    if (choice == 'T') or (choice == 't'):
        hw12_thankyou()
        return True
    elif (choice == 'R') or (choice == 'r'):
        hw12_report(D_DONERS)
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
        list_name(doners)
    elif (choice == 'quit'):
        return
    else:
        found = find_name(doners, choice)
        # no difference if one nested list per transaction
        # since there is no partial list just for doner's name
        if (not found):
            amount = take_donation()
        else:
            amount = take_donation()
        if (amount != 'quit'):
            add_record(doners, choice, amount)
            print(letter(choice, amount))
            input('Press Enter to Continue...\n\n> ')
    # always return to the main menu
    return True


def hw12_thankyou():
    text = ('\nPlease enter a name, or choose from the following:\n\n' +
            'list - Print a list of previous donors\n\n' +
            'quit - Return to main menu\n\n> ')
    choice = input(text)
    if (choice == 'list'):
        hw12_list_name_pretty(D_DONERS)
    elif (choice == 'quit'):
        return
    else:
        names = hw12_list_name(D_DONERS)
        if (choice not in names):
            D_DONERS[choice] = []

        amount = take_donation()
        if (amount != 'quit'):
            D_DONERS[choice].append(amount)
            letter(choice, amount)
    # always return to the main menu
    return True


def countall(donerlist):
    my_count = {}
    my_names = set()
    my_total = {}
    for doner in donerlist:
        name_key = doner[0]
        my_amount = float(doner[1])
        if (name_key in my_names):
            my_count[name_key] = my_count[name_key] + 1
            my_total[name_key] = my_total[name_key] + my_amount
        else:
            my_names.add(name_key)
            my_count[name_key] = 1
            my_total[name_key] = my_amount
    return(my_count, my_names, my_total)


def hw12_countall(dict_doner):
    totals = {}
    counts = {}
    for doner, donations in dict_doner.items():
        totals[doner] = sum(donations)
        counts[doner] = len(donations)
    return totals, counts


def report(donerlist):
    my_count, my_names, my_total = countall(doners)
    header = ('Name'.center(20) + '|' +
              'Total'.rjust(10) + ' |' +
              '#'.rjust(4) + ' |' +
              'Average'.rjust(10) + '\n\n' + '_' * 60 + '\n')
    print(header)
    for k in my_names:
        n = k.ljust(20)
        c = str(my_count[k]).rjust(4)
        t = ('$' + format(my_total[k], '.2f')).rjust(10)
        avg = my_total[k] / my_count[k]
        a = ('$' + format(avg, '.2f')).rjust(10)
        line = (n + '|' + t + ' |' + c + ' |' + a)
        print(line)
    input('\nPress Enter to Continue...\n\n> ')


def hw12_report(dict_doner):
    (totals, counts) = hw12_countall(dict_doner)
    names = hw12_list_name(dict_doner)
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


def list_name(donerlist):
    namelist = []
    for doner in donerlist:
        if (doner[0] not in namelist):
            namelist.append(doner[0])
    print('')
    for i in namelist:
        print(i)
    input('\nPress Enter to Continue...\n\n> ')


def hw12_list_name(dict_doner):
    """HW12 version, read from dictionary and store into set"""
    names = set()
    for doner in dict_doner:
        if doner not in names:
            names.add(doner)
    return names


def hw12_list_name_pretty(dict_doner):
    """print doner names one per line"""
    for doner in hw12_list_name(dict_doner):
        print(doner)
    input('\nPress Enter to Continue...\n\n> ')


def find_name(donerlist, my_name):
    my_found = False
    for doner in donerlist:
        if (doner[0] == my_name):
            my_found = True
    return my_found


def add_record(donerlist, my_name, my_amount):
    record = [my_name, my_amount]
    donerlist = donerlist.append(record)


def letter(name, amount):
    text = ('Dear {},\n\n' +
            'Thank you so much for your kind donation of ${:.2f}' +
            '. We here at the Foundation for Homeless Whales greatly ' +
            'appreciate it. Your money will go towards creating new oceans ' +
            'on the moon for whales to live in.\n\n' +
            'Thanks again,\n\n' +
            'Jim Grant\n' +
            'Director, F.H.W.\n').format(name, float(amount))
    warn = '\nCannot write letter to disk. Press Enter to Continue...\n\n> '
    if write_letter(name, text):
        print(text)
        input('Press Enter to Continue...\n\n> ')
    else:
        input(warn)


def write_letter(name, text):
    filename = name.replace(' ', '_') + '.txt'
    try:
        f = open(filename, 'w')
    except IOError:
        return False
    else:
        f.write(text)
        f.close
        return True


ANSWER = True

if (__name__ == '__main__'):
    while ANSWER:
        ANSWER = main_menu()
        if not ANSWER:
            # exit the program
            break
