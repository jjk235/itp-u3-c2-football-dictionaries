
def players_by_country_and_position(SQUADS_DATA):
    new_country_dict={}
    for key,pos_dict in SQUADS_DATA.items():
     
        for pos_player in pos_dict:   
            new_country_dict.setdefault(pos_player['country'],{})
            new_country_dict[pos_player['country']].setdefault(pos_player['position'],[])
            
            new_country_dict[pos_player['country']][pos_player['position']].append(pos_player)
            
    return new_country_dict
