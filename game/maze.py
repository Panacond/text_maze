SIGN = {
    "space": "🌳",
    "crossroads": "  ",
    "road_h": "||",
    "road_g": "==",
    "gate": "🧌🫥",
    "searcher": "😊",
}


class Point(object):
    def __init__(self, x, y, tag=" "):
        self.x = x
        self.y = y
        self.tag = tag

    def __str__(self):
        ret = str(self.x) + str(self.y)
        return ret


class MazeTemplate(object):
    def __init__(self):
        self.row = range(5)
        self.col = range(5)
        self.points = []

    def __str__(self):
        yo = 0
        lab = ""
        for p in self.points:
            if p.x == yo:
                lab += p.tag + " "
            else:
                lab += "\n" + p.tag + " "
            yo = p.x
        return lab

    def replace_tag(self, x, y, tag):
        for p in self.points:
            if p.x == x and p.y == y:
                i = self.points.index(p)
                self.points[i] = Point(x, y, tag)

    def find_tag(self, x, y):
        for p in self.points:
            if p.x == x and p.y == y:
                return p.tag

    def check_tag(self, x, y, test_tag):
        for p in self.points:
            if p.x == x and p.y == y and p.tag == test_tag:
                return True
        return False

    def empty_base(self):
        points = []
        for x in self.col:
            for y in self.row:
                point = Point(x, y, SIGN["space"])
                points.append(point)
        self.points = points

    def test_maze(self):
        new = (
            (0, 0, SIGN["crossroads"]),
            (0, 1, SIGN["road_g"]),
            (0, 2, SIGN["gate"]),
            (1, 2, SIGN["road_h"]),
            (2, 0, SIGN["crossroads"]),
            (2, 1, SIGN["road_g"]),
            (2, 2, SIGN["crossroads"]),
            (2, 3, SIGN["road_g"]),
            (2, 4, SIGN["crossroads"]),
            (3, 0, SIGN["road_h"]),
            (3, 2, SIGN["road_h"]),
            (3, 4, SIGN["road_h"]),
            (4, 0, SIGN["crossroads"]),
            (4, 2, SIGN["crossroads"]),
            (4, 3, SIGN["road_g"]),
            (4, 4, SIGN["crossroads"]),
        )
        if len(self.points) > 0:
            for p in new:
                for ip in self.points:
                    if p[0] == ip.x and p[1] == ip.y:
                        i = self.points.index(ip)
                        self.points[i] = Point(ip.x, ip.y, p[2])
        else:
            self.points = []
            for p in new:
                self.points += [Point(p[0], p[1], p[2])]


class Searcher(Point):
    def __init__(self, x, y, tag=SIGN['searcher']):
        super().__init__(x, y, tag)
        self.again = True

    def show(self, pat):
        pat.replace_tag(self.x, self.y, self.tag)
        print(pat)

    def exit_pat(self, maze):
        if maze.find_tag(self.x, self.y) == SIGN["gate"]:
            command = input("Do you want to leave? (+ or q,- or e)")
            if command == "q" or command == "+":
                self.again = False

    def monitor(self, pattern, riches):
        self.riches_find(riches)
        note = "You can go {}, type {} or {}"
        list_check = [
            [0, -1, "<-", "4", "a"],
            [0, +1, "->", "6", "d"],
            [-1, 0, "up⬆️", "8", "w"],
            [+1, 0, "down⬇️", "2", "x"],
        ]
        correct_tag = [SIGN["crossroads"], SIGN["gate"], SIGN["road_g"], SIGN["road_h"]]
        for i in list_check:
            tag = pattern.find_tag(self.x + i[0], self.y + i[1])
            if  tag in correct_tag :
                print(note.format(i[2], i[3], i[4]))
        go = None
        while go not in ("a", "4", "d", "6", "x", "2", "8", "w", "else"):
            go = input("Type your command:")
            for i in list_check:
                tag = pattern.find_tag(self.x + i[0], self.y + i[1])
                if tag in correct_tag and (go == i[3] or go == i[4]):
                    self.y += i[1]
                    self.x += i[0]
            print("Correct your command")

    def riches_find(self, riches):
        if self.x == riches.x and self.y == riches.y and riches.info == False:
            riches.replace_info


class Riches(Point):
    def __init__(self, x, y, tag="."):
        super(Riches, self).__init__(x, y, tag=".")
        self.info = False

    @property
    def replace_info(self):
        self.info = True
        print("💰 💰 💰  You found treasure 💰 💰 💰")
