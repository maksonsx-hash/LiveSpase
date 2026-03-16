import random


def random_pos_krator1(types_krator, max_cell=20):
    bad_pos = {}
    for i in types_krator:
        bad_pos[i] = []
    unic_values = []
    for i in types_krator:
        count = 0
        while count != max_cell // len(types_krator):
            b = random.randint(1, 10), random.randint(1, 10)
            if b in unic_values:
                continue
            bad_pos[i].append(b)
            unic_values.append(b)
            count += 1
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


types = ['gold', 'orange', 'iron']

print(random_pos_krator1(types, 10))
