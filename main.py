from game.create_maze import maze_data
from game.maze import GameMaze, Searcher, Riches

def main():
    print("Hello!\n It's the maze game")
    load_file = input("You can load text data?\ntype 1 - yes, 0 - no")
    if load_file == 1:
        path = input('Type path')
        points, searcher, treasure, x_max, y_max = maze_data(path)
    else:
        points, searcher, treasure, x_max, y_max = maze_data('maze.txt')
    maze = GameMaze(x=x_max, y=y_max, p=points)
    print("Let's go for treasure")
    searcher = Searcher(searcher[0],searcher[1])
    riches = Riches(treasure[0], [1])
    searcher.show(maze.sercher)
    while searcher.again:
        searcher.exit_pat(maze.sercher)
        if searcher.again:
            searcher.monitor(maze.sercher, riches)
            maze.template.create_maze()
            searcher.show(maze.template)
    print('And now you can go home')
    if riches.info:
        print('You go home taking digital, non-linear bitcoins with you')
    else:
        print('You go home after a pleasant walk 😊')

if __name__ == '__main__':
    main()