import math as m
from pyquil.api import QVMConnection
from pyquil.quil import Program
from pyquil.gates import H

def main():
    num_bits = int(input("Number of bits to use: "))

    # Rigetti QVM only allows 19 qubits max right now
    if num_bits < 1 or num_bits > 19:
        print("Number of bits must be between 1 and 19")
        exit()

    num_samples = int(input("Number of samples: "))
    if num_samples < 1:
        print("Number of samples must be positive")
        exit()

    points = get_points(num_bits, num_samples)

    num_within_radius = 0
    for x, y in points:
        if m.sqrt(x * x + y * y) < 1:
            num_within_radius += 1

    ratio = num_within_radius / num_samples

    pi_estimate = 4 * ratio

    print("Number of samples within radius: {0}".format(num_within_radius))
    print("Estimate for pi: {0}".format(pi_estimate))
# end main

# use Rigetti computing's Forest API to generate random numbers from a quantum
# virtual machine
def get_points(num_bits, num_samples):

    # the max number we can have with the specified number of bits
    max_num = 2 ** (num_bits) - 1

    qvm = QVMConnection()

    # create the Quill program
    # each Qubit is put through an H gate to put it in the Hammard state. Every
    # time we measure a qubit in this state, it has a 50-50 chance of being a 1
    # or 0. By doing this we can generate random bits
    p = Program()
    for i in range(0, num_bits):
        p.inst(H(i)) # put each qubit in the Hammard state
    p.measure_all()

    # run the Quill program on the quantum virtual machine
    xs = qvm.run(p, trials=num_samples)
    # convert the list of lists of results for each trial into a list of
    # floating point numbers between 0-1. These will be our x coordinates
    xs = list(map(lambda x: bits_to_int(x) / max_num, xs))

    ys = qvm.run(p, trials=num_samples)
    ys = list(map(lambda y: bits_to_int(y) / max_num, ys))

    return zip(xs, ys)
#end get_points


# convert the list of bits we get back from a single trial into an integer
def bits_to_int(bits):
    ret = 0
    for bit in bits:
        ret = (ret << 1) | bit

    return ret
# end bits_to_int

if __name__ == "__main__":
    main()
