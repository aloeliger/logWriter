# two utility classes for holding events
# and a list of events,
# and related widgets for it
# sub classes of this will handle the specifics of the information that go into each

import urwid
import datetime
import pytz
from collections import OrderedDict

from inputForm import inputFormWButtons

parisTimezone = pytz.timezone("Europe/Paris")


def displayButtonPress(button, user_data=None):
    button.parentEvent.inputForm.setFields(button.parentEvent.getFieldContents())
    button.parentEvent.currentDisplayWidget = button.parentEvent.inputForm
    button.parentEvent.parentList.updateDisplayList()


def saveButtonPress(button, user_data=None):
    button.parentEvent.inputForm.updateFields()
    button.parentEvent.fieldContents = button.parentEvent.inputForm.getFields()
    button.parentEvent.currentDisplayWidget = button.parentEvent.displayButtonBox
    button.parentEvent.parentList.updateDisplayList()


def deleteButtonPress(button, user_data=None):
    theEvent = button.parentEvent
    theList = theEvent.parentList
    theList.removeElement(theEvent)
    theList.updateDisplayList()


class logEvent:
    def __init__(self, fieldContents: OrderedDict, type:str):
        self.time = datetime.datetime.now(parisTimezone)

        self.str_time = self.time.strftime("%H:%M")
        self.fieldContents = fieldContents
        self.type = type

        self.label = f"{self.str_time}: {self.type}"

        self.inputForm = inputFormWButtons(
            fields=self.fieldContents,
            title=self.label,
        )
        self.inputForm.saveButton.parentEvent = self
        urwid.connect_signal(
            self.inputForm.saveButton,
            "click",
            callback=saveButtonPress,
        )
        self.inputForm.deleteButton.parentEvent = self
        urwid.connect_signal(
            self.inputForm.deleteButton, "click", callback=deleteButtonPress
        )

        self.displayButton = urwid.Button(
            label=self.label,
            on_press=displayButtonPress,
        )
        self.displayButton.parentEvent = self
        self.displayButtonAttr = urwid.AttrMap(
            self.displayButton,
            'log_event_button',
            'log_event_button_focus',
        )
        self.displayButtonBox = urwid.LineBox(
            self.displayButtonAttr,
        )

        self.currentDisplayWidget = self.inputForm

    def getFieldContents(self):
        return self.fieldContents
    
    def toString(self):
        raise RuntimeError('Default log event toString called.')


class logEventList:
    def __init__(self, theInputList, theEvents: list = []):
        self.theInputList = theInputList
        self.theEvents = []
        for event in theEvents:
            self.appendEvent(event)

    def __getitem__(self, key):
        return self.theEvents[key]

    def __setitem__(self, key, value):
        self.theEvents[key] = value

    def sort(self):
        self.theEvents.sort(key=lambda x: x.time)

    def appendEvent(self, theEvent):
        theEvent.parentList = self
        self.theEvents.append(theEvent)
        self.theInputList.append(theEvent.currentDisplayWidget)

    def getListOfDisplayWidgets(self):
        displayWidgets = []
        for event in self.theEvents:
            displayWidgets.append(event.currentDisplayWidget)
        return displayWidgets

    def removeElement(self, theElement):
        # figure out what the current display widget is and remove it from the input list
        theLocation = self.theInputList.index(theElement.currentDisplayWidget)
        # print("Found it!")
        # print(theLocation)
        self.theInputList.pop(theLocation)
        self.theEvents.remove(theElement)

    # After we do something that should change what gets displayed in
    # the list that contains all the displayable elements
    def updateDisplayList(self):
        self.sort()
        displayWidgets = self.getListOfDisplayWidgets()
        for i in range(len(displayWidgets)):
            self.theInputList[i] = displayWidgets[i]  # in theory this should be smart?
