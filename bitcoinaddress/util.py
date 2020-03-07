import hashlib


def doublehash256(v):
    return hashlib.sha256(hashlib.sha256(v).digest())