import tkinter as tk

# 创建一个临时的 Tkinter 窗口
root = tk.Tk()

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 关闭临时窗口
root.destroy()

print("屏幕宽度：", screen_width)
print("屏幕高度：", screen_height)
