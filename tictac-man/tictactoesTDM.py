#This program is being written by Dahlin Moeller, (3/15/2021) and only by me. I will be googling any syntax I don't understand, but otherwise
#I am working alone. I however will be comparing my work to the "solution" after I am done or if I am stuck for over 2 hours. This is being written at

def main():
    current_player = turn_order("")
    playspace = playspace_maker()
    while not (a_winner_is_you(playspace) or cats(playspace)):
        display_playspace(playspace)
        open_de_game(current_player,playspace)
        current_player = turn_order(current_player)
    display_playspace(playspace)
    print("GG Scrub. {in russian accent}")

#this section is from the solution
def display_playspace(playspace):
    print()
    print(f"{playspace[0]}|{playspace[1]}|{playspace[2]}")
    print('-+-+-')
    print(f"{playspace[3]}|{playspace[4]}|{playspace[5]}")
    print('-+-+-')
    print(f"{playspace[6]}|{playspace[7]}|{playspace[8]}")
    print()

def playspace_maker():
    playspace = []
    for space in range(9):
        playspace.append(space + 1)
    return playspace

def cats(playspace):
    all_your_base = True
    for space in range(9):
        if playspace[space] != "O" or playspace[space] != "X":
            all_your_base = False
    return all_your_base
       

def a_winner_is_you(playspace):
    return (playspace[0] == playspace[1] and playspace[1] == playspace[2] or
            playspace[3] == playspace[4] and playspace[4] == playspace[5] or
            playspace[6] == playspace[7] and playspace[7] == playspace[8] or
            playspace[0] == playspace[3] and playspace[3] == playspace[6] or
            playspace[1] == playspace[4] and playspace[4] == playspace[7] or
            playspace[2] == playspace[5] and playspace[5] == playspace[8] or
            playspace[0] == playspace[4] and playspace[4] == playspace[8] or
            playspace[2] == playspace[4] and playspace[4] == playspace[6])

def open_de_game(current_player, playspace):
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    yo_mama = "XBOX_LIVE!!!!!!!!!"
    so_american = "XBOX_LIVE!!!!!!!!!"
    while yo_mama == so_american:
        try:
            space = int(input(f"{current_player}, open de game. Choose space or die. (1-9): "))
            if playspace[space-1] == "X" or playspace[space-1] == "O":
                display_playspace(playspace)
                print("This territory is claimed by Bean Bois Encorpurated. Find different spot.")
            else:
                playspace[space - 1] = current_player
                yo_mama = "no"
        except:
            display_playspace(playspace)
            print("(Select 1-9. This isn't open world tic-tac-toe.)")


def turn_order(sushi_loving_player):
    if sushi_loving_player == "" or sushi_loving_player == "O":
        return "X"
    else:
        return "O"

if __name__ == "__main__":
    main()
