import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import time
from datetime import datetime
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout

class Task(BoxLayout):
    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.checkbox = CheckBox(active=False)
        self.textinput = TextInput(text="Write here", multiline=False)
        self.add_widget(self.checkbox)
        self.add_widget(self.textinput)
        # self.remove_widget(self.checkbox)
        # self.clear_widgets(self.checkbox)
        

class RemindMeApp (App):
    def build(self):
        self.tasks = []
        self.layout = BoxLayout(orientation='vertical')

# Add a TextInput to create new tasks
        self.new_task_input=TextInput(hint_text='Enter your task topic and press "Add Task" button every time you want to add a new task', multiline=False)
        self.layout.add_widget(self.new_task_input)

# Button to add tasks
        add_task_button = Button(text="Add Task")
        add_task_button.bind(on_press=self.add_task)
        self.layout.add_widget(add_task_button)

# Button to delete tasks
        delete_task_button = Button(text="Delete Task")
        delete_task_button.bind(on_press=self.delete_task)
        self.layout.remove_widget(delete_task_button)

# # Button to delete tasks
#         clear_tasks_button = Button(text="Delete Task")
#         clear_tasks_button.bind(on_press=self.clear_tasks)
#         self.layout.remove_widget(clear_tasks_button)

# Reset checkboxes at midnight
        Clock.schedule_interval(self.reset_checkboxes_at_midnight, 60) # Check every 60 seconds
        return self.layout
    
    def add_task(self, instance):
        #Create a new task
        task = Task()
        self.tasks.append(task)
        self.layout.add_widget(task)

    def delete_task(self, instance):
        #Delete a task
        task = Task()
        self.tasks.remove(task)
        self.layout.remove_widget(task)

    # def clear_tasks(self, instance):
    #     #Clear all tasks
    #     task = Task()
    #     self.tasks.clear(task)
    #     self.layout.clear_widgets(task)

    def reset_checkboxes_at_midnight(self, dt):
        current_time = datetime.now().strftime("%H:%M")
        # Reset all checkboxes at midnight
        if current_time == "00:00":
            for task in self.tasks:
                task.checkbox.active=False

# Run the app
if __name__ == '__main__':
    RemindMeApp().run()