#! /usr/bin/python3
import sys


class CityCounter:
    def __init__(self) -> None:
        self.city_list_list = []
        self.city_list_i = -1
        self.first = True

    def run(self, line: str):
        if line.isdigit() and self.first:
            self.first = False
        elif line.isdigit():
            self.city_list_i += 1
            self.city_list_list.append([])
        else:
            city_list = self.city_list_list[self.city_list_i]
            city_list.append(line)

    def print(self):
        for city_list in self.city_list_list:
            print(len(set(city_list)))


if __name__ == "__main__":
    cc = CityCounter()
    for line in sys.stdin:
        cc.run(line=line)
    cc.print()
