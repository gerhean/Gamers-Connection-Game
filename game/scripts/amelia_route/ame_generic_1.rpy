label ame_generic_1:
    scene bg_library_day
    show ame smile
    with fade

    l "Hey."
    a "Hey, wanna study together again?"
    menu:
        "Just checking up on you.":
            a "Aww..."
            jump day_manager
        "I would love to":
            a "Thanks!"

    stop music fadeout 1.0
    queue music "audio/music/vntrack06_nostal.mp3"
    "You sat down beside Amelia, and took out your tablet to read your e-book on software engineering."
    scene bg_library_day
    show ame wonder
    with fade

    a "Hey [name], about this problem..."
    "The library was a perfect place to study, and review existing knowledge with Amelia."
    "You felt your knowledge go up!"
    $ stat_knowledge_flag += 1
    jump day_end_manager
