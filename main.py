<<<<<<< HEAD
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDTimePicker
from datetime import datetime
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from database import Database
import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

db = Database()

class ListItemWithCheckbox(TwoLineAvatarIconListItem):

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk
    def mark(self, check, the_list_item):
        '''mark the task as complete or incomplete'''
        if check.active == True:
            the_list_item.text = '[s]'+the_list_item.text+'[/s]'
            db.mark_lesson_as_complete(the_list_item.pk)
        else:
            the_list_item.text = str(db.mark_lesson_as_incomplete(the_list_item.pk))

    def delete_item(self, the_list_item):
        '''Delete the task'''
        self.parent.remove_widget(the_list_item)
        db.delete_task(the_list_item.pk)




class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left CheckBox'''

class DialogContent(MDBoxLayout):
    """OPENS A DIALOG BOX """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # set the date_text label to today's date when useer first opens dialog box
        self.ids.time_text.text = str(datetime.now().strftime('%H:%M %p'))


    def show_time_picker(self):
        """Opens the time picker"""
        date_dialog = MDTimePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value):

        time = value.strftime('%H:%M %p')
        self.ids.time_text.text = str(time)


class MainApp(MDApp):
    #...
    lesson_list_dialog = None
    def build(self):
        # Setting theme 
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"

    
    def show_task_dialog(self):
        if not self.lesson_list_dialog:
            self.lesson_list_dialog = MDDialog(
                title="Add Lecture",
                type="custom",
                content_cls=DialogContent(),
            )

        self.lesson_list_dialog.open()
    
    def on_start(self):
        """Load the saved tasks and add them to the MDList widget when the application starts"""
        try:
            completed_tasks, uncomplete_tasks = db.get_lessons()

            if uncomplete_tasks != []:
                for task in uncomplete_tasks:
                    add_task = ListItemWithCheckbox(pk=task[0],text=task[1], secondary_text=task[2])
                    self.root.ids.container.add_widget(add_task)

            if completed_tasks != []:
                for task in completed_tasks:
                    add_task = ListItemWithCheckbox(pk=task[0],text='[s]'+task[1]+'[/s]', secondary_text=task[2])
                    add_task.ids.check.active = True
                    self.root.ids.container.add_widget(add_task)
        except Exception as e:
            print(e)
            pass
    def close_dialog(self, *args):
        self.lesson_list_dialog.dismiss()
    def add_task(self, task, task_date):
            '''Add task to the list '''

            # Add task to the db
            created_task = db.create_task(task.text, task_date)

            # return the created task details and create a list item
            self.root.ids['container'].add_widget(ListItemWithCheckbox(pk=created_task[0], text='[b]'+created_task[1]+'[/b]', secondary_text=created_task[2]))# Here
            task.text = ''
if __name__ == '__main__':

    MainApp().run()




=======
from kivy.lang import Builder
import psycopg2
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDTimePickerDialVertical
from kivymd.uix.snackbar import MDSnackbar,MDSnackbarSupportingText
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
        self.size_hint_x = None
        self.size_hint_y = None
        self.size = (150, 150)
        self.color = (0.8, 0.8, 0.8, 1)
    


class App1(MDApp):
    def create_table(self):
        '''
        conn = psycopg2.connect(
			host = "ccu6unqr99fgui.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com", 
			user = "u5n26bf6f6ifpr",
			password = "pc9052ef292d5046cdf83fb6731101b7f66209a03709ded41f53a4028108d6a4d",
			dbname = "d3o7isrekq6ci5",
			port="5432"
			)
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists timetable
			(name TEXT , time TEXT);
		 """)
        conn.commit()
        conn.close()
        '''
    def app_method(self):
        self.root.manager.current = self.root.manager.next()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        
        
        return Builder.load_file('layout.kv')
    def on_ok(
    self, time_picker_vertical: MDTimePickerDialVertical
):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Time is `{time_picker_vertical.time}`",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()
        time_picker_vertical.dismiss()


    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_cancel=self.on_cancel_time)
        time_picker_vertical.bind(on_ok=self.on_ok)
        time_picker_vertical.bind()
        time_picker_vertical.open()
    def on_cancel_time(
        self, time_picker_vertical: MDTimePickerDialVertical
    ):
        time_picker_vertical.dismiss()

    

    def show_alert_dialog(self,*args):
        
        self.dialog = MDDialog(
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
                        text="Lecture Name/Code",
                    ),
                    mode="outlined",

                    
                    ),

                MDDivider(
                ),
                MDButton(
                    MDButtonText(text="Select Time",pos_hint={"center_x": 0.5, "center_y": 0.5},),
                    style="outlined",
                    theme_width = 'Custom',
                    size_hint_x=1,
                    pos_hint={"center_x": 0.5, "center_y": 0.8},
                    on_release=self.show_time_picker_vertical
                    
                        
                ),
                orientation="vertical"
                    ),
                
            
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancel"),
                    style="text",
                    on_release=lambda x:self.close_dialog(),
       
                ),
                MDButton(
                    MDButtonText(text="Accept"),
                    style="text",
                    on_release=lambda x:self.submit()
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        )
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()

    
    def submit(self):
        self.dialog.dismiss()
        for _ in range(50):
            self.root.ids.container.add_widget(
                MDListItem(
                    MDListItemHeadlineText(text="Headline",),
                )                  
            )
            

        

        






App1().run()
>>>>>>> 55fbd6bf5129c73ba3cde657113d0f833d2bb545
