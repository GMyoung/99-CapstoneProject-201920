import M2_rosebot
import mqtt_remote_method_calls as com
import time
import m2_gui_delegate

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_run()
    # go_along_black()
    # go_straight_for_seconds(99999,50)


def real_run():
    gui = m2_gui_delegate.Delegate_on_laptop()
    delegate = m2_gui_delegate.ResponderToGUIMessages(gui)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_ev3()

    while True:
        if delegate.stop_program:
            break
        time.sleep(0.01)