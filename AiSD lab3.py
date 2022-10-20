from typing import Any


class Node:
    wartosc: Any
    nastepny = None

    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.nastepny = None


class LinkedList:
    def __init__(self):
        self.glowa = Node
        self.ogon = Node

    def __str__(self):
        temp = self.glowa
        wynik = str(temp.wartosc)
        while temp.nastepny:
            temp = temp.nastepny
            wynik += " -> " + str(temp.wartosc)
        return wynik

    def push(self, wartosc: Any) -> None:
        nowe = Node(wartosc)
        nowe.nastepny = self.glowa
        self.glowa = nowe

    def append(self, wartosc: Any) -> None:
        nowe = Node(wartosc)
        if self.glowa is None:
            self.glowa = nowe
        else:
            temp = self.glowa
            while temp.nastepny:
                temp = temp.nastepny
            temp.nastepny = nowe
            self.ogon = nowe

    def node(self, na: int) -> Any:
        licznik = 1
        temp = self.glowa
        while temp.nastepny:
            if licznik == na:
                break
            temp = temp.nastepny
            licznik += 1
        if licznik == na:
            return temp
        else:
            return "blad"

    def insert(self, value: Any, after: Node) -> None:
        temp = self.glowa
        while temp.nastepny:
            if temp.wartosc == after.wartosc and temp.nastepny == after.nastepny:
                break
            temp = temp.nastepny
        tym = Node(value)
        tym.nastepny = temp.nastepny
        temp.nastepny = tym

    def pop(self) -> Any:
        temp = self.glowa
        self.glowa = temp.nastepny
        return temp.wartosc

    def remove_last(self) -> Any:
        temp = self.glowa
        while temp.nastepny.nastepny:
            temp = temp.nastepny
        tym = temp.nastepny
        temp.nastepny = None
        return tym.wartosc


saf = LinkedList()
saf.glowa = Node(12)
n1 = Node(10)
saf.glowa.nastepny = n1
saf.push(7)
saf.append(2)
saf.insert(1, n1)
print(saf)
print(saf.remove_last())
