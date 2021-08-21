# File Process Basic 项目说明  

###### Create Time: 2021/08/19 15:53
###### Creator: yanghao2233 
###### Contributor: /


### 1. 项目综述  
  File Process Basic 项目是基于日常Python学习中遇到的各类文件读取, 写入, 预处理等重复性相对较高, 代码相对冗杂的问题进行处理,   
  以方便日后调用. 项目目前已实现或待实现下列基本处理方法:  
* 常见格式文件读取: txt, csv, json, xls, xlsx, npy
* 常见格式文件写入: txt, csv, json, npy, pkl; xlsx(待实现)
* 常用数据预处理方式: 
  * 缺失值处理, 随机抽样, 数据转化 (已实现). 
  * 数据集合 (部分实现)
  * 其他待实现.
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
   miss_value() 是用于处理常见数据中的缺失值问题的类. 目前支持删除法, 常规填充法, 随机森林填充法以及回归填充法.  
###### 使用的正确姿势  
    miss_value(输入的数据).处理方法函数()
    for example:
      需要处理的数据: data = pd.Dataframe(miss_sample)  
      处理方法为以缺失值所在列的均值填充  
        -> cleaned = miss_value(data).general_fill('mean')  

#### class integrate():
    integrate() 是用于处理多个数据列表需要进行合并, 去重等情况的类. 目前支持数据表直接合并.  
    *** 本数据类支持自定义扩展, 使用时只需额外定义 data_n 即可 ***
###### 使用的正确姿势
    integrate(需要合并的数据集, 以逗号分隔).合并方法函数()
    for example:  
      需要合并的数据表: df1, df2  
      合并方法为直接填充  
        -> merge_test = integrate(df1, df2).merge()

#### class transform():
    transform() 是用于数据分析过程中常用的数据标准化等情况. 目前支持 归一化, 标准化和最大绝对值标准化
###### 使用的正确姿势
    transform(需要标准化的数据).处理方式函数()  
    for example:  
      需要处理的数据: data = pd.Dataframe(trans_sample)  
      处理方法为最大绝对值标准化.  
        -> trans_test = transform(data).maxAbs()

#### class sampling():
    sampling() 是用于简单降维或数据集划分情况下的抽样类别. 目前支持简单随机抽样, 分层抽样, 系统抽样, 以及雪球抽样.  
###### 使用的正确姿势  
    sampling(需要进行抽样的数据, 抽样数目).抽样方法函数()  
    for example:
      需要抽样的数据: data = list(sampling_sample)  
      抽样方法为简单随机抽样.  
        -> sample_test = sampling(data, 10).simple_random()
### 4. To Do List
  pass
