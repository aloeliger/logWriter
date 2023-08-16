import urwid


def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


# Setup right column
from clock import clock, update_time
from timer import timer, timerStartButton, timerResetButton
from eventButtons import buttonList, buttons

rightColumnFocusList = urwid.SimpleFocusListWalker(
    contents=[
        buttonList,
        timer,
    ]
)

rightColumnListBox = urwid.ListBox(rightColumnFocusList)

rightColumn = urwid.Frame(
    body=rightColumnListBox,
    header=clock,
)

# Setup event log and left column
from event import logEventList

leftColumnFocusList = urwid.SimpleFocusListWalker(contents=[])

eventLogList = logEventList(theInputList=leftColumnFocusList)

leftColumn = urwid.ListBox(leftColumnFocusList)

# hook up the right column buttons
for button in buttons:
    button.theLogEventList = eventLogList

# setup the overall columns
theColumns = urwid.Columns([leftColumn, rightColumn])

# setup main loop
from logPalette import thePalette

loop = urwid.MainLoop(theColumns, unhandled_input=exit_on_q, palette=thePalette)

timerStartButton.loop = loop
timerResetButton.loop = loop
update_time(loop)

loop.run()
