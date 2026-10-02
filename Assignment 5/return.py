"""
1. 函数内部算出/得到变量
2. return 把这个变量的值送回调用处
3. 调用处用变量接收这个值

def get_number():
    n = 10
    return n

result = get_number()

第 1 步:n = 10

第 2 步:return n 把 10 送回去

第 3 步:result = get_number() 接收到 10

最终:result = 10

**************************************************
if __name__ == "__main__":
    main()
用来判断当前 .py 文件是：
被直接运行，还是
被当作模块导入

直接运行文件时:
python temperature_conversion.py
Python 会把： __name__ = "__main__"
所以:if __name__ == "__main__":
        main()
条件成立，执行 main()。

被导入时:
另一个文件里写：
import temperature_conversion
Python 会把:__name__ = "temperature_conversion"
所以:if __name__ == "__main__":
        main()
条件不成立,main() 不会自动执行。

这是为了让一个文件:
直接运行时：执行主程序
被导入时：只提供函数和常量，不自动运行主程序
所以推荐 
if __name__ == "__main__":
    main()(更规范)

main()(用于永远不导入得文件,因为这样就不会
产生: 被导入 → 也会立刻执行 main()，这个副作用)
"""