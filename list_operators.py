# *************************************************************************************************
# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
'''
Konso : elemen, List → List
    {Konso(e,L): menghasilkan sebuah list dari e dan L, dengan e sebagai elemen pertama e: e o L → L'} 

Konsi : List, elemen → List
    {Konsi(L,e): menghasilkan sebuah list dari L dan e, dengan e sebagai elemen terakhir list : L • e → L'} 

FirstElmt: List tidak kosong → elemen
    {FirstElmt(L) Menghasilkan elemen pertama list L} 

Tail : List tidak kosong → List
    {Tail(L) : Menghasilkan list tanpa elemen pertama list L, mungkin kosong}

LastElmt : List tidak kosong → elemen
    {LastElmt(L) : Menghasilkan elemen terakhir list L}

Head : List tidak kosong → List
    {Head(L) : Menghasilkan list tanpa elemen terakhir list L, mungkin kosong}  

IsEmpty : List → boolean
    {IsEmpty(L) benar jika list kosong}

NbElmt : List → integer
    {NbElmt(L) : Menghasilkan banyaknya elemen list, nol jika kosong} 
'''
# *************************************************************************************************
# REALISASI
def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:] 

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def IsEmpty(L):
    return L == []

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
# *************************************************************************************************
