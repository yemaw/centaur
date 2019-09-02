
control.inBackground(function () {
    while (true) {
        motor.MotorRun(motor.Motors.M1, (Data['M1'] >= 0 ? motor.Dir.CW : motor.Dir.CCW), Math.constrain(Math.abs(Data['M1']), 0, 255))
        motor.MotorRun(motor.Motors.M2, (Data['M2'] >= 0 ? motor.Dir.CW : motor.Dir.CCW), Math.constrain(Math.abs(Data['M2']), 0, 255))
        motor.MotorRun(motor.Motors.M3, (Data['M3'] >= 0 ? motor.Dir.CW : motor.Dir.CCW), Math.constrain(Math.abs(Data['M3']), 0, 255))
        motor.MotorRun(motor.Motors.M4, (Data['M4'] >= 0 ? motor.Dir.CW : motor.Dir.CCW), Math.constrain(Math.abs(Data['M4']), 0, 255))
        basic.pause(10)
    }
})

serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    let line = serial.readUntil(serial.delimiters(Delimiters.NewLine))
    let data: any[] = line.split(' ')
    if (data[0] == 'MOTORS_STOP') {
        Data['M1'] = 0
        Data['M2'] = 0
        Data['M3'] = 0
        Data['M4'] = 0
    } else {
        Data[data[0]] = parseInt(data[1])
    }

})
let Data: any = {
    'M1': 0,
    'M2': 0,
    'M3': 0,
    'M4': 0
}

motor.motorStopAll()


