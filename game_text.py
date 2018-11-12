libtsk4 = {
'next_lib' : 'none',
# right choice in 0 base count from the list of options
'right' : 2,
'alive' : [0,1],
'dead' : [3],
# description
'description':
"""You pick up the note and begin reading it:
"Dear Victim,
So sorry to do this to you, but you were very easy to kidnap.
Anyways, we are holding you here, against your will so that our government
can test our new mind controlling shampoo and conditioner.
We'd like to thank you for your invulentary participation,
so we left some milk and cookies on the dresser."
------------------------------------------------
You look up and notice milk and cookies on the dresser,
somehow you didn't notice them until this point.
You continued reading the note.
-------------------------------------------------
"Anyways, if you are wondering how much time you have left with your own mind;
don't think about it! We will be seeing you shortly...
With Love <3,
Your Evil Bureaucratic Government
"
-------------------------------
Darn, you think to yourself, as you pace back and forth.
It will only be a matter of days before they finish filling the paperwork
nessisary to test their mind controlling products.""",
# goal
'goal':
"""You need to escape, or do you???
Yes, you do, get out A$AP!""",
# choices
'choices':
["HULK SMASH THE DOOR!", 'Meditate', "Look Around", "Find Key"],
# results from choices
'results':
{"HULK SMASH THE DOOR!":
"You epicly run towards the door and you bounce right off of it like a tennis ball.",
'Meditate':
"This is a great idea. Your body relaxes and your mind clears but you are still trapped :(",
"Look Around":
"""Hey, a good idea, you look around the room aimlessly and just as you are about to give up,
you look under the bed and discover a secret hatch that has a note ontop of it.
The note reads:
"THIS IS NOT AN ESCAPE HATCH! DO NOT OPEN, YOU WILL NOT ESCAPE!"
You might be onto something...""",
"Find Key":
"""You look around the room in circles, and you cannot find the key so you keep
going in circles untill you pass out from exhaustion and die."""}}

libtsk3 = {
'next_lib' : libtsk4,
# right choice in 0 base count from the list of options
'right' : 2,
'alive' : [0,3],
'dead' : [1],
# description
'description':
"""As you awake, the light you just turned on shines in your face.
You can now see the room around you and you get up.
You try to open the door but, the knob won't budge.""",
# goal
'goal':
"""You should figure out why you are locked in a room.
Are you crazy? Were you kidnapped? What the heck is going on?""",
# choices
'choices':
["Ahh I don't know what's happening!", 'Panic!', "Don't Panic!", "Look for clues!"],
# results from choices
'results':
{"Ahh I don't know what's happening!":
"Yeah nobody really does...",
'Panic!':
"Nope. Bad Idea. You die instantly for no decernable reason",
"Don't Panic!":
"""Looks like someone has their towel with them. (Hitchhiker's Guide to the Galaxy ref. duh.)
As you "don't panic" you realize that there is a note on the nightstand where you broke the lamp!""",
"Look for clues!":
"""WHO DO YOU THINK YOU ARE???
Sherlock Homes? hah.
Not gonna work this time..."""}}

libtsk2 = {
'next_lib' : libtsk3,
'right' : 2,
'alive' : [1],
'dead' : [0],
# description
'description':
"""The light you just ran into, crashes into the ground
and brakes into pieces, you will need to find another light source.""",
# goal
'goal':
"""You should look for a lighswitch, one is on the wall. Duh.""",
# choices
'choices':
['get up and try to find the switch', 'go back to sleep', 'run as fast as you can in a random direction'],
# results from choices
'results':
{'get up and try to find the switch':
"You get up and trip over a T-shirt on the ground, your head violently smacks the table in front of the T-shirt and you die.",
'go back to sleep':
"You lay back down and try to fall asleep but the fact that you cannot find the lighswitch bothers you so much that you get back up.",
'run as fast as you can in a random direction':
"""Once again, thinking on your feet!
You run violently into the wall in the front of the room and luckly,
you find and flip the switch on, eligantly before you pass out."""}}

libtsk1 = {
'next_lib' : libtsk2,
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
