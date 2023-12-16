
print('''
      

                                   ]=I==II==I=[
                                    \\__||__//                 ]=I==II==I=[
               ]=I==II==I=[          |.. ` *|                   \\__||__//
                \\__||__//           |. /\ #|                    |-_ []#|
                 | []   |            |  ## *|                    |      |
                 |    ..|            | . , #|                  ]=I==II==I=[
 ___   ____  ___ |   .. |         __ |..__.*| __                \\__||__//
 ] I---I  I--I [ |..    |        |  ||_|  |_|| |                 |    _*|
 ]_____________[ | .. []|         \--\-|-|--/-//                 |   _ #|
  \_\| |_| |/_/  |_   _ | _   _   _|      ' *|                   |`    *|
   |  .     |'-'-` '-` '-` '-` '-` | []     #|-|--|-_-_-_-_ _ _ _|_'   #|
   |     '  |=-=-=-=-=-=-=-=-=-=-=-|      []*|-----________` ` `   ]   *|
   |  ` ` []|      _-_-_-_-_  '    |-       #|      ,    ' ```````['  _#|
   | '  `  '|   [] | | | | |  []`  |  []    *|   `          . `   |'  I*|
   |      - |    ` | | | | | `     | ;  '   #|     .  |        '  |    #|
  /_'_-_-___-\__,__|_|_|_|_|_______|   `  , *|    _______+___,__,-/._.._.\
              _,--'    __,-'      /,_,_v_Y_,_v\\-'
      ''')

print("\n Welcome to Treasure Island.\nYour Mission is to find the treasure island.")

my_location = input(
    "You're at a croos road, Where do you want to go? Type \"left\" or \"right\" \n").lower()

if my_location == "left":
    next_location = input(
        "You come to a lake. There is an Island in the middle of the lake. type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    if next_location == "wait":
        arrive = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow amd one blue. Which color do you choose? \n").lower()
        if arrive == 'red':
            print("Burned by Fire.\nGame Over.")
        elif arrive == 'blue':
            print("Eaten By Beasts.\nGame Over.")
        elif arrive == 'yellow':
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over")

else:
    print("Fall into a hole. Game Over")
