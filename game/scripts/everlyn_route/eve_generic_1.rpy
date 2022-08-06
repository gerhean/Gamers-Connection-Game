# Outline:
# Help Eve with student council work

label eve_generic_1:
    scene bg_school_hallway_day
    show eve smile
    with fade

    l "Hey."
    e "Hey [name]. I'm a little busy right now."
    menu:
        "Got something to do.":
            e "Sorry..."
            jump day_manager
        "Do you need help?":
            e "Thanks!"

    stop music fadeout 1.0
    queue music "audio/music/vntrack06_nostal.mp3"
    scene club_room_day
    show eve wonder
    with fade

    e "Help go through these application forms for me..."
    "While rejecting overly ambitious cultural festival exhibits, you felt the amount of effort that went into them."
    "You felt your understanding go up!"
    $ stat_understand_flag += 1
    jump day_end_manager
