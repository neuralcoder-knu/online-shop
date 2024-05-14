import hashlib


def encode_md5(string):
    string_bytes = string.encode('utf-8')

    md5_hash = hashlib.md5()
    md5_hash.update(string_bytes)

    return md5_hash.hexdigest()