# Prologue (Day 2):
# Reveal that Amelia has failed her tests.
# Introduce Everlyn as the top scorer in class.

label prologue_2:
    queue music "audio/music/sunny_day_happy.ogg"
    scene bg_classroom_05_day
    with fade

    a "Sigh..."
    show ame sad
    a "I hope I scored well... How do you think you did?"

    menu:
        "It was kinda hard.":
            show ame wonder
            a "Dude, stop being so humble."

        "I did it with my eyes closed.":
            show ame wonder
            a "Dude, stop being such a show off."

    scene bg_classroom_05_day
    show sm1_sensei_normal
    with dissolve
    teacher "I will be calling out your names in order for you to collect your test paper."
    teacher "Amelia!"

    hide sm1_sensei_normal
    show ame sad
    a "Why must my name start with A..."

    hide ame sad
    with dissolve
    l "..."

    show ame sad
    with dissolve
    menu:
        a "..."
        "So how was it?":
            a "Thanks for your concern."
            a "But my test scores are strictly confidential."
        "Failed?":
            show ame wonder
            a "You meanie!"
            a "My test scores are strictly confidential."
    l "..."

    scene bg_classroom_05_day
    show sm1_sensei_normal
    with dissolve
    teacher "Everlyn, you achieved the class highest score again, congratulations!"
    hide sm1_sensei_normal
    with dissolve
    show eve smile
    e "..."
    e "Thanks."

    hide eve smile
    with dissolve
    show ame sad
    a "Everlyn's not only pretty, but she's so smart too!"
    a "Why is life so unfair!\nHaaa..."
    menu:
        "You're pretty cute too.":
            show ame blush
            a "[name]!"
            a "You know that's not true!"
        "Some people are just way over us.":
            a "And water is wet."
    
    scene bg_classroom_05_day
    show sm1_sensei_normal
    with dissolve
    teacher "[name]!"
    n "I anxiously moved to the front of the classroom."
    n "75/100"
    n "I suppose it's still better than average."
    nvl clear
    nvl hide

    hide sm1_sensei_normal
    with dissolve
    show ame sad
    l "About my..."
    a "Don't tell me! You can't trick me like that!"
    show black
    with fade
    "Bell" "Dum dum dum dum"
    scene bg_classroom_05_day
    with fade
    show sm1_sensei_normal
    teacher "And that will be all for today."
    teacher "Amelia, follow me to the office, I have something to discuss with you."

    hide sm1_sensei_normal
    show ame smile
    with dissolve
    a "Haha, it seems that I have been captured."
    a "You should eat lunch without me, this might take some time."
    menu:
        "I'll wait.":
            show ame blush
        "Good luck!":
            show ame wonder
    a "Don't worry, I'll just grab some bread on the way back."
    a "I have a feeling this discussion will ruin my appetite anyway."
    a "See you later!"

    scene bg_classroom_05_day
    with dissolve
    n "Now that Amelia has left, I was reminded that I didn’t have any other friends in my class."
    n "As a man of few words, I must have done something amazing in my previous\
    life that my childhood friend would keep ending up in the same class as me."
    n "My attention wandered towards one of the larger cliques of my class."
    nvl clear
    nvl hide

    "Classmate B" "Hey, you coming for Karaoke later?"
    show kei smile
    "Classmate K" "Nah, I've got somewhere to go later."
    hide kei smile
    "I yawned."
    "It would surely be better to read my new ebook somewhere a little quieter."
    stop music fadeout 1.0
    jump prologue_3
