# You went to watch the class play, since you are not involved in the performance.
# If stat_kei_flag < 2 or R3 not seen, then it will just be the standard Snow White
# Otherwise, it will be a weird gender reversed snow white

label epilogue_2:
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    scene bg_auditorium
    with fade
    show ame smile
    a "I can't wait to see how the class play will be like!"
    l "Me too. I was sick for the last few days so I didn't see the rehearsals at all..."
    l "I remember it was Snow White?"
    a "Look, the play is starting. Let's watch it quietly."
    hide ame
    if stat_creative_flag >= 6 and stat_kei_flag >= 2:
        jump epilogue_2_true
    else:
        jump epilogue_2_normal

label epilogue_2_enter_classroom:
    scene bg_classroom_05_day
    with fade
    stop music fadeout 1.0
    queue music "audio/music/chat_menu_happy.ogg"
    show ame smile at left:
        zoom 0.8
    if romance_target == "ame":
        "Classmate B" "Hey look! The idiot couple has arrived!"
        "Classmate C" "Amelia, congrats on the confession!"
        "Classmate B" "When will your wedding be at?"
        show ame emb
        a "Huh? I'm just his childhood friend..."
        a "I mean I'm his girlfriend now..."
        a "GAH! Just shut up!"
        l "Let's get married after we're done with university."
        l "After all you really need to concentrate on your studies."
        voice "ame/gasp"
        a "[name]! Here isn't the time to talk about this!"
        a "We can discuss this at home... Or somewhere with more privacy..."
        show kei smile at right:
            zoom 0.8
        k "Congrats on the wedding you two!"
        a "Just stop with the wedding thing!"
        k "Sorry, sorry."
        k "So what are you here for, if not to be teased?"
    else:
        show kei smile at right:
            zoom 0.8
        voice "kei/whatsup"
        k "What's up [name] and Amelia, what are you two here for."
    show ame smile
    return
    
label epilogue_2_normal:
    "Evil Stepmother" "Mirror, mirror on the wall, who's the fairest of them all?"
    scene black
    with fade
    n "It was a fairly standard Snow White story."
    n "Keith played the hunter who tried to hunt down Snow White, but was instead swayed by her beauty."
    n "The play ended when the prince kissed Snow White, and she woke up."
    nvl clear
    nvl hide

    scene bg_auditorium
    with fade
    show ame smile
    a "Honestly, the play was kind of boring."
    l "Still, shall we visit our classmates and see how they're doing?"
    a "Sure."

    call epilogue_2_enter_classroom from _call_epilogue_2_enter_classroom
    a "This is a little hard to ask, but..."
    l "Is that really it?"
    k "Even completing each other's sentences now..."
    k "I had this other idea, but we decided to just stick to the more socially acceptable script."
    k "After all, who would want to stand out from the crowd?"
    k "I wonder if things would have turned out differently if you two were more involved in the play."
    k "Since Amelia is one of the most creative person in our class and you're her closest friend."
    if romance_target == "ame":
        k "...Or boyfriend now."
        show ame emb
        voice "ame/gasp"
        a "!!!"
    k "But the past is in the past, it can't possibly change."
    show ame smile
    jump epilogue_2_ending

label epilogue_2_true:
    stop music fadeout 1.0
    queue music "audio/music/sunny_day_happy.ogg"
    "???" "Mirror, mirror on the wall, who's the strongest of them all?"
    a "Is that a guy?"
    l "Would that make him the Evil Stepfather?"
    "Mirror" "My master, you are the strongest of them all."
    "Evil Stepfather" "For as long as I live?"
    "Mirror" "No... The chosen one, Snow White... He will become stronger than you."
    "Evil Stepfather" "My stepson? Impossible! He must be rid of at once!"

    a "Hey look... Is that Keith?"
    show kei smile
    k "Whew, another good day of working out."
    k "My dream is to join the royal knights."
    k "So I ought to do a hundred push ups, a hundred sit ups, and run ten kilometers everyday!"
    show kei wonder
    stop music fadeout 1.0
    queue music "audio/music/vntrack02_confront.mp3"
    k "Huh? Bandits are attacking me!"

    scene bg_auditorium
    with fade
    "Narrator" "As hard as he tried to fight back, he couldn't win against so many armed men."
    "Narrator" "And so, he had no choice but to run away into the forest."
    "Narrator" "There, he found a small hut."
    show kei sad
    k "Help me..."
    "Dwarf 1" "Oh my, a wounded man."
    "Dwarf 2" "Is he dangerous?"
    k "I'll help you with the fields and clean the house."
    k "Please, I don't want to die..."
    "Dwarf 3" "He seems to be a sincere man."
    "Dwarf 4" "Let's help him!"

    scene bg_auditorium
    with fade
    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    "Narrator" "Luckily Snow White was able to survive."
    "Narrator" "For a year, he trained and helped the dwarfs."
    show kei smile
    k "Friends, I have stayed here for long enough. I must go now."
    "Dwarf 1" "If you stay here and train less, I am sure that no one will be able to find you!"
    k "Sorry, but I exist to exact justice on those who wronged me."
    k "I do not wish to put you in any more danger."
    k "So farewell"

    scene bg_auditorium
    with fade
    stop music fadeout 1.0
    queue music "audio/music/vntrack02_confront.mp3"
    "Narrator" "Eventually, Snow White reached the castle of the evil stepfather."
    "Evil Stepfather" "How are you still alive?"
    "Evil Stepfather" "Who are you, exactly?"
    k "I, I am Snow White."
    k "And Snow White will be the only thing you'll ever see after I punch your face out!"
    k "HIYAHHHH!"
    "Evil Stepfather" "ARGGGGGG!"

    scene bg_auditorium
    with fade
    show ame wonder
    stop music fadeout 1.0
    queue music "audio/music/sunny_day_happy.ogg"
    a "That was definitely not Snow White."
    l "Well, Keith said he wanted to put a spin to it."
    a "I heard that the actors will be resting in the classroom before their next appearance."
    a "Let's ask them what's up with that!"

    call epilogue_2_enter_classroom from _call_epilogue_2_enter_classroom_1
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    k "But before I forget, thanks for helping us with making the costume and props."
    k "You two have helped enough, just go enjoy the festival!"
    a "Well..."
    a "We wanted to know what's with that wacky play you made."
    k "It was actually thanks to you, Amelia."
    a "What did I have to do with this?"
    show kei wonder
    k "You told me that being a human is all about being able to express yourself."
    a "Did I really say that?"
    k "I was inspired by that little speach of yours, and [name]'s support."
    k "Instead of keeping my ideas to myself, I decided to share them with our actors."
    voice "kei/laugh"
    k "Well, they thought it was totally brillant, and here we are!"
    show kei smile
    jump epilogue_2_ending

label epilogue_2_ending:
    k "Anyway, we've got another performance coming up, so we need to go soon."
    if romance_target == "ame":
        k "If you ever need any help with planning your wedding."
        k "You can always come to me."
        show ame blush
        a "Keith!"
        l "Sure!"
    show ame smile
    voice "kei/yeah"
    k "See you two later! Make sure to properly enjoy the festival for us poor actors who couldn't!"
    voice "ame/bye"
    a "Bye!"
    l "Bye! See you around sometime!"
    jump epilogue_3