#!/usr/bin/python3
""" Task 0. UTF-8 Validation """

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given dataset represents a valid UTF-8 encoding."""
    valid_headers = ['0', '110', '1110', '11110', '10']

    expect = 0
    for byte in data:
        # Binary of 8 least significant bits
        b = format(byte, 'b')[-8:]
        b = f"{b:0>8}"  # left pad with zero(s)

        # Header
        header = None
        for h in valid_headers:
            if b.startswith(h):
                header = h
        # print(f"byte: {byte} b: {b} header: {header} expect: {expect}")
        if header is None:
            return False

        # Match follower bytes
        if header == '10':
            if expect <= 0:
                return False
            expect -= 1
        else:
            if expect > 0:
                return False
            # set expected bytes
            expect = valid_headers.index(header)

    return True if expect == 0 else False
