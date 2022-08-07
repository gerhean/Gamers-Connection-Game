# Only happens if stat_ame_flag >= 2, and R3 is seen
# Ame brings you to the art club room
# Her painting is the biggest in the room, and it's titled <Games I Love>.
# It's you playing a game
# Ame says that she loves you, in which you can accept or reject.

default romance_target = "none"

label epilogue_1:
    stop music fadeout 1.0
    queue music "audio/music/vntrack15_happy.mp3"
    scene bg_art_gallery
    with fade
    show ame smile
    l "I didn't expect that the art club room could be transformed into this!"
    a "Ehe, that's the power of the art club for you."
    l "So which one's your..."
    l "Wait! That face looks familiar!"
    if stat_knowledge_flag >= 6 and stat_ame_flag >= 2:
        jump epilogue_1_true
    else:
        jump epilogue_1_normal

label epilogue_1_normal:
    l "It's you?"
    a "Yup, it's a self portrait of myself studying for the make up test."
    a "It's amazing right?"
    l "What's so special about it? I see this everyday."
    show ame blush
    a "Hey!"
    l "I'm joking! It's really well done!"
    show ame sad
    a "Actually I was planning on making something else."
    a "But since I spent so much time studying, I didn't get the chance to make it."
    a "If only you helped me with my studies more frequently, and indulged me more..."
    a "But the past is in the past, it can't possibly change."
    a "Shall we go off to see our class play next?"
    l "Let's go!"
    jump epilogue_2

label epilogue_1_true:
    stop music fadeout 1.0
    queue music "audio/music/vntrack06_nostal.mp3"
    l "It's... me?"
    a "Ding ding ding! You are absolutely correct!"
    a "More precisely, it's a painting of you lying on your bed, playing your Switch!"
    "I got closer to the painting."
    l "Games I Love, by Amelia."
    l "Your painting skills are truly extraordinary... Even someone like me who as no knowledge of art can tell."
    l "Just one question, why is it that the background of the painting is so abstract."
    l "While the me in the painting is so focused that it looks almost like a photograph?"
    
    show ame blush
    a "You really have no delicacy at all [name]!"
    a "Can't you be a little less dense?"
    show ame emb
    a "It's a potrayal of the artist's emotional state."
    a "It signifies how the artist has gone so completely crazy that when the subject enters her view,\
    everything just becomes an abstract mess."
    a "It shows how much the artist cares about the subject that he is drawn with such detail."

    a "In other words, it's a expression of the artist's deep affection for the subject."
    show ame blush
    a "You know, I was teased so much by the other art club members when I submitted this."
    a "I sure hope it is worth it."
    show ame emb
    a "That is to say!"
    a "This is me conveying my true feelings to you!"
    a "I love you, will you stay with me forever?"
    menu:
        "Haven't I promised you before?":
            jump epilogue_1_romance            
        "Sorry..." if stat_ame_flag <= 3:
            "But I need more time to think about my feelings."
            $ romance_target = "none"
            show ame sad
            a "Yea, it was kinda sudden."
            a "I don't think I could have answered so quickly either."
            a "Shall we go off to see our class play next?"
            l "Good idea."
            jump epilogue_2

label epilogue_1_romance:
    $ romance_target = "ame"
    show ame smile
    a "AHAHA!"
    a "That's just such a [name] answer!"
    a "It feels like a weight has been lifted off my shoulders."
    a "Ha! Take that Mary! He's not my long time unrequited love! He loves me back!"

    l "But let me just say it."
    l "I love you too, Amelia."
    "Slowly, you hear the sound of clapping throughout the room."
    "Art Club Member M" "Kiss! Kiss! Kiss!"
    show ame emb
    a "Gahh! I somehow forgot that we're in public with how quiet this place is."
    l "Amelia, the class play is about to start."
    l "Let's make our escape, shall we?"
    "I grab her hand, and pulled her out of the art club room."

    scene bg_school_hallway_day
    with fade
    show ame emb
    a "[name]!"
    a "Don't just suddenly hold my hand like that!"
    l "Say's the one who confessed to me in open public view."
    show ame blush
    a "Haa... You really have no delicacy at all!"

    l "By the way, who's Mary?"
    a "She's that art club member who teased me when I submitted the artwork."
    a "Don't mention her anymore."
    l "Understood!"
    jump epilogue_2
