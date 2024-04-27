import wave
import os
class AudioSteg:
#encode****************************************
# Read wave audio file
 def encod(self, audio, msg, key, newfile):
  audio = audio + '.wav'
  newfile = newfile + '.wav'
  isExist = os.path.exists(audio)
  if isExist is False:
     exit
     print("file not found")

  else:
   song = wave.open(audio, mode='rb')

# Read frames and convert to byte array
   frame_bytes = bytearray(list(song.readframes(song.getnframes())))


   delimiter = '<DELI>'

# Append key and message with delimiters
   string=  key + '#' + msg +  '#' + delimiter

# Convert text to bit array
   bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

# Replace LSB of each byte of the audio data by one bit from the text bit array
   for i, bit in enumerate(bits):
       frame_bytes[i] = (frame_bytes[i] & 254) | bit

# Get the modified bytes
   frame_modified = bytes(frame_bytes)

# Write bytes to a new wave audio file
   with wave.open( newfile, 'wb') as fd:
       fd.setparams(song.getparams())
       fd.writeframes(frame_modified)
       print("encoded successfuly")

   song.close()


   #decode**************************************

 def decod(self ,filename, reference_key):
   filename = filename + '.wav'
   isExist = os.path.exists(filename)
   if isExist is False:
      print("file not exist")
      exit  
   else:
    song = wave.open(filename, mode='rb')
  
#  Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

# Find and split key and message using delimiter '#'
    if '<DELI>' in string:
        key_and_message = string[:string.find('<DELI>')]
        delimiter_index = key_and_message.find('#')
        key = key_and_message[:delimiter_index]
        if key != reference_key:
           exit
           print ("Key verification failed.")
          
        else:
           message = key_and_message[delimiter_index + 1:]
           print("Successfully decoded: " + message[:-1])
           return message[:-1]

    song.close()