

d = {'p': {'q': {}, 'r': {'s': 1}}}
# d = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}


def count_key_value_pairs(data):
    if not data:
        return 0

    count = 0
    for k, v in data.items():
        count += 1

        if isinstance(v, dict):
            if v:
                count += count_key_value_pairs(v)

        return count

