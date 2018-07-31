#!/usr/bin/python

import unittest

def nways(steps, max_steps = 3):
    """ Return in how many possible ways we can run up the stairs """

    # steps are number of steps
    # max_steps are max hops allowed
    # At any given time we can hop up to 'max_steps' steps up the stairs: for
    # each possibility we need to compute the different number of ways in which
    # the remaining steps can be walked. The number of steps that we hop cannot
    # be greater than the number of remaining steps in the staircase (i.e., if
    # there are only two steps left we cannot hop three). Stop when the number
    # of remaining steps is zero: it means that we have reached the top.

    if not steps:
        return 1
    elif steps < 0:
        return 0
    else:
        total = 0
        for n in xrange(1, min(steps, max_steps) + 1):
            total += nways(steps - n, max_steps = max_steps)
        return total

class NwaysTest(unittest.TestCase):

    def test_nways(self):
        self.assertEqual(nways(1), 1)
        self.assertEqual(nways(2), 2) # (1 + 1) or (2)
        self.assertEqual(nways(3), 4) # (1 + 1) or (2 + 1) or (1 + 2) or (3)
        self.assertEqual(nways(4), 7)
        self.assertEqual(nways(5), 13)
        self.assertEqual(nways(6), 24)
        self.assertEqual(nways(7), 44)
        self.assertEqual(nways(8), 81)
        self.assertEqual(nways(9), 149)
        self.assertEqual(nways(10), 274)
        self.assertEqual(nways(11), 504)
        self.assertEqual(nways(12), 927)
        self.assertEqual(nways(13), 1705)
        self.assertEqual(nways(14), 3136)
        self.assertEqual(nways(15), 5768)
        self.assertEqual(nways(16), 10609)
        self.assertEqual(nways(17), 19513)
        self.assertEqual(nways(18), 35890)
        self.assertEqual(nways(19), 66012)
        self.assertEqual(nways(20), 121415)
        self.assertEqual(nways(21), 223317)
        self.assertEqual(nways(22), 410744)
        self.assertEqual(nways(23), 755476)
        self.assertEqual(nways(24), 1389537)
        self.assertEqual(nways(25), 2555757)
        self.assertEqual(nways(26), 4700770)
        self.assertEqual(nways(27), 8646064)
        self.assertEqual(nways(28), 15902591)
        self.assertEqual(nways(29), 29249425)
        self.assertEqual(nways(30), 53798080)

# nways 3 hops max 7 steps
tot = nways(3, 2)
print (tot)

# if the Python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value "__main__". I
# f this file is being imported from another module, __name__ will be set to the module's name.

if __name__ == "__main__":
    unittest.main()
