import sys


def odd_indexes(items):
    return list(filter(lambda item: (items.index(item) + 1) % 2 != 0, items))


def even_indexes(items):
    return list(filter(lambda item: (items.index(item) + 1) % 2 == 0, items))


def params_to_dict(args):
    keys = odd_indexes(args)
    values = even_indexes(args)
    return dict(zip(keys, values))


def get_sys_params(offset=1):
    return params_to_dict(sys.argv[offset:])
