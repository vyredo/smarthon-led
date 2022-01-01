def on_wifi_connect(IP_Address, Device_ID):
    basic.show_icon(IconNames.YES)
    basic.show_string(IP_Address)
WiFiIoT.on_wifi_connect(on_wifi_connect)

def on_wifi_disconnect(Error_code):
    basic.show_icon(IconNames.NO)
    basic.pause(1000)
    basic.show_icon(IconNames.ANGRY)
    basic.show_string(Error_code)
WiFiIoT.on_wifi_disconnect(on_wifi_disconnect)

WiFiIoT.initialize_wifi(SerialPin.P16, SerialPin.P8)
WiFiIoT.set_wifi("deco E4", "Family5664536")
basic.show_icon(IconNames.HEART)
led.enable(False)
SmartCity.turn_white_led(1023, AnalogPin.P3)
basic.pause(300)
SmartCity.turn_white_led(523, AnalogPin.P3)
basic.pause(300)
SmartCity.turn_white_led(0, AnalogPin.P3)

def on_forever():
    if SmartCity.read_motion_sensor(AnalogPin.P0) == True:
        SmartCity.turn_white_led(1023, AnalogPin.P3)
        basic.pause(5000)
    else:
        SmartCity.turn_white_led(0, AnalogPin.P3)
basic.forever(on_forever)
