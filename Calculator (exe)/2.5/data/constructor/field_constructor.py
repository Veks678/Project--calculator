from tkinter import *
import tkinter as tk
import pyperclip


class Creating_fields:
    field_list = []

    def __init__(self, frame_fields, bg_fields, fg_fields, font_fields, \
                 wight_fields, padx_buttons, pady_buttons, fields_type, \
                 fields_label):
        self.__frame_fields = frame_fields
        self.__bg_fields = bg_fields
        self.__fg_fields = fg_fields
        self.__font_fields = font_fields
        self.__wight_fields = wight_fields
        self.__padx_buttons = padx_buttons
        self.__pady_buttons = pady_buttons
        self.__fields_type = fields_type
        self.__fields_label = fields_label

    def create_widgets(self):
        def check_keys(event):
            if self.__fields_label in 'Decision':
                if (event.keysym != 'BackSpace' and event.char != str() and \
                    event.state != 36):
                    return 'break'
                elif event.state == 36 and event.char in ('\x03'):
                      pyperclip.copy(self.field_list[1].get())
            elif self.__fields_label in 'Expression':
                if event.char.isdigit() == False and \
                   event.char not in ('+','-','*','/') and \
                   event.keysym != 'BackSpace' and event.state != 36:
                    return 'break'
                elif event.state == 36 and event.char in ('\x03'):
                    pyperclip.copy((self.field_list[0].get('1.0', END) \
                                    + event.char).replace('\n',''))

                elif event.state == 36 and event.char in ('\x16') and \
                     pyperclip.paste().isdigit():
                    self.field_list[0].insert(END, pyperclip.paste())

        self.__Field = self.__fields_type(self.__frame_fields,
                                        bg = self.__bg_fields,
                                        fg = self.__fg_fields,
                                        font = self.__font_fields,
                                        width = self.__wight_fields)

        self.__Field.bind("<Key>", check_keys)

    def run_widgets(self):
        self.__Field.pack(padx = self.__padx_buttons, \
                          pady = self.__pady_buttons, \
                          side = LEFT, fill = BOTH, expand = True)

        if len(self.field_list) > 1:
            del self.field_list[:]
        else:
            self.field_list.append(self.__Field)
