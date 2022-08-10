# Class elects Keith to organise the class exhibit

label prologue_4:
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
    voice "kei/sorry"
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
    voice "kei/yeah"
    k "...Alright then! I'll do my best not to let you down!"
    hide kei smile

    show ame wonder
    a "Poor Keith."
    l "Agreed."
    stop music fadeout 1.0
    hide ame wonder
    jump prologue_5
