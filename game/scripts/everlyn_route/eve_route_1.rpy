# Outline:
# You meet eve again on the rooftop, and she looks to be at a difficult part of the game
# If you help her, she will start to complain about how nobody understands her, and the expectations on her
# She wishes she can be more carefree about everything. Such as her desire to be a software developer.
# She mentions that you were to help her with student council work, she might be able to help you. 

label eve_route_1_0:
    scene bg_rooftop_day
    show eve sad
    with fade

    "Seems like Everlyn is having trouble with a difficult part of the game."
    "Should I help her?"

    menu:
        "Ignore her.":
            jump day_manager
        "Help her.":
            jump eve_route_1_1

label eve_route_1_1:
    if debug_gameplay_only:
        $ stat_understand_flag += 1
        $ stat_eve_flag += 1
        jump day_end_manager
    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    l "Hey, I've played through that stage before. Let me show you the trick."
    voice "eve/good_afternoon"
    e "It's you."
    e "I don't mind if you sat next to me."
    e "But I rather complete this level relying only on myself."
    scene black
    with fade
    "Some time passes..."
    scene bg_rooftop_day
    show eve sad
    with fade

    voice "eve/sigh"
    e "Alright I give up, what's the solution to this problem?"
    l "Well, if you do this and this..."
    e "Wow, I would never have thought that there was a clue there..."
    show eve wonder
    e "You solved this by yourself?"

    l "Actually it was Amelia who helped me spot that hidden clue. Her eyes can be quite sharp."
    e "Amelia?"
    l "The girl who sits next to me in class."
    e "I don't think I talked to her before. In fact I don't think I really talked to anyone much in class."
    l "Wait, do you even know my name?"
    e "It's... Bob?"
    if name == "Bob":
        l "That's just a lucky guess."
    else:
        l "It's [name]."
    e "Sorry, it's just hard for me to remember names."
    e "So your name is [name], and the girl who sits next to you is Amelia?"
    l "Correct."
    e "You didn't tell anyone about me being here right?"
    l "Correct."
    e "About gacha game?"
    l "What would I even gain from that."
    show eve smile
    with dissolve
    voice "eve/thanks"
    e "Thank goodness."
    e "I don't know how others would treat me if they knew I played this..."
    e "Everyone thinks I'm just a boring good honour student, but I just don't want to cause any trouble."
    e "Just because I'm a little smarter than others doesn't mean I'll be good at being in the student council..."

    menu:
        "Woah, those are some heavy topics there.":
            show eve sad
            e "Sorry, I just got too excited that I have someone to talk to..."
            jump eve_route_1_2
        "I can't relate, but I can still offer a listening ear.":
            $ stat_eve_flag += 1
            show eve blush
            with dissolve
            e "Thanks..."
            e "You're the first person who properly tried to listen to me."
            jump eve_route_1_2


label eve_route_1_2:
    e "Anyway, if it's okay with you..."
    e "Can you help me with some student council work?"
    e "I'm not really good at dealing with others, but maybe it would go better with you by my side..."
    l "Sorry, but I have this project..."
    scene black
    with fade
    "You told Everlyn about how you want to submit a game for the cutural festival."
    scene bg_rooftop_day
    show eve smile
    with fade
    voice "eve/laugh"
    e "That's amazing!"
    e "It must take a lot of courage to be able to express yourself to the world."
    e "How about this."
    e "If you help me with student council work, I'll help you with the programming."
    e "I haven't told anyone yet, but I want to be a software developer in the future."
    e "I've been practising writing code by myself, but contributing to a project, it could be nice."
    e "So here's my number, and call me maybe?"

    scene bg_rooftop_day
    show eve smile
    with fade
    "You became more aware of the feelings of a misunderstood girl."
    "You felt your understanding go up!"
    $ stat_understand_flag += 1

    scene bg_rooftop_day
    show eve smile
    with fade
    voice "eve/goodbye"
    "You waved goodbye to Everlyn, and went home."
    jump day_end_manager
