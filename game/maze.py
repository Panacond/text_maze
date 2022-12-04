from game.create_maze import test_mase, SIGN


class Point(object):
    def __init__(self, x, y, tag=" "):
        self.x = x
        self.y = y
        self.tag = tag

    def __str__(self):
        ret = str(self.x) + str(self.y)
        return ret

x, y, p = test_mase()

class MazeTemplate(object):
    def __init__(self, row= x, col = y, points =p):
        self.row = row
        self.col = col
        self.points = []
        self.list_points = points
        self.template = self.empty_base()
        self.template = self.create_maze()
        self.sercher = self.create_maze()

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
        for x in range(self.col):
            for y in range(self.row):
                point = Point(x, y, SIGN["space"])
                points.append(point)
        self.points = points

    def create_maze(self):
        if len(self.points) > 0:
            for p in self.list_points:
                for ip in self.points:
                    if p[0] == ip.x and p[1] == ip.y:
                        i = self.points.index(ip)
                        self.points[i] = Point(ip.x, ip.y, p[2])
        else:
            self.points = []
            for p in self.list_points:
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
    def __init__(self, x, y, tag=SIGN["crossroads"]):
        super(Riches, self).__init__(x, y, tag=".")
        self.info = False

    @property
    def replace_info(self):
        self.info = True
        print("💰 💰 💰  You found treasure 💰 💰 💰")

class GameMaze:
    def __init__(self, x= x, y = y, p =p) -> None:
        self.template = MazeTemplate(x,y,p)
        self.template.empty_base()
        self.template.create_maze()
        self.sercher = MazeTemplate(x,y,p)
        self.sercher.empty_base()
        self.sercher.create_maze()
