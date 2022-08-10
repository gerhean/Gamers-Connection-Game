label ame_generic_1:
    scene bg_library_day
    show ame smile
    with fade

    voice "ame/hey"
    a "Hey, wanna study together again?"
    menu:
        "Just checking up on you.":
            voice "ame/bye"
            a "Aww..."
            jump day_manager
        "I would love to":
            voice "ame/laugh"
            a "Thanks!"

    stop music fadeout 1.0
    queue music "audio/music/vntrack04_adventure.mp3"
    "You sat down beside Amelia, and took out your tablet to read your e-book on software engineering."
    scene bg_library_day
    show ame wonder
    with fade

    a "Hey [name], about this problem..."
    "The library was a perfect place to study, and review existing knowledge with Amelia."
    "You felt your knowledge go up!"
    $ stat_knowledge_flag += 1
    jump day_end_manager
