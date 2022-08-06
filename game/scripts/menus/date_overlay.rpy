# https://lemmasoft.renai.us/forums/viewtopic.php?t=25098
init python:
    class Execute(Action):
        """
        Well... it executes... :)
        This has NOTHING to do with calendar, just makes using it with screen language easier.
        """
        def __init__(self, func, *args, **kwargs):
            self.func = func
            self.args = args
            self.kwargs = kwargs
        
        def __call__(self):
            self.func(*self.args, **self.kwargs)
            return False
    
    class Calendar(object):
        '''Provides time-related information.
        Cheers to Rudi for mooncalendar calculations.
        '''
        def __init__(self, day=1, month=1, year=1, leapyear=False, week_offset=0):
            """
            Expects day/month/year as they are numbered in normal calender.
            If you wish to add leapyear, specify a number of the first Leap year to come.
            """
            self.day = day
            self.month = month - 1
            self.year = year
            self.week_offset = week_offset
            if not leapyear:
                self.leapyear = self.year + 4
            else:    
                self.leapyear = leapyear
            
            self.daycount_from_gamestart = 0
            
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            self.month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            self.days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
            self.mooncycle = 29
            self.newmoonday = 1
            
        def game_day(self):
            """
            Returns amount of days player has spent in game.
            Counts first day as day 1.
            """
            return self.daycount_from_gamestart + 1
            
        def string(self):
            # return "(%s) - %s %d %d"%(self.weekday(), self.month_names[self.month], self.day, self.year)
            return "%s %d (%s)"%(self.month_names[self.month], self.day, self.weekday())
            
        def next(self, days=1):
            """
            Next day counter.
            Now supports skipping.
            """
            self.daycount_from_gamestart += days
            while days:
                self.day += 1
                days -= 1
                if self.leapyear == self.year and self.month == 1:
                    if self.day > self.days_count[self.month] + 1:
                        self.month += 1
                        self.day = 1
                        self.leapyear += 4
                elif self.day > self.days_count[self.month]:
                    self.month += 1
                    self.day = 1
                    if self.month > 11: 
                        self.month = 0
                        self.year += 1
                        

        def weekday(self):
            '''Returns the name of the current day according to daycount.'''
            daylistidx = (self.daycount_from_gamestart + self.week_offset) % len(self.days)
            return self.days[daylistidx]

        def week(self):
            '''Returns the number of weeks, starting at 1 for the first week.
            '''
            weekidx = self.daycount_from_gamestart / len(self.days)
            return weekidx + 1

        def lunarprogress(self):
            '''Returns the progress in the lunar cycle since new moon as percentage.
            '''
            newmoonidx = self.newmoonday - 1
            dayidx = self.daycount_from_gamestart - newmoonidx
            moonidx = dayidx % self.mooncycle
            moondays = moonidx + 1
            percentage = moondays * 100.0 / self.mooncycle
            return int(round(percentage))

        def moonphase(self):
            '''Returns the lunar phase according to daycount.

            Phases:
            new moon -> waxing crescent -> first quater -> waxing moon ->
                full moon -> waning moon -> last quarter -> waning crescent -> ...
            '''
            # calculate days into the cycle
            newmoonidx = self.newmoonday - 1
            dayidx = self.daycount_from_gamestart - newmoonidx
            moonidx = dayidx % self.mooncycle
            moondays = moonidx + 1
            # substract the number of named days
            unnamed_days = self.mooncycle - 4
            # calculate the days per quarter
            quarter = unnamed_days / 4.0
            # determine phase
            if moonidx<1:
                phase = "new moon"
            elif moonidx<(quarter+1):
                phase = "waxing crescent"
            elif moonidx<(quarter+2):
                phase = "first quarter"
            elif moonidx<(2*quarter+2):
                phase = "waxing moon"
            elif moonidx<(2*quarter+3):
                phase = "full moon"
            elif moonidx<(3*quarter+3):
                phase = "waning moon"
            elif moonidx<(3*quarter+4):
                phase = "last quarter"
            else:
                phase = "waning crescent"
            return phase

# screen calendar_testing:
#     vbox:
#         xminimum 500
#         xfill True
#         spacing 10
#         align(0.5, 0.1)
#         text "Day: %d"%calendar.game_day()
#         text "Week: %d"%calendar.week()
#         text "Date: %s"%calendar.string()
#         text "Next Leap Year: %s"%calendar.leapyear
#         text "Lunar Progress: %d%%"%calendar.lunarprogress()
#         text "Moon Phase: %s"%calendar.moonphase().capitalize()

screen calendar_hud_ui():
    frame:
        background "#f54242"
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        vbox:
            text "%s"%calendar.string()
            
# label start:
#     $ calendar = Calendar(5, 2, 2014, 2016) # Calendar(day, month, year, first leap year (can be ignored))
#     # $ calendar.next() <--- This will cause your calendar to advance by one day.
#     # $ calendar.next(days=7) <--- By one week, if one turn of your game is a week.
    
#     show screen calendar_testing
    
#     while True: # This has nothing to do with calendar, just to make sure that we can toy with it without leaving the game.
#         $ result = ui.interact()
