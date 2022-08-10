# Outline:
# Eve expresses how bad she is at socialising
# You tell her that you understand that it is hard
# If you do something wrong, people will critise you
# But if she had supervison and support, the effect will be lower
# You suggest to intoduce her to Amelia (and Keith if stat is high)

label eve_route_2_0:
    scene bg_rooftop_day
    show eve smile
    with fade

    l "On the roof again today?"
    voice "eve/good_afternoon"
    e "Good afternoon [name]. I'm just taking a short break from work."
    menu:
        "I'll leave you then.":
            voice "eve/goodbye"
            e "Alright."
            jump day_manager
        "Wanna talk?":
            show eve wonder
            e "You want to talk to a dull girl like me? Sure..."

label eve_route_2_1:
    if debug_gameplay_only:
        $ stat_understand_flag += 1
        $ stat_eve_flag += 1
        jump day_end_manager
    stop music fadeout 1.0
    queue music "audio/music/vntrack12_peaceful.mp3"
    scene bg_rooftop_day
    show eve smile
    l "Not playing Puzzle Impact today?"
    scene bg_rooftop_day
    show eve sad
    voice "eve/laugh"
    e "I'm a little burned out right now."
    e "So I'm just resting and enjoying the gentle breeze."
    scene bg_rooftop_day
    show eve smile
    e "Even though this might sound weird, but there's a certain comfort in being able to\
    sit beside a friend, just exchanging small talk."
    e "It's just that I've always been alone, always been too shy to do just that."
    l "You're talking with me just fine though?"
    e "Maybe it's the effect of having a shared interest?"
    e "I joined the student council because I thought I could fit in there."
    scene bg_rooftop_day
    show eve sad
    e "But everyone is just so goal driven and motivated, almost everything they talk about is related to academics."
    voice "eve/sigh"
    e "I felt that I just didn't fit in."
    menu:
        "You should still try to talk to them.":
            scene bg_rooftop_day
            show eve sad
            e "Everyone says that to me..."
        "It's okay not to fit in.":
            scene bg_rooftop_day
            show eve wonder
            $ stat_eve_flag += 1
            l "Everyone is different. It's only natural that some people don't gel well together."
            e "But does that mean I'll never get along with anyone?"
            l "You're getting along with me just fine."
            e "But I'll need to be able to talk to people other than you..."
    scene bg_rooftop_day
    show eve sad
    e "Learning social skills is scary, just making a small mistake will make others hate me."
    e "That's why I'm normally so quiet. Even though I have so much things to say."
    l "Everyone starts somewhere, you can start by talking with me."
    if stat_knowledge_flag >= 3:
        l "And I can introduce you to Amelia too! She's really struggling in her studies right now."
        l "She'll definitely be happy if you were to teach her about math."
    if stat_creative_flag >= 3:
        l "I can introduce you to Keith too!"
        l "I believe he'll understand your feelings."
    scene bg_rooftop_day
    show eve smile
    voice "eve/thanks"
    e "Thanks [name]. So I just need to take small steps at a time..."
    e "In the meantime, with your help, my workload has also been greatly reduced."
    e "So I'll be able to help you more with your project if this continues."

    scene bg_rooftop_day
    show eve smile
    with fade
    "You had a deep discussion about your feelings."
    play sound "audio/sound/statup.ogg"
    "You felt your understanding go up!"
    $ stat_understand_flag += 1

    scene bg_rooftop_day
    show eve smile
    with fade
    voice "eve/goodbye"
    "You waved goodbye to Everlyn, and went home."
    jump day_end_manager
