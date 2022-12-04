from game.maze import MazeTemplate, Searcher, Riches, SIGN

def main():
    maze = MazeTemplate() 
    maze.empty_base()
    maze.test_maze()
    pattern_move = MazeTemplate() 
    pattern_move.test_maze()
    print("Let's go for treasure")
    searcher = Searcher(0,2, SIGN['searcher'])
    riches = Riches(4, 0, SIGN['crossroads'])
    searcher.show(maze)
    while searcher.again:
        searcher.exit_pat(pattern_move)
        if searcher.again:
            searcher.monitor(pattern_move, riches)
            maze.test_maze()
            searcher.show(maze)
    print('And now you can go home')
    if riches.info:
        print('You go home taking digital, non-linear bitcoins with you')
    else:
        print('You go home after a pleasant walk 😊')

if __name__ == '__main__':
    main()