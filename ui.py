import tkinter as tk  
from tkinter import messagebox  
from ans import takeCommand, speak  # 假设您的脚本名为your_script_name.py  
  
def on_recognize_button_click():  
    try:  
        query = takeCommand()  
        text_box.delete('1.0', tk.END)  # 清空文本框内容  
        text_box.insert(tk.END, query)  # 插入识别结果  
    except Exception as e:  
        messagebox.showerror("错误", str(e))  
        speak("请再说一遍...")  
  
def on_clear_button_click():  
    text_box.delete('1.0', tk.END)  # 清空文本框内容  
  
# 创建主窗口  
root = tk.Tk()  
root.title("语音识别UI")  
root.geometry("800x500")  # 设置窗口大小  
  
# 创建识别按钮  
recognize_button = tk.Button(root, text="开始识别", command=on_recognize_button_click)  
recognize_button.pack(pady=20)  # 添加内边距并放置按钮  
  
# 创建文本框来显示识别结果  
text_box = tk.Text(root, height=10, width=50)  
text_box.pack(pady=20)  # 添加内边距并放置文本框  
  
# 创建清除按钮  
clear_button = tk.Button(root, text="清除", command=on_clear_button_click)  
clear_button.pack(pady=10)  # 添加内边距并放置按钮  
  
# 运行主循环  
root.mainloop()