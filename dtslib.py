def counting_sort(list):
    m = list[0]
    for i in range(0, len(list)):
        if list[i] > m:
            m = list[i]

    max = m
    nlist = [0] * (max + 1)
    aux = [0] * (len(list))

    for i in range(0, len(list)):
        for f in range(0, max + 1):
            if list[i] == f:
                nlist[f] += 1

    for i in range(1, max + 1):
        nlist[i] = nlist[i] + nlist[i - 1]

    for i in range(max, 0, -1):
        nlist[i] = nlist[i - 1]

    nlist[0] = 0

    for i in range(0, len(list)):
        for f in range(0, max + 1):
            if list[i] == f:
                aux[nlist[f]] = list[i]
                nlist[f] = nlist[f] + 1

    return (f"{aux}")

    # print(f"{nlist}")
    # print(f"{aux}")
