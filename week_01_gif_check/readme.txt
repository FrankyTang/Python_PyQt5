编程过程：
1，打开 XXX\Anaconda3\Scripts\designer.exe，设计UI 界面，保存为 check_gif_main.ui 的文件；
2，在 .ui 的文件夹里， SHIFT + 右键 打开powershell，输入 XXX\Anaconda3\Scripts\pyuic5.exe  .\check_gif_main.ui -o check_gif_main.py,
     将.ui 转换为.py 文件；
3，创建新的.py class 继承check_gif_main.py 中的class 
