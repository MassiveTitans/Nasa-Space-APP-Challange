


class Led:
    def __init__(self ,  port ):
        self.port = port


    def led(self , aa , bb ):
        x = int(aa/bb)
        if x == 5:
            self.port.digital[2].write(0)
            self.port.digital[3].write(0)
            self.port.digital[4].write(0)
            self.port.digital[5].write(0)

        elif x  == 4:
            self.port.digital[2].write(0)
            self.port.digital[3].write(0)
            self.port.digital[4].write(0)
            self.port.digital[5].write(0)
            self.port.digital[2].write(1)
        elif x == 3:
            self.port.digital[2].write(0)
            self.port.digital[3].write(0)
            self.port.digital[4].write(0)
            self.port.digital[5].write(0)
            self.port.digital[2].write(1)
            self.port.digital[3].write(1)
        elif x == 2:
            self.port.digital[2].write(0)
            self.port.digital[3].write(0)
            self.port.digital[4].write(0)
            self.port.digital[5].write(0)
            self.port.digital[2].write(1)
            self.port.digital[3].write(1)
            self.port.digital[4].write(1)

        elif x == 1:
            self.port.digital[2].write(0)
            self.port.digital[3].write(0)
            self.port.digital[4].write(0)
            self.port.digital[5].write(0)
            self.port.digital[2].write(1)
            self.port.digital[3].write(1)
            self.port.digital[4].write(1)
            self.port.digital[5].write(1)


    def qizil_led(self , aa , bb):
        x = int(aa / bb)
        if x  ==  5:
            self.port.digital[6].write(0)
            self.port.digital[7].write(0)
            self.port.digital[8].write(0)
            self.port.digital[9].write(0)
        elif  x == 4:
            self.port.digital[6].write(0)
            self.port.digital[7].write(0)
            self.port.digital[8].write(0)
            self.port.digital[9].write(0)
            self.port.digital[6].write(1)
        elif x == 3:
            self.port.digital[6].write(0)
            self.port.digital[7].write(0)
            self.port.digital[8].write(0)
            self.port.digital[9].write(0)
            self.port.digital[6].write(1)
            self.port.digital[7].write(1)
        elif x == 2:
            self.port.digital[6].write(0)
            self.port.digital[7].write(0)
            self.port.digital[8].write(0)
            self.port.digital[9].write(0)
            self.port.digital[6].write(1)
            self.port.digital[7].write(1)
            self.port.digital[8].write(1)

        elif x == 1:
            self.port.digital[6].write(0)
            self.port.digital[7].write(0)
            self.port.digital[8].write(0)
            self.port.digital[9].write(0)
            self.port.digital[6].write(1)
            self.port.digital[7].write(1)
            self.port.digital[8].write(1)
            self.port.digital[9].write(1)
