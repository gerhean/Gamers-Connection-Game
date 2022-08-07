# Epilogue about recieving congratulations from the university.
# Maybe get a scholarship?

label epilogue_4:
    scene black
    with fade
    stop music fadeout 1.0
    queue music "audio/music/vntrack06_nostal.mp3"
    hide screen calendar_hud_ui
    "And so, the festival gradually draws to a close."
    "A few days later, you recieved a letter from the Game Development Group of Angsana University"

    n """
    Dear [name],
    
    I hope this find you well.

    The judges were very impressed with the game you had made.
    
    We will need to confirm some details with you before officially announcing the winners.

    Furthermore, we would recommend you to look into applying to this scholarship program.
    We believe you are a strong candidate, and can offer to support you through our testimonials.

    Regards, Game Jam Organisers.
    """
    nvl clear
    nvl hide
    "It seems that a brand new adventure is just around the corner!"

    scene bg_ending
    with fade
    "You have reached the end of the game!"
    "Thank you very much for playing!"
    pause
