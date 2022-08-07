# Easy implementation:
# Game works in 4 day cycles, where you get pairs for first 3 days and all 3 for 4th day
# Ame - 0, 2, 3
# Eve - 0, 1, 3
# Kei - 1, 2, 3

# Important days:
# 1: prologue 1
# 2: prologue 2
# 3, 4, 5: route 1

# Each character will have a pattern of
# r1 - generic - r2 - generic - r3
# Since there are only 14 days of free activity, it is impossible to get r3, 3 times.

default location = "class0"
default day_mod_value = 0

label day_manager:
    menu:
        "Where do you want to go?"
        "Look Around" if location == "class0":
            jump area_class_manager
        "My Classroom" if location != "class" and location != "class0":
            jump area_class_manager
        "School Hallway" if location != "hallw":
            jump area_hallway_manager
        "School Library" if location != "lib":
            jump area_library_manager
        "School Rooftop" if location != "roof":
            jump area_roof_manager
        "Nearby Park" if location != "park":
            jump area_park_manager
        "Go Home" if calendar.game_day() > 5:
            menu:
                "Are you sure you don't want to spend time doing something meaningful?"
                "Yes":
                    jump day_end_manager
                "No":
                    jump day_manager

label area_class_manager:
    $ location = "class"
    # Keith will typically be in this location
    if day_mod_value in [1, 2, 3]:
        if stat_creative_flag == 3:
            pass
        elif stat_creative_flag == 5:
            if calendar.game_day() >= 14:
                jump kei_route_3_0
            else:
                pass
        elif calendar.game_day() <= 5:
            pass
        else:
            jump kei_generic_1
    scene bg_classroom_05_day
    with fade
    "The classroom is noisy. But no one is approaching you."
    jump day_manager

label area_hallway_manager:
    $ location = "hallw"
    # Eve will typically be in this location
    if day_mod_value in [0, 1, 3]:
        if stat_understand_flag == 3:
            pass
        elif stat_understand_flag == 5:
            if calendar.game_day() >= 14:
                jump eve_route_3_0
            else:
                pass
        elif calendar.game_day() <= 5:
            pass
        else:
            jump eve_generic_1
    scene bg_school_hallway_day
    with fade
    "The hallway is crowded and not particularly interesting."
    jump day_manager

label area_library_manager:
    $ location = "lib"
    # Ame will typically be in this location
    if stat_knowledge_flag == 1:
        jump ame_route_1_0
    if day_mod_value in [0, 2, 3]:
        if stat_knowledge_flag == 3:
            jump ame_route_2_0
        if stat_knowledge_flag == 5:
            if calendar.game_day() >= 14:
                jump ame_route_3_0
            else:
                pass
        elif calendar.game_day() <= 5:
            pass
        else:
            jump ame_generic_1
    scene bg_library_day
    with fade
    "The library is a perfect place to study, but I don't want to do that right now."
    jump day_manager

label area_roof_manager:
    $ location = "roof"
    # Eve will typically be in this location
    if stat_understand_flag == 1:
        jump eve_route_1_0
    if day_mod_value in [0, 1, 3]:
        if stat_understand_flag == 3:
            jump eve_route_2_0
        else:
            pass
    scene bg_rooftop_day
    with fade
    "It seems that the door to the roof is locked. There is no one outside."
    jump day_manager

label area_park_manager:
    $ location = "park"
    # Keith will typically be in this location
    if stat_creative_flag == 1:
        jump kei_route_1_0
    if day_mod_value in [1, 2, 3]:
        if stat_creative_flag == 3:
            jump kei_route_2_0
    scene bg_park_day
    with fade
    "I feel refreshed walking in the park, but there's no reason to remain here."
    jump day_manager

label day_end_manager:
    stop music fadeout 1.0
    if calendar.game_day() == 2:
        jump evening_interlude_1
    if calendar.game_day() == 5:
        jump evening_interlude_2
    jump day_next_manager

label day_next_manager:
    # Also to control morning interlude events
    stop music fadeout 1.0
    scene black
    with fade
    $ calendar.next()
    $ temp = 22 - calendar.game_day()
    "There are only [temp] days left until the submission deadline."
    $ location = "class0"
    $ day_mod_value = calendar.game_day() % 4
    if calendar.weekday() == "Saturday" or calendar.weekday() == "Sunday":
        if calendar.game_day() <= 9:
            $ max_weekend_count = 1
            jump weekend_1
        elif calendar.game_day() <= 16:
            $ max_weekend_count = 2
            jump weekend_1
        else:
            jump weekend_3
    
    if calendar.game_day() == 6:
        jump morning_interlude_1
    jump morning_generic_1