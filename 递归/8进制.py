"""
利用递归实现十进制转换为2进制或8/16进制字符串
"""

def demo(n,base):
    all_string="0123456789ABCDEF"
    if n<base:
        return all_string[n]
    else:
        return demo(n//base,base)+all_string[n%base]


print(demo(108,16))

