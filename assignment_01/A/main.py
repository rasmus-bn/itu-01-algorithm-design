#! /usr/bin/python3
import sys


class QueueNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self._last: QueueNode = None
        self.next: QueueNode = None

    def add(self, value):
        node = QueueNode(value)
        if self._last:
            self._last.next = node
            self._last = node
        else:
            self.next = node
            self._last = node

    def pop(self) -> QueueNode:
        return_value = None
        if self.next:
            return_value = self.next
            if self.next == self._last:
                self.next = None
            else:
                self.next = self.next.next
        if self.next is None:
            self._last = None
        return return_value

    def is_empty(self):
        return self._last is None


class Person:
    def __init__(self, line: str) -> None:
        names = line.split()
        self.name = names.pop(0)
        self.priorities = Queue()
        for name in names:
            self.priorities.add(value=name)


def run(input):
    first_line = True

    people = Queue()
    people_dict = {}
    pairs = []

    for line in input:
        if first_line:
            first_line = False
            continue
        p = Person(line=line)
        people_dict[p.name] = p
        people.add(p)


    while not people.is_empty():
        p = people.next()




    print(people)


if __name__ == "__main__":
    run(input=sys.stdin)
