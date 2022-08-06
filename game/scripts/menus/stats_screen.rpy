# Source: https://zeillearnings.itch.io/stats-ui
screen stats_hud_ui():
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "ui/ui_stats_%s.png"
        action ShowMenu("stats_menu_ui")

## Stats UI
screen stats_menu_ui():
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
                text "Knowledge" size 60
                text "Understanding" size 60
                text "Creativity" size 60

            # Values Column     
            vbox:    
                spacing 10
                text "[stat_knowledge_flag]" size 60
                text "[stat_understand_flag]" size 60
                text "[stat_creative_flag]" size 60
     
    ## Show a Return button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "ui/ui_return_%s.png"
        action Return()