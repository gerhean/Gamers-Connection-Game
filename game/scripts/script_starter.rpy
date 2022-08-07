# This file is to make it easier to jump between scripts for debugging.
default debug_gameplay_only = False

label script_starter:
    show screen calendar_hud_ui
    if debug_gameplay_only:
        show screen stats_hud_ui
        $ calendar.next()
        jump day_end_manager
    jump prologue_1_1
