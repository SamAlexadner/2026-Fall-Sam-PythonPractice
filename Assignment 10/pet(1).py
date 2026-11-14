class Pet:
    def __init__(self, name, animal_types, age):
    # __init__这是构造方法,创建对象时会自动调用
    # self 是固定第一个参数, 代表这个对象自己
    # name, animal_types, age 这是创建对象时要传进来的三个值
        self.__name = name
        self.__animal_types = animal_types
        self.__age = age
        # "__"这是私有属性的标志, 需要放在类里面,不然会报错
        # 且只能通过getter/setter访问
        # 为啥加self 因为不加就是局部变量,结束就消失;加了才真正的"挂在对象身上",后面才能用
        # 右边的name:第一行传进来的参数, "=":把传进来的值存进对象的私有属性里
    
    # getter(访问器)--把私有属性读出来
    def get_name(self):
        # 定义一个方法,名字叫get_name(get就是getter命名惯例)
        # 只收self, 不需要额外参数--因为只是"读自己身上的值"
        return self.__name
        # 把对象自己的_name的值返回出去
        # 为什么不能外面直接 pet.__name？因为私有。
        # 所以给一个"官方窗口"get_name() 来读
    
    def get_animal_type(self):
        return self.__animal_types
   
    def get_age(self):
        return self.__age

    def set_name(self, name):
        # 方法名 set_name（set_ 前缀是 setter 惯例）。
        # 参数：self + 一个新值 name（要改成什么）。
        # 把传进来的新值覆盖到对象的私有属性上。
        # 为什么需要它： 私有属性外面改不了，必须走这个"官方窗口"。
        # 三个属性三个 setter：
        self.__name = name
    
    def set_animal_type(self, animal_types):
        self.__animal_types = animal_types
    
    def set_age(self, age):
        self.__age = age
        # 对比记忆：
        # getter 是"只收 self，return 属性"；
        # setter 是"收 self + 新值，赋值给属性"。
        # 两者结构完全对称。

    #__str__ 方法（必须是类里最后一个方法）
    def __str__(self):
        return(f"pet: {self.__name}\n"
                f"type: {self.__animal_types}\n"
                f"age: {self.__age}")
    # __str__ 也是固定名字（前后双下划线）。
    # 只收 self，没有别的参数。
    # 作用：当你 print(对象) 或 str(对象) 时，
    # Python 自动调用它，用它的返回值当输出。
    # \n 是换行符——示例输出是三行，所以中间要 \n。
    # 三行字符串用括号 (...) 包起来，可以分行写，
    # Python 会把它们连成一个字符串（这叫隐式拼接）。
    # 必须是 return，不能是 print。如果写 print，print(pet) 
    # 会输出 None——这是初学者第一大坑。


from pet import Pet  # don't have this one will NameError

def main():
    name = input("Enter the name of the pet: ")
    animal_types = input("Enter the type of the animal: ")
    age = int(input("Enter the age of the pet: "))
    pet = Pet(name, animal_types, age)
    # 调用Pet类 ->python自动执行__init__
    # 把刚才三个变量按顺序传进去：
    # name → name，animal_type → animal_type，age → age。
    # 注意：调用时不用传 self，
    # Python 自动把 pet 这个新对象当 self。
    # 结果：pet 这个变量指向一个装好三个私有属性的 Pet 对象
    print("Here is the data that you entered:")
    print(pet)

if __name__ == "__main__":
    main()