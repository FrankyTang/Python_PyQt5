编程过程：
1，打开 XXX\Anaconda3\Scripts\designer.exe，设计UI 界面，保存为 .ui 的文件；
2，在 .ui 的文件夹里， SHIFT + 右键 打开powershell，输入 XXX\Anaconda3\Scripts\pyuic5.exe  .\AAA.ui -o AAA.py,
     将.ui 转换为.py 文件；
3，创建新的.py class 继承AAA.py 中的class 
