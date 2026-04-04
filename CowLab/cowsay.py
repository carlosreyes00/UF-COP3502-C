import sys
import heifer_generator
from dragon import Dragon
from ice_dragon import IceDragon
from cow import Cow

"""
python cowsay.py -l Lists the available cows (this is a lowercase L)
python cowsay.py -n COW MESSAGE Prints out the MESSAGE using the specified COW
python cowsay.py MESSAGE Prints out the MESSAGE using the default COW
"""

if sys.argv[1] == "-l":
    print("Cows available:", end=" ")
    for item in heifer_generator.get_cows():
        print(item.get_name(), end=" ")
    print()
elif sys.argv[1] == "-n":
    if Cow(sys.argv[2]) in heifer_generator.get_cows():
        print(" ".join(sys.argv[3:]))
        for item in heifer_generator.get_cows():
            if item.get_name() == sys.argv[2]:
                print(item.get_image())

                if isinstance(item, IceDragon):
                    print("This dragon cannot breathe fire.")
                elif isinstance(item, Dragon):
                    print("This dragon can breathe fire.")
    else:
        print("Could not find ninja cow!")
else:
    print(" ".join(sys.argv[1:]))
    print(heifer_generator.get_cows()[0].get_image())
