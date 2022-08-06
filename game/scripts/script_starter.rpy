# This file is to make it easier to jump between scripts for debugging.
label script_starter:
    init python:
        config.overlay_screens.append('calendar_hud_ui')
    jump prologue_1_1
