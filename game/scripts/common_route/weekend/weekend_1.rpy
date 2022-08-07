default ame_ring_flag = False
default eve_ring_flag = False
default kei_ring_flag = False

default ame_weekend_count = 0
default eve_weekend_count = 0
default kei_weekend_count = 0

default max_weekend_count = 1

label weekend_1:
    play music "audio/music/vntrack20_funky.mp3"
    scene bg_room_noon
    with fade
    "It is a lovely weekend!"
    "A good day to work on my game."
    $ ame_ring_flag = False
    $ eve_ring_flag = False
    $ kei_ring_flag = False
    jump weekend_1_call

menu weekend_1_call:
    "Who should I call for help?"
    "Amelia" if not ame_ring_flag:
        "Phone" "Ring... Ring..."
        if ame_weekend_count < max_weekend_count:
            jump ame_weekend_1
        else:
            a "Thanks for calling me, but I'm stuck studying..."
            $ ame_ring_flag = True
            jump weekend_1_call
    "Everlyn" if not eve_ring_flag:
        "Phone" "Ring... Ring..."
        if eve_weekend_count < max_weekend_count:
            jump eve_weekend_1
        else:
            a "Sorry, but I'm a little busy."
            $ eve_ring_flag = True
            jump weekend_1_call
    "Keith" if not kei_ring_flag:
        "Phone" "Ring... Ring..."
        if kei_weekend_count < max_weekend_count:
            jump kei_weekend_1
        else:
            a "Sorry man, but there's something I need to deal with."
            $ kei_ring_flag = True
            jump weekend_1_call

label ame_weekend_1:
    scene bg_room_noon
    show ame smile_casual
    with fade
    if stat_knowledge_flag <= 3:
        a "Yay, thanks for inviting me!"
        a "But I can only help you for a short while before it's back to studying for me..."
        a "But I'll try my best!"
    else:
        a "Yay, thanks for inviting me!"
        a "Since you helped me lots with my studying, I will also put in more effort into my art."
    show screen game_progress_menu_ui
    "As always, you are impressed by the quality of artwork which Amelia produced."
    $ creative_progress += 3 * (stat_knowledge_flag - 1)
    "The art for your game is now closer to being done!"
    call self_game_progress from _call_self_game_progress
    a "I had a lot of fun!"
    a "After I'm done with my test, I'll sure to spend more time with you!"
    $ ame_weekend_count += 1
    jump day_end_manager

label eve_weekend_1:
    scene bg_cafe_day
    show eve smile_casual
    with fade
    if stat_understand_flag <= 3:
        if eve_weekend_count == 0:
            e "This is the first time I ever went out with a friend..."
        e "Thanks for inviting me, but I'm still a little nervous."
        e "Please take care of me."
    else:
        e "A nice cup of coffee is always a good way to destress."
        e "Thanks for always helping me with work, I'll be sure to return the favour."
    scene bg_cafe_day
    show eve smile_casual
    with fade
    show screen game_progress_menu_ui
    "You are in awe of Everlyn's coding skills."
    $ knowledge_progress += 3 * (stat_understand_flag - 1)
    "The code for your game is now closer to being done!"
    call self_game_progress from _call_self_game_progress_1
    e "I feel much more relaxed now."
    scene bg_cafe_day
    show eve blush
    e "Looking forward to going out with you again."
    $ eve_weekend_count += 1
    jump day_end_manager

label kei_weekend_1:
    scene bg_cafe_day
    show kei smile_casual
    with fade
    if kei_weekend_count == 0:
        k "This is the first time I ever came to this cafe!"
    if stat_creative_flag <= 3:
        k "It has always been my dream to develop a game."
        k "Being able to work together with you, I'm all pumped up!"
    else:
        k "There's just something about this cafe that's really chill."
        k "Thanks for always helping me, I'll also try my best to help you out!"
    scene bg_cafe_day
    show kei smile_casual
    with fade
    show screen game_progress_menu_ui
    "You are impressed by Keith's extensive knowledge on games."
    $ understand_progress += 3 * (stat_creative_flag - 1)
    "You are now clearer about the design of the game!"
    call self_game_progress from _call_self_game_progress_2
    k "Thanks for hanging out with me dude."
    a "Let's hang out again sometime alright?"
    $ kei_weekend_count += 1
    jump day_end_manager
