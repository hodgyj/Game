deaths=["A crossbow bolt flies straight through your head, Kirilling you instantly.",
"You feel something lightly hit you in the neck, and your vision fades to black.",
"A large axe swings from the ceiling cutting you in half, how did you not see that?",
"Is it getting hot in here? Oh. You are on fire, guess you should have seen that fire arrow coming.",
"The door slams shut as water starts pouring in from holes in the walls. Guess you're done here now.",
"Your Galaxy note 7 explodes in your pocket, probably should have left that in the office.",
"The walls rapidly begin to close in around. You hurry for the door behind you, but it's too late for you now.",
"A knight at the end of room spots you and charges ahead, impaling you with their lance in the heart.",
"A rabid dog drops down onto you, tearing at your throat until your weak struggles stop altogether.",
"Hot oil pours down onto you, burning you so badly you can't even breathe.",
"A loud buzzing sound emerges from the back of the room. Oh no! Not the Bees!",
"The runes begin to blink in a pattern, before you explode in a pulse of arcane energy.",
 "You prick yourself as you brush the wall, and feel an immense pain before falling to the floor.",
 "Your head overflows with complicated maths equations and late coursework, the pressure is too much and you fall.", 
 "A tombstone flies through the air and smacks into your head. Ironic, I guess.", 
 "A javelin is flung at you from the corner of your eye, and lands straight into your chest. Good catch moron.", 
 "A snake slithers up your leg, and bites you. Well you deserve to die to that, how slow ARE your reactions?\nThis also brings a new meaning to the phrase 'trouser snake'",
 "A holy hand grenade lands in front of you, HALLELUJAH! BOOM!",
 "Something spoopy happens, now you're dead.",
 "You smell the faintest elderberry in the distance, 'father?' before falling face first into the ground.",
 "The ground dissipates below you. Oh dear, you seem to have fallen into some kind of burning hell . . . at least it's warm.", 
 "The hallucinogen wears off, and as you realise the horrors you have been though, your very life leaves you.",
 "The pressure put on you by the publishers becomes too much to bear, \n you release a game with passive agressive deaths to show your displeasure."]

def kill_player():
    import random
    import time
    time.sleep(0.5)
    print(deaths[random.randrange(0, len(deaths))])
    time.sleep(3)
