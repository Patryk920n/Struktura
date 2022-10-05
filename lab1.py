#  ZADANIE 1
# lista = []
# for i in range(10):
#     lista.append(i)
# print(lista)
#
# listaB = []
# for i in range(21):
#     if(i%2 == 0):
#         listaB.append(i)
# print(listaB)
#
# listaC = []
# for i in range(1,11):
#     i*=i
#     listaC.append(i)
# print(listaC)
#
# listaD = []
# for i in range(1,11):
#     listaD.append(0)
# print(listaD)
#
# listaE = []
# for i in range(1,11):
#     if(i%2 == 0):
#         listaE.append(1)
#     else: listaE.append(0)
# print(listaE)
#
# listaF = []
# a = 0
# for i in range(10):
#     if(a == 5):
#         a = 0
#     listaF.append(a)
#     a+=1
# print(listaF)
# lista = []
# i=1
# while i<=10:
#     lista.append(i)
#     i+=1
# print(lista)

# lista = []
# i=0
# while i<=20:
#     if(i%2==0):
#         lista.append(i)
#     i+=1
# print(lista)
#
#  ZADANIE 3
# lista = [-1,2,-3,4,-5,6,-7,8,-9,10]
# def ile_ujemnych(lista):
#     ile = 0
#     for x in range(10):
#         if lista[x] < 0:
#             ile += 1
#     return ile
# print(ile_ujemnych(lista))
# ile = 0
# for x in range(10):
#     if lista[x] < 0:
#         ile += 1
# print(ile)

#   ZADANIE 4
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def iloczyn(lista):
#     ilocz = 1
#     for x in range(10):
#         ilocz *= lista[x]
#     return ilocz
# print(iloczyn(lista))
# ilocz = 1
# for x in range(10):
#     ilocz *= lista[x]
# print(ilocz)

#   ZADANIE 5
#
# a = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# def minmax(lista):
#     max=lista[0]
#     min=lista[0]
#     for x in range(12):
#         if(max<lista[x]):
#             max=lista[x]
#         if (min > lista[x]):
#             min = lista[x]
#     wynik = (min, max)
#     return wynik
# print(minmax(a))
#
#   ZADANIE 6
#
# a = [1, 4, 16, 9, 9, 7, 4, 9, 11]
# def sum(lista):
#     wynik = 0
#     for x in range(9):
#         if x%2 == 0:
#             wynik += lista[x]
#         else: wynik -= lista[x]
#     return wynik
# print(sum(a))

# lista = [1, 2, 3, 4, 5, 6, 7]
# a = 0
#
# while a < 9:
#     b = input("Wpisz liczbe")
#
#     if b != lista[a]:


