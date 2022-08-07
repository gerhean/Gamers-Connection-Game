# You went to watch the class play, since you are not involved in the performance.
# If stat_kei_flag < 2 or R3 not seen, then it will just be the standard Snow White
# Otherwise, it will be a weird gender reversed snow white

label epilogue_2:
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    scene bg_auditorium
    with fade
    show ame smile
    a "I can't wait to see how the class play will be like!"
    l "Me too. I was sick for the last few days so I didn't see the rehearsals at all..."
    jump epilogue_3