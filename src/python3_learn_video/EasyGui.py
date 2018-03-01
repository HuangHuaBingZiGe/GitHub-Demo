"""
EasyGui官网：
http://easygui.sourceforge.net

官方教学文档：
easygui-docs-0.96\tutorial\index.html

翻译改编的教学文档：
http://bbs.fishc.com/thread-46069-1-1.html

"""

"""
导入方式1：
import easygui
easygui.msgbox('嗨，你好')
"""

"""
导入方式2：
from easygui import *
msgbox('嗨，小美女')
"""

"""
导入方式3：推荐方式
import easygui as g
g.msgbox('嗨，小boy')
"""

import sys

import easygui as g

while 1:
    g.msgbox('嗨，欢迎进入第一个页面小游戏^-^')
    
    msg = '请问你希望在鱼C工作室学习到什么知识呢？'
    title = '小游戏互动'
    choices = ['谈恋爱', '编程', '琴棋书画']
    
    choice = g.choicebox(msg, title, choices)
    
    # note that we convert choice to string,in case
    # the user cancelled the choice, and we got None.
    g.msgbox('你的选择是：' + str(choice), '结果')
    
    msg = '你希望重新开始小游戏吗？'
    title = '请选择'
    
    if g.ccbox(msg, title):  # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)  # user chose Cancel
