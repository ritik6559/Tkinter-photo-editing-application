import customtkinter as ctk
from panel import * 

class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars,export_image):
        super().__init__(master = parent)
        self.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

        self.add('Position')
        self.add('Color')
        self.add('Effects')
        self.add('Export')

        PositionFrame(self.tab('Position'), pos_vars)
        ColorFrame(self.tab('Color'), color_vars)
        EffectFrame(self.tab('Effects'), effect_vars)
        ExportFrame(self.tab('Export'), export_image)

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master = parent, fg_color='transparent')
        self.pack(expand = True, fill = 'both')
        SlidePanel(self, 'Rotation', pos_vars['rotate'], 0, 360)
        SlidePanel(self, 'Zoom', pos_vars['zoom'], 0, 200)
        SegmentedPanel(self, 'InverT', pos_vars['flip'], FLIP_OPTIONS)
        RevertButton(
            self, 
            (pos_vars['rotate'], ROTATE_DEFAULT),
            (pos_vars['zoom'], ZOOM_DEFAULT),
            (pos_vars['flip'], FLIP_OPTIONS[0])
        )

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(master = parent, fg_color='transparent')
        self.pack(expand = True, fill = 'both')

        SwitchPanel(self, (color_vars['grayscale'], 'B/W'), (color_vars['invert'], 'Invert'))
        SlidePanel(self, 'Brightness', color_vars['brightness'], 0, 5)
        SlidePanel(self, 'Vibrance', color_vars['vibrance'], 0, 5)
        RevertButton(
            self, 
            (color_vars['brightness'], BRIGHTNESS_DEFAULT),
            (color_vars['grayscale'], GRAYSCALE_DEFAULT),
            (color_vars['vibrance'], VIBRANCE_DEFAULT)
        )

class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(master = parent, fg_color='transparent')
        self.pack(expand = True, fill = 'both')

        DropDownPanel(self, effect_vars['effect'],EFFECT_OPTIONS )
        SlidePanel(self, 'Blur', effect_vars['blur'], 0, 30)
        SlidePanel(self, 'Contrast', effect_vars['contrast'], 0, 10)

        RevertButton(
            self, 
            (effect_vars['blur'], BLUR_DEFAULT),
            (effect_vars['contrast'], CONTRAST_DEFAULT),
            (effect_vars['effect'], EFFECT_OPTIONS[0])
        )

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_image):
        super().__init__(master = parent, fg_color='transparent')
        self.pack(expand = True, fill = 'both')

        self.name_string = ctk.StringVar()
        self.file_string = ctk.StringVar(value = 'jpg')
        self.path_string = ctk.StringVar()

        FileNamePanel(self, self.name_string, self.file_string)
        FilePathPanel(self,self.path_string )
        SaveButton(self, export_image, self.name_string, self.file_string,self.path_string)
