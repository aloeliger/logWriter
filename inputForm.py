# custom widgets for handling pairs forms full of editable fields
import urwid
from collections import OrderedDict


class labeledTextField(urwid.WidgetWrap):
    def __init__(self, label, initial_text="", on_text_change=None):
        self.label = label
        self.initial_text = initial_text
        self.on_text_change = on_text_change
        self.textWidget = urwid.Text(self.label)
        self.textWidgetAttr = urwid.AttrMap(
            self.textWidget,
            "input_form_label",
            "input_form_label",
        )
        self.editWidget = urwid.Edit(edit_text=self.initial_text, multiline=True)
        self.editWidgetAttr = urwid.AttrMap(
            self.editWidget,
            "input_form_edit",
            "input_form_edit_focus",
        )
        self.columns = urwid.Columns(
            [
                ("fixed", len(self.label), self.textWidgetAttr),
                ("weight", 1, self.editWidgetAttr),
            ]
        )
        super().__init__(self.columns)

        urwid.connect_signal(self.editWidget, "change", self._on_edit_text_change)

    def _on_edit_text_change(self, widget, new_edit_text):
        if self.on_text_change:
            self.on_text_change(new_edit_text)

    def get_edit_text(self):
        return self.editWidget.get_edit_text()

    def set_edit_text(self, text):
        self.editWidget.set_edit_text(text)

    def get_label(self):
        return self.textWidget.get_text()[0]

    def set_label(self, text):
        self.textWidget.set_text(text)


class inputForm(urwid.WidgetWrap):
    def __init__(self, fields: OrderedDict, title: str = ""):
        self.fields = fields
        self.title = title
        self.labeledTextFields = []
        for field in self.fields:
            self.labeledTextFields.append(
                labeledTextField(
                    label=field + ": ",
                    initial_text=self.fields[field],
                )
            )
        self.pile = urwid.Pile(self.labeledTextFields)
        self.box = urwid.LineBox(self.pile, title=self.title)

        super().__init__(self.box)

    def __getitem__(self, key):
        return self.labeledTextFields[key]

    def __setitem__(self, key, value):
        self.labeledTextFields[key] = value

    def setFields(self, theFields):
        self.fields = theFields
        self.labeledTextFields = []
        newPileContents = []
        for field in self.fields:
            theField = labeledTextField(
                label=field + ": ", initial_text=self.fields[field]
            )
            self.labeledTextFields.append(theField)
            newPileContents.append(
                (theField, ("pack", None)),
            )

        self.pile.contents = newPileContents

    def updateFields(self):
        for labeledTextField in self.labeledTextFields:
            key = labeledTextField.get_label()
            key = key.rstrip(": ")
            value = labeledTextField.get_edit_text()
            self.fields[key] = value

    def getFields(self):
        return self.fields


class inputFormWButtons(urwid.WidgetWrap):
    def __init__(self, fields: OrderedDict, title: str = ""):
        self.fields = fields
        self.title = title

        self.theInputForm = inputForm(fields=self.fields, title=self.title)

        self.saveButton = urwid.Button(label="Save")
        self.saveButtonAttr = urwid.AttrMap(
            self.saveButton,
            'input_form_save_button',
            'input_form_save_button_focus',
        )
        self.saveButtonBox = urwid.LineBox(
            self.saveButtonAttr
        )

        self.deleteButton = urwid.Button(label="Delete")
        self.deleteButtonAttr = urwid.AttrMap(
            self.deleteButton,
            'input_form_delete_button',
            'input_form_delete_button_focus',
        )
        self.deleteButtonBox = urwid.LineBox(
            self.deleteButtonAttr
        )

        self.buttonColumn = urwid.Columns([self.saveButtonBox, self.deleteButtonBox])
        self.formPile = urwid.Pile(
            [
                self.theInputForm,
                self.buttonColumn,
            ]
        )

        super().__init__(self.formPile)

    def __getitem__(self, key):
        return self.theInputForm[key]

    def __setitem__(self, key, value):
        self.theInputForm[key] = value

    def setFields(self, theFields):
        self.theInputForm.setFields(theFields=theFields)

    def updateFields(self):
        self.theInputForm.updateFields()

    def getFields(self):
        return self.theInputForm.getFields()
