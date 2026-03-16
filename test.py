import random


def random_pos_krator1(types_krator):
    bad_pos = {}
    for i in types_krator:
        bad_pos[i] = []
    switch = True
    i = 0
    count = 0
    for i in types_krator:
        for j in range(4):
            b = random.randint(1, 10), random.randint(1, 10)
            if b in bad_pos.values():
                continue
            bad_pos[i].append(b)

    return bad_pos

def random_pos_krator(types_krator):
    bad_pos = {}
    for i in types_krator:
        bad_pos[i] = []
    switch = True
    i = 0
    count = 0
    while switch:
        i += 1
        if i <= 5:
            b = random.randint(1, 10), random.randint(1, 10)
            if b in bad_pos:
                continue
            bad_pos['gold'].append(b)
            count += 1
        if 5 < i <= 10:
            a = random.randint(1, 10), random.randint(1, 10)
            if a in bad_pos:
                continue
            bad_pos['orange'].append(a)

            count += 1
        if i > 10:
            type = random.choice(types_krator)
            if type == 'gold':
                b = random.randint(1, 10), random.randint(1, 10)
                if b in bad_pos:
                    continue
                bad_pos['gold'].append(b)

                count += 1
                if count == 20:
                    switch = False
            if type == 'orange':
                a = random.randint(1, 10), random.randint(1, 10)
                if a in bad_pos:
                    continue
                bad_pos['orange'].append(a)

                count += 1
                if count == 20:
                    switch = False
    return bad_pos


types = ['gold','orange','iron','brbr','blue']

print(random_pos_krator1(types))






