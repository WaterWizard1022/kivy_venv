from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
    MDTextFieldTrailingIcon,
    MDTextFieldMaxLengthText,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)

from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.list import MDListItem, MDListItemHeadlineText


Window.size = (400,800)

class Monday(Screen):
    pass
class Tuesday(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Monday(name='Monday'))
sm.add_widget(Tuesday(name='Tuesday'))


class NoteBox(MDListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        
       



class App1(MDApp):
    def app_method(self):
        self.root.manager.current = self.root.manager.next()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('layout.kv')
    def show_alert_dialog(self):
        MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="account-box-edit-outline",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="Add Lecture",
            ),

            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(
                    size_hint_x=0.5,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                ),
                MDTextField(
                    MDTextFieldLeadingIcon(
                        icon="account",
                    ),
                    MDTextFieldHintText(
                        text="Lecture Name",
                    ),
                    mode="outlined",

                    
                    pos_hint={"center_x": 0.5, "center_y": 0.5},),
                MDTextField(
                    MDTextFieldLeadingIcon(
                        icon="account",
                    ),
                    MDTextFieldHintText(
                        text="Lecture Name",
                    ),
                    mode="outlined",
                    
                    
                    pos_hint={"center_x": 0.5, "center_y": 0.5}),
                MDDivider(
                    size_hint_x=0.5,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                ),
                orientation="vertical"
                    ),
                
            
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancel"),
                    style="text",
                    
                        
                ),
                MDButton(
                    MDButtonText(text="Accept"),
                    style="text",
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        ).open()






App1().run()