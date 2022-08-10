# Outline:
# In the first week, Amelia had stopped coming over to your house.
# You can find her at the library in the first week afternoon period
# She reveals that she had failed her test, and need to get her grades up else she will be barred from participating in her club activity
# Of course, that meant she is unable to help you with your game project.
# She hints that if you were to help with her maths assessments, she might be able to dedicate some time to help you


label ame_route_1_0:
    scene bg_library_day
    show ame sad
    with fade

    voice "ame/hey"
    a "Hey, wanna study with me?"
    menu:
        "Just checking up on you.":
            voice "ame/bye"
            "Aww..."
            jump day_manager
        "I would love to":
            jump ame_route_1_1

label ame_route_1_1:
    if debug_gameplay_only:
        $ stat_knowledge_flag += 1
        $ stat_ame_flag += 1
        jump day_end_manager
    show ame smile
    stop music fadeout 1.0
    queue music "audio/music/chat_menu_happy.ogg"
    voice "ame/laugh"
    a "Wow really?"
    a "I hate to admit it, but since you scored so well, won't you be bored?"
    menu:
        "My dear Amelia,":
            pass
    menu:
        "It's because I studied that I scored well.":
            pass
    l "Besides, there are some books I wanna check out too."
    a "Thanks for being here with me."

    scene bg_library_day
    show ame wonder
    with fade

    a "Hey [name], about this problem..."
    "By teaching others, you also reviewed your own knowledge."
    "You felt your knowledge go up!"
    $ stat_knowledge_flag += 1

    scene bg_resident_street_afternoon
    show ame smile
    with fade

    a "Man, I'm beat!"
    a "Studying together really helps keep me motivated!"
    voice "ame/laugh"
    a "You know how I wanted to be an artist when I grew up right?"
    a "That's why I never really cared about my grades."
    a "But Mr Smith told me that I couldn't participate in the cultural festival if I didn't pass the next test."
    a "I asked him why an artist might need math, but he just talked about how artists are paid poorly!"
    a "He is right, but I can't let go of my passion so easily!"
    a "So now I'm finally forced to study."
    a "I really wanted to help with your game project too, but I need to study first..."
    a "Hey, you haven't talked at all."
    a "Am I just being a bother to you?"

    menu:
        "Let's talk about something more fun.":
            jump ame_route_1_2
        "I'll always be here to listen to you.":
            $ stat_ame_flag += 1
            jump ame_route_1_3


label ame_route_1_2:
    scene bg_resident_street_afternoon
    show ame sad
    with dissolve
    a "I knew it..."
    a "Sorry, but I'm not really in the mood."
    a "Maybe next time!"
    jump day_manager


label ame_route_1_3:
    l "After all, that's what friends are for."
    l "And I'm really happy too, that you consider me your closest friend."

    scene bg_resident_street_afternoon
    show ame blush
    with dissolve
    voice "ame/gasp"
    a "[name]!"
    a "I knew I can count on you!"
    a "You know, if you help me with my studying more, I might still have time to help you."
    a "It might mean less time with my games, but anything for my closest friend!"

    scene black
    with fade
    "You walked home with Amelia."
    voice "ame/bye"
    a "Bye [name]!"
    jump day_end_manager
