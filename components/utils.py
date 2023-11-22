import os
import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
import hashlib, random, string


salt_len = 8
def hash_password(password, salt_len):
    salt = os.urandom(salt_len)
    hashed_password = hashlib.sha256(password.encode()).digest() + salt
    return hashed_password.hex()
def get_digest(password_hex, salt_len):
    password_digest = bytes.fromhex(password_hex)
    return password_digest[:len(password_digest) - salt_len]
def validate_password(input, from_dir, salt_len):
    hashed_password = hashlib.sha256(input.encode()).digest()
    from_dir = get_digest(from_dir, salt_len)
    if hashed_password == from_dir:
        return True
    return False

def forget_old_widgets(frame: tk.Frame):
    if frame.children:
        for name, widget in list(frame.children.items()):
            if name != 'loginframe':
                widget.destroy()

def read_size_bs_bytes(size, data):
    bs = AES.block_size
    chunk_size = size * bs
    offset = 0
    while offset < len(data):
        chunk = data[offset:offset + chunk_size]
        offset += chunk_size
        yield chunk

def create_vol(address, name, size):
    file_path = address + "/" + name
    size_bytes = size * 1024 * 1024 
    with open(file_path, 'wb') as fileVol:
        fileVol.seek(0)
        address_in_byte = bytes(address, 'utf-8')
        fileVol.write(address_in_byte)

        fileVol.seek(8)
        size_in_byte = size_bytes.to_bytes(4, byteorder='big')
        fileVol.write(size_in_byte)

        fileVol.seek(12)
        name_in_byte = bytes(name, 'utf-8')
        fileVol.write(name_in_byte)

        fileVol.write(b'\0' * (int(size_bytes)-20))

    return True  

def format_vol(vol, name):
    with open(vol, 'rb') as fileVol:
        default_data = fileVol.read()
        fileVol.seek(8)
        size = int.from_bytes(fileVol.read(4),byteorder='big')
        idbackup = int(size*2.5/4)
        fileVol.seek(idbackup)
        backup_content = fileVol.read()
    with open(vol, 'wb') as fileVol:
        fileVol.seek(0)
        fileVol.write(default_data) 
        
        fileVol.seek(12)
        name_in_byte = bytes(name, 'utf-8')
        fileVol.write(name_in_byte)

        fileVol.write(b'\0' * (size-20))

        fileVol.seek(idbackup)
        fileVol.write(backup_content)
    
    filename = str(vol)
    elements = filename.split('/')
    addr = '/'.join(elements[:-1])

    name = addr + '/' + name

    os.rename(filename, name)
    return True  

def setpass_vol(vol, oldpw, newpw):
    check = hash_password(oldpw, int(salt_len))
    isPass = b'\x00'
    with open(vol, 'rb') as fileVol:
        default_data = fileVol.read()
        fileVol.seek(20)
        isPass = fileVol.read(1)
        fileVol.seek(21)
        passhase = fileVol.read(len(check))
        pass_hashed = passhase[:len(check)].decode()
    
    with open(vol, 'wb') as fileVol:
        if (isPass != b'\x00'):
            if validate_password(oldpw, pass_hashed, int(salt_len)):
                fileVol.seek(0)
                fileVol.write(default_data)
                newpw_in_byte = bytes(hash_password(newpw, salt_len),'utf-8')
                fileVol.seek(21)
                fileVol.write(newpw_in_byte)
            else: 
                fileVol.seek(0)
                fileVol.write(default_data)
                messagebox.showerror(title='LỖI', message='Mật khẩu cũ volume không đúng!')
                return False
        else:
            fileVol.seek(0)
            fileVol.write(default_data)
            fileVol.seek(20)
            c = 1
            fileVol.write(c.to_bytes(c, byteorder='big'))
            newpw_in_byte = bytes(hash_password(newpw, salt_len),'utf-8')
            fileVol.seek(21)
            fileVol.write(newpw_in_byte)
    
    return True   

def open_vol(vol):
    listfile = []
    with open(vol, 'rb') as fileVol:
        fileVol.seek(101)
        n = 0
        n = int.from_bytes(fileVol.read(1),byteorder='big')
        for i in range(n):
            file = []
            filename = fileVol.read(8)
            filename = filename.decode('utf-8').replace('\x00','')
            file.append(filename)

            fileex = fileVol.read(3)
            file.append(fileex.decode('utf-8'))

            filesize = int.from_bytes(fileVol.read(4),byteorder='big')
            file.append(filesize)
            idfile = int.from_bytes(fileVol.read(4),byteorder='big')
            file.append(idfile)
            listfile.append(file) 

    return listfile   

def import_file_in(vol, file):
    with open(file, 'rb') as f:
        name = str(file).split('/')
        name = name[-1]
        content = f.read()
        size =  f.tell()
    list = open_vol(vol)
    with open(vol, 'rb') as fileVol:
        fileVol.seek(0)
        default_data = fileVol.read() 
        fileVol.seek(8)
        volsize = int.from_bytes(fileVol.read(4),byteorder='big')
    if len(list) != 0:
        last = list[-1]
        sizelast = last[2]
        idlast = last[3]
    else:     
        sizelast = 0
        idlast = int(volsize/8)
    
    with open(vol, 'wb') as fileVol:
        fileVol.seek(0)
        fileVol.write(default_data) 
    
        fileVol.seek(101)
        n = len(list)+1
        fileVol.write(n.to_bytes(1, byteorder='big'))
        
        arr = name.split('.')
        bname = '.'.join(arr[:-1])
        aname = arr[-1]
        fileVol.seek(102+19*len(list))
        name_in_byte = bytes(bname, 'utf-8')
        fileVol.write(name_in_byte)
        fileVol.seek(110+19*len(list))
        name_in_byte = bytes(aname, 'utf-8')
        fileVol.write(name_in_byte)

        fileVol.seek(113+19*len(list))
        size_in_byte = size.to_bytes(4, byteorder='big')
        fileVol.write(size_in_byte)

        id = idlast + (81+sizelast)#*len(list)
        fileVol.seek(117+19*len(list))
        id_in_byte = id.to_bytes(4, byteorder='big')
        fileVol.write(id_in_byte)
        
        fileVol.seek(id+81)
        fileVol.write(content)
        
    return True


def export_file_out(vol, name, des):
    list = open_vol(vol)
    file = ''
    for i in list:
        filename = '.'.join(i[:2])
        if filename == name:
            file = i[0] + '.' + i[1]
            size = i[2]
            id = i[3]
            break
    if file == '':
        messagebox.showerror(title='LỖI', message='Không tìm thấy file đã nhập tên')
        return False
    else:
        #Giải mã file nếu file có cài mật khẩu
        with open(vol, 'rb') as fileVol:
            fileVol.seek(id)
            isPass = fileVol.read(1)
            fileVol.seek(id+81)
            content = fileVol.read(size)
        desfile = des + '/' + file
        with open(desfile, 'wb') as desfi:
            desfi.write(content)    
    return True

def getVolsize(volume):
    with open(volume, 'rb') as fileVol:
        fileVol.read()
        return fileVol.tell()

def delefile(volume, name):
    list = open_vol(volume)
    file = ''
    vt = 0
    for i in list:
        filename = '.'.join(i[:2])
        if filename == name:
            file = i[0] + '.' + i[1]
            size = i[2]
            id = i[3]
            break
        vt = vt + 1
    if file == '':
        messagebox.showerror(title='LỖI', message='Không tìm thấy file đã nhập tên')
        return False
    else:
        with open(volume, 'rb') as fileVol:
            default_data = fileVol.read()
            if (vt < len(list)-1):
                fileVol.seek(121+vt*19) 
                data1 = fileVol.read(19*(len(list)-vt+1))
                
                fileVol.seek(id + size + 81) 
                data2 = fileVol.read()
        with open(volume, 'wb') as fileVol:
            fileVol.write(default_data)
            fileVol.seek(id)    
            fileVol.write(b'\0' * (size+81))
            fileVol.seek(102+vt*19) 
            fileVol.write(b'\0' * (19))
            if (vt < len(list)-1):
                fileVol.seek(id)  
                fileVol.write(data2)
                fileVol.seek(102+vt*19)
                fileVol.write(data1)
                newlist = list[vt+1:len(list)]
                newid = id
                for i in newlist:
                    fileVol.seek(117+vt*19) 
                    vt=vt+1
                    fileVol.write(newid.to_bytes(4, byteorder='big'))
                    newid = newid + i[2] + 81
            n = len(list)-1
            fileVol.seek(101) 
            fileVol.write(n.to_bytes(1, byteorder='big'))
                
    return True

def passfile(volume, namefile, oldpw, newpw):
    return True