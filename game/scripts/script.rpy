# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amelia", who_color="#edae1a")
define e = Character("Everlyn", who_color="#ed1a1a")
define k = Character("Keith", who_color="#1aed4f")
define l = Character("Me")
define teacher = Character("Teacher")
define n = nvl_narrator

# Declare variables
default calendar = Calendar(19, 3, 2021, week_offset=6)
default name = "Luke"
default stat_ame_flag = 0
default stat_eve_flag = 0
default stat_kei_flag = 0
default stat_knowledge_flag = 1
default stat_understand_flag = 1
default stat_creative_flag = 1

# The game starts here.
label start:
    jump script_starter
