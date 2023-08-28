
class Savefile :

    def __init__ ( self ) :
        pass

    def read_savefile ( self , filename ) :
        print(f"Reading savefile {filename}...")
        with open(filename , "rb") as f :
            self.savefile = f.read()
        print(f"Read {len(self.savefile)} bytes.")
