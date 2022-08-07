# You submit the game on the last minute of sunday and hope for the best.
# The festival lasts two days, from friday to saturday.
# You were too tired to do much on monday
# You frantically planned how to display your game in the next few days, and had to design a poster.
# Walking around the festival with Amelia

label epilogue_0_sick:
    scene bg_classroom_05_day
    show sm1_sensei_normal
    with fade
    stop music fadeout 1.0
    queue music "audio/music/sunny_day_happy.ogg"
    teacher "...day, we'll be learn... abou..."
    scene black
    with fade
    stop music fadeout 1.0
    queue music "audio/music/good_news_drama.ogg"
    a "[name]! Are you okay?"
    $ show_blur("bg_classroom_05_day")
    show ame sad at center:
        blur 3
    l "Huh?"
    a "You look so tired! You really worked hard on your game..."
    show ame wonder
    a "Huh? Your forehead's burning hot!"
    a "I'll carry you to the nurse's office!"
    hide ame
    l "What about preparing for the class play?"
    show kei smile at center:
        blur 3
    k "Don't worry man! I'll be able to handle this with the rest of the class!"
    k "Just get some rest so you can enjoy the festival when it comes okay?"
    hide kei
    l "What about student council work?"
    show eve smile at center:
        blur 3
    e "[name], did you forget that you aren't actually on the student council?"
    e "I'll be responsible for my own work."
    e "Meanwhile, you should get some rest."
    hide eve
    show ame sad at center:
        blur 3
    a "Come, jump into my arms!"
    l "You're not strong enough to princess carry me... you dummy..."
    a "At least let me lend you my shoulder to support you!"
    l "What if you get sick too... What about your work?"
    show ame blush
    a "You don't get it! You're more important than some silly artwork!"
    show ame smile
    a "Anyway idiots like me can't get sick!"
    a "So let's go!"

    scene bg_school_hallway_day
    $ show_blur("bg_school_hallway_day")
    with fade
    with Pause(1)
    scene black
    with fade
    $ show_blur("bg_school_nurses_office")
    show ame sad at center:
        blur 3
    a "Stay here and get some rest ok?"
    a "I've already told the school nurse to watch over you."
    a "I'm really worried about you okay..."
    a "But I can't stay here for too long."
    a "I'll need to take the make up test later today."
    a "And there is also the submission for the cultural festival I have to complete!"
    show ame blush
    a "So get well soon!"
    a "And I'll show you what a genius like me is capable of!"

    jump epilogue_0_visit

label epilogue_0_visit:
    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    # Tuesday
    "3 days left until the cultural festival begins on Friday."

    queue music "audio/music/vntrack12_peaceful.mp3"
    scene bg_room_noon
    with fade
    "My head is still burning hot..."
    if game_completed_flag:
        "Phone" "Ring... Ring..."
        e """
        [name]?
        
        I have talked to the IT club about your game.

        And they seemed to really like it, and will be willing to host it in their own exhibition.

        The IT club has prior experience hosting digital content.
        
        So don't worry that no one will see it during the festival.
        
        Hope you get better soon.
        """
        l "Thanks Everlyn..."
    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    # Wednesday
    "2 days left until the cultural festival begins on Friday."

    queue music "audio/music/vntrack13_mystery.mp3"
    scene bg_room_noon
    with fade
    "The fever has subsided a little, but I still feel dizzy, and my throat is a little sore."
    if game_completed_flag:
        "Phone" "Ring... Ring..."
        k """
        Hey [name]!
        
        The preparations for the class play is all ready now!

        We rehearsed the entire day, and everyone's just perfect!

        Also, I have spread the word about your game.

        I can't wait to try the finished version too!

        So get well soon!
        """
        l "Thanks Keith..."
    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    # Thursday
    "1 day left until the cultural festival begins on Friday."

    queue music "audio/music/chat_menu_happy.ogg"
    scene bg_room_noon
    with fade
    "My temperature is back to normal, but I still feel tired."
    "I decided to take leave from school just in case."

    show ame smile
    l "Amelia?"
    l "What are you doing here?"
    a "Ehe, just visiting a sick childhood friend!"
    l "What about your art submission?"
    a "Just who do you think I am?"
    a "By using a hundred percent of my brainpower, I was able to finish it in a mere few days!"
    l "Stop being so dramatic..."
    show ame blush
    a "I've even cooked you some porridge just for you!"
    a "If you eat this, you'll definitely get better in no time!"
    a "Promise that we'll walk around the cultural festival together?"
    l "Yea, I promise."

    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    "The cultural festival begins today."
    jump epilogue_0_festival

label epilogue_0_festival: