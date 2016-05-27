class Event(enumerate):
    changeBumpsWheeldrops = 1
    changeWall = 2
    changeCliLeft = 3
    changeCliFrontLeft = 4
    changeCliFrontRight = 5
    changeCliRight = 6
    changeVirtualWall = 7
    changeOvercurrents = 8
    changeDirtDetect = 9
    changeUnused1 = 10
    changeIrOpcode = 11
    changeButtons = 12
    changeDistance = 13
    changeAngle = 14
    changeChargingState = 15
    changeVoltage = 16
    changeCurrent = 17
    changeTemperature = 18
    changeBatteryCharge = 19
    changeBatteryCapacity = 20
    changeWallSignal = 21
    changeCliLeftSignal = 22
    changeCliFrontLeftSignal = 23
    changeCliFrontRightSignal = 24
    changeCliRightSignal = 25
    changeUnused2 = 26
    changeUnused3 = 27
    changeChargerAvailable = 28
    changeOpenInterfaceMode = 29
    changeSongNumber = 30
    changeSongPlaying = 31
    changeOiStreamNumPackets = 32
    changeVelocity = 33
    changeRadius = 34
    changeVelocityRight = 35
    changeVelocityLeft = 36
    changeEncoderCountsLeft = 37
    changeEncoderCountsRight = 38
    changeLightBumper = 39
    changeLightBumpLeft = 40
    changeLightBumpFrontLeft = 41
    changeLightBumpCenterLeft = 42
    changeLightBumpCenterRight = 43
    changeLightBumpFrontRight = 44
    changeLightBumpRight = 45
    changeIrOpcodeLeft = 46
    changeIrOpcodeRight = 47
    changeLeftMotorCurrent = 48
    changeRightMotorCurrent = 49
    changeMainBrushCurrent = 50
    changeSideBrushCurrent = 51
    changeStasis = 52
    reachDistance = 53
    reachAngle = 54
    timeout = 55
    pushBumperLeft = 56
    pushBumperCenter = 57
    pushBumperRight = 58
    arriveTarget = 59
    leaveTarget = 60
    reachSonicDistance = 61