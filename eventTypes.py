from event import logEvent
from collections import OrderedDict


# Run start event
class runStartLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Run", ""),
                ("Key", ""),
                ("Prescale Column", ""),
                ("Prescale Column Name", ""),
                ("DAQ L1 Rate", ""),
                ("DAQ Stream Physics", ""),
                ("DAQ Stream Express", ""),
                ("OMS L1A Calibration", ""),
                ("OMS L1A Physics", ""),
                ("OMS L1A Random", ""),
                ("OMS L1A Total", ""),
                ("Deadtime", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Run Start")

    def toString(self):
        return ""


class runEndLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Run", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Run End")

    def toString(self):
        return ""


class prescaleChangeLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Old Prescale Column", ""),
                ("Old Prescale Column Name", ""),
                ("New Prescale Column", ""),
                ("New Prescale Column Name", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Prescale Change")

    def toString(self):
        return ""


class persistentWarningLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Subsystems", ""),
                ("Noticed Duration", ""),
                ("Warning Info", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Persistent Warning")

    def toString(self):
        return ""


class persistentErrorLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Subsystems", ""),
                ("Noticed Duration", ""),
                ("Error Info", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Persistent Error")

    def toString(self):
        return ""


class errorLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Subsystems", ""),
                ("Error Info", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Error")

    def toString(self):
        return ""


class otherLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Other Info", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Other Event")

    def toString(self):
        return ""


class shiftStartLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Run", ""),
                ("Key", ""),
                ("Prescale Column", ""),
                ("Prescale Column Name", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Shift Start")

    def toString(self):
        return ""


class shiftEndLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Notes", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Shift End")

    def toString(self):
        return ""
