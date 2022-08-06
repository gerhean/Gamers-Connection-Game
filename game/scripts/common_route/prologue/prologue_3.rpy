# Everlyn playing puzzle games alone. 
# You recognise the game, and she lights up a little.

label prologue_3:
    show black
    with fade

    n "The stairs leading to the roof of the school's clubrooms building is among the most isolated places in school. \
    Not only is the place far from the classrooms, the roof door is also locked."
    n "Or at least, the door was supposed to be locked."
    nvl clear
    nvl hide

    "Noticing the light shining through the edges of the door, I slowly opened it..."

    scene bg_rooftop_day
    show eve wonder
    with fade
    queue music "audio/music/vntrack12_peaceful.mp3"

    "The top scorer of today's test is sitting on the rooftop."
    "Moreover, she is fiddling with her phone."

    l "..."

    show eve blush
    with dissolve

    e "Ah."

    "The device slipped from her grasp."
    "Unable to look away, I saw a brief flash of white"

    menu:
        "That loading screen...":
            pass
        "...is that Puzzle Impact?":
            pass
    
    e "No... how could it be possible that an honour student such like myself"

    e "Would be playing this s***ty MTX infested gacha game?"
    
    menu:
        "MTX infested?":
            pass
        "Gacha game?":
            pass
    
    e "!!!"
    e "Don't you dare tell anyone about this!"
    l "Meh."
    l "But if you need any pointers for that game, just let me know."
    e "You realy won't?"
    l "No."
    l "I won't even tell anyone how abused your position to be on the roof."
    l "That is, if you let me stay here too."
    show eve sad
    e "Fine."

    scene bg_rooftop_day
    with dissolve
    "I moved to an area by the stairwell, near to where Everlyn is."
    "Shaded from the sun, yet blown by the gentle breeze."
    "Armed with a melon bread on one hand, and a tablet on the other."
    "It is truly the perfectly quiet place to read my newly bought ebook on game design."
    stop music fadeout 1.0
    scene black
    with fade
    jump prologue_4
