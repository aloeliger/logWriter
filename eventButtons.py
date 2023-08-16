import urwid
from eventTypes import *


def runStartEvent(button, user_data=None):
    theEvent = runStartLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def runEndEvent(button, user_data=None):
    theEvent = runEndLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def prescaleChangeEvent(button, user_data=None):
    theEvent = prescaleChangeLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def persistentWarningEvent(button, user_data=None):
    theEvent = persistentWarningLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def persistentErrorEvent(button, user_data=None):
    theEvent = persistentErrorLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def errorEvent(button, user_data=None):
    theEvent = errorLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def otherEvent(button, user_data=None):
    theEvent = otherLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def shiftStartEvent(button, user_data=None):
    theEvent = shiftStartLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def shiftEndEvent(button, user_data=None):
    theEvent = shiftEndLogEvent()
    button.theLogEventList.appendEvent(theEvent)


def writeLogEvent(button, user_data=None):
    pass


runStartButton = urwid.Button(
    label="Run Start",
    on_press=runStartEvent,
)

runStartButtonAttr = urwid.AttrMap(
    runStartButton,
    "run_start_button",
    "run_start_button_focus",
)

runEndButton = urwid.Button(
    label="Run End",
    on_press=runEndEvent,
)

runEndButtonAttr = urwid.AttrMap(
    runEndButton,
    "run_end_button",
    "run_end_button_focus",
)

prescaleChangeButton = urwid.Button(
    label="Prescale Change",
    on_press=prescaleChangeEvent,
)

prescaleChangeButtonAttr = urwid.AttrMap(
    prescaleChangeButton,
    "prescale_change_button",
    "prescale_change_button_focus",
)

persistentWarningButton = urwid.Button(
    label="Persistent Warning",
    on_press=persistentWarningEvent,
)

persistentWarningButtonAttr = urwid.AttrMap(
    persistentWarningButton,
    "persistent_warning_button",
    "persistent_warning_button_focus",
)

persistentErrorButton = urwid.Button(
    label="Persistent Error",
    on_press=persistentErrorEvent,
)

persistentErrorButtonAttr = urwid.AttrMap(
    persistentErrorButton,
    "persistent_error_button",
    "persistent_error_button_focus",
)

errorButton = urwid.Button(
    label="Error",
    on_press=errorEvent,
)

errorButtonAttr = urwid.AttrMap(
    errorButton,
    "error_button",
    "error_button_focus",
)

otherButton = urwid.Button(
    label="Other Event",
    on_press=otherEvent,
)

otherButtonAttr = urwid.AttrMap(
    otherButton,
    "other_button",
    "other_button_focus",
)

shiftStartButton = urwid.Button(
    label="Shift Start",
    on_press=shiftStartEvent,
)

shiftStartButtonAttr = urwid.AttrMap(
    shiftStartButton,
    "shift_start_button",
    "shift_start_button_focus",
)

shiftEndButton = urwid.Button(
    label="Shift End",
    on_press=shiftEndEvent,
)

shiftEndButtonAttr = urwid.AttrMap(
    shiftEndButton,
    "shift_end_button",
    "shift_end_button_focus",
)

writeLogButton = urwid.Button(
    label="Write Log",
    on_press=writeLogEvent,
)

writeLogButtonAttr = urwid.AttrMap(
    writeLogButton,
    "write_log_button",
    "write_log_button_focus",
)

buttons = [
    runStartButton,
    runEndButton,
    prescaleChangeButton,
    persistentWarningButton,
    persistentErrorButton,
    errorButton,
    otherButton,
    shiftStartButton,
    shiftEndButton,
    writeLogButton,
]

buttonAttrs = [
    runStartButtonAttr,
    runEndButtonAttr,
    prescaleChangeButtonAttr,
    persistentWarningButtonAttr,
    persistentErrorButtonAttr,
    errorButtonAttr,
    otherButtonAttr,
    shiftStartButtonAttr,
    shiftEndButtonAttr,
    writeLogButtonAttr,
]

buttonList = urwid.Pile(buttonAttrs)
