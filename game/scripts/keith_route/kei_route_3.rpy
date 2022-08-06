# Outline:
# Keith buys some props in town
# Ame stalks you, but gets discovered easily
# Ame helps Kei select the props to buy
# They discover that they have a lot in common in terms of gaming interests
# He realises that there is always someone who appreciates him for who he is.

label kei_route_3_0:
    scene bg_classroom_05_day
    show kei wonder
    with fade
    k "[name]! There's something I need to buy in town, will you acompany me?"
    menu:
        "Maybe another time.":
            k "Don't worry dude, I'll survive this!"
            jump day_manager
        "Lets go.":
            k "Thanks man!"
            jump kei_route_3_1

label kei_route_3_1:
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    scene bg_building_street_day
    with fade
    show kei smile
    l "So what exactly are we buying?"
    k """
    Well, since I have already finalised the script, we now need to look for costumes.

    The costumes owned by the drama club are in high demand.
    
    While we have people who can sew in our class,
    I would prefer for most of the costumes to be pre-made.

    That way, we can reduce the amount of work they need to do, and concentrate on the
    main characters.
    """ 
    l "You thought of all these by yourself? No wonder you were the popular choice to be elected for class representative."
    k "It's not really that hard."
    k "Just read the atmosphere, listen to what others are saying."
    l "It's an impossibility for a certain someone I can think of."
    k "She's just the exception to the rule, no big deal man."

    "Cat" "Nyaa..."

    k "Hey, it's that cat who sat on my lap a few days back!"
    l "You can tell?"
    k "Kinda. It's like recognising a familiar face."
    l "I wonder where the cat is headed..."

    show kei smile at right:
        zoom 0.8
    l "Amelia?"
    show ame blush at left:
        zoom 0.8
    
    stop music fadeout 1.0
    queue music "audio/music/chat_menu_happy.ogg"
    a "Geh. Bad kitty... How could you do this to me..."
    l "You were following us around?"
    show ame sad
    a "I'm sorry..."
    a "I saw the both of you leaving school together"
    a "And I just wanted to see what kind of person Keith is."
    l "Isn't that just stalking..."
    k "Hey [name], your gir-"
    k "Uhm I mean your childhood friend is just worried for you."
    k "I don't mind if she tags along."
    l "But Amelia, don't you need to study?"
    show ame smile
    a "Ehehe, I just need a break. I feel my head's gonna explode if I had to sit down any longer."
    l "I suppose a short break wouldn't hurt"
    l "Take the time to relax, so your mind is clearer for the next study session and all"
    a "Yes Mom!"
    show kei blush
    k "Ahem!"
    show ame blush
    a "Eep! Sorry... I kinda forgot you were there."
    k "It's fine, just get a room... Uhh so you don't disturb others, yea!"
    a "Ehehe..."

    $ stat_kei_flag += 1
    $ stat_creative_flag += 1
    "Route is under construction"
    jump day_end_manager