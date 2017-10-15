def search_data(data,data_find):
    # 中间值的索引号的定义：数组长度/2
    mid = int(len(data)/2)
    # 判断从1开始的数字数组内查找
    if data[mid] >= 1:
        # 如果我们要找的值（data_find）比中间值（data[mid]）小
        if data[mid] > data_find:
            print("你要找的数字比中间值[%s]小..." % data[mid]);
            # 在中间值（data[mid]）的左侧继续查找，在此函数中继续循环
            search_data(data[:mid],data_find)
            # 如果我们要找的值（data_find）比中间值（data[mid]）大
        elif data[mid] < data_find:
            print("你要找的数字比中间值[%s]大..." % data[mid])
            # 在中间值（data[mid]）的右侧继续查找，在此函数中继续循环
            search_data(data[mid:],data_find)
        else:
            # 如果我们要找的值（data_find）既不比中间值（data[mid]）大，也不比中间值（data[mid]）小，则就是它
            print("这就是你要找的[%s]！" % data[mid])
    else:
         print("不好意思，没有找到你要的值...")
 
if __name__ == '__main__':
    # 创建一个1到6000万的连续数字数组
    data = list(range(60000000))
    # 调用函数找到95938的值
    search_data(data,95938)
