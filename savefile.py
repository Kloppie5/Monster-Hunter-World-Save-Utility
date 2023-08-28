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
        self.infodump()

    def infodump ( self ) :
        print(f"SavefileSignature       : [0x000000 - 0x000004] = 01 00 00 00")
        print(f"UNKNOWN_4_8             : [0x000004 - 0x00000C]")
        print(f"DataHash                : [0x00000C - 0x000020]")
        print(f"DataSize                : [0x000020 - 0x000028] = AC30A0")

        print(f"SteamID                 : [0x000028 - 0x000030]")
        print(f"PADDING_30_16           : [0x000030 - 0x000040]")
        print(f"OffsetControls          : [0x000040 - 0x000048] = 000060")
        print(f"OffsetOptions           : [0x000048 - 0x000050] = 300070")
        print(f"OffsetSection2          : [0x000050 - 0x000058] = 301080")
        print(f"OffsetCharacters        : [0x000058 - 0x000060] = 3010C8 {int.from_bytes(self.savefile[0x000058:0x000060], byteorder='little'):08X}")
        # Controls
        print(f"ControlsSignature       : [0x000060 - 0x000064] = {self.savefile[0x000060:0x000064].hex().upper()}")
        print(f"UNKNOWN_64_4            : [0x000064 - 0x000068] = 0C 00 00 00")
        print(f"ControlsSize            : [0x000068 - 0x000070] = 300000")
        print(f"ControlsData            : [0x000070 - 0x300070]")
        # Options
        print(f"OptionsSignature        : [0x300070 - 0x300074] = {self.savefile[0x300070:0x300074].hex().upper()}")
        print(f"UNKNOWN_300074_4        : [0x300074 - 0x300078] = 0C 00 00 00")
        print(f"OptionsSize             : [0x300078 - 0x300080] = 001000")
        print(f"OptionsData             : [0x300080 - 0x301080]")
        # Section2
        print(f"Section2Signature       : [0x301080 - 0x301084] = {self.savefile[0x301080:0x301084].hex().upper()}")
        print(f"UNKNOWN_301084_4        : [0x301084 - 0x301088] = 0C 00 00 00")
        print(f"Section2Size            : [0x301088 - 0x301090] = 000038")
        print(f"Section2Data            : [0x301090 - 0x3010C8]")
        # Characters
        print(f"CharactersSignature     : [0x3010C8 - 0x3010CC] = {self.savefile[0x3010C8:0x3010CC].hex().upper()}")
        print(f"UNKNOWN_3010CC_4        : [0x3010CC - 0x3010D0] = 0C 00 00 00")
        print(f"CharactersSize          : [0x3010D0 - 0x3010D8] = 7C2000")
        print(f"CharactersData          : [0x3010D8 - 0xAC30D8]")
        # Padding
        print(f"PADDING_AC30D8_8        : [0xAC30D8 - 0xAC30E0]")
