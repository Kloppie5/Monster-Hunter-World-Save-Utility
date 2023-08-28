from Crypto.Cipher import Blowfish

def endianness_reversal ( data: bytearray ) :
    for i in range(0, len(data), 4):
        data[i:i+4] = data[i:i+4][::-1]
    return data
def hexdump ( data: bytearray, start: int = 0, end: int = None, width: int = 16 ) :
    if end is None :
        end = len(data)
    for i in range(start , end , width) :
        ascii = ""
        for j in range(i, i+width) :
            if j < end :
                ascii += chr(data[j]) if 32 <= data[j] <= 126 else "."
            else :
                ascii += " "
        hexstr = " ".join(f"{data[j]:02x}" for j in range(i, i+width) if j < end)
        print(f"{i:08x}  {hexstr:48}  {ascii}")

class Savefile :
    # Monster Hunter World savefile class

    cipher = Blowfish.new(b"xieZjoe#P2134-3zmaghgpqoe0z8$3azeq", Blowfish.MODE_ECB)

    def __init__ ( self ) :
        pass

    def read_savefile ( self , filename ) :
        with open(filename , "rb") as f :
            data = bytearray(f.read())
        self.savefile = bytearray(endianness_reversal(bytearray(Savefile.cipher.decrypt(endianness_reversal(data)))))
        hexdump(self.savefile, 0, 0x100)
