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
    a "I have a submission for the cultural festival I have to make!"
    a "So get well soon!"
    a "And I'll show you what a genius like me is capable of!"

    jump epilogue_1
