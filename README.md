# File Process Basic 项目说明  

###### Create Time: 2021/08/19 15:53
###### Creator: yanghao2233 
###### Contributor: /


### 1. 项目综述  
  File Process Basic 项目是基于日常Python学习中遇到的各类文件读取, 写入, 预处理等重复性相对较高, 代码相对冗杂的问题进行处理,   
  以方便日后调用. 项目目前已实现或待实现下列基本处理方法:  
* 常见格式文件读取: txt, csv, json, xls, xlsx, npy
* 常见格式文件写入: txt, csv, json, npy, pkl; xlsx(待实现)
* 常用数据预处理方式: 缺失值处理(部分实现); 其他待实现.
* 常见初步数据可视化方式: 待实现.

### 2. 需求库
  numpy  
  xlrd, csv, json  
  pickle  
  traceback  
  
### 3. 主要函数或函数类
#### class file_read():
  file_read() 是用于读取生产生活中常见的数据文件格式内容的类. 目前支持读取 txt, excel, json 等主流数据存储格式.  
###### 使用的正确姿势  
    file_read(文件路径).文件类型函数()  
    for example:  
      需要读取的文件路径: path = '../data/sample.txt'  
        -> file_read(path).txt()  
    
#### class file_write():
  file_write() 是用于将处理好的数据信息写入常用的数据格式内容的类. 目前支持写入 txt, csv, json 等主流存储格式.
###### 使用的正确姿势
    file_write(文件路径).文件类型函数()  
    for example:  
      需要写入的文件路径: path = '../output/sample_out.txt'  
      需要写入的数据: data = [1, 2, 3, 4, 5]  
        -> file_write(path).txt(data)    

#### class miss_value():  
   miss_value() 是用于处理常见数据中的缺失值问题的类. 目前支持删除法, 常规填充法. 待实现 随机森林填充法以及回归填充法.  
###### 使用的正确姿势  
    miss_value(输入的数据).处理方法函数()
    for example:
      需要处理的数据: data = pd.Dataframe(miss_sample)  
      处理方法为以缺失值所在列的均值填充  
        -> cleaned = miss_value(data).general_fill('mean')  
        
### 4. 实例化 (针对预处理和可视化)
  pass
### 5. To Do List
  pass
