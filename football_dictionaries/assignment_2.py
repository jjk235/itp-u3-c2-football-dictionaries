def players_by_position(SQUADS_DATA):
    new_dict={}
    for player in SQUADS_DATA:
        new_dict.setdefault(player['position'],[])
        new_dict[player['position']].append(player)
    return new_dict
