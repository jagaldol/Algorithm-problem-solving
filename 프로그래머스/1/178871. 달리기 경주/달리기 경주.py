def solution(players, callings):
    ranking = {player: idx for idx, player in enumerate(players)}
    
    for calling in callings:
        rank = ranking[calling]
        
        ranking[calling] , ranking[players[rank - 1]] = ranking[players[rank - 1]], ranking[calling]
        players[rank], players[rank - 1] = players[rank - 1], players[rank]
        
        
    return players