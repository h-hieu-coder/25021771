import struct
def solve(path):
   with open(path , 'rb') as f:
      while True:
         byte_chunk = f.read(8)
         if (len(byte_chunk) < 8):
            break
         number = struct.unpack('d' , byte_chunk)[0]
         print(f'{number:.5f}')
path = input()
solve(path)