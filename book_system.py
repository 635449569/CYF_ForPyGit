# coding:utf-8

# 成员变量  --存放管理员信息
user_datas = []
book_datas =[]

def read_user_from_file():
    """从user.data文件中读取管理员数据"""
    # 打开文件、读取数据、关闭文件
    user_file = open("./user.data","r",encoding="utf-8")
    content = user_file.read()
    # print(content)
    # print(type(content))
    user_file.close()
    # 若要修改成员变量的值,则必须事先声明
    global user_datas
    # eval()
    user_datas = eval(content)
    # print(user_datas)
    # print(type(datas))

def read_book_from_file():
    book_file=open("./book.data","r",encoding="utf-8")
    content=book_file.read()
    book_file.close()
    global book_datas
    book_datas=eval(content)
    # print(book_datas)

def is_check_login_success(name, pwd):
    """检测是否登录成功,返回True/False"""
    # 循环取管理员信息
    index = 0
    while index<len(user_datas):
        # 用户  {'username': 'admin1', 'password': '123456'}
        user = user_datas[index]
        # 文件中的用户名、密码
        file_username = user["username"]
        file_password = user["password"]
        # print("用户名:%s,密码:%s"%(file_username,file_password))
        if name == file_username and pwd == file_password:
            return True
        index += 1
    return False

def show_operate_view():
    """显示操作界面"""
    print("本图书管理系统可完成如下操作:")
    print('.'*30)
    print("\t\t1.添加图书;")
    print("\t\t2.修改图书;")
    print("\t\t3.删除图书;")
    print("\t\t4.查询图书;")
    print("\t\t5.保存信息;")
    print("\t\t0.退出系统.")
    print('.'*30)

def add_book_info():
    """添加图书"""
    print("------添加图书操作------")
    # 书名
    name = input("请输入要添加的图书名称:")
    # 作者
    author = input("请输入要添加的作者:")
    # 价格
    price = float(input("请输入要添加的价格(float):"))
    # 出版日期
    date = input("请输入要添加的出版日期:")
    # 页数
    page = int(input("请输入要添加的页数:"))
    # 描述信息
    descript = input("请输入要添加的描述信息:")
    # 一本图书
    book = {"name": name, "author": author, "price": price, "publishdate": date, "page": page, "description": descript}
    # 添加
    book_datas.append(book)
    # 自动显示
    query_all_book()

def query_all_book():
    """查询图书"""
    print("------------查询图书操作-----------")
    print("\t\t书名\t\t作者\t\t价格\t\t出版日期\t\t页数\t\t描述信息")
    # 遍历
    index = 0
    while index < len(book_datas):
        # 书籍
        book = book_datas[index]
        # print(book)
        # 书名
        name = book["name"]
        # 作者
        author = book["author"]
        # 价格
        price = book["price"]
        # 出版日期
        date = book["publishdate"]
        # 页数
        page = book["page"]
        # 描述信息
        decipt = book["description"]
        print("\t%s\t%s\t%f\t%s\t%d\t%s" % (name, author, price, date, page, decipt))
        index += 1

def save_book_info():
    """保存图书信息"""
    print("------保存图书信息操作------")
    # 操作  打开文件、写入数据、关闭文件
    book_file = open("./book.data","w",encoding="utf-8")
    # 所有图书信息
    book_strs = str(book_datas)
    book_file.write(book_strs)
    book_file.close()
    print("图书信息已保存成功,谢谢!")

def update_book_info():
    """修改图书"""
    print("------修改图书操作------")
    # 书名
    name = input("请输入要修改的图书名称:")
    # 作者
    author = input("请输入要修改的作者:")
    # 价格
    price = float(input("请输入要修改的价格(float):"))
    # 出版日期
    date = input("请输入要修改的出版日期:")
    # 页数
    page = int(input("请输入要修改的页数:"))
    # 描述信息
    descript = input("请输入要修改的描述信息:")
    # 要修改的书名匹配文件中的书名
    index = 0
    while index<len(book_datas):
        book = book_datas[index]
        if name == book["name"]:
            # 修改其他信息
            book["author"] = author
            book["price"] = price
            book["publishdate"] = date
            book["page"] = page
            book["description"] = descript
        index += 1
    query_all_book()



def delete_book_info():
    """删除图书"""
    print("------删除图书操作------")
    name = input("请输入要删除的图书名称:")
    delete = input("是否确认删除?Y/N-->")
    index = 0
    while index < len(book_datas):
        # 找到当前的这本书,删除该下标
        book = book_datas[index]
        if name == book["name"] and (delete == "Y" or delete == "y"):
            del book_datas[index]
        index += 1
    query_all_book()


def main():
    print("---欢迎使用本图书管理系统---")
    # 读取管理员信息
    read_user_from_file()
    # 读取图书信息
    read_book_from_file()

    # 三次登录：循环while   Ctrl+/
    login_num = 0
    while login_num < 3:
        # 用户名
        username = input("请输入用户名:")
        # 密码
        password = input("请输入密码:")
        # print("用户名:",username)
        # print("密码:",password)
        # 判断
        # if username == "admin" and password == "123456":
        if is_check_login_success(username, password):  # bool  -->True/False
            # print("登录成功!")  # 显示操作界面
            show_operate_view()
            # 跳出循环
            break

        login_num += 1

    # 登录失败
    if login_num == 3:
        print("亲爱的用户,您输入用户名或密码3次有误,登录失败!")
    else:
        # print("---------成功!-----------")
        while True:
            # 操作序号
            number = int(input("请输入要操作的序号(int):"))
            # 判断
            if number == 1:
                # print("添加图书.")
                add_book_info()
            elif number == 2:
                # print("修改图书.")
                update_book_info()
            elif number == 3:
                # print("删除图书.")
                delete_book_info()
            elif number == 4:
                # print("查询图书.")
                query_all_book()
            elif number == 5:
                # print("保存信息.")
                save_book_info()
            elif number == 0:
                # print("退出系统.")
                out = input("您确实要退出系统吗?Y/N -->")
                if out == "Y" or out == "y":
                    print("期待您的下次使用!")
                    # 跳出循环
                    break
            else:
                print("您输入的操作序号暂不存在,敬请期待...")


if __name__ == '__main__':
    # 程序入口
    main()