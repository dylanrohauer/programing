# sause
libtsk1 = {
'next_lib' : 'none',
'dead' : [2],
'right' : 1,
'alive' : [0],
# description
'description' :
"""You awake inside of a dark room.
You cannot see much, like not a lot stuff.
Yep.""",
# goal
'goal':
"""You should turn on the light before you go any further. Probably a good idea.""",
# choices
'choices' :
['look around','flail around in the dark', 'do nothing'],
# results from the choices
'results' :
{'look around' :
"You cannot see anything, how are you supposed to look in the dark.",
'flail around in the dark' :
"""Good Idea! Your body smashes into the wall until you notice a light sitting on the nightstand next to you.""",
'do nothing':
"Your breathing climbs to a dangerously slow pace and you die."}}
