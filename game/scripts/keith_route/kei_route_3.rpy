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
    voice "kei/whatsup"
    k "[name]! There's something I need to buy in town, will you acompany me?"
    menu:
        "Maybe another time.":
            k "Don't worry dude, I'll survive this!"
            jump day_manager
        "Lets go.":
            k "Thanks man!"
            jump kei_route_3_1

label kei_route_3_1:
    if debug_gameplay_only:
        $ stat_creative_flag += 1
        $ stat_kei_flag += 1
        jump day_end_manager
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
    voice "kei/yeah"
    k "But she's just the exception to the rule, no big deal man."

    play sound "audio/sound/cat.ogg"
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
    voice "ame/why"
    a "Geh. Bad kitty... Why would you do this to me..."
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
    voice "ame/laugh"
    a "Ehehe, I just need a break. I feel my head's gonna explode if I had to sit down any longer."
    l "I suppose a short break wouldn't hurt"
    l "Take the time to relax, so your mind is clearer for the next study session and all"
    a "Yes Mom!"
    show kei blush
    k "Ahem!"
    show ame wonder
    voice "ame/gasp"
    a "Eep! Sorry... I kinda forgot you were there."
    k "It's fine, just get a room... Uhh so you don't disturb others, yea!"
    a "Ehehe..."

    scene bg_building_street_day
    show kei smile at right:
        zoom 0.8
    show ame smile at left:
        zoom 0.8
    with fade
    voice "ame/hey"
    a "We're buying costumes right?"
    k "That's right!"
    a "As a member of the art club, I am clearly the best canditate for this job!"
    l "Whatever happened to your dislike of Keith?"
    a "He's just, more cheerful than I expected. I guess we just caught him at a bad time that day."
    k "Hey, not so loud, what if someone hears you?"
    a "There's no way we'll meet anyone we know here, just look around."
    k "Haa... I suppose so."

    scene black
    with fade
    a "Ooh, this costume looks pretty!"
    "By picking out costumes, you gained a deeper appreciation for asthetics."
    play sound "audio/sound/statup.ogg"
    "Your creativity went up!"
    $ stat_creative_flag += 1

    scene bg_building_street_day
    show kei smile at right:
        zoom 0.8
    show ame smile at left:
        zoom 0.8
    with fade
    k "That should be all right?"
    a "Yep, I'm sure everyone will be delighted by my superior taste in fashion."
    l "You think too highly of yourself."
    stop music fadeout 1.0
    queue music "audio/music/good_news_drama.ogg"

    k "Honestly, I'm envious of the two of you."
    show kei blush
    k "Just talking about anything and everything without a care for the world."
    k "Even I'm getting affected by it."
    show kei smile
    voice "kei/laugh"
    k "Don't you feel embarrassed at times?"

    a "Nah... being an artist is all about being able to express yourself."
    a "To be able to experience all the different emotions, and to tell others about them."
    a "You try too hard to please other people."
    a "But we only have like what, seventy years to live?"
    a "Better to tell others what you want, instead of regretting it for life."
    voice "kei/wow"
    k "I'm surprised. I sure didn't expect this from the only student who failed math."
    a "Hey! Enough about that! How about we talk about Doki Doki Photography Club?"
    show kei sad
    menu:
        l "Keith..."
        "Just go with the flow":
            l "Amelia is just energetic like that."
            voice "kei/sorry"
            k "Sorry, I'm not really comfortable about this..."
        "You should think about what you really want":
            l "Are you really comfortable talking about this in a public area?"
            l "And Amelia, do think about how others would feel once in a while."
            show ame sad
            a "Sorry..."
            $ stat_kei_flag += 1
            show kei smile
            k "Man, I almost got sucked into the flow. Thanks for pulling me out."
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    k "Honestly, I do want to talk about that game."
    k "But not here."
    show kei smile
    k "If it's okay with you, wanna meet up at [name]'s house after the cultural festival ends?"
    show ame smile
    l "Sure."
    voice "ame/laugh"
    a "Yay! I love you [name]!"
    show kei blush
    k "Ahem."
    show ame emb
    a "...As a friend..."

    jump day_end_manager
