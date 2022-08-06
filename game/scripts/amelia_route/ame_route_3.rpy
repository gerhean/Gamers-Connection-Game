# Outline:
# While studying, eve joins.
# Ame gets a little jealous and emotional, while eve remains logical.
# But Ame tells hereself not to fall into self deprecation
# Ame suggests a deal, in which if eve helps her with her studies, they can play this new coop game
# Ame declares that she will make sure that you will ultimately look at her via her own achievements.

label ame_route_3_0:
    scene bg_library_day
    show ame smile
    with fade

    l "Hey."
    a "I'm feeling really motivated for some reason."
    a "Feels like the makeup test will be a piece of cake!"
    menu:
        "There's something else I need to do.":
            a "Aww..."
            jump day_manager
        "You sure about that? Let me test you.":
            jump ame_route_3_1

label ame_route_3_1:
    stop music fadeout 1.0
    queue music "audio/music/chat_menu_happy.ogg"
    a "I'll show you, what I'm capable of now!"
    l "Ha! You sure grown overconfident. Are you sure, you can solve... this?"
    "You took out your tablet, and opened the math exercise book you were using."
    show ame sad
    a "H-Hey! That's no fair! I never seen that question before!"
    l "And it is also quite similar to question six in that test we took."
    show ame blush
    a "Give me that! I'll show you what I learnt in the last week!"

    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    scene bg_library_day
    with fade
    show ame sad
    a "How do I even integrate this?"
    e "Good afternoon [name]."
    hide ame sad
    show ame wonder at right:
        zoom 0.8
    show eve smile at left:
        zoom 0.8
    with dissolve
    e "And I assume this is the Amelia you always speak so fondly of?"
    a "Everlyn?"
    l "What are you doing here?"
    e "I just happened to finish the work that was assigned to me for today."
    e "It has been some time since I last came to the library, but I did not expect to meet you here."

    stop music fadeout 1.0
    queue music "audio/music/vntrack02_confront.mp3"
    show ame blush at right:
        zoom 0.8
    a "We never properly talked before did we."
    a "Even though we saw each other every weekday for a few months, you could only assume I was Amelia."
    show eve sad at left:
        zoom 0.8
    e "I'm sorry... I'll make sure to remember you next time..."
    l "Calm down ladies."
    hide ame blush
    show ame sad at right:
        zoom 0.8
    a "I can't stand how she looks down on me."
    l "Amelia, at least try to listen to her..."
    a "If you say so..."

    e "That wasn't my intention."
    e "I didn't approach you in the past because I didn't think you would accept me."
    show eve smile at left:
        zoom 0.8
    e "But [name] approached me and tried to befriended."
    e "That couldn't have happened if he had been a coward."
    e "And I am very thankful for it."
    e "Since [name] is also here, I decided to gather up my own courage and strike a greeting."
    e "I want to get to know you better. I cannot stay shy forever, I need to work on myself."

    e "I'm not sure if [name] has told you before, but I love playing games like Puzzle Impact."
    e "To me, emotions are also like a puzzle. There are many times which I might get stumped."
    e "However, if I keep trying and trying again, I will eventually be able to understand it."
    e "So please, give me another chance."

    stop music fadeout 1.0
    queue music "audio/music/good_news_drama.ogg"
    hide ame sad
    show ame wonder at right:
        zoom 0.8
    a "Fine."
    show ame sad at right:
        zoom 0.8
    a "I admit that I was too emotional."
    a "[name] has told me before about how you had problems with understanding others."
    a "Since you're [name]'s friend, I'll give you a chance."
    menu:
        l "Amelia..."
        "Try to keep your emotions in check.":
            a "I..."
        "Do you want to share your emotions with us?":
            l "It's not good to keep them all bottled up."
            l "If you have a problem, then let's work through it together."
            a "[name]..."
            a "I think I'll need some time to reflect on my own feelings."
            a "When I reach a conclusion, I promise I'll talk through them with you."
            $ stat_ame_flag += 1
    
    e "Amelia, I can't claim to understand you yet. But I'll definitely put in my best effort."
    a "Everlyn..."
    a "Actually, you're really smart right?"
    a "Will you help to explain how to solve this question?"
    e "Well, I might be lacking in many aspects, but I would like to believe that I am good at Math."
    a "I think good is an understatement..."

    stop music fadeout 1.0
    queue music "audio/music/chat_menu_happy.ogg"
    scene bg_library_day
    with fade
    show ame wonder at right:
        zoom 0.8
    show eve smile at left:
        zoom 0.8

    e "You see, to integrate this statement, you just need to move these terms over, and use this formula."
    a "Woah, that was fast. How did you know which formula to use?"
    e "I guess intuition? Like how there's a sin here and a cos here. So that already narrows down the possible formulas to use."
    a "Huh, I don't really get it."
    "You tried to keep up with Everlyn's unrefined teaching."
    "You felt your knowledge go up!"
    $ stat_knowledge_flag += 1

    scene bg_library_day
    show ame smile at right:
        zoom 0.8
    show eve smile at left:
        zoom 0.8
    with fade
    a "Everlyn, I don't think you'll make a good teacher in the future."
    show eve sad at left:
        zoom 0.8
    e "Sorry..."
    a "Don't get so down, everyone has different strengths."
    a "As thanks for tutoring us, what about you come over to my house sometimes!"
    a "There's this new multiplayer game I wanted to play with [name], but it can support up to three players."
    hide eve sad
    e "I would love to!"
    a "It's settled then, let's meet up after the cultural festival!"
    if stat_ame_flag == 2:
        scene bg_library_day
        show ame blush
        a "And [name], I've decided what artwork to submit for the cultural festival."
        a "Everlyn might be better than me in many ways, but I'll show you something only I can do."
        a "And you'll have no choice but to look only at me."
        a "But don't peek until it's done, I want to surpise you."
    jump day_end_manager
