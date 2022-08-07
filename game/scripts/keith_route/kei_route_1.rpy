# Outline:
# You meet Keith in the park, deep in thought.
# You can ask him what's wrong, he will tell you nothing is, but then you bring up doki...
# He reveals how he just wants to fit in, and how he doesn't actually want the representative role.
# He just wants to be popular, just the typical teenage boy things
# You notice a stray cat on his lap
# He asks you to help prepare materials for the class's cultural festival exhibit.
# As a person who had played a lot of games in his middle school years,
# he might be able to help with game desgin

default kei_route_1_rep_flag = False
default kei_route_1_alone_flag = False
default kei_route_1_game_flag = False

label kei_route_1_0:
    scene bg_park_day
    show kei sad
    with fade
    "Seems like Keith is deep in thought."
    "Should I approach him?"
    menu:
        "Ignore him.":
            jump day_manager
        "Talk to him.":
            jump kei_route_1_1

label kei_route_1_1:
    if debug_gameplay_only:
        $ stat_creative_flag += 1
        $ stat_kei_flag += 1
        jump day_end_manager
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    l "Hey, a penny for your thoughts? You look down."
    k "Nothing, I'm fine. Don't bother me."
    l "Want me to talk about how you went to buy Doki..."
    k "Chill man, if you want to talk, then let's talk."
    k "I'm not really doing anything anyway..."

menu kei_route_1_2:
    "You didn't want to be the class rep?" if not kei_route_1_rep_flag:
        $ kei_route_1_rep_flag = True
        jump kei_route_1_2_1
    "Why are you alone?" if not kei_route_1_alone_flag:
        $ kei_route_1_alone_flag = True
        jump kei_route_1_2_2
    "You are interested in dating sims?" if not kei_route_1_game_flag:
        $ kei_route_1_game_flag = True
        jump kei_route_1_2_3
    "There's a cat on your lap." if kei_route_1_rep_flag and kei_route_1_alone_flag and kei_route_1_game_flag:
        jump kei_route_1_3

label kei_route_1_2_1:
    k "Of course not, it's such a pain having to organise everything."
    k "I need to guide the class to decide on a viable project."
    k "And ensure that the project runs smoothly and finishes in time."
    k "Even participate in the labour."
    k "Very tiring."
    jump kei_route_1_2

label kei_route_1_2_2:
    k "Just a little tired."
    k "It's hard to keep acting energetically in front of people."
    k "You know, I wasn't very popular back in middle school."
    k "So I read a lot of magazines, and followed a lot of online advice."
    k "It's through hard work that I was able to make my high school debut."
    k "But I rather be alone sometimes."
    jump kei_route_1_2

label kei_route_1_2_3:
    k "Not in particular."
    k "I play all sorts of games, like action, puzzle or rpg."
    k "And there were good online reviews of it."
    k "You heard of it too right?"
    k "Games can help me to experience new things."
    jump kei_route_1_2

label kei_route_1_3:
    scene bg_park_day
    show kei wonder
    with dissolve
    k "Huh, when did it...?"
    "He starts to stroke the cat's head gently."
    l "You like cats?"
    k "Yea. I never owned any, but they seem to like me for some reason."
    k "Maybe it's the way I smell? Hahaha."
    "I try to touch the cat as well."
    "But as soon as I reached out, it jumped off Keith's lap, and ran away."
    l "I guess cats just hate me."
    k "Maybe it's the way you look? After all, most people don't approach you in school."
    k "Except Amelia. What's the deal with her? You interested in her?"
    menu:
        "I love her.":
            k "I knew it. I'm cheering for you man!"
        "I'm not sure yet.":
            k "It's okay to think through your feelings first."
            k "But when the time comes, you need to give a firm answer."
    k "But I'm envious of you, having such a strong bond with someone else."
    l "Perks of being childhood friends."
    show kei sad
    k "My friends don't seem to truly understand me at all."
    menu:
        "Why not you leave them?":
            k "It's not so easy."
            k "I don't want to go back to how I was like in middle school."
        "It's great that you make an effort to connect with others.":
            $ stat_kei_flag += 1
            l "You're kind and approachable, you will surely find someone who understands you deeply too."
            l "Being relatively alone like me comes with disadvantages too."
            k "Thanks for your support."
            k "I guess the grass is always greener on the other side."
    k "Sorry if I misjudged you before, let's be friends man."
    k "Is it alright if you helped me with preparing the cultural festival?"
    l "Sorry, but I have this project..."
    scene black
    with fade
    "You told Keith about how you want to submit a game for the cultural festival."
    scene bg_park_day
    show kei smile
    with fade
    k "Dude that's so cool."
    k "You know what, if you help me with the cultural festival, I'll help with designing your game."
    k "I spent my middle school years playing games, I know a trick or two about what makes them fun."
    k "But first, let's come up with some ideas for the class exhibit."
    
    scene bg_park_day
    show kei smile
    with fade
    "By being forced to write up some ideas, you became better at brainstorming."
    "You felt your creativity go up!"
    $ stat_creative_flag += 1

    scene bg_park_day
    show kei smile
    with fade
    k "Before we split up, here's my number. Give me a call sometime alright?"
    "You waved goodbye to Keith, and went home."
    jump day_end_manager
