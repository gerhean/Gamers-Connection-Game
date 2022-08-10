# Outline:
# Help Keith with creating props for the cultural festival

label kei_generic_1:
    scene bg_classroom_05_day
    show kei smile
    with fade

    l "Hey."
    voice "kei/whatsup"
    k "What's up dude! I'll be working on the props for the play soon."
    menu:
        "Got something to do.":
            k "I got this dude, Don't worry!"
            jump day_manager
        "Do you need help?":
            k "I knew I can count on you dude!"

    stop music fadeout 1.0
    queue music "audio/music/vntrack04_adventure.mp3"
    scene bg_classroom_05_day
    show kei wonder
    with fade

    k "Huh, how are these things supposed to look like..."
    "With only vague instructions for the props, you had to draft out the designs."
    play sound "audio/sound/statup.ogg"
    "You felt your creativity go up!"
    $ stat_creative_flag += 1
    jump day_end_manager