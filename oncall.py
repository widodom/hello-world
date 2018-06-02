import random

# A list of devs for on-call rotation, listed with weights to randomize

devs = {
    'Brandon': 1,
    'Byran': 1,
    'Carlos': 3,
    'Dan': 1,
    'Ed': 5,
    'Kelley': 2,
    'Kevin': 3,
    'Kyle': 1,
    'Nikhil': 2,
    'Scott': 2
}


big_list = []
for name in devs:
    big_list += [name] * devs[name]


random.shuffle(big_list)

print('with my solution: {}'.format(big_list[0]))
print('with random library: {}'.format(random.choices(list(devs.keys()), devs.values(), k=1)[0]))
