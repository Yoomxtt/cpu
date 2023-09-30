#!/usr/bin/env python3

import sys
import itertools
from cmdconsts import *

ROM_SIZE = 512 * 1024
WIDTH = 20
HEIGHT = 4


def out(b):
    out.written += len(b)
    sys.stdout.buffer.write(b)

out.written = 0

def pause():
    out(INI * 40)


if __name__ == '__main__':
    if sys.stdout.isatty():
        sys.stderr.write('Usage: screensize.py > prog.bin\n')
        sys.exit(1)
    # INIT
    out(INI)
    out(CUR)
    out(EIN)
    out(CLR)

    # define cgram
    out(C00)
    out(B31)     # XXXXX
    out(B17 * 6) # X...X
    out(B31)     # XXXXX

    # fill screen
    out(D00)
    out(CG0 * 20 * 4)

    for i in range(12):
        pause()
        for pos in [D00, E00, D20, E20]:
            out(pos)
            out(BLK * 20)
            pause()
            out(pos)
            out(CG0 * 20)

    pause()
    pause()
    for i in range(12):
        pause()
        for j in range(20):
            out(bytes([ord(E20) + j]))
            out(BLK)
            out(bytes([ord(D20) + j]))
            out(BLK)
            out(bytes([ord(E00) + j]))
            out(BLK)
            out(bytes([ord(D00) + j]))
            out(BLK)
            pause()
            out(bytes([ord(E20) + j]))
            out(CG0)
            out(bytes([ord(D20) + j]))
            out(CG0)
            out(bytes([ord(E00) + j]))
            out(CG0)
            out(bytes([ord(D00) + j]))
            out(CG0)

    while out.written < ROM_SIZE:
        out(INI)
