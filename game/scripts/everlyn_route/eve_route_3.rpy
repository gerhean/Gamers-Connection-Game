# Outline:
# Eve will need to talk to Kei about the progress of the class play.
# You encourage eve to use this opportunity to know her classmates more.
# Then you discovered a surprising story in which Keith had confessed his feelings to Eve once.
# Although Eve offered to remain friends, Kei avoided her, leading to awkwardness.
# With your support, Keith was able to talk about how ashamed he was that he never actually loved eve.
# Eve forgives him

label eve_route_3_0:
    scene bg_school_hallway_day
    show eve wonder
    with fade

    e "Hey [name]. I need to meet the class representatives, and I'm a little nervous."
    e "Will you support me?"
    menu:
        "Maybe some other time...":
            e "Thanks anyway..."
            jump day_manager
        "No problem.":
            e "I'm grateful for your assistance."

label eve_route_3_1:
    stop music fadeout 1.0
    queue music "audio/music/vntrack02_confront.mp3"
    scene bg_classroom_05_day
    show eve smile
    with fade
    "Student" "Can't you just give some leeway?"
    e "Sorry, but these school regulations exist for a reason."
    e "I am sure you are aware of why. If you feel they are too strict, do submit an appeal to the president."
    "Student" "How did such a beauty turn out to be such a wet blanket..."
    e "I..."
    "Student" "Come on, what's so bad about having a little more fun..."
    l "Please stop, or I'll report you for harassment."
    hide eve smile
    with dissolve
    "I walked in between the space seperating them, and stared harshly at the student."

    "Student" "Tch."
    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    show eve sad
    with dissolve
    e "He walked away..."
    e "Thanks [name]. I don't think anything too serious would have happened, but I'm still glad you stood up for me."
    e "Even though I was doing the right thing."
    e "Was there something I could have done better?..."
    l "Sorry... I'm not really sure either."

    e "In any case, the next, and last class we need to review is ours."
    e "Our class representative has yet to submit the finalised proposal..."    
    
    scene bg_classroom_05_day
    show eve smile at right:
        zoom 0.8
    with fade
    e "If I remember correctly, the class representative Keith has blonde hair..."
    l "You know, this can be a great chance to get to know him better."
    l "Try to ask him out for tea break or something."
    e "But..."

    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    show kei smile at left:
        zoom 0.8
    k "Hey [name]!"
    k "And Everlyn..."
    k "What are you two doing together?"
    e "Hello Keith. I have teamed up with [name] to collect the finalised proposal for the class play."
    k "Sorry, give me a little more time to finish it."
    k "I'll submit it by the end of today."
    k "Catch you later [name]!"

    hide eve smile
    show eve wonder at right:
        zoom 0.8
    e "Wait!"
    e "Keith, if you do not mind, I would like to have a short tea break with you."
    l "That sure came out wrongly..."
    e "Huh?"
    show kei sad at left:
        zoom 0.8
    k "Man, I know that the finalised proposal is important."
    k "But I'm not a child who needs to be supervised."
    hide eve wonder
    show eve sad at right:
        zoom 0.8
    e "No..."

    $ stat_eve_flag += 1
    $ stat_understand_flag += 1
    "Route is under construction"
    jump day_end_manager
