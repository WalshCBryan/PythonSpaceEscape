# room_map = [[1, 1, 1, 1, 1],
#             [1, 0, 0, 0, 1],
#             [1, 0, 1, 0, 1],
#             [1, 0, 0, 0, 1],
#             [1, 0, 0, 0, 1],
#             [1, 0, 0, 0, 1],
#             [1, 1, 1, 1, 1]
#             ]
#
# #this command will print the room map as a list of list,
# #not particularly helpful
# print(room_map)
#
# #a loop would print the room maps more appropriately
# for y in range (7):
#     print(room_map[y])
#
# #even though arrays are 0 based, the for loop wants the total
# #number of elements to parse through
#
# for y in range (7):
#     for x in range (5):
#         print("y=",y,"x=",x)
#     print()
# #nested loop syntax
#
# for y in range (7):
#     for x in range (5):
#         print(room_map[y][x], end="")
#     print()
#
#

room_map = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
            ]

WIDTH = 800
HEIGHT = 800

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar]

room_height = 7
room_width = 5

def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw,
                        (top_left_x + (x*30),
                         top_left_y + (y*30) - image_to_draw.get_height()))

