# Afternoon, game store: Show Kei buying a dating sim.
# You recognise the game, and he becomes less embarrassed.

label prologue_5:
    queue music "audio/music/chat_menu_happy.ogg"
    scene bg_resident_street_afternoon
    with fade

    show ame wonder
    voice "ame/why"
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
    voice "ame/laugh"
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
    voice "kei/whatsup"
    k "Amelia and [name]!"
    k "Whatever are you doing in this part of town?"
    k "Bringing your girlfriend to a GameMove shop, isn't that a little tacky?"

    show ame blush at left:
        zoom 0.8
    voice "ame/gasp"
    a "Wha!"
    a "Me and [name] are just friends!"
    a "Do you want me to tell everyone that you were buying Doki Doki..."
    show kei blush
    l "Amelia! Calm down."
    show ame sad
    a "I just... sorry..."

    scene bg_building_street_day
    show kei blush at center
    with dissolve
    voice "kei/sorry"
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
