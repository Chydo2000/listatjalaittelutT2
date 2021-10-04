def sort2D(a):
    
    # Listan alkioista a[i] on poistettu tyhjät alkiot.
    af = []
    for i in range(0, len(a)):
        if (a[i]!=[]):
            af.append(a[i])
    a = af
    n = len(a)
    
    # Listan a listojen a[i] alkiot on järjestetty nousevaan järjestykseen kaikilla i=0,...,len(a[i]).
    for k in range(n):
        nk = len(a[k])
        for i in range(nk):
            minind = i
            for j in range (i+1, nk):
                if (a[k][minind] > a[k][j]):
                    minind = j

            a[k][i], a[k][minind] = a[k][minind], a[k][i]
    
    # Listan a listat a[i] on järjestetty listojen a[i] alkioiden lukumäärän (len(a[i])) perusteella nousevaan järjestykseen.
    for i in range(n):
        minind = i
        for j in range (i+1, n):
            if (len(a[minind]) > len(a[j])):
                minind = j
        a[i], a[minind] = a[minind], a[i]

    # Listan a samanpituiset listat (sama len(a[i])) on järjestetty listojen a[i] alkioiden summan (sum(a[i])) perusteella nousevaan järjestykseen.
    for i in range(n):
        minind = i
        vlen = len(a[i])
        for j in range (i+1, n):
            newlen = len(a[j])
            if (sum(a[minind]) > sum(a[j])) & (vlen == newlen):
                minind = j
        a[i], a[minind] = a[minind], a[i]
    
    return a