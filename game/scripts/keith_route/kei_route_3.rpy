# Outline:
# Keith buys some props in town
# Ame stalks you, but gets discovered easily
# Ame helps Kei select the props to buy
# They discover that they have a lot in common in terms of gaming interests

label kei_route_3_0:
    scene bg_classroom_05_day
    show kei wonder
    with fade
    k "[name]! There's something I need to buy in town, will you acompany me?"
    menu:
        "Maybe another time.":
            e "Don't worry dude, I'll survive this!"
            jump day_manager
        "Lets go.":
            jump kei_route_3_1

label kei_route_3_1:
    stop music fadeout 1.0
    queue music "audio/music/vntrack13_mystery.mp3"
    $ stat_kei_flag += 1
    $ stat_creative_flag += 1
    "Route is under construction"
    jump day_end_manager