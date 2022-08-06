# Outline:
# Keith talks about how even though snow white has been chosen
# The play is extremely cliche and people have been complaining
# You talk to him about how he can get inspiration from the games he played
# Maybe mix in some of his life experiences
# He decides that snow white could hide forever with the dwarfs, but decide to reveal herself
# Because it is human nature to show off.

label kei_route_2_0:
    scene bg_park_day
    show kei sad
    with fade
    "Seems like Keith is deep in thought."
    menu:
        "Should I approach him?"
        "Maybe another time.":
            jump day_manager
        "Talk to him.":
            jump kei_route_2_1

label kei_route_2_1:
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    l "You in the park again?"
    show kei smile
    with fade
    k "Dude, you're here!"
    k "Just having a small problem which requires some fresh air."
    k "You see, the actual script for the play hasn't been written yet."
    k "The only thing which we had decided on so far is to work on Snow White."
    l "Why Snow White?"
    k "It's one of the more well known fairy tales with a completely happy ending, where no one dies."
    k "I asked around, and no one else seems to be doing Snow White this year. There was a Cinderella though."
    
    show kei wonder
    k "However since Snow White is very popular, so we have been trying to think of a way to introduce a twist."
    k "I believe that I might be able to draw some inspiration from games, but all I have been daring so far is a blank."

    l "Is there no one else to write the script?"
    k "So here's the thing, there are many artists in our class, but apparently not a single one really wrote stories before."
    k "At least not outside of homework."

    menu:
        "You should just give up.":
            l "There's nothing wrong with reusing the same story."
            k "That might be an obvious choice, but I rather not let anyone down..."
        "Surely, there is something you can use.":
            l "Even if it is not in games, maybe you can look into yourself."
            l "Didn't you struggle a lot in order to get to where you are today?"
            k "Sounds crazy, but it might be just what I need... Thanks..."
            $ stat_kei_flag += 1
    
    l "What about that dating sim you bought a few days back. Would that be helpful for inspiration?"
    k "Honestly I had been so busy that I hardly had the time to play it."
    k "But the girl in the game who I got closer to, I was really moved by her story."
    show kei sad
    k "You don't mind spoilers do you?"
    l "Don't worry. I'm the type who reads spoilers while playing the game."
    show kei smile
    k "Well this girl, she came from a well to do family, she often isn't allowed to take part in the photography's club activities."
    k "Her familiy would prefer that she just give up taking pictures."
    k "After all, the salary of a photographer can be non-existent at times."
    k "However, the girl strongly rebelled, stating that photography is a part of her identity."

    k "It's the same for me to. I have to keep my love for games hidden from others. Even though it might hurt me."
    l "Maybe if Snow White had something she could not bare to give up?"
    k "Like her beauty?"
    k "Perhaps it was Snow White who was too prideful of her appearance."
    k "The dwarfs could have protected her if she just stayed in the forest."
    k "But Snow White might have been too ambitious to stay in a forest hut for the rest of her life..."

    scene bg_park_day
    show kei smile
    with fade
    "You had a meaningful discussion with Keith about the narrative of the play."
    "You felt your creativity go up!"
    $ stat_creative_flag += 1

    scene bg_park_day
    show kei smile
    with fade
    k "Dude, thanks so much for your help! I couldn't have done this without you."
    "You waved goodbye to Keith, and went home."
    jump day_end_manager
