import gpiozero as GPIO
from numpy import uint16
from time import sleep

FPS: int = 16

LEDs: list[GPIO.LED] = [GPIO.LED(17), GPIO.LED(27), GPIO.LED(22), GPIO.LED(23), GPIO.LED(24), GPIO.LED(25), GPIO.LED(5), GPIO.LED(6), GPIO.LED(16), GPIO.LED(26)]

def PlayStr(String: str) -> None:
    for I in range(10):
        if String[I] == "0":
            LEDs[I].off()
        else:
            LEDs[I].on()

def PlayUInt8(Num: uint16) -> None:
    for I in range(10):
        LEDs[I].on() if Num & uint16(2**I) else LEDs[I].off()

if __name__ == "__main__":
    Frames: list[str | uint16] = []
    
    with open("./frames.txt", "rt", encoding="ascii") as FrameData:
        for Line in FrameData.readlines():
            CLine: str = Line.strip()
            if CLine.startswith("$"):
                Frames = []
                continue
            if not CLine.startswith("#"):
                if not CLine.startswith("I"):
                    Frames.append(CLine)
                else:
                    Frames.append( uint16( CLine.replace("I", "") ) )

    for Frame in Frames:
        sleep(1/FPS)

        if isinstance(Frame, str):
            PlayStr(Frame)
        else:
            PlayUInt8(Frame)
    
    sleep(2)
    for I in range(10):
        LEDs[I].off()