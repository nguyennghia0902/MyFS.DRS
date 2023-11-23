import tkinter as tk
from tkinter import font
import tkinter.ttk as TTK
from tkinter import messagebox, filedialog

from components.utils import *

window_height = 400
window_width = 600

def page(mainframe: tk.Frame):

    mainframe.children['loginframe'].forget()

    user_page_frame = tk.Frame(
        mainframe,
        name='userpage',
        width=window_width,
        height=window_height
    )

    user_page_frame.pack(fill='both', expand=1)

    user_page_header_frame = tk.Frame(
        user_page_frame,
        name='header_frame',
        padx = 70,
        highlightthickness=3,
        highlightbackground='black'
    )
    
    user_page_header_frame.pack(fill='both')
    
    # Menu panel
    user_page_content_frame_left = tk.Frame(
        user_page_frame,
        name='menu_content_frame',
        width=50
    )
    func_label = tk.Label(
        user_page_content_frame_left,
        text='MENU',
        font=('Verdana',18,'bold')
    )
    
    create_vol_button = tk.Button(
        user_page_content_frame_left,
        text='Tạo volume',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    format_vol_button = tk.Button(
        user_page_content_frame_left,
        text='Định dạng volume',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    pass_vol_button = tk.Button(
        user_page_content_frame_left,
        text='Đặt/đổi mật khẩu volume',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    open_vol_button = tk.Button(
        user_page_content_frame_left,
        text='Mở/liệt kê các file trong volume',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    import_button = tk.Button(
        user_page_content_frame_left,
        text='Chép file vào volume',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    export_button = tk.Button(
        user_page_content_frame_left,
        text='Chép file ra ngoài',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    passfile_button = tk.Button(
        user_page_content_frame_left,
        text='Đặt/đổi mật khẩu file',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    delefile_button = tk.Button(
        user_page_content_frame_left,
        text='Xóa file trong volume',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    about_button = tk.Button(
        user_page_content_frame_left,
        text='Thông tin đồ án',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    
    user_page_content_frame_left.pack(fill='both',side = 'left', padx=20, pady=10)

    func_label.grid(row=0, column=0, columnspan=3)
    create_vol_button.grid(row=1, column=0, pady=5)
    format_vol_button.grid(row=2, column=0, pady=5)
    pass_vol_button.grid(row=3, column=0, pady=5)
    open_vol_button.grid(row=4, column=0, pady=5)
    import_button.grid(row=5, column=0, pady=5)
    export_button.grid(row=6, column=0, pady=5)
    passfile_button.grid(row=7, column=0, pady=5)
    delefile_button.grid(row=8, column=0, pady=5)
    about_button.grid(row=9, column=0, pady=5)
    
    # Content panel
    
    user_page_content_frame_right = tk.Frame(
        user_page_frame,
        name='content_frame',
        highlightthickness=2,
        bg='white',
        highlightbackground='black',
        width=360,
        height=290
    )
    user_page_content_frame_right.pack(pady=10, side='left', ipady=40)
    user_page_content_frame_right.grid_propagate(False)
    user_page_content_frame_right.pack_propagate(False)
    mess = '''
        ĐỒ ÁN GIỮA KỲ - An toàn và phục hồi dữ liệu - 20_22
        
        SINH VIÊN THỰC HIỆN:
        1. Bùi Nguyên Nghĩa - 19120600@student.hcmus.edu.vn
        2. Trà Như Khuyên - 20120130@student.hcmus.edu.vn
        
        GIẢNG VIÊN HƯỚNG DẪN:
        Thầy Thái Hùng Văn - thvan@fit.hcmus.edu.vn
        '''
    welcome_label = tk.Label(
            user_page_content_frame_right,
            text='Welcome!',
            bg='white',
            font=('Arial', 55)
        )
    welcome_label.grid(row=0, column=0, pady=5, sticky='w')
    welcome_label.place(x=175, y=150, anchor="center")
    
    def create_volume():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        address_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        address_frame.pack(side='left', fill='both')
        address_frame.grid_propagate(False)
        
        
        address_choose_label = tk.Label(
            address_frame,
            text='Chọn vị trí: ',
            font=('Verdana',8),
        )
        address_display = tk.Label(
            address_frame,
            wraplength=150,
            bg='white'
        )
        addr = tk.StringVar(address_frame)
        def get_address():
            get_address = filedialog.askdirectory(
                title='Chọn vị trí',
                initialdir=user_dir
            )
            addr.set(get_address)
            address_display['textvariable']=addr

        file_choose_button = tk.Button(
            address_frame,
            text='Chọn vị trí',
            command=get_address,
            anchor='w'
        )

        name_function_label = tk.Label(
            address_frame,
            text='TẠO VOLUME',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        address_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        address_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')

        user_frame = tk.Frame(
            user_page_content_frame_right,
            name='user_pick_frame',
            bg='white',
            width=190,
            height=290
        )

        user_frame.pack(side='left')
        user_frame.grid_propagate(False)

        
        setname_label = tk.Label(
            user_frame,
            text='Đặt tên:',
            font=('Verdana',8)
        )
        setname_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8)
        )

        setsize_label = tk.Label(
            user_frame,
            text='Chọn kích thước (MB):',
            font=('Verdana',8)
        )
        n = tk.StringVar()
        size_menu = TTK.Combobox(user_frame, width = 27,  
                            textvariable = n) 
        size_menu['values'] = ('100', '500', '1000', '2000') 
        
        size_menu.grid(column = 1, row = 15) 
    
        size_menu.current(0)  
        
        def submit():
            name = setname_entry.get().strip()
            size = int(size_menu.get().strip())
            if create_vol(addr.get(), name, size):
                messagebox.showinfo(title='CHÚC MỪNG', message='Tạo volume thành công')
            else: messagebox.showerror(title='LỖI', message='Tạo volume không thành công')
        submit_button = tk.Button(
            user_frame,
            text='Xác nhận',
            width=10,
            command=submit
        )
        
        
        setname_label.grid(row=0, column=0, pady=5)
        setname_entry.grid(row=1, column=0, pady=5)
        setsize_label.grid(row=3, column=0, pady=5)
        size_menu.grid(row=4, column=0, pady=5)
        submit_button.grid(row=5,column=0, pady=5)

    def format_volume():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        volume_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )

        volume_frame.pack(side='left', fill='both')
        volume_frame.grid_propagate(False)

        volume_choose_label = tk.Label(
            volume_frame,
            text='Chọn volume: ',
            font=('Verdana',8),
        )
        volume_display = tk.Label(
            volume_frame,
            wraplength=150,
            bg='white'
        )
        volume = tk.StringVar(volume_frame)
        
        def get_volume():
            get_volume = filedialog.askopenfilename(
                title='Chọn volume',
                initialdir=user_dir
            )
            volume.set(get_volume)
            volume_display['textvariable']=volume

        file_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )

        pass_label = tk.Label(
            volume_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            volume_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        checkpass_button = tk.Button(
            volume_frame,
            text='Kiểm tra',
            anchor='w'
        )
        name_function_label = tk.Label(
            volume_frame,
            text='ĐỊNH DẠNG VOLUME',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        volume_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        volume_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        checkpass_button.grid(row=6, column=0, pady=5, sticky='w')
        
        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)

            setname_label = tk.Label(
                user_frame,
                text='Đặt tên:',
                font=('Verdana',8)
            )
            setname_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )

            def submit():
                name = setname_entry.get().strip()
                if format_vol(volume.get(), name):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Định dạng volume thành công')
                else: messagebox.showerror(title='LỖI', message='Định dạng volume không thành công')
            submit_button = tk.Button(
                user_frame,
                text='Xác nhận',
                width=10,
                command=submit
            )
            setname_label.grid(row=0, column=0, pady=5)
            setname_entry.grid(row=1, column=0, pady=5)
            submit_button.grid(row=5,column=0, pady=5) 
        
        def check():
            pw = pass_entry.get().strip()
            vol = volume.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                default_data = fileVol.read()
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()
            if (isPass != b'\x00'):
                if validate_password(pw, pass_hashed, int(salt_len)):    
                    showright()
                    checkpass_button.grid_remove()
                else: messagebox.showerror(title='LỖI', message='Mật khẩu sai!')
            else:
                showright()
                checkpass_button.grid_remove()
                pass_label.grid_remove()
                pass_entry.grid_remove()
        checkpass_button['command'] = check
        
    def pass_volume():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        volume_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        volume_frame.pack(side='left', fill='both')
        volume_frame.grid_propagate(False)

        volume_choose_label = tk.Label(
            volume_frame,
            text='Chọn volume: ',
            font=('Verdana',8),
        )
        volume_display = tk.Label(
            volume_frame,
            wraplength=150,
            bg='white'
        )
        volume = tk.StringVar(volume_frame)
        def get_volume():
            get_volume = filedialog.askopenfilename(
                title='Chọn volume',
                initialdir=user_dir
            )
            volume.set(get_volume)
            volume_display['textvariable']=volume

        file_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )

        name_function_label = tk.Label(
            volume_frame,
            text='ĐẶT MẬT KHẨU VOLUME',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        volume_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        volume_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')

        user_frame = tk.Frame(
            user_page_content_frame_right,
            name='user_pick_frame',
            bg='white',
            width=190,
            height=290
        )

        user_frame.pack(side='left')
        user_frame.grid_propagate(False)

        oldpass_label = tk.Label(
            user_frame,
            text='Nhập mật khẩu cũ:',
            font=('Verdana',8)
        )
        oldpass_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8),  show='*'
        )

        setpass_label = tk.Label(
            user_frame,
            text='Nhập mật khẩu mới:',
            font=('Verdana',8)
        )
        setpass_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8),  show='*'
        )

        def submit():
            oldpw = oldpass_entry.get().strip()
            newpw = setpass_entry.get().strip()
            
            if setpass_vol(volume.get(), oldpw, newpw):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Đặt mật khẩu volume thành công')
            else: messagebox.showerror(title='LỖI', message='Đặt mật khẩu volume không thành công')
           
        submit_button = tk.Button(
            user_frame,
            text='Xác nhận',
            width=10,
            command=submit
        )

        oldpass_label.grid(row=0, column=0, pady=5)
        oldpass_entry.grid(row=1, column=0, pady=5)
        setpass_label.grid(row=3, column=0, pady=5)
        setpass_entry.grid(row=4, column=0, pady=5)
        submit_button.grid(row=5,column=0, pady=5)
    
    def open_volume():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        volume_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        volume_frame.pack(side='left', fill='both')
        volume_frame.grid_propagate(False)

        volume_choose_label = tk.Label(
            volume_frame,
            text='Chọn volume: ',
            font=('Verdana',8),
        )
        volume_display = tk.Label(
            volume_frame,
            wraplength=150,
            bg='white'
        )
        volume = tk.StringVar(volume_frame)
        def get_volume():
            get_volume = filedialog.askopenfilename(
                title='Chọn volume',
                initialdir=user_dir
            )
            volume.set(get_volume)
            volume_display['textvariable']=volume

        volume_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )
        
        name_function_label = tk.Label(
            volume_frame,
            text='MỞ VÀ XEM VOLUME',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        volume_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        volume_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        volume_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')

        user_frame = tk.Frame(
            user_page_content_frame_right,
            name='user_pick_frame',
            bg='white',
            width=190,
            height=290
        )

        user_frame.pack(side='left')
        user_frame.grid_propagate(False)

        pass_label = tk.Label(
            user_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8), show='*'
        )
        namefiles = []
        def submit():
            pw = pass_entry.get().strip()
            vol = volume.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()
            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                    listfile = open_vol(volume.get())
                    for i in listfile:
                        full = i[0] + '.' + i[1]
                        namefiles.append(full)
                    var = tk.Variable(value=namefiles)
                    listbox = tk.Listbox(
                        user_frame,
                        listvariable=var,
                        height=6,
                        selectmode=tk.EXTENDED
                    )
                    listbox.pack(expand=True, fill=tk.BOTH)
            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                messagebox.showerror(title='LỖI', message='Mật khẩu sai!')
        
        submit_button = tk.Button(
            user_frame,
            text='Danh sách các file',
            width=20,
            command=submit
        )

        pass_label.grid(row=0, column=0, pady=5)
        pass_entry.grid(row=1, column=0, pady=5)
        submit_button.grid(row=4,column=0, pady=5)
    
    def import_file():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        volume_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        volume_frame.pack(side='left', fill='both')
        volume_frame.grid_propagate(False)

        volume_choose_label = tk.Label(
            volume_frame,
            text='Chọn volume: ',
            font=('Verdana',8),
        )
        volume_display = tk.Label(
            volume_frame,
            wraplength=150,
            bg='white'
        )
        volume = tk.StringVar(volume_frame)
        def get_volume():
            get_volume = filedialog.askopenfilename(
                title='Chọn volume',
                initialdir=user_dir
            )
            volume.set(get_volume)
            volume_display['textvariable']=volume
        
        volume_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )

        pass_label = tk.Label(
            volume_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            volume_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        checkpass_button = tk.Button(
            volume_frame,
            text='Kiểm tra',
            anchor='w'
        )

        name_function_label = tk.Label(
            volume_frame,
            text='CHÉP FILE VÀO VOLUME',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        volume_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        volume_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        volume_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        checkpass_button.grid(row=6, column=0, pady=5, sticky='w')
        
        def showright():
            user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)
            file_choose_label = tk.Label(
                user_frame,
                text='Chọn file: ',
                font=('Verdana',8),
            )
            file_display = tk.Label(
                user_frame,
                wraplength=150,
                bg='white'
            )
            file = tk.StringVar(volume_frame)
            def get_file():
                get_file = filedialog.askopenfilename(
                    title='Chọn file',
                    initialdir=user_dir
                )
                file.set(get_file)
                file_display['textvariable']=file

            file_choose_button = tk.Button(
                user_frame,
                text='Chọn file',
                command=get_file,
                anchor='w'
            )
            file_choose_label.grid(row=5, column=0, pady=5, sticky='w')
            file_choose_button.grid(row=6, column=0, pady=5, sticky='w')
            file_display.grid(row=7, column=0, columnspan=1, pady=5, sticky='w')
            def submit():
                pw = ""
                addfile = file.get()
                if import_file_in(volume.get(), addfile):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Chép file vào thành công')
                else: messagebox.showerror(title='LỖI', message='Chép file vào không thành công')
            submit_button = tk.Button(
                    user_frame,
                    text='Chép',
                    width=10,
                    command=submit
                )
            submit_button.grid(row=8,column=0, pady=5)

        def check():
                pw = pass_entry.get().strip()
                vol = volume.get()
                check = hash_password(pw, int(salt_len))
                isPass = b'\x00'
                with open(vol, 'rb') as fileVol:
                    fileVol.seek(20)
                    isPass = fileVol.read(1)
                    fileVol.seek(21)
                    passhase = fileVol.read(len(check))
                    pass_hashed = passhase[:len(check)].decode()
                
                if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                    showright()
                    checkpass_button.grid_remove()
                    pass_label.grid_remove()
                    pass_entry.grid_remove()
                if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                    messagebox.showerror(title='LỖI', message='Mật khẩu sai!')
                
        checkpass_button['command'] = check

    def export_file():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        volume_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )
        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )
        volume_frame.pack(side='left', fill='both')
        volume_frame.grid_propagate(False)

        volume_choose_label = tk.Label(
            volume_frame,
            text='Chọn volume: ',
            font=('Verdana',8),
        )
        volume_display = tk.Label(
            volume_frame,
            wraplength=150,
            bg='white'
        )
        volume = tk.StringVar(volume_frame)
        def get_volume():
            get_volume = filedialog.askopenfilename(
                title='Chọn volume',
                initialdir=user_dir
            )
            volume.set(get_volume)
            volume_display['textvariable']=volume

        volume_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )

        pass_label = tk.Label(
            volume_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            volume_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        find_file_button = tk.Button(
                volume_frame,
                text='Danh sách các file',
                width=20
            )
        name_function_label = tk.Label(
            volume_frame,
            text='CHÉP FILE RA VOLUME',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        volume_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        volume_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        volume_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        find_file_button.grid(row=6,column=0, pady=5)
        
        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)
            
            type_label = tk.Label(
                user_frame,
                text='Nhập tên file cần chép:',
                font=('Verdana',8)
            )
            type_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )

            destination_choose_label = tk.Label(
                user_frame,
                text='Chọn thư mục: ',
                font=('Verdana',8),
            )
            destination_display = tk.Label(
                user_frame,
                wraplength=150,
                bg='white'
            )
            destination = tk.StringVar(volume_frame)
            def get_destination():
                get_destination = filedialog.askdirectory(
                    title='Chọn đích đến',
                    initialdir=user_dir
                )
                destination.set(get_destination)
                destination_display['textvariable']=destination

            destination_choose_button = tk.Button(
                user_frame,
                text='Chọn đích đến',
                command=get_destination,
                anchor='w'
            )
            passfile_label = tk.Label(
                user_frame,
                text='Nhập mật khẩu file:',
                font=('Verdana',8)
            )
            passfile_entry = tk.Entry(
                user_frame,
                width=10,
                font=('Verdana',8), show='*'
            )
            type_label.grid(row=0,column=0, pady=5)
            type_entry.grid(row=1,column=0, pady=5)
            passfile_label.grid(row=2,column=0, pady=5)
            passfile_entry.grid(row=3,column=0, pady=5)
            destination_choose_label.grid(row=4, column=0, pady=5, sticky='w')
            destination_choose_button.grid(row=5, column=0, pady=5, sticky='w')
            destination_display.grid(row=6, column=0, columnspan=1, pady=5, sticky='w')
            

            def submit():
                name = type_entry.get().strip()
                passfile = passfile_entry.get().strip()
                if export_file_out(volume.get(), name, passfile, destination.get()):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Chép file ra ngoài thành công')
                else: messagebox.showerror(title='LỖI', message='Chép file ra ngoài không thành công')
            submit_button = tk.Button(
                user_frame,
                text='Chép',
                width=10,
                command=submit
            )
            submit_button.grid(row=7,column=0, pady=5)

        def find_file():
            pw = pass_entry.get().strip()
            vol = volume.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()

            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                        namefiles=[]
                        listfile =  open_vol(volume.get())
                        for i in listfile:
                            full = i[0] + '.' + i[1]
                            namefiles.append(full)
                        var = tk.Variable(value=namefiles)

                        listbox = tk.Listbox(
                            volume_frame,
                            listvariable=var,
                            height=6,
                            selectmode=tk.EXTENDED
                        )
                        showright()
                        find_file_button.grid_remove()
                        pass_label.grid_remove()
                        pass_entry.grid_remove()
                        listbox.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        listbox.grid(row=4, column=0, pady=5)

            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                        messagebox.showerror(title='LỖI', message='Mật khẩu sai!')

        find_file_button['command']=find_file

    def delete_file():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        volume_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )
        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )
        volume_frame.pack(side='left', fill='both')
        volume_frame.grid_propagate(False)

        volume_choose_label = tk.Label(
            volume_frame,
            text='Chọn volume: ',
            font=('Verdana',8),
        )
        volume_display = tk.Label(
            volume_frame,
            wraplength=150,
            bg='white'
        )
        volume = tk.StringVar(volume_frame)
        def get_volume():
            get_volume = filedialog.askopenfilename(
                title='Chọn volume',
                initialdir=user_dir
            )
            volume.set(get_volume)
            volume_display['textvariable']=volume

        volume_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )

        pass_label = tk.Label(
            volume_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            volume_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        find_file_button = tk.Button(
                volume_frame,
                text='Danh sách các file',
                width=20
            )

        name_function_label = tk.Label(
            volume_frame,
            text='XÓA FILE TRONG VOLUME',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        volume_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        volume_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        volume_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        find_file_button.grid(row=6,column=0, pady=5)

        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)
            
            type_label = tk.Label(
                user_frame,
                text='Nhập tên file cần xóa:',
                font=('Verdana',8)
            )
            type_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )
            passfile_label = tk.Label(
                user_frame,
                text='Nhập mật khẩu file:',
                font=('Verdana',8)
            )
            passfile_entry = tk.Entry(
                user_frame,
                width=10,
                font=('Verdana',8), show='*'
            )

            def submit():
                name = type_entry.get().strip()
                passfile = passfile_entry.get().strip()
                if delefile(volume.get(), name, passfile):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Xóa file thành công')
                else: messagebox.showerror(title='LỖI', message='Xóa file  không thành công')
            submit_button = tk.Button(
                user_frame,
                text='Xóa',
                width=10,
                command=submit
            )
            type_label.grid(row=0,column=0, pady=5)
            type_entry.grid(row=1,column=0, pady=5)
            passfile_label.grid(row=2,column=0, pady=5)
            passfile_entry.grid(row=3,column=0, pady=5)
            submit_button.grid(row=4,column=0, pady=5)
        
        def find_file():
            pw = pass_entry.get().strip()
            vol = volume.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()

            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                        namefiles=[]
                        listfile =  open_vol(volume.get())
                        for i in listfile:
                            full = i[0] + '.' + i[1]
                            namefiles.append(full)
                        var = tk.Variable(value=namefiles)

                        listbox = tk.Listbox(
                            volume_frame,
                            listvariable=var,
                            height=6,
                            selectmode=tk.EXTENDED
                        )
                        showright()
                        find_file_button.grid_remove()
                        pass_label.grid_remove()
                        pass_entry.grid_remove()
                        listbox.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        listbox.grid(row=4, column=0, pady=5)

            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                        messagebox.showerror(title='LỖI', message='Mật khẩu sai!')

        find_file_button['command']=find_file    
        
    def pass_file():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        volume_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )
        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )
        volume_frame.pack(side='left', fill='both')
        volume_frame.grid_propagate(False)

        volume_choose_label = tk.Label(
            volume_frame,
            text='Chọn volume: ',
            font=('Verdana',8),
        )
        volume_display = tk.Label(
            volume_frame,
            wraplength=150,
            bg='white'
        )
        volume = tk.StringVar(volume_frame)
        def get_volume():
            get_volume = filedialog.askopenfilename(
                title='Chọn volume',
                initialdir=user_dir
            )
            volume.set(get_volume)
            volume_display['textvariable']=volume

        volume_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )

        pass_label = tk.Label(
            volume_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            volume_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        find_file_button = tk.Button(
                volume_frame,
                text='Danh sách các file',
                width=20
            )

        name_function_label = tk.Label(
            volume_frame,
            text='ĐẶT MẬT KHẨU FILE',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        volume_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        volume_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        volume_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        find_file_button.grid(row=6,column=0, pady=5)

        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)
            
            type_label = tk.Label(
                user_frame,
                text='Nhập tên file cần đặt mật khẩu:',
                font=('Verdana',8)
            )
            type_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )

            oldpass_label = tk.Label(
                user_frame,
                text='Nhập mật khẩu cũ:',
                font=('Verdana',8)
            )
            oldpass_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8),  show='*'
            )

            setpass_label = tk.Label(
                user_frame,
                text='Nhập mật khẩu mới:',
                font=('Verdana',8)
            )
            setpass_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8),  show='*'
            )

            def submit():
                name = type_entry.get().strip()
                oldpw = oldpass_entry.get().strip()
                newpw = setpass_entry.get().strip()
                if setpass_file(volume.get(), name, oldpw, newpw):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Đổi/đặt mật khẩu file thành công')
                else: messagebox.showerror(title='LỖI', message='Đổi/đặt mật khẩu file  không thành công')
            submit_button = tk.Button(
                user_frame,
                text='Xác nhận',
                width=10,
                command=submit
            )
            type_label.grid(row=0,column=0, pady=5)
            type_entry.grid(row=1,column=0, pady=5)
            oldpass_label.grid(row=2,column=0, pady=5)
            oldpass_entry.grid(row=3,column=0, pady=5)
            setpass_label.grid(row=4,column=0, pady=5)
            setpass_entry.grid(row=5,column=0, pady=5)
            submit_button.grid(row=6,column=0, pady=5)
        
        def find_file():
            pw = pass_entry.get().strip()
            vol = volume.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()

            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                        namefiles=[]
                        listfile =  open_vol(volume.get())
                        for i in listfile:
                            full = i[0] + '.' + i[1]
                            namefiles.append(full)
                        var = tk.Variable(value=namefiles)

                        listbox = tk.Listbox(
                            volume_frame,
                            listvariable=var,
                            height=6,
                            selectmode=tk.EXTENDED
                        )
                        showright()
                        find_file_button.grid_remove()
                        pass_label.grid_remove()
                        pass_entry.grid_remove()
                        listbox.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        listbox.grid(row=4, column=0, pady=5)

            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                        messagebox.showerror(title='LỖI', message='Mật khẩu sai!')

        find_file_button['command']=find_file    

    def about():
        messagebox.showinfo(title='Thông tin đồ án', message=mess)

    create_vol_button['command']=create_volume
    format_vol_button['command']=format_volume
    open_vol_button['command']=open_volume
    pass_vol_button['command']=pass_volume
    import_button['command']=import_file
    export_button['command']=export_file
    delefile_button['command']=delete_file
    about_button['command']=about
    passfile_button['command']=pass_file
