class Info:
    def __init__(self,name,acc_num,acc_pass,addr,reg_num,left):
        self.__name = name
        self.__acc_num = acc_num
        self.__acc_pass = acc_pass
        self.__addr = addr
        self.__reg_num = reg_num
        self.__left = left
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_acc_num(self):
        return self.__acc_num
    def set_acc_num(self,acc_num):
        self.__acc_num = acc_num
    def get_add_pass(self):
        return self.__acc_pass
    def set_add_pass(self,acc_pass):
        self.__acc_pass = acc_pass
    def get_addr(self):
        return self.__addr
    def set_addr(self,addr):
        self.__addr
    def get_reg_num(self):
        return self.__reg_num
    def set_reg_num(self,reg_num):
        self.__reg_num = reg_num
    def get_left(self,):
        return self.__left
    def set_left(self,left):
        self.__left = left