label morning_generic_1:
    scene bg_classroom_05_day
    show sm1_sensei_normal
    with fade
    queue music "audio/music/sunny_day_happy.ogg"
    teacher "Today, we'll be learning about..."
    scene black
    with fade
    play sound "audio/sound/church_bell.ogg"
    "Bell" "Dum dum dum dum"
    scene bg_classroom_05_day
    with fade
    jump day_manager
