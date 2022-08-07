# If game is completed:
# The last part of the story takes place at the IT club room
# If eve is r3 and high enough stat, she would become friends with IT club members.

# If game is not completed:
# You will explore the festival more until you are tired
# Eve spots the two of you and drags you to the stuco room
# She talks about how the IT club was a little upset that she bought an unfinished game
# The visual novel will the end here

label epilogue_3_incomplete_game:
    a "All that running around really made me tired."
    l "Agreed."
    a "I wonder if there's anywhere to sit at?"
    e "[name]! Amelia!"
    scene bg_school_hallway_day
    show ame smile at left:
        zoom 0.8
    show eve smile at right:
        zoom 0.8
    with dissolve
    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    l "Hey Everlyn. What's up?"
    e "I just finished up my patrol work."
    e "And now I am just walking around the school, looking around at the various exhibits."
    e "There is truly a large difference between the written proposal and the real thing."
    l "You can remember Amelia's name?"
    show eve blush
    e "[name]'s my friend."
    e "So I just thought I should at least recognise my friend's closest friend."
    if romance_target == "ame":
        a "Girlfriend now."
        l "Look who's getting bolder."
        e "Oh! I didn't know! Congratulations!"
        a "Thanks!"
    show eve smile
    e "Right now, I'm headed for the student council room to rest."
    e "Feel free to come as well, there are empty chairs to rest on."
    l "Let us take you up on that offer then."
    scene club_room_day
    show ame smile at left:
        zoom 0.8
    show eve sad at right:
        zoom 0.8
    with fade
    e "It was truly a shame that your game was unfinished."
    e "I thought that the gameplay was quite decent, but the IT club just did not want to accept unfinished games."
    e "Perhaps if you worked harder on a single skill, and worked with people who complemented your weaknesses."
    e "You might have been able to finish the game."
    e "But the past is in the past, it can't possibly change."
    l "At the very least, I learnt a lot about the process of game development."
    e "I suppose that is good as well..."

    scene black
    with fade
    "And so the festival gradually draws to a close."
    "Although you never completed your game, the taste of game development has left you wanting for more."
    "You started working on your next project..."
    scene bg_ending
    with fade
    "You have reached the end of the game!"
    "Thank you very much for playing!"
    pause

label epilogue_3:
    stop music fadeout 1.0
    queue music "audio/music/vntrack04_adventure.mp3"
    scene bg_school_hallway_day
    with fade
    show ame smile
    if not game_completed_flag:
        jump epilogue_3_incomplete_game
    
    a "Come to think of it, I haven't seen how your game turned out in the end."
    a "Didn't you say that the IT club was hosting it?"
    a "There's still time to make it!"

    scene bg_school_hallway_day
    with fade
    show ame smile at left:
        zoom 0.8
    a "Woah, what happened?"
    a "Why is there such a long queue outside the IT club's exhibit?"
    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    e "[name]! Amelia!"
    show eve smile at right:
        zoom 0.8
    l "Hey Everlyn. What's up?"
    e "I just finished up my patrol work."
    e "And now I am just walking around the school, looking around at the various exhibits."
    e "There is truly a large difference between the written proposal and the real thing."
    l "You can remember Amelia's name?"
    show eve blush
    e "[name]'s my friend."
    e "So I just thought I should at least recognise my friend's closest friend."
    if romance_target == "ame":
        a "Girlfriend now."
        l "Look who's getting bolder."
        e "Oh! I didn't know! Congratulations!"
        a "Thanks!"
    show eve smile
    if stat_understand_flag >= 6 and stat_eve_flag >= 2:
        jump epilogue_3_true
    else:
        jump epilogue_3_normal


label epilogue_3_normal:
    e "It would seem that your game is popular with the students here."
    e "It's just that, I'm not really close to anyone in the IT club."
    l "Didn't you say that you were interested in software?"
    e "I did, but I didn't think that it was important to mention it to the club when promoting your game."
    e "I made the wrong decision again, didn't I?"
    e "If only I had more experience with dealing with others with support from friends."
    e "But the past is in the past, it can't possibly change."
    e "Well, there's still time before the day festival ends."
    e "I'm a little tired so I don't think I can keep up."
    l "Everlyn, you really worked hard, didn't you."
    e "That I did, and I'm glad for it."
    e "So you two should just enjoy the festival I worked so hard on."
    l "Alright. See you soon and take care!"
    a "Bye Everlyn!"
    e "Goodbye!"
    jump epilogue_4

label epilogue_3_true:
    "Student" "Everlyn! So you came huh?"
    e "Daniel? What happened?"
    "Daniel" "Nothing much. It's just that [name]'s game is way too popular."
    "Daniel" "Trying to contain the crowd had been a tiring process, so I stepped out for a while to take a breather."
    "Daniel" "So who are these two? Your friends?"
    e "You could say that."
    e "This one is [name]..."
    e "And this one over here is Amelia"
    "Daniel" "Wait. Did you just say [name]?"
    "Daniel" "The original creator of the game which is causing this out of control queue?"
    l "That's me alright."
    if stat_knowledge_flag >= 6:
        "Daniel" "And Amelia, one of the major contributors to the project?"
        a "You got that right!"
    "Daniel" "It is truly a great honour to meet you!"
    "Daniel" "I'm Daniel, one of the members of the IT club."
    "Daniel" "Do come inside, I'm sure the other club members would want to meet you too!"
    scene bg_computer_lab
    with fade
    show ame smile at left:
        zoom 0.8
    show eve smile at right:
        zoom 0.8
    e "Thanks, Daniel."
    "Daniel" "Don't mention it."
    "Daniel" "Besides, didn't you express interest in joining out club?"
    "Daniel" "Why not submit the official club membership form?"
    e "I'm not sure if I can handle being in a club and the student council at the same time."
    "Daniel" "Don't worry, we are not involved in any clubwide competitions, so attendence is never compulsory."
    "Daniel" "Besides, I can tell you're genuinely interested in software."
    "Daniel" "We could tell how passionate you were when you presented [name]'s game a few days ago."
    "Daniel" "And when we told you that there was a bug, you just sat down and fixed it almost immediately."
    l "A bug..."
    e "Don't worry, even senior engineers can't avoid buggy code."
    "Daniel" "Do think about joining us for real alright?"
    e "Alright..."

    "Daniel" "In any case, there are a few spare computers in which you and your friends can try the games."
    l "No thanks. As the creator of the game, I can run it just fine on my personal computer."
    l "Amelia, let me show it to you once we reach home."
    l "But for now, we should enjoy the experiences which are only available during the cultural festival."
    a "Agreed."

    e "[name], before you go."
    e "I would like to thank you for helping me understand that it is okay to open up to others."
    e "And for teaching me tips on how to be more understanding of others."
    e "If not for your influence, I would never have gotten close to the IT club."
    e "So thanks again."
    e "And do have lots of fun at the festival!"
    l "Don't worry, I will!"
    a "Me too!"
    jump epilogue_4
