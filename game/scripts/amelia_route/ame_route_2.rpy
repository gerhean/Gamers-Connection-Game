# Outline:
# In the second week
# You try asking Amelia about what her project is, but she says it is a secret.
# Amelia reminisces how games have bought the two of you together,
# and wonders how long this will last

label ame_route_2_0:
    scene bg_library_day
    show ame sad
    with fade

    l "Hey."
    a "I can't seem to study properly today..."
    a "Wanna go out a bit?"
    menu:
        "There's something else I need to do.":
            voice "ame/bye"
            a "Aww..."
            jump day_manager
        "To where?":
            jump ame_route_2_1        

label ame_route_2_1:
    if debug_gameplay_only:
        $ stat_knowledge_flag += 1
        $ stat_ame_flag += 1
        jump day_end_manager
    hide ame sad
    show ame smile
    stop music fadeout 1.0
    queue music "audio/music/chat_menu_happy.ogg"
    a "Let's go to the town area then!"
    voice "ame/laugh"
    a "There's this book I really wanna buy!"
    "Student" "Shhh!"
    a "Ahaha... Sorry, we'll be going now..."

    scene bg_building_street_day
    show ame smile
    with fade

    a "Look! It's the new book on graphic design by Larry Johnson!"
    a "His books are all really easy to follow!"

    scene black
    with fade
    "You browsed and bought a few books on programming that you thought you might enjoy."
    "You felt your knowledge go up!"
    $ stat_knowledge_flag += 1
    scene bg_building_street_day
    show ame smile
    with fade

    a "[name]! I'm done with buying the book!"
    l "Your first book on graphic design is by this Johnson fellow too right?"
    hide ame smile
    show ame blush
    a "I still remember when you gave it to me for my birthday..."
    l "That was a long time ago."
    hide ame blush
    show ame smile
    voice "ame/laugh"
    a "I know, but the fact that you're still with me after so long makes me happy."
    a "Back when I only started drawing, you gave me the book"
    a "And you told me that I would be the greatest artist in the world."
    hide ame smile
    show ame blush
    a "Now that I'm a little more grown up, I can see that the road ahead might be bleak."
    a "Hey, you'll always be with me right?"
    menu:
        "I don't know...":
            l "We might go to different universities..."
            l "And we might grow apart."
            hide ame blush
            show ame sad
            a "I guess the world is just unfair like that."
        "Of course.":
            l "We might go to different universities..."
            l "But I'll always chase after you."
            $ stat_ame_flag += 1
            a "[name]!"
            a "Why are you being so unfair!"
            a "You better not go back on your promise..."

    scene bg_resident_street_afternoon
    with fade
    if stat_creative_flag >= 3:
        show ame sad
        a "You've been getting closer to Keith recently right?"
        a "I didn't have the best impression of him."
        a "You should introduce him to me someday so I can truly judge whether he is worthy of being your friend."
    else:
        show ame smile
        a "I wonder how the preparation for the class exhibit is going."
        l "I haven't being paying attention either."

    scene bg_resident_street_afternoon
    show ame smile
    a "But thanks for always helping me study!"
    a "I believe I can pass the make up test now!"
    if stat_understand_flag >= 3:
        a "You've been hanging out with Everlyn recently right?"
        a "Perhaps if we studied together, our grades would just shoot up."
        a "But I don't really like how cold and perfect she is."
        a "She just wears this fake smile like nothing bothers her."
        a "I'm not really sure if I really want to meet her."

    scene black
    with fade
    "You walked home with Amelia."
    voice "ame/bye"
    a "Bye [name]!"
    jump day_end_manager
