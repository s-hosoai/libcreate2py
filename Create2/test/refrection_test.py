from create2.sensor import Sensor


while(True):
    raw = raw_input(">")
    temp = raw.split(" ")
    if(temp[0]=="stop"):
        break
    elif(len(temp)>1):
        command = temp[0]
        arg = temp[1] 
        sensor = Sensor()
        try:
            if getattr(sensor, command) != None:
                attr = setattr(sensor, command, int(arg))
                print sensor.current
        except AttributeError:
            pass
        except ValueError:
            pass
        
        