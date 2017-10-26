import math as m
import random as r

def main():
    numSamples = int(input("Number of Samples: "))

    numWithinRadius = 0

    for i in range(0, numSamples):
        x = r.uniform(0,1)
        y = r.uniform(0,1)

        if m.sqrt(x * x + y * y) < 1:
            numWithinRadius += 1

    ratio = numWithinRadius / numSamples

    piEstimate = 4 * ratio

    print("Number of samples within radius: {0}".format(numWithinRadius))
    print("Estimate for pi: {0}".format(piEstimate))

if __name__ == "__main__":
    main()

