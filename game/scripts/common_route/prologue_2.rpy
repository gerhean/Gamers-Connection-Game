# Prologue Part 1 (Day 2):
# Outline:
# Classroom: Reveal that Amelia has failed her tests. 
# Introduce Everlyn as the top scorer in class. Class elects Keith to organise the class exhibit

# Lunch, classroom: Show Kei as the popular guy. Due to the classroom being noisy, 
# you left in search of a quieter place to eat your lunch

# Lunch, stairs: Everlyn playing puzzle games alone. 
# You recognise the game, and she lights up a little.

# Afternoon, game store: Show Kei buying a dating sim. You recognise the game, and he becomes less embarrassed.


label prologue_2_1:
    # Reveal that Amelia has failed her tests.
    # Introduce Everlyn as the top scorer in class.
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
    jump prologue_2_2


label prologue_2_2:
    # Everlyn playing puzzle games alone. 
    # You recognise the game, and she lights up a little.
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
    jump prologue_2_3


label prologue_2_3:
    # Class elects Keith to organise the class exhibit
    queue music "audio/music/sunny_day_happy.ogg"
    "Bell" "Dum dum dum dum"
    scene bg_rooftop_day
    with fade
    "Lunch break passed by in a flash."
    "When I looked up from my tablet, Everlyn was already gone."
    "Thank goodness she did not leave the roof door locked after leaving."

    scene bg_classroom_05_day
    with fade
    "I reached the classroom just in time."
    show sm1_sensei_normal
    teacher "As you would all know, the school's yearly cultural festival will be happening next month."
    teacher "A month might seem like a long time,"
    teacher "But it will pass you by quickly."
    teacher "First, we will need a class representative."
    teacher "Is anyone willing to volunteer?"

    "..."

    teacher "Any nominations then?"

    hide sm1_sensei_normal

    "Classmate B" "I nominate Keith! He's totally got the vibes to lead this!"

    show kei smile
    k "No way! I can't handle such a large responsibility!"
    hide kei smile

    "Classmate C" "Keith is kind and charasmatic. I don't mind if he takes this role."

    show kei smile
    k "Guys, I..."
    hide kei smile

    "Classmate D" "I think Keith is good too!"

    show sm1_sensei_normal
    teacher "So I take it that Keith will be the class representative for the cultural festival?"
    teacher "It's settled then."
    teacher "Keith, come to my office later, you will be briefed about the responsibilities of the the class representative."
    hide sm1_sensei_normal

    show kei smile
    k "...Alright then! I'll do my best not to let you down!"
    hide kei smile

    show ame wonder
    a "Poor Keith."
    l "Agreed."
    stop music fadeout 1.0
    hide ame wonder


label prologue_2_4:
    # Afternoon, game store: Show Kei buying a dating sim.
    # You recognise the game, and he becomes less embarrassed.
    queue music "audio/music/chat_menu_happy.ogg"
    scene bg_resident_street_afternoon
    with fade

    show ame wonder
    a "I can't believe I failed the test!"
    a "I know I promised to play Monster Hunter with you."
    a "But I've got to study for my supplementary tests!"
    a "Why are tests so hard anyway? Do we really need to use math in our daily lives?"
    l "I would think that most jobs would need math..."
    l "Anyway, we're here."

    scene bg_building_street_day
    with fade

    l "Buying a physical game still feels so much better than buying digital."
    show ame smile
    a "I totally get you!"
    a "But coming here feels like I'm delaying the inevitable."
    show ame sad
    a "I need to study, but those new games..."
    show ame smile
    l "This is why your grades are always terrible..."

    scene bg_building_street_day
    show kei smile at right
    with dissolve
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    l "???"
    a "That's Keith from our class right?"
    l "And he's buying Doki Doki Photography Club?"
    k "!!!"
    hide kei smile
    show ame wonder
    a "Seems like he noticed us."
    hide ame wonder

    show kei smile at right:
        zoom 0.8
    k "Amelia and [name]!"
    k "Whatever are you doing in this part of town?"
    k "Bringing your girlfriend to a GameMove shop, isn't that a little tacky?"

    show ame blush at left:
        zoom 0.8
    a "Wha!"
    a "Me and [name] are just friends!"
    a "Do you want me to tell everyone that you were buying Doki Doki..."
    show kei blush at right:
        zoom 0.8
    l "Amelia! Calm down."
    hide ame blush
    show ame sad at left:
        zoom 0.8
    a "I just... sorry..."

    scene bg_building_street_day
    show kei blush at center
    with dissolve
    k "No, it's my fault for suggesting it in the first place."
    k "Also, can you two keep it a secret that I was here?"
    k "I don't know how you can live without caring about others' opinion of you,\
    but I need to maintain my social image."

    l "Don't worry, we aren't like you."
    l "We won't pointlessly gossip about what you do in your personal life."
    l "People should be able to live however they want if it doesn't harm others."
    scene bg_building_street_day
    show ame blush
    "[name]..."
    scene bg_building_street_day
    show ame sad at left:
        zoom 0.8
    show kei sad at right:
        zoom 0.8
    with dissolve
    k "That's kinda harsh man..."
    k "I'll be getting out of your face. Just forget ever meeting me here alright?"
    stop music fadeout 1.0
    queue music "audio/music/chat_menu_happy.ogg"
    scene bg_building_street_day
    show ame sad at center
    with dissolve
    a "He completely ruined the mood!"
    a "Go on without me, I'll just go home to study..."
    
    menu:
        "Let's get some food to cheer you up.":
            pass
        "Let me walk you home then.":
            pass
    
    a "Thanks..."
    stop music fadeout 1.0
    jump day_end_manager
