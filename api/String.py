#!/usr/local/bin/python
# coding: utf-8

import numpy as np
import unicodedata


def normalize(text: str) -> str:
    return str(unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")).lower()


def levenshtein_index(seq1: str, seq2: str) -> float:
    return 1-levenshtein(seq1, seq2)/len(seq1+seq2)


# https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
def levenshtein(seq1: str, seq2: str) -> float:
    seq1 = normalize(seq1)
    seq2 = normalize(seq2)
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix[x, y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1] + 1,
                    matrix[x, y-1] + 1
                )
    return matrix[size_x - 1, size_y - 1]