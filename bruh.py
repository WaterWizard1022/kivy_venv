# Source - https://stackoverflow.com/a
# Posted by user13676212
# Retrieved 2025-11-26, License - CC BY-SA 4.0

from kivy.lang import Builder

from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox

KV = """
<CB@TwoLineAvatarIconListItem>:
    IconLeftWidget:
        id: i1
        icon: "pencil" #root.icon
    IconRightWidget:
        icon: "a11.png" #this is a transparent png image of 188 bytes
        MDCheckbox:
            id: x54
            on_active:
                app.save_checked(*args,root.text,root.secondary_text,root.ids.i1.icon,root)

BoxLayout:
    ScrollView:
        MDList:
            id: scroll
            #for i in range(15)#
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello jbsidis"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Josue Carranza"
                secondary_text: "jbsidis"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            CB:
                text: "Hello"
                secondary_text: "Two"
                icon: "pencil"
            
    MDRaisedButton:
        id: cm
        text: "Save"
        on_release: app.save_checked()
"""

selected_item = []
class MainAppjbsidis(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def save_checked(self,checkbox, value,a,b,c,w):
        mmm="""
            You clicked on:  Josue Carranza jbsidis
            Selected Items 4: [[<WeakProxy to <kivy.factory.CB object at 0x7efc032f4430>>], [<WeakProxy to <kivy.factory.CB object at 0x7efc032f4430>>], [<WeakProxy to <kivy.factory.CB object at 0x7efc0324d9e0>>], [<WeakProxy to <kivy.factory.CB object at 0x7efc03137b30>>]]
            """
        if value:
            print('The checkbox is active', 'and', checkbox.state, 'state')
            global selected_item
            if len(selected_item)==0:
                selected_item = []
                selected_item.append([w])
                print("\n\nYou clicked on: ",a,b,c)
                print("Selected Items "+str(len(selected_item))+": "+str(selected_item))
            if len(selected_item)>0:
                selected_item.append([w])
                print("\n\nYou clicked on: ",a,b,c)
                print("Selected Items "+str(len(selected_item))+": "+str(selected_item))
                self.root.ids.cm.text="Save "+str(len(selected_item))
        else:
            print('\n\nThe checkbox is inactive', 'and', checkbox.state, 'state')
            new_list=[]
            if len(selected_item)>0:
                for x in selected_item:
                    if x==w:
                        pass
                    if x!=w:
                        new_list=new_list+[w]
                selected_item=new_list
                
                print("\n\nNew Items: "+str(selected_item))
                
MainAppjbsidis().run()
