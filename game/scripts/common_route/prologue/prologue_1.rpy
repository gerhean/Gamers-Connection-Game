# Day 1
label prologue_1_1:
    play music "audio/music/chat_menu_happy.ogg"
    scene bg_sign_up_form
    "The name field of the sign up form stared menacingly towards me."
    "Am I... Really going to do this?"
    "Gulp"

    scene bg_room_evening_light_on
    show ame smile_casual
    with fade
    a "How long are you gonna stare at that?"
    l "Quit nagging at me. I just need a little more time to prepare myself."

    show ame sad_casual
    a "Sure, but I'm hungry... I wanna go out for dinner soon..."
    l "Amelia... all you're doing is playing Further Fantasy in my room, go grab dinner yourself."
    a "Nah, eating alone is the worst."
    l "Then why not sign up for this with me? After all, the project can be done in a team."
    n "Every year, Maple High School holds an art festival, in which students may submit their artwork to be showcased."
    n "At the same time, the Game Development Group of Angsana University had just announced their yearly game jam."
    n "And so, I came up with the brilliant plan of submitting a game to both of these competitions at once."
    n "Kill two birds with one stone and all that."
    nvl clear
    nvl hide

    show ame wonder_casual
    a "Eh... I don't have talent for game making, maybe next time?"
    "Although I did not need to sign up for either of the events so early,"
    "I decided to do so anyway in order to strengthen my resolve, starting with my name..."

    scene bg_sign_up_form
    with dissolve
    jump prologue_1_2

label prologue_1_2:
    $ name = renpy.input("First Name:", default="Luke")
    $ name = name.strip() or "Luke"

    if name == "Keith" or name == "Amelia" or name == "Everlyn":
        "That can't be my name..."
        jump prologue_1_2
    menu:
        "I double checked my name, is it [name]?"
        "Yes":
            jump prologue_1_3
        "No":
            "The stress must really be getting to me..."
            jump prologue_1_2

label prologue_1_3:
    scene black
    with fade
    "..."
    "After taking the first step, the rest of the form was easier to get through."
    
    scene bg_room_evening_light_on
    show ame smile_casual
    with fade

    l "Hey, I'm finally done, shall we go now?"
    a "Wait... I'm still halfway through this boss..."
    l "Seriously?"
    stop music
    $ calendar.next()
    jump prologue_2
