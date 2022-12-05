from game.create_maze import maze_data
from game.maze import MazeTemplate, Searcher, Riches

def main():
    print("Hello!\n It's the maze game")
    load_file = input("You can load text data?\ntype 1 - yes, 0 - no")
    if load_file == 1:
        path = input('Type path')
        points, searcher, treasure, x_max, y_max = maze_data(path)
    else:
        points, searcher, treasure, x_max, y_max = maze_data('maze.txt')
    maze = MazeTemplate(row=x_max, col=y_max, points=points)
    print("Let's go for treasure")
    searcher = Searcher(searcher[0],searcher[1])
    riches = Riches(treasure[0], treasure[1])
    while searcher.again:
        searcher.exit_maze(maze)
        if searcher.again:
            searcher.show(maze)
            searcher.check(maze, riches)
            maze.create_maze()
    print('And now you can go home')
    if riches.info:
        print('You go home taking digital, non-linear bitcoins with you')
    else:
        print('You go home after a pleasant walk 😊')

if __name__ == '__main__':
    main()