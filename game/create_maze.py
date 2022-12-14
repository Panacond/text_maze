SIGN = {
    "space": "🌳",
    "crossroads": "  ",
    "road_h": "||",
    "road_g": "==",
    "gate": "🧌🫥",
    "searcher": "😊",
}

def read_file (path):
    with open(path) as f:
        contents = f.read()
    list_row = contents.split('\n')
    for i in list_row:
        i = list(i)
    return list_row


DESIGNATIONS ={
    'g': SIGN["gate"],
    '-': SIGN["road_g"],
    '|': SIGN["road_h"],
    ' ': SIGN["space"],
    '+': SIGN["crossroads"],
    's': SIGN["crossroads"],
    'x': SIGN["crossroads"]
}

def maze_point(list_chapters):
    points = []
    x_max = len(list_chapters)
    y_max = 0
    for y, string in enumerate(list_chapters):
        y_max = len(string) if len(string) > y_max else y_max
        for x, character in enumerate(string):
            sign = DESIGNATIONS[character]
            if character == "s":
                searcher = [y,x]
            if character == "x":
                treasure = [y,x]
            points.append((y,x, sign))
    return points, searcher, treasure,  y_max, x_max


def maze_data(path):
    list_chapters = read_file (path)
    return maze_point(list_chapters)

def test_mase():
    row = 5 
    col = row
    points = (
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
    return row, col, points
