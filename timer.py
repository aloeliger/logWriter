import urwid
import time

timerBar = urwid.ProgressBar('timer_bg', 'timer_fill')

class timerHandle():
    def __init__(self):
        self.handle = None

theHandle = timerHandle()

#this method will update the timer every second and update the handle
# necessary to stop the timer
def update_timer(loop, user_data=0):
    timeElapsed = user_data #time elapsed in seconds
    totalProgress = (timeElapsed/28800) * 100.0 # total progress on eight hours
    if totalProgress > 100.0:
        totalProgress = 100.0
    timerBar.set_completion(totalProgress)
    theHandle.handle = loop.set_alarm_at(time.time()+1, update_timer, user_data=timeElapsed+1)

# This method will remove the ticking timer, and reset the timer
# requires button.loop to be set to a handle to the main loop
def reset_timer(button, user_data=None):
    if theHandle.handle != None:
        timerStop = button.loop.remove_alarm(theHandle.handle)
        if not timerStop:
            raise RuntimeError("Failed to stop timer on reset")
    timerBar.set_completion(0.0)

# initial kick start from the start button, 
# requires button.loop to be set to a handle to the main loop
def start_timer(button, user_data=None):
    update_timer(button.loop, user_data=0)

timerStartButton = urwid.Button(
    label='Start',
    on_press=start_timer,
)

timerResetButton = urwid.Button(
    label='Reset',
    on_press=reset_timer,
)

timerStartAttr = urwid.AttrMap(
    timerStartButton,
    'start_button',
    'start_button_focus'
)

timerResetAttr = urwid.AttrMap(
    timerResetButton,
    'reset_button',
    'reset_button_focus'    
)

buttonColumns = urwid.Columns(
    widget_list=[
        timerStartAttr,
        timerResetAttr,
    ]
)

timerColumns = urwid.Columns(
    widget_list=[
        timerBar,
        buttonColumns
    ]
)

timer = urwid.LineBox(timerColumns)