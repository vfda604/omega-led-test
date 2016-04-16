_exportpath = '/sys/class/gpio/gpiochip0/subsystem/export'
_unexportpath = '/sys/class/gpio/gpiochip0/subsystem/unexport'
_gpiopath = '/sys/class/gpio/gpio'

def writetofs(fname,data):
	f = open(fname, w)
    f.write(data)
    f.close()
    
    
    def readfromfs(fname):
        f = open(fname, r)
        s = f.read()
        f.close()
        if s[0] == '1':
            v = 1
            else:
                v = 0
                return v
                
    def readinput(pin):
        rdval = readfromfs(_gpiopath+str(pin))
        writetofs(_gpiopath+str(pin)+'direction',direction)
        
    def initpin(pin,direction):
        writetofs(_exportpath,str(pin))
        writetofs(_unexportpath,str(pin)+'/direction',direction)
        
    def closepin(pin):
        writetofs(_unexportpath,str(pin))
        
    def setoutput(pin,value):
        if value == 0:
            wrval='0'
        else
            wrval='1'
        writetofs(_gpiopath+str(pin)+'/value',wrval)    
                                    