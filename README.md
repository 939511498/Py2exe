# Py2exe
运行过程及生成结果如下图，其中红框的pyd文件即编译好了。因为我是64位的系统和python，所以会生成amd64后缀，我们把这个删掉重命名为mylib.pyd即可。
注：当同时存在mylib.pyd和mylib.py时，引入优先级是pyd>py，所以不用移除py文件，默认引入时就是pyd。
![2020041509441825](https://user-images.githubusercontent.com/29809009/167633639-6eafd8ca-9574-4f48-ae8d-03df2e269518.jpg)
# 建议用这种方式：
              创建一个新的Py文件(比如是main1)，将转换为pyd格式的文件(main)作为模块导入main1
              要注意main中的主函数要注释掉
![image](https://user-images.githubusercontent.com/29809009/167634038-646d2f05-c6ce-4651-a8f5-db1a8d681b8a.png)

pyinstaller -F main1.py

加密打包成功

可通过命令 python pyinstxtractor.py main1.exe 来查看pyc没有了
