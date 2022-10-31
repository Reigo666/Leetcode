import collections
from typing import  List,Optional
import copy
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        l1=queryIP.split(".")
        l2=queryIP.split(":")

        def isHex(s:str):
            s=s.lower()
            for l in s:
                if not (l.isdecimal() or (ord(l)>=ord('a') and ord(l)<=ord('f'))):
                    return False
            return True


        #check l1 if ipv4
        #ipv4不允许前导0 转为数字时需要判断长度大于等于2的第一位是否是0
        if len(l2)==1:
            if len(l1)!=4:
                return "Neither"
            for num in l1:
                if not num.isdecimal():
                    return "Neither"
                if len(num)>=2 and num[0]=='0':
                    return "Neither"
                if int(num)<0 or int(num)>255:
                    return "Neither"
            return "IPv4"
        #check l2 if ipv6
        # 1 <= xi.length <= 4 ->长度=0或长度>4的均为错误
        # xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。 isHex时大写转为小写判断
        # 在 xi 中允许前导零。
        else:
            if len(l2)!=8:
                return "Neither"
            for num in l2:
                if len(num)>4 or len(num)==0:
                    return "Neither"
                else:
                    for l in num:
                        if not isHex(l):
                            return "Neither"
            return "IPv6"
        return "Neither"

