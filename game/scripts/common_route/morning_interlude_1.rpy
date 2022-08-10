# Class votes to do a play for the cultural festival
# Happens after kei_1.

label morning_interlude_1:
    queue music "audio/music/sunny_day_happy.ogg"
    scene bg_classroom_05_day
    with fade
    show sm1_sensei_normal
    
    teacher "We will now be deciding the class exhibition for the cultural festival."
    teacher "Keith, do you have any proposals, or do we ask the class to vote?"
    scene bg_classroom_05_day
    show kei smile
    voice "kei/yeah"
    k "I want to do a play."
    k "There are a few reasons why I want to do so..."
    
    n "Keith talked about the extra effort needed to run a food shop, noting how the student council\
    is more shorthanded this year, and it might take extra time to approve our requests."
    n "He also talked about how he noticed how our class had a higher proportion of creatively minded\
    people from the drama and art clubs, and that we should play to our strengths."
    n "Keith delivered his speech with such confidence, that no one voiced any objection to his plan\
    of holding a play."
    nvl clear
    nvl hide

    k "Now that everyone is on the same page with me, we will be allocating roles..."
    scene black
    with fade
    "Bell" "Dum dum dum dum"
    scene bg_classroom_05_day
    with fade

    jump day_manager
