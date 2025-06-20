"""
考试试卷生成系统 - 主程序入口

功能：
1. 创建主窗口
2. 初始化应用程序
3. 启动主事件循环

依赖：
- gui.ExamGeneratorGUI
"""

from gui import ExamGeneratorGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = ExamGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()