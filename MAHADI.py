import os,time,platform
os.system('clear')
print('[>] Checking Updates')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    os.system("chmod +x USER");os.system("./USER")
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
 
