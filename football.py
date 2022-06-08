def change_info(command, point):
    if command not in game_info:
        game_info[command] = [0, 0, 0, 0, 0]
    game_info[command] = [game_info[command][0] + 1,
                          game_info[command][1] + 1 if point == 3 else game_info[command][1],
                          game_info[command][2] + 1 if point == 1 else game_info[command][2],
                          game_info[command][3] + 1 if point == 0 else game_info[command][3],
                          game_info[command][4] + point]


game_info = {}
for _ in range(int(input())):
    data = input().strip().split(';')
    player1, goal1, player2, goal2 = data[0], int(data[1]), data[2], int(data[3])
    change_info(player1, 3 if goal1 > goal2 else 1 if goal1 == goal2 else 0)
    change_info(player2, 3 if goal2 > goal1 else 1 if goal1 == goal2 else 0)

for command in game_info:
    print('{}:{} {} {} {} {}'.format(command, *game_info[command]))
