# If game is completed:
# The last part of the story takes place at the IT club room
# If eve is r3 and high enough stat, she would become friends with IT club members.

# If game is not completed:
# You will explore the festival more until you are tired
# Eve spots the two of you and drags you to the stuco room
# She talks about how the IT club was a little upset that she bought an unfinished game
# The visual novel will the end here

label epilogue_3_incomplete_game:
    pause

label epilogue_3:
    if not game_completed_flag:
        jump epilogue_3_incomplete_game
    
    stop music fadeout 1.0
    queue music "audio/music/vntrack04_adventure.mp3"
    scene bg_school_hallway_day
    with fade
    show ame smile
    a "Come to think of it, I haven't seen how your game turned out in the end."
    a "Didn't you say that the IT club was hosting it?"
    a "There's still time to make it!"

    scene bg_school_hallway_day
    with fade
    show ame wonder
    a "Woah, what happened?"
    a "Why is there such a long queue outside the IT club's exhibit?"


label epilogue_3_normal:
    jump epilogue_4