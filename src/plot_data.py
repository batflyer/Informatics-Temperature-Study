# Copyright © 2019 Alexander L. Hayes
# MIT License

"""
================
``plot_data.py``
================

Plot the contents of the ``data/`` directory.

Instructions
------------

1. This needs to be run from the base of the repository. For example:

    .. code-block:: bash

        $ pythonw src/plot_data.py -i 1     # Mac
        $ python src/plot_data.py -i 1      # Linux

2. ``-i FILE`` where FILE={1,2} sets which data set to plot.

3. Images are not saved automatically. Make adjustments with the matplotlib
   interface and save images locally.
"""

import argparse
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "-i",
        "--input",
        help="Text file for input {1 or 2}. Should be comma-delimited with a row of labels at the top.",
        default="1",
    )
    ARGS = PARSER.parse_args()

    if ARGS.input == "1":

        _data = np.loadtxt("data/data1.txt", delimiter=",", dtype=float, skiprows=1)

        fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, sharex=False)

        ax1.plot(_data[0:151].T[0], _data[0:151].T[1])
        ax1.set_ylabel("Sitting at Desk")

        ax2.plot(_data[170:260].T[0], _data[170:260].T[1])
        ax2.axvline(x=438)
        ax2.axvline(x=518)
        ax2.set_ylabel("Walking Outside")

        ax3.plot(_data[436:477].T[0], _data[436:477].T[1])
        ax3.set_ylabel("Random Classroom")

        ax4.plot(_data[571:612].T[0], _data[571:612].T[1])
        ax4.set_ylabel("The Fridge")

        ax5.plot(_data[679:845].T[0], _data[679:845].T[1])
        ax5.axvline(x=1462)
        ax5.axvline(x=1536)
        ax5.axvline(x=1640)
        ax5.set_ylabel("Random Walk through Informatics")

        plt.show()

    else:

        _data = np.loadtxt("data/data2.txt", delimiter=",", dtype=float, skiprows=1)

        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False)

        ax1.plot(_data[29:46].T[0], _data[29:46].T[1])
        ax1.set_ylabel("Walking Outside")

        ax2.plot(_data[51:70].T[0], _data[51:70].T[1])
        ax2.set_ylabel("1st Floor Classroom")

        plt.show()
