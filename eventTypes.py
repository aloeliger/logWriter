from event import logEvent
from collections import OrderedDict
from prettytable import PrettyTable


def leftPadPrettyTable(theTable, nSpaces: int):
    theTable = theTable.split("\n")
    for i in range(len(theTable)):
        theTable[i] = " " * nSpaces + theTable[i] + "\n"
    theTable = "".join(theTable)
    return theTable


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
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        theRun = self.fieldContents["Run"]
        theStr += "{:<15}{:<30}{:>15}\n".format(str_time, "Run Start:", theRun)

        theStr += "-" * 60 + "\n"
        theStr += "\n"

        runKey = self.fieldContents["Key"]
        prescaleColumnName = self.fieldContents["Prescale Column"]
        prescaleColumn = self.fieldContents["Prescale Column Name"]
        deadtime = self.fieldContents["Deadtime"]

        runInfoTable = PrettyTable()
        runInfoTable.field_names = ["Run Info", "Value"]
        runInfoTable.add_rows(
            [
                ["Run key", runKey],
                ["Prescale Column Name", prescaleColumnName],
                ["Prescale Column", prescaleColumn],
                ["Deadtime", deadtime],
            ]
        )
        theStr += leftPadPrettyTable(runInfoTable.get_string(), nSpaces=15) + "\n"

        DAQL1Rate = self.fieldContents["DAQ L1 Rate"]
        DAQStreamPhysics = self.fieldContents["DAQ Stream Physics"]
        DAQStreamExpress = self.fieldContents["DAQ Stream Express"]
        L1ACalib = self.fieldContents["OMS L1A Calibration"]
        L1APhysics = self.fieldContents["OMS L1A Physics"]
        L1ARandom = self.fieldContents["OMS L1A Random"]
        L1ATotal = self.fieldContents["OMS L1A Total"]

        rateInfoTable = PrettyTable()
        rateInfoTable.field_names = ["Rate Type", "Rate (Hz)"]
        rateInfoTable.add_rows(
            [
                ["L1 Rate (Total, DAQ)", DAQL1Rate],
                ["Physics Stream Rate (DAQ)", DAQStreamPhysics],
                ["Express Stream Rate (DAQ)", DAQStreamExpress],
                ["L1A Calibration Rate (OMS)", L1ACalib],
                ["L1A Physics Rate (OMS)", L1APhysics],
                ["L1A Random Rate (OMS)", L1ARandom],
                ["L1A Total Rate (OMS)", L1ATotal],
            ]
        )
        theStr += leftPadPrettyTable(rateInfoTable.get_string(), nSpaces=15) + "\n"

        return theStr


class runEndLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Run", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Run End")

    def toString(self):
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        theRun = self.fieldContents["Run"]

        theStr += "{:<15}{:<30}{:>15}\n".format(str_time, "Run End:", theRun)
        theStr += "-" * 60 + "\n"
        theStr += "\n"

        return theStr


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
        theStr = ""

        str_time = self.time.strftime("%H:%M")

        theStr += "{:<15}{:<30}{:>15}\n".format(str_time, "Prescale Column Change:", "")
        theStr += "{:<15}{:<30}{:>15}\n".format("", "-" * 30, "")

        oldPrescaleColumnName = self.fieldContents["Old Prescale Column Name"]
        oldPrescaleColumn = self.fieldContents["Old Prescale Column"]
        newPrescaleColumnName = self.fieldContents["New Prescale Column Name"]
        newPrescaleColumn = self.fieldContents["New Prescale Column"]

        prescaleColumnChangeTable = PrettyTable()
        prescaleColumnChangeTable.field_names = ["", "Old", "New"]
        prescaleColumnChangeTable.add_rows(
            [
                ["Column Number", oldPrescaleColumn, newPrescaleColumn],
                ["Column Name", oldPrescaleColumnName, newPrescaleColumnName],
            ]
        )

        theStr += (
            leftPadPrettyTable(prescaleColumnChangeTable.get_string(), nSpaces=15)
            + "\n"
        )

        theStr += "\n"

        return theStr


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
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        warningDuration = self.fieldContents["Noticed Duration"]

        theStr += "{:<15}{:<30}{:>15}\n".format(
            str_time, "Persistent System Warning:", warningDuration
        )
        theStr += "{:<15}{:<30}{:>15}\n".format("", "-" * 30, "")

        subsystems = self.fieldContents["Subsystems"]
        warningInfo = self.fieldContents["Warning Info"]
        theStr += " " * 15 + f"Noticed in subsystems: {subsystems}"
        theStr += "\n"
        theStr += " " * 15 + f"Warning Info: {warningInfo}"
        theStr += "\n"
        theStr += "\n"

        return theStr


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
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        errorDuration = self.fieldContents["Noticed Duration"]

        theStr += "{:<15}{:<30}{:>15}\n".format(
            str_time, "Persistent System Error:", errorDuration
        )
        theStr += "{:<15}{:<30}{:>15}\n".format("", "-" * 30, "")

        subsystems = self.fieldContents["Subsystems"]
        errorInfo = self.fieldContents["Error Info"]
        theStr += " " * 15 + f"Noticed in subsystems: {subsystems}"
        theStr += "\n"
        theStr += " " * 15 + f"Error Info: {errorInfo}"
        theStr += "\n"
        theStr += "\n"

        return theStr


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
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        theStr += "{:<15}{:<30}{:>15}\n".format(str_time, "System Error:", "")
        theStr += "{:<15}{:<30}{:>15}\n".format("", "-" * 30, "")

        subsystems = self.fieldContents["Subsystems"]
        theStr += " " * 15 + f"noticed in subsystems: {subsystems}\n"

        errorInfo = self.fieldContents["Error Info"]
        theStr += " " * 15 + f"Info: {errorInfo}\n"

        theStr += "\n"

        return theStr


class otherLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Other Info", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Other Event")

    def toString(self):
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        theStr += "{:<15}{:<30}{:>15}\n".format(str_time, "Other:", "")
        theStr += "{:<15}{:<30}{:>15}\n".format("", "-" * 30, "")

        otherInfo = self.fieldContents["Other Info"]
        theStr += " " * 15 + f"{otherInfo}\n"

        theStr += "\n"

        return theStr


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
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        theRun = self.fieldContents["Run"]
        theStr += "{:<15}{:<30}{:>15}\n".format(
            str_time, "Shift Start:", f"Run: {theRun}"
        )
        theStr += "{:<15}{:<30}{:<15}\n".format("", "-" * 30, "")

        runKey = self.fieldContents["Key"]
        prescaleColumn = self.fieldContents["Prescale Column"]
        prescaleColumnName = self.fieldContents["Prescale Column Name"]
        runInfoTable = PrettyTable()
        runInfoTable.field_names = ["Run Info", "Value"]
        runInfoTable.add_rows(
            [
                ["Run Key", runKey],
                ["Prescale Column Name", prescaleColumnName],
                ["Prescale Column", prescaleColumn],
            ]
        )
        theStr += leftPadPrettyTable(runInfoTable.get_string(), nSpaces=15) + "\n"

        theStr += "\n"

        return theStr


class shiftEndLogEvent(logEvent):
    def __init__(self):
        fieldContents = OrderedDict(
            [
                ("Notes", ""),
            ]
        )
        super().__init__(fieldContents=fieldContents, type="Shift End")

    def toString(self):
        theStr = ""

        str_time = self.time.strftime("%H:%M")
        theStr += "{:<15}{:<30}{:>15}\n".format(str_time, "Shift End:", "")
        theStr += "{:<15}{:<30}{:>15}\n".format("", "-"*30, "")

        theNotes = self.fieldContents["Notes"]
        theStr += " "*15 + f"NOTES TO THE NEXT SHIFTER: {theNotes}\n"

        theStr += "\n"

        return theStr
