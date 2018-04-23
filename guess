import time
secret = 22

ponovi = True

for i in range(10):
    guess = int(raw_input("Guess number:"))

    if guess == secret:
        print "Guess %s!" % secret
        #ponovi = False;
        break
    else:
        print "Guess is not correct!"

    nadaljuj = raw_input("Ponovi? D/N: ")

    if nadaljuj.upper() != "D": ponovi = False

    print "I will sleep for 5 s"
    for j in range (15):
        print j
        time.sleep(1)

print "END!"
