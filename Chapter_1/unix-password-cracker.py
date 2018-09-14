import crypt

def testPassword(cryptPass):

    salt = cryptPass[0:2]
    dictFile = open("dictionary.txt", 'r')

    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word.salt)

        if (cryptWord == cryptPass):
            print("[+]\tFound password: {}\n".format(word))
            return

        print("Password not found!\n")

        return

def main():

    passFile = open("passwords.txt")

    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*]\tCracking password for: {}".format(user))

            testPassword(cryptPass)

if __name__ == '__main__': main()
