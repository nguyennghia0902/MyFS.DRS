import tkinter as tk
import tkinter.ttk as TTK
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry

import os, json
from datetime import datetime

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
        width=25
    )
    format_vol_button = tk.Button(
        user_page_content_frame_left,
        text='Định dạng volume',
        width=25
    )
    pass_vol_button = tk.Button(
        user_page_content_frame_left,
        text='Đặt/đổi mật khẩu volume',
        width=25
    )
    open_vol_button = tk.Button(
        user_page_content_frame_left,
        text='Mở/liệt kê các file trong volume',
        width=25
    )
    

    user_page_content_frame_left.pack(fill='both',side = 'left', padx=20, pady=10)

    func_label.grid(row=0, column=0, columnspan=3)
    create_vol_button.grid(row=1, column=0, pady=5)
    format_vol_button.grid(row=2, column=0, pady=5)
    pass_vol_button.grid(row=3, column=0, pady=5)
    open_vol_button.grid(row=4, column=0, pady=5)
    
    

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

        address_choose_label.grid(row=0, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=1, column=0, pady=5, sticky='w')
        address_display.grid(row=2, column=0, columnspan=1, pady=5, sticky='w')

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
            size = size_menu.get().strip()
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

        volume_choose_label.grid(row=0, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=1, column=0, pady=5, sticky='w')
        volume_display.grid(row=2, column=0, columnspan=1, pady=5, sticky='w')

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

        def submit():
            name = setname_entry.get().strip()
            if format_vol(volume.get(), name):
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
        submit_button.grid(row=5,column=0, pady=5)
 
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

        volume_choose_label.grid(row=0, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=1, column=0, pady=5, sticky='w')
        volume_display.grid(row=2, column=0, columnspan=1, pady=5, sticky='w')

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
            oldpw = setpass_entry.get().strip()
            newpw = setpass_entry.get().strip()
            if (validate_password(oldpw, newpw, str(''))):
                if setpass_vol(volume.get(), newpw):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Đặt mật khẩu volume thành công')
                else: messagebox.showerror(title='LỖI', message='Đặt mật khẩu volume không thành công')
            else: messagebox.showerror(title='LỖI', message='Mật khẩu cũ volume không đúng!')
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

        file_choose_button = tk.Button(
            volume_frame,
            text='Chọn volume',
            command=get_volume,
            anchor='w'
        )

        volume_choose_label.grid(row=0, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=1, column=0, pady=5, sticky='w')
        volume_display.grid(row=2, column=0, columnspan=1, pady=5, sticky='w')

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

        def submit():
            pw = pass_entry.get().strip()
            if open_vol(volume.get(), pw):
                messagebox.showinfo(title='CHÚC MỪNG', message='Mở volume thành công')
            else: messagebox.showerror(title='LỖI', message='Mở volume không thành công')
        submit_button = tk.Button(
            user_frame,
            text='Xác nhận',
            width=10,
            command=submit
        )

        pass_label.grid(row=0, column=0, pady=5)
        pass_entry.grid(row=1, column=0, pady=5)
        submit_button.grid(row=5,column=0, pady=5)
    
    
    create_vol_button['command']=create_volume
    format_vol_button['command']=format_volume
    open_vol_button['command']=open_volume
    pass_vol_button['command']=pass_volume
    