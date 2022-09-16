from tkinter import Button, Label, Entry

class MyButton(Button):

    def __init__(self, root, text, command, *args, **kwargs):
        button_font = ("Helvetica", 12, "bold")
        button_background = "#084c61"
        button_text_colour = "#bee9e8"
        self.root = root
        self.text = text
        self.font = button_font
        self.command = command
        super().__init__()
        self["text"] = self.text
        self["command"] = self.command
        self["bg"] = button_background
        self["fg"] = button_text_colour
        self["activebackground"] = "#457b9d"
        self["width"] = 10
        self["font"] = button_font

class MyLabel(Label):

    def __init__(self, root, textvariable, font=("Helvetica", 12), highlightthickness=2, width=18, borderwidth=2, relief="groove"):
        font_style = ("Helvetica", 12)
        self.root = root
        self.textvariable = textvariable
        self.font = font
        self.highlightthickness = highlightthickness
        self.width = width
        self.borderwidth = borderwidth
        self.relief = relief
        super().__init__()
        self["textvariable"] = self.textvariable
        self["font"] = font_style
        self["highlightthickness"] = 2
        # self["width"] = 18
        self["borderwidth"] = 2
        self["relief"] = "groove"


class MyEntry(Entry):

    def __init__(self, root, textvariable, font=("Helvetica", 11), width=5, highlightthickness=2,  borderwidth=2, relief="groove"):
        font_style = ("Helvetica", 12)
        self.root = root
        self.textvariable = textvariable
        self.font = font
        self.highlightthickness = highlightthickness
        self.width = width
        self.borderwidth = borderwidth
        self.relief = relief
        super().__init__()
        self["textvariable"] = self.textvariable
        self["font"] = font_style
        self["highlightthickness"] = 2
        self["width"] = 18
        self["borderwidth"] = 2
        self["relief"] = "groove"


class MyEntryRight(Entry):

    def __init__(self, root, textvariable, font=("Helvetica", 11), width=5, justify="right", highlightthickness=2,  borderwidth=2, relief="groove"):
        font_style = ("Helvetica", 12)
        self.justify = justify
        self.root = root
        self.textvariable = textvariable
        self.font = font
        self.highlightthickness = highlightthickness
        self.width = width
        self.borderwidth = borderwidth
        self.relief = relief
        super().__init__()
        self["textvariable"] = self.textvariable
        self["justify"] = "right"
        self["font"] = font_style
        self["highlightthickness"] = 2
        self["width"] = 18
        self["borderwidth"] = 2
        self["relief"] = "groove"
