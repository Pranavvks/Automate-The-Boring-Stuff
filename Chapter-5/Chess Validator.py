def validate_board(dictionary):
    if 'bking' or 'wking' not in dictionary.values():
        return False

    bking=0
    wking=0
    for king in dictionary.values():
        if king == 'bking':
            bking += 1
        if king == 'wking':
            wking += 1
    if bking > 1 or wking >1:
        return False

   pieces_white = 0
   pieces_black = 0
   for item in dictionary.values():
       if item [0] == 'w':
           pieces_white += 1
       elif item[0] == 'b' :
          pieces_black += 1
    
    if pieces_black >=17 or white_player = 17:
        return False
    
    pawn_white = 0
    pawn_black = 0
    for p in dictionary.values():
        if p =='bpawn':
            pawn_black += 1
        elif p== 'wpawn':
            pawn_white += 1
    if pawn_black >8 or pawn_white > 8:
        return False
    board_location = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                  'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                  'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                  'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                  'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                  'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                  'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                  'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
    
    for location in dictionary.keys():
        if location not in board_location():
            return False

    for pieces in board_dict.values():
        if pieces [0]!= "b" and pieces[0]!= "w":
            return False
    
    names = ["king","knight" "bishop","rock","queen","king"]
    
    for pieces in dictionary.values():
        if pieces[1:] not in piece_names:
            return False
