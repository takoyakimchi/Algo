N, player_atk = map(int, input().split())
rooms = []
player_hp = 0
lowest_hp = 0

for _ in range(N):
    rooms.append(map(int, input().split()))

for info in rooms:
    room_type, atk, hp = info
    # 몬스터 방
    if room_type == 1:
        # hp 100 player_atk 50인 경우 2대 치고 1대 맞음
        # hp 100 player_atk 49인 경우 3대 치고 2대 맞음
        attack_amount = hp // player_atk
        if hp % player_atk != 0:
            attack_amount += 1

        player_hp -= atk * (attack_amount - 1)
        if player_hp < lowest_hp:
            lowest_hp = player_hp

    # 포션 방
    elif room_type == 2:
        player_atk += atk
        player_hp += hp
        if player_hp > 0:
            player_hp = 0

    # print("atk: {}, hp: {}".format(player_atk, player_hp))

print(-lowest_hp + 1)