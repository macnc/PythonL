#! /usr/bin/python
# _*_coding: utf-8

db = {}


def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try again: '
            continue
        else:
            break

    pwd = raw_input('passwd: ')
    db[name] = pwd
    print "Congratulations! Your user name %s has been created!" % name


def olduser():
    name = raw_input('login: ')
    pwd = raw_input('password: ')
    passwd = db.get(name)

    if passwd == pwd:
        print "Welome back!", name
    else:
        print "login incorrect, plz try again one more time!"
        return olduser()


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    Enter choice: """

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
            break
        if choice == 'e':
            olduser()
            break


if __name__ == '__main__':
    showmenu()
