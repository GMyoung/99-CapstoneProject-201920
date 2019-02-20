import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import m2_gui
from PIL import ImageTk as itk
import time


# def real_run():
#     delegate = GUI(canvas)
#     mqtt_receiver = com.MqttClient(delegate)
#     mqtt_receiver.connect_to_pc()
#
#     while True:
#         time.sleep(0.01)

def main():
    delegate=Delegate_on_laptop()
    # real_run()s
    mqtt_sender=com.MqttClient(delegate)
    mqtt_sender.connect_to_ev3()


    welcome=tkinter.Tk()
    welcome.title("Boba Fett: Nemisis")
    welcome_page(welcome)
    main_frame=ttk.Frame(welcome,padding=10,borderwidth=5,relief='groove')
    main_frame.grid()
    welcome.mainloop()

    root = tkinter.Tk()
    root.title("Boba Fett: Nemisis")
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    control_panel,canvas=get_shared_frames(main_frame,mqtt_sender,delegate)
    grid_frames(control_panel,canvas)
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender,delegate):
    # global canvas
    control_panel = m2_gui.control_panel(main_frame, mqtt_sender)
    canvas,cv = m2_gui.canvas(main_frame)
    delegate.canvas=cv

    return control_panel, canvas

def grid_frames(control_panel, canvas):
    canvas.grid(row=0, column=0)
    control_panel.grid(row=1, column=0)

def welcome_page(root):
    global photo
    a = tkinter.Canvas(root, width=1200, height=600)
    photo = itk.PhotoImage(file='/Users/wushixin/Downloads/bobafett.gif')
    a.create_image(600, 250, image=photo)

    a.grid(row=0, column=0)
    continue_button = ttk.Button(root, text='Continue')
    continue_button.grid(row=1, column=0)
    continue_button['command'] = lambda: handle_continue(root)

    # return photo

# def introduction_page(root):
#     global photo
#     a = tkinter.Canvas(root, width=1200, height=600)
#     photo = itk.PhotoImage(file='/Users/wushixin/Downloads/bobafett.gif')
#     a.create_image(600, 250, image=photo)
#
#     a.grid(row=0, column=0)
#     continue_button = ttk.Button(root, text='Continue')
#     continue_button.grid(row=1, column=0)
#     continue_button['command'] = lambda: handle_continue(root)

def handle_continue(welcome):
    welcome.destroy()
    return True


# class GUI(object):
#     def __init__(self,cv):
#         self.cv=cv
#     def red(self):
#         print("red")

class Delegate_on_laptop(object):
    def __init__(self, canvas=None):
        self.canvas = canvas
    def test(self):
        print('test2')
        self.canvas.create_text(500,100,text='test!',fill='black')
    def blast(self,color,k):
        print('blast')
        self.canvas.create_rectangle(60+k*200,100,120+k*200,300,fill=color)

    # def










main()