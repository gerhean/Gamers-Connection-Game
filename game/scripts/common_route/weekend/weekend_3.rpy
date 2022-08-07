# Invite two friends to rush the deadline of the game
# Only friends with r3 done can be invited
# If game cannot be done, you will game over.

default ame_ring_accept_flag = False
default eve_ring_accept_flag = False
default kei_ring_accept_flag = False

label weekend_3:
    stop music fadeout 1.0
    queue music "audio/music/vntrack20_funky.mp3"
    scene bg_room_noon
    with fade
    "It's the last weekend before the submission deadline of my game!"
    "I better call for help, and fast!"
    $ ame_ring_flag = False
    $ eve_ring_flag = False
    $ kei_ring_flag = False
    jump weekend_3_call

menu weekend_3_call:
    "Who should I call for help?"
    "Amelia" if not ame_ring_flag:
        "Phone" "Ring... Ring..."
        $ ame_ring_flag = True
        if stat_knowledge_flag >= 6:
            a "Yay! Thanks for inviting me!"
            $ ame_ring_accept_flag = True
        else:
            a "Thanks for calling me, but I'm stuck studying..."    
        jump weekend_3_call

    "Everlyn" if not eve_ring_flag:
        "Phone" "Ring... Ring..."
        if stat_understand_flag >= 6:
            a "Yay! Thanks for inviting me!"
            $ eve_ring_accept_flag = True
        else:
            a "Sorry, but I'm a little busy."
        $ eve_ring_flag = True
        jump weekend_3_call

    "Keith" if not kei_ring_flag:
        "Phone" "Ring... Ring..."
        if stat_creative_flag >= 6:
            k "Sure man, anything to help!"
            $ kei_ring_accept_flag = True
        else:
            a "Sorry man, but there's something I need to deal with."
        $ kei_ring_flag = True
        jump weekend_3_call
    
    "I'm ready!" if ame_ring_flag and eve_ring_flag and kei_ring_flag:
        jump weekend_3_work


label weekend_3_work:
    scene bg_room_noon
    with fade

    if ame_ring_accept_flag:
        show ame smile_casual
        a "The submission deadline is tomorrow night right?"
        a "We don't have much time left!"
        hide ame
    if eve_ring_accept_flag:
        show eve smile_casual
        e "This is my first time visiting a friend's house..."
        e "Since the deadline is near, I'll try to put in my best effort!"
        hide eve
    if kei_ring_accept_flag:
        show kei smile_casual
        k "Woah, your room's pretty cool!"
        k "But there's no time to play around right?"
        k "After all, the submission deadline is tomorrow!"
        hide kei

    show screen game_progress_menu_ui
    if ame_ring_accept_flag:
        scene bg_room_noon
        show ame smile_casual
        with fade
        "As always, you are impressed by the quality of artwork which Amelia produced."
        $ creative_progress += 3 * (stat_knowledge_flag - 1)
        "The art for your game is now closer to being done!"
    if eve_ring_accept_flag:
        scene bg_room_noon
        show eve smile_casual
        with fade
        "You are in awe of Everlyn's coding skills."
        $ knowledge_progress += 3 * (stat_understand_flag - 1)
        "The code for your game is now closer to being done!"
    if kei_ring_accept_flag:
        scene bg_room_noon
        show kei smile_casual
        with fade
        "You are impressed by Keith's extensive knowledge on games."
        $ understand_progress += 3 * (stat_creative_flag - 1)
        "You are now clearer about the design of the game!"
    scene bg_room_noon
    with fade
    call self_game_progress
    
    scene bg_room_evening_light_on
    with fade
    if eve_ring_accept_flag:
        show eve smile_casual
        e "Sorry, but I have to leave soon."
        e "There's work I need to do tommorrow as well, so I am not able to come over."
        e "Still, best of luck to you."
        hide eve
    if kei_ring_accept_flag:
        show kei smile_casual
        k "Woah, time really passed quickly! I'll have to go off soon."
        k "Anyway, I promised to meet up with my other friends tomorrow."
        k "So I won't be able to accompany you on the last stretch."
        k "Good luck, you're almost there!"
        hide kei
    
    if ame_ring_accept_flag:
        show ame emb_casual
        a "Hey, I need to prepare my own submission for the festival."
        a "So I can't help you tomorrow."
        hide ame