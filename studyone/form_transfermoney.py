# coding:utf8
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from studyone.models import account


class TransferMoneySerializer(serializers.ModelSerializer):
    # def __init__(self, data):
    #     # instances = TransferMoneySerializer.describe_instances(Filters=filters)
    #     data = self.data
    #     self.source_acctid = self.source_acctid
    #     self.target_acctid = self.target_acctid
    #     self.money = self.money
    #
    #     tr_money = TransferMoneySerializer(data)
    #
    #     try:
    #         tr_money.transfer(self.source_acctid, self.target_acctid, self.money)
    #     except ValidationError as e:
    #         print("出现问题" + str(e))


    # 判断发起转账账户和收款账户是否存在
    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s" % acctid
            cursor.execute(sql)
            print("check_acct_available" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise ValidationError("账号%s不存在" % acctid)
        finally:
            cursor.close()
    # 判断发起转账账户的余额是否小于转账金额
    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>=%s" % (acctid, money)
            cursor.execute(sql)
            print("has_enough_moneye" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise ValidationError("账号%s没有足够的钱" % acctid)
        finally:
            cursor.close()
    # 判断发起转账账户的余额是否减款成功
    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print("reduce_money" + sql)
            if cursor.rowcount != 1:
                raise ValidationError("账号%s减款失败" % acctid)
        finally:
            cursor.close()
    # 判断收款账户是否收到钱
    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print("add_money" + sql)
            if cursor.rowcount != 1:
                raise ValidationError("账号%s加款失败" % acctid)
        finally:
            cursor.close()

    def transfer(self, source_acctid, target_acctid, money):
        try:
            # 检查转账发起账户是否可用
            self.check_acct_available(source_acctid)
            # 检查转账目标账户是否可用
            self.check_acct_available(target_acctid)
            # 检查转账发起账户的余额是否大于转账金额
            self.has_enough_money(source_acctid, money)
            # 判断转账发起账户的余额在转账后的余额是否正确
            self.reduce_money(source_acctid, money)
            # 判断目标账户在转账后余额是否增加
            self.add_money(target_acctid, money)
            # 提交转账事务
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    class Meta:
        model = account
        fields = '__all__'

# if __name__ == "__main__":
#     source_acctid = sys.argv[1]
#     target_acctid = sys.argv[2]
#     money = sys.argv[3]
#
#     conn = pymysql.connect('localhost', 'admin', '2018@wang', 'Blog',charset='utf8')
#     tr_money = TransferMoneySerializer(conn)
#
#     try:
#         tr_money.transfer(source_acctid, target_acctid, money)
#     except Exception as e:
#         print("出现问题"+str(e))
#     finally:
#         conn.close()