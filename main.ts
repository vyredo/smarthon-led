WiFiIoT.on_wifi_connect(function (IP_Address, Device_ID) {
    basic.showIcon(IconNames.Yes)
    basic.showString(IP_Address)
})
WiFiIoT.on_wifi_disconnect(function (Error_code) {
    basic.showIcon(IconNames.No)
    basic.pause(1000)
    basic.showIcon(IconNames.Angry)
    basic.showString(Error_code)
})
WiFiIoT.initializeWifi(SerialPin.P16, SerialPin.P8)
WiFiIoT.setWifi("deco E4", "Family5664536")
basic.showIcon(IconNames.Heart)
led.enable(false)
SmartCity.turn_white_led(1023, AnalogPin.P3)
basic.pause(300)
SmartCity.turn_white_led(523, AnalogPin.P3)
basic.pause(300)
SmartCity.turn_white_led(0, AnalogPin.P3)
basic.forever(function () {
    if (SmartCity.read_motion_sensor(AnalogPin.P0) == true) {
        SmartCity.turn_white_led(1023, AnalogPin.P3)
        basic.pause(5000)
    } else {
        SmartCity.turn_white_led(0, AnalogPin.P3)
    }
})
