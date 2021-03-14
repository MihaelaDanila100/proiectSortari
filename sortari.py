import random
import time

bule = open("rezultateBubble.txt", "w")
cSort = open("rezultateCount.txt", "w")
merge = open("rezultateMerge.txt", "w")
quick = open("rezultateQuick.txt", "w")

def generate_numbers(nr_numere, val_maxima, cod):
    l = []
                                        #CODUL "random" - VALORI ALEATORII
    if cod == 'random':
        while len(l) < nr_numere:               #fiecare dintre cele nr_numere elemente primeste o valoare aleatoare intre 0 si val_maxima
            l.append(random.randint(0, val_maxima))

                                        #SIRURI ORDONATE CRESCATOR

            #CODUL "sortate_crescator_cu_egalitati" - ŞIR CRESCĂTOR ÎN CARE SUNT ŞI VALORI EGALE

    if cod == 'sortate_crescator_cu_egalitati':
        if val_maxima < nr_numere:
            pivot = random.randint(0, val_maxima)

            for i in range(0, pivot):
                l.append(i)

            while len(l) < nr_numere - pivot:
                l.append(pivot)

            for i in range(pivot + 1, val_maxima + 1):
                l.append(i)
        else:
            start = random.randint(0, val_maxima)
            zona = nr_numere // 3

            for i in range(0, zona):
                l.append(i + start)

            for i in range(zona, 2 * zona):
                l.append(l[i-1])

            for i in range(2*zona, nr_numere):
                l.append(l[i-1] + 1)

            # CODUL "sortate_crescator_distincte" - ŞIR CRESCĂTOR CU VALORI DISTINCTE

    if cod == 'sortate_crescator_distincte':
        if nr_numere > val_maxima:
            print("Pentru un sir crescator de numere distincte trebuie ca lungimea sirului sa fie mai mica sau egala cu valoarea maxima")
            return False

        start = random.randint(0, val_maxima - nr_numere)

        for i in range(0, nr_numere):
            l.append(start + i)


            # CODUL "sortate_aproape_crescator" - ŞIR PARŢIAL CRESCĂTOR
    if cod == 'sortate_aproape_crescator':
        l = generate_numbers(nr_numere, val_maxima, 'sortate_crescator_distincte')
        if nr_numere < 4:
            print("Prea putine numere!")
            return False

        if l is False:
            return l

        nr_interschimbari = random.randint(1, 5)
        for i in range(0, nr_interschimbari):
            aux = l[i]
            l[i] = l[i+2]
            l[i+2] = aux

                                        #SIRURI ORDONATE DESCRESCATOR

            #CODUL "sortate_descrescator_cu_egalitati" - ŞIR DESCRESCĂTOR ÎN CARE SUNT ŞI VALORI EGALE


    if cod == 'sortate_descrescator_cu_egalitati':
        if val_maxima < nr_numere:
            pivot = random.randint(0, val_maxima)

            for i in range(val_maxima + 1, pivot + 1, -1):
                l.append(i)

            while len(l) < nr_numere - pivot:
                l.append(pivot)

            for i in range(pivot, 0, -1):
                l.append(i)

        else:
            pivot = random.randint(nr_numere, val_maxima)
            zona = nr_numere // 3

            for i in range(pivot + zona, pivot, -1):
                l.append(i)

            for i in range(0, zona):
                l.append(pivot)

            for i in range(2*zona, nr_numere):
                l.append(l[i-1]-1)

    if cod == 'sortate_descrescator_distincte':
        if nr_numere > val_maxima:
            print("Pentru un sir descrescator de numere distincte trebuie ca lungimea sirului sa fie mai mica sau egala cu valoarea maxima")
            return False

        start = random.randint(nr_numere, val_maxima)
        for i in range(0, nr_numere):
            l.append(start - i)

            # CODUL "sortate_aproape_descrescator" - ŞIR PARŢIAL CRESCĂTOR
    if cod == 'sortate_aproape_descrescator':
        l = generate_numbers(nr_numere, val_maxima, 'sortate_descrescator_distincte')
        if nr_numere < 4:
            print("Prea putine numere!")
            return False

        if l is False:
            return False

        nr_interschimbari = random.randint(1, 5)

        for i in range(0, nr_interschimbari):
            l[i], l[i + 2] = l[i + 2], l[i]

    if cod == 'egale':
        x = random.randint(1, val_maxima)
        l = [x for i in range(0, nr_numere)]

    if cod == 'valori_mari':
        val_maxima = 2 ** 32
        while len(l) < nr_numere:
            l.append(random.randint(2 ** 31, val_maxima))

    return l


def test_sort(v):
    nr_elemente = len(v)
    for i in range(0, nr_elemente-1):       #parcurgem vectorul sortat element cu element
        if v[i] > v[i+1]:       #daca nu sunt in ordine crescatoare 2 elemente consecutive, sirul nu e sortat corect
            return False

        if v[i] in v_aux:       #verificam daca elementul curent era si in vectorul initial, caz in care il eliminam
            v_aux.remove(v[i])
        else:                   #daca elementul nu se afla initial in vector, sirul nu e sortat corect
            return False

    if v[nr_elemente - 1] in v_aux:             #verificam si ultimul element, care nu a fost acoperit de for
        v_aux.remove(v[nr_elemente - 1])
    else:
        return False

    if len(v_aux) != 0:        #daca au ramas elemente in vectorul initial neaduse in vectorul sortat, sirul nu este sortat corect
        return False

    return True             #sirul este sortat corect

                        #BUBBLE SORT
def BubbleSort(nr_elemente, v):
    sortat = False

    if nr_elemente > 10 ** 6:
        bule.write("Nu se poate sorta cu Bubble sort")
        return False

    while sortat == False:
        sortat = True

        for i in range(0, nr_elemente - 2):
            if v[i] > v[i + 1]:
                v[i], v[i+1] = v[i+1], v[i]
                sortat = False

    return v

                    #COUNT SORT
def countSort(v):
    # variabila max reține cea mai mare valoare din vector, până la care vom reține numărul de apariții al fiecărei valori în elemente
    max = -1
                    # calculam maximul
    for element in v:
        if max < element:
            max = element

    if max > 10 ** 6:
        print("Nu se poate sorta")
        return False

    # inițializăm variabila frecv(vectorul de frecvență) cu 0 pe fiecare poziție: momentan fiecare element apare de 0 ori

    frecv = [0] * (max + 1)

    #formăm vectorul de frecvență:
    # parcurgem elementele vectorului și incrementăm frecv[indexul egal cu elementul], pentru a actualiza numărul de apariţii
    for element in v:
        frecv[element] += 1

    #pentru obtinerea sirului ordonat:
    #parcurgem indecşii din vectorul de frecvenţă şi adaugam fiecare valoare de frecv[index] ori
    cnt = 0
    for i in range(1, max + 1):
        for j in range(0, frecv[i]):
            v[cnt] = i
            cnt += 1

    return v

                    #RADIX SORT
def sortarePeCifra(lista, pas):
    d = [0] * 10

    for element in lista:
        cifra = element // pas
        cifra = cifra % 10
        d[cifra] += 1
        buckets[cifra].append(element)

    print(buckets)

def RadixSort(lista):
    poz = 1
    maxi = max(lista)
    while poz < maxi:
        sortarePeCifra(lista, poz)
        poz *= 10

                #MERGE SORT
def interclasare(A, B):
    return sorted(A + B)

def merge_sort(A):
    n = len(A)

    if n <= 1:
        return A

    A_stanga = merge_sort(A[:n//2])
    A_dreapta = merge_sort(A[n//2:])

    A_rezultat = interclasare(A_stanga, A_dreapta)
    return A_rezultat

                #QUICK SORT
def QuickSort(v, pozitie_pivot, st, dr):
    i = st
    j = dr
    pivot = v[pozitie_pivot]

    while i < dr and v[i] < pivot:
        i += 1

    while j > st and v[i] > pivot:
        j -= 1

    if i <= j:
        v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1

    while i <= j:
        while i < dr and v[i] < pivot:
            i += 1

        while j > st and v[i] > pivot:
            j -= 1

        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1

    if st < j:
        QuickSort(v, pozitie_pivot, st, j)

    if i < dr:
        QuickSort(v, pozitie_pivot, i, dr)


lista_teste = ['random', 'sortate_crescator_cu_egalitati', 'sortate_crescator_distincte', 'sortate_aproape_crescator', 'sortate_descrescator_cu_egalitati',
               'sortate_descrescator_distincte', 'sortate_aproape_descrescator', 'egale', 'valori_mari']

contor_numere = [10, 1000]
valori = [10, 1000, 10 ** 6, 10 ** 8, 10 ** 18]

elemente = [21, 34, 52, 12]
buckets = [[]] * 10
#RadixSort(elemente)

for n in contor_numere:
    bule.write("Avem " + str(n) + " numere:\n")
    for test in lista_teste:
        bule.write("\tCodul " + test + ":\n")
        for maxi in valori:
            bule.write("\t\tValoarea maxima " + str(maxi) + ":\n")
            v = generate_numbers(n, maxi, test)
            if v is not False:
                v_aux = v.copy()

                start = time.time()
                v_1 = BubbleSort(n, v)
                stop = time.time()
                if v_1 is not False:
                    bule.write("\t\t\tDurata: " + str(stop - start) + ";\n\t\t\tSortat corect: " + str(test_sort(v_1)) + "\n")

for n in contor_numere:
    cSort.write("Avem " + str(n) + " numere:\n")
    for test in lista_teste:
        cSort.write("\tCodul " + test + ":\n")
        for maxi in valori:
            cSort.write("\t\tValoarea maxima " + str(maxi) + ":\n")
            v = generate_numbers(n, maxi, test)
            start = time.time()
            v_2 = countSort(v)
            stop = time.time()
            if v_2 is not False:
                cSort.write("\t\t\tDurata: " + str(stop - start) + ";\n\t\t\tSortat corect: " + str(test_sort(v_2)) + "\n")

for n in contor_numere:
    merge.write("Avem " + str(n) + " numere:\n")
    for test in lista_teste:
        merge.write("\tCodul " + test + ":\n")
        for maxi in valori:
            merge.write("\t\tValoarea maxima " + str(maxi) + ":\n")
            v = generate_numbers(n, maxi, test)
            start = time.time()
            v_3 = merge_sort(v)
            stop = time.time()
            if v_3 is not False:
                merge.write("\t\t\tDurata: " + str(stop - start) + ";\n\t\t\tSortat corect: " + str(test_sort(v_3)) + "\n")


for n in contor_numere:
    quick.write("Avem " + str(n) + " numere:\n")
    for test in lista_teste:
        quick.write("\tCodul " + test + ":\n")
        for maxi in valori:
            quick.write("\t\tValoarea maxima " + str(maxi) + ":\n")
            v = generate_numbers(n, maxi, test)
            pozitie_pivot = 0
            start = time.time()
            QuickSort(v,pozitie_pivot,0,len(v))
            stop = time.time()
            if v is not False:
                quick.write("\t\t\tDurata: " + str(stop - start) + ";\n\t\t\tSortat corect: " + str(test_sort(v)) + "\n")

for n in contor_numere:
    quick.write("Avem " + str(n) + " numere:\n")
    for test in lista_teste:
        quick.write("\tCodul " + test + ":\n")
        for maxi in valori:
            quick.write("\t\tValoarea maxima " + str(maxi) + ":\n")
            v = generate_numbers(n, maxi, test)
            pozitie_pivot = len(v)
            start = time.time()
            QuickSort(v,pozitie_pivot,0,len(v))
            stop = time.time()
            if v is not False:
                quick.write("\t\t\tDurata: " + str(stop - start) + ";\n\t\t\tSortat corect: " + str(test_sort(v)) + "\n")

for n in contor_numere:
    quick.write("Avem " + str(n) + " numere:\n")
    for test in lista_teste:
        quick.write("\tCodul " + test + ":\n")
        for maxi in valori:
            quick.write("\t\tValoarea maxima " + str(maxi) + ":\n")
            v = generate_numbers(n, maxi, test)
            pozitie_pivot = len(v) // 2
            start = time.time()
            QuickSort(v,pozitie_pivot,0,len(v))
            stop = time.time()
            if v is not False:
                quick.write("\t\t\tDurata: " + str(stop - start) + ";\n\t\t\tSortat corect: " + str(test_sort(v)) + "\n")


for n in contor_numere:
    quick.write("Avem " + str(n) + " numere:\n")
    for test in lista_teste:
        quick.write("\tCodul " + test + ":\n")
        for maxi in valori:
            quick.write("\t\tValoarea maxima " + str(maxi) + ":\n")
            v = generate_numbers(n, maxi, test)
            pozitie_pivot = random.randint(0, len(v))
            start = time.time()
            QuickSort(v, pozitie_pivot, 0, len(v))
            stop = time.time()
            if v is not False:
                quick.write("\t\t\tDurata: " + str(stop - start) + ";\n\t\t\tSortat corect: " + str(test_sort(v)) + "\n")


bule.close()
cSort.close()
merge.close()
quick.close()