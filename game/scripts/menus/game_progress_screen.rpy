default knowledge_progress = 0
default understand_progress = 0
default creative_progress = 0

# Progress needed for each stat to finish the game
default required_progress = 30

# Each character will give 5 x flag value progress

label self_game_progress:
    "Not wanting to fall behind, I too put in effort into my own game."
    $ knowledge_progress += stat_knowledge_flag
    $ understand_progress += stat_understand_flag
    $ creative_progress += stat_creative_flag
    "As a result, the game is closer to completion!"
    hide screen game_progress_menu_ui
    return

screen game_progress_menu_ui():
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        hbox:
            spacing 40
            # Text Column
            vbox:
                spacing 10
                text "Coding" size 60
                text "Design" size 60
                text "Art" size 60

            # Values Column
            vbox:    
                spacing 10
                text "[knowledge_progress]/[required_progress]" size 60
                text "[understand_progress]/[required_progress]" size 60
                text "[creative_progress]/[required_progress]" size 60