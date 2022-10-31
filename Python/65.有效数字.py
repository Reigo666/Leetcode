import collections
from typing import  List,Optional
import copy

class Solution:
    def isNumber(self, s: str) -> bool:
        def isInt(s:str):
            if s=="":
                return False
            if s[0]=='+' or s[0]=='-':
                s=s[1:]
            return s.isdigit()
            
        def isFloat(s:str):
            musthavedigit=0
            if s=="":
                return False
            if s[0]=='+' or s[0]=='-':
                s=s[1:]
            if s=="":
                return False
            if s[0]==".":
                musthavedigit=1
            while s[0]!='.':
                if not s[0].isdigit():return False
                else:
                    s=s[1:]
            if s[0]=='.':
                s=s[1:]
            else:
                return False
            
            if not musthavedigit:
                return s=="" or s.isdigit()
            elif musthavedigit:
                return s.isdigit()
            return True

        counte=s.count('e')+s.count('E')
        if counte>=2:
            return False
        elif counte==1:
            pose=max(s.find('e'),s.find('E'))
            if not isInt(s[:pose]) and not isFloat(s[:pose]):
                return False
            if not isInt(s[pose+1:]):
                return False
            return True
        elif counte==0:
            if isInt(s) or isFloat(s):
                return True
        return False

sol=Solution()
s1="0123"
s2="-.9"
s3="-123.4566"
validlist=["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
invalidlist=["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
for s in invalidlist:
    print(s,sol.isNumber(s))
# 部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
#print(sol.isNumber(s2))
# 有效数字（按顺序）可以分成以下几个部分：
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数

# 小数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字


# 整数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字


# 输入：s = "0"
# 输出：true