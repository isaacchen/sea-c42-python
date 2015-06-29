doners = [['John Smith', 320],
          ['Mary Simpson', 100],
          ['Chris Finch', 400],
          ['Larry Bookman', 150],
          ['Victoria Black', 60],
          ['Mary Simpson', 150],
          ['Mary Simpson', 200],
          ['Larry Bookman', 200]]


def main_prompt():
    text = ('\nWelcome to Mailroom Madness\n\n' +
            'Choose from the following:\n\n' +
            'T - Send a (T)hank you\n\n' +
            'R - Create a (R)eport\n\n' +
            'quit - Quit the program\n\n> ')
    my_choice = input(text)
    if (my_choice == 'T') or (my_choice == 't'):
        thankyou()
    elif (my_choice == 'R') or (my_choice == 'r'):
        report(doners)
    elif (my_choice == 'quit'):
        answer = False
        return answer
    else:
        main_prompt()


def thankyou():
    text = ('\nPlease enter a name, or choose from the following:\n\n' +
            'list - Print a list of previous donors\n\n' +
            'quit - Return to main menu\n\n> ')
    my_name = input(text)
    if (my_name == 'list'):
        list_name(doners)
    elif (my_name == 'quit'):
        main_prompt()
    else:
        found = find_name(doners, my_name)
        if (not found):
            amount = take_donation()
        else:
            amount = take_donation()
        add_record(doners, my_name, amount)
        print(letter(my_name, amount))
        input('Press Enter to Continue...\n\n> ')
        main_prompt()


def countall(donerlist):
    my_count = {}
    my_names = {}
    my_total = {}
    for doner in donerlist:
        name_orig = doner[0]
        name_key = doner[0].replace(' ', '')
        my_amount = float(doner[1])
        if (name_key in my_names):
            my_count[name_key] = my_count[name_key] + 1
            my_total[name_key] = my_total[name_key] + my_amount
        else:
            my_count[name_key] = 1
            my_names[name_key] = name_orig
            my_total[name_key] = my_amount
    return(my_count, my_names, my_total)


def report(donerlist):
    my_count, my_names, my_total = countall(doners)
    header = ('Name'.center(20) + '|' +
              'Total'.rjust(10) + ' |' +
              '#'.rjust(4) + ' |' +
              'Average'.rjust(10) + '\n\n' + '_' * 60 + '\n')
    print(header)
    for k in my_names:
        n = (my_names[k]).ljust(20)
        c = str(my_count[k]).rjust(4)
        t = format(my_total[k], '.2f').rjust(10)
        avg = my_total[k] / my_count[k]
        a = format(avg, '.2f').rjust(10)
        line = (n + '|' + t + ' |' + c + ' |' + a)
        print(line)
    input('\nPress Enter to Continue...\n\n> ')
    main_prompt()


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def take_donation():
    while True:
        str_amount = input("\nPlease enter a donation amount or 'quit':\n\n> ")
        if (str_amount == 'quit'):
            main_prompt()
        elif (is_number(str_amount)):
            return str_amount
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
    main_prompt()


def find_name(donerlist, my_name):
    my_found = False
    for doner in donerlist:
        if (doner[0] == my_name):
            my_found = True
    return my_found


def add_record(donerlist, my_name, my_amount):
    record = [my_name, my_amount]
    donerlist = donerlist.append(record)


def letter(my_name, my_amount):
    print
    dollar = format(float(my_amount), '.2f')
    text = ('Dear ' + my_name + ',\n\n' +
            'Thank you so much for your kind donation of $' + dollar +
            '. We here at the Foundation for Homeless Whales greatly ' +
            'appreciate it. Your money will go towards creating new oceans ' +
            'on the moon for whales to live in.\n\n' +
            'Thanks again,\n\n' +
            'Jim Grant\n' +
            'Director, F.H.W.\n')
    return text


answer = True

if (__name__ == '__main__'):
    while answer:
        answer = main_prompt()
