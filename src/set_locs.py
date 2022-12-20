solution_squares = '''2 5 26
2 4 26
1 4 25
1 5 24
1 6 24
2 6 24
3 6 23
3 5 22
3 4 21
3 3 20
2 3 19
1 3 18
0 3 17
0 4 16
0 5 15
0 6 14
0 7 13
1 7 12
2 7 11
3 7 10
4 7 9
4 6 8
4 5 7
4 4 6
4 3 5
4 2 4
3 2 3
3 1 3
2 1 3
1 1 2
1 0 1
0 0 1'''.split('\n')
solution = set()
for line in solution_squares:
    r, c, _ = [int(s) for s in line.split()]
    solution.add((r, c))
print(solution)
