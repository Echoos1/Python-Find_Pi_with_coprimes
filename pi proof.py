# Created by Matthew DiMaggio - 25 February 2021
import math
import secrets
import winsound

gen = secrets.SystemRandom()
rpi = math.pi


def pregame():

    def domath():
        n = int(input("Please enter number of trials: "))
        r = int(input("Please enter range of calculations: "))
        print("Computing...", end = "\r")
        a = 0
        nt = n / 10000
        perc = 0
        for i in range(n):
            gcf = math.gcd(gen.randrange(1, r+1), gen.randrange(1, r+1))
            if gcf == 1:
                a = a + 1
            else:
                pass
            if (i+1)%nt == 0:
                perc = perc + 0.01
                print(f"Computing... {round(perc, 2)}%      ", end="\r")
            else:
                pass

        p = a / n
        pi = math.sqrt(6 / p)

        print(f"\n\nTrials: {n}\n"
              f"Range: 1 - {r}\n"
              f"Found Co-primes: {a}\n"
              f"Probability: {round(p,6)} or {round(p*100, 6)}%\n"
              f"Calculated pi: {pi}\n"
              f"% Error: {abs(round(((rpi-pi)/pi)*100, 6))}%\n")
        winsound.Beep(2048, 100)

        retry = input("Try Again? (y/n): ")
        if retry.lower() == "y":
            pregame()
        elif retry.lower() == "credits" or retry.lower() == "credit":
            print("\nCreated by:  Matthew DiMaggio  -  25 February 2021\n")
            pregame()
            quit()

    domath()


pregame()
