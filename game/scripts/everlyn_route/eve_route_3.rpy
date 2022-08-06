# Outline:
# Eve will need to talk to Kei about the progress of the class play.
# You encourage eve to use this opportunity to know her classmates more.
# Then you discovered a surprising story in which Keith had confessed his feelings to Eve once.
# Although Eve offered to remain friends, Kei avoided her, leading to awkwardness.
# With your support, Keith was able to talk about how ashamed he was that he never actually loved eve.
# Eve forgives him

label eve_route_3_0:
    scene bg_school_hallway_day
    show eve wonder
    with fade

    e "Hey [name]. I need to meet the class representatives, and I'm a little nervous."
    e "Will you support me?"
    menu:
        "Maybe some other time...":
            e "Thanks anyway..."
            jump day_manager
        "No problem.":
            e "I'm grateful for your assistance."

label eve_route_3_1:
    stop music fadeout 1.0
    queue music "audio/music/vntrack02_confront.mp3"
    scene bg_classroom_05_day
    show eve smile
    with fade
    "Student" "Can't you just give some leeway?"
    e "Sorry, but these school regulations exist for a reason."
    e "I am sure you are aware of why. If you feel they are too strict, do submit an appeal to the president."
    "Student" "How did such a beauty turn out to be such a wet blanket..."
    e "I..."
    "Student" "Come on, what's so bad about having a little more fun..."
    l "Please stop, or I'll report you for harassment."
    hide eve smile
    with dissolve
    "I walked in between the space seperating them, and stared harshly at the student."

    "Student" "Tch."
    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    show eve sad
    with dissolve
    e "He walked away..."
    e "Thanks [name]. I don't think anything too serious would have happened, but I'm still glad you stood up for me."
    e "Even though I was doing the right thing."
    e "Was there something I could have done better?..."
    l "Sorry... I'm not really sure either."

    "You dealt with a difficult negotiation."
    "You felt your understanding go up!"
    $ stat_understand_flag += 1

    e "In any case, the next, and last class we need to review is ours."
    e "Our class representative has yet to submit the finalised proposal..."    
    
    scene bg_classroom_05_day
    show eve smile at right:
        zoom 0.8
    with fade
    e "If I remember correctly, the class representative Keith has blonde hair..."
    l "You know, this can be a great chance to get to know him better."
    l "Try to ask him out for tea break or something."
    e "But..."

    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    show kei smile at left:
        zoom 0.8
    k "Hey [name]!"
    k "And Everlyn..."
    k "What are you two doing together?"
    e "Hello Keith. I have teamed up with [name] to collect the finalised proposal for the class play."
    k "Sorry, give me a little more time to finish it."
    k "I'll submit it by the end of today."
    k "Catch you later [name]!"

    show eve wonder
    e "Wait!"
    e "Keith, if you do not mind, I would like to have a short tea break with you."
    l "That sure came out wrongly..."
    e "Huh?"
    stop music fadeout 1.0
    queue music "audio/music/vntrack02_confront.mp3"
    show kei sad
    k "Man, I know that the finalised proposal is important."
    k "But I'm not a child who needs to be supervised."
    show eve sad
    e "No..."
    l "Keith! It's my fault, I'm sorry."
    show kei wonder
    k "Huh? What this gotta do with you?"
    l "Well I asked Everlyn to try to get to know you better."
    l "But the way she talks is a little..."
    e "Sorry..."
    show kei smile
    k "So that's what it was about. Sorry man, I seemed to have misunderstood you."
    show eve smile
    e "No problem, I'm used to it anyway..."
    e "Let me try again properly this time."
    e "You seem a little tired. I'll treat you some coffee?"
    k "If you insist."

    stop music fadeout 1.0
    queue music "audio/music/good_news_drama.ogg"
    scene bg_rooftop_day
    with fade
    show kei smile at left:
        zoom 0.8
    k "Is it really okay to use the rooftop like that."
    show eve smile at right:
        zoom 0.8
    e "Just don't tell anyone else about it."
    k "Woah, even someone as straight laced has a bad side."
    show eve sad
    e "Sorry for showing you my disappointing side..."
    show kei wonder
    k "You take things too seriously man."
    k "It was supposed to be a compliment."
    show eve blush
    e "Really? Let me take a mental note of that..."
    show kei happy
    k "I never realised I had misunderstood you so much."
    show eve wonder
    l "Did something happen between the two of you?"
    k "Yea, I confessed to Everlyn like last month."
    l "!!!"
    k """
    It's a little of a tragic story.
    
    I fell in love a little after we were placed in the same class.

    Everlyn is smart, cute, confident, all the qualities I like in a girl.
    She's a little quiet, but I didn't mind that.

    So I gathered my courage and confessed to her behind the school building one day.

    But she simply rejected me with that blank smile she always has.
    Even though we were classmates, she didn't even know my name.

    So from that day on, I just avoided her as much as possible.
    """

    show eve sad
    e "I'm sorry you had to experience that."
    k "Don't worry about that, it's also my fault that I over-idealised you."
    k "Remember how you offered to be friends with me that time?"
    k "I'll take you up on that."
    e "Keith..."
    menu:
        l "Everlyn..."
        "You should be more careful of how you speak.":
            e "Sorry..."
            k "Dude you're too harsh on her!"
        "What is done is done.":
            l "But we'll be here to support you in the future."
            l "As your friends."
            show eve blush
            $ stat_eve_flag += 1
            e "Thanks..."
            k "Well said!"

    show eve happy
    k "Hey, after the cultural festival ends, let's continue to hang out together alright?"
    e "Sure!"
    l "I'm up for it too!"
    jump day_end_manager
