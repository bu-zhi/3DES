# 生成子密钥的置换表1，将64位的密钥转换为56位
key_table1 = [57, 49, 41, 33, 25, 17, 9,
              1, 58, 50, 42, 34, 26, 18,
              10, 2, 59, 51, 43, 35, 27,
              19, 11, 3, 60, 52, 44, 36,
              63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
              14, 6, 61, 53, 45, 37, 29,
              21, 13, 5, 28, 20, 12, 4]
# 生成子密钥的置换表2，将56位的密钥转换为48位
key_table2 = [14, 17, 11, 24, 1, 5,
              3, 28, 15, 6, 21, 10,
              23, 19, 12, 4, 26, 8,
              16, 7, 27, 20, 13, 2,
              41, 52, 31, 37, 47, 55,
              30, 40, 51, 45, 33, 48,
              44, 49, 39, 56, 34, 53,
              46, 42, 50, 36, 29, 32]
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
IP_NI = [40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41, 9, 49, 17, 57, 25]
kuoz = [32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1]
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

S = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],

]

def miyao(mi):  # 生成密钥
    key = mi
    allkey = []
    key0 = [0 for i in range(56)]
    for i in range(len(key_table1)):
        key0[i] = key[key_table1[i] - 1]
    c = key0[:28]
    d = key0[28:]
    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            c = c[1:] + c[:1]
            d = d[1:] + d[:1]
        else:
            c = c[2:] + c[:2]
            d = d[2:] + d[:2]
        key0 = c + d
        key1 = [0 for j in range(48)]
        for j in range(len(key_table2)):
            key1[j] = key0[key_table2[j] - 1]
        allkey.append(key1)
    return allkey

def extend(data):  # 扩展
    data1 = [0 for i in range(48)]
    for i in range(len(kuoz)):
        data1[i] = data[kuoz[i] - 1]
    return data1

def int2bit(n):  # 十进制换成二进制
    a = []
    for i in range(0, 4):
        a.insert(0, str(n % 2))
        n = int(n / 2)
    return a

def ip(text):
    MING1 = [0 for i in range(64)]
    for i in range(len(IP)):  # 初始置换
        MING1[i] = text[IP[i] - 1]
    return MING1

def yihuo(text1, text2):
    r1 = [0 for j in range(len(text1))]
    for j in range(len(text1)):  # 异或
        r1[j] = str(int(text1[j]) ^ int(text2[j]))
    return r1

def s_place(text):
    r2 = [0 for k in range(32)]
    for k in range(8):  # s盒代换
        row = 2 * int(text[k * 6]) + int(text[k * 6 + 5])
        column = 8 * int(text[k * 6 + 1]) + 4 * int(text[k * 6 + 2]) + 2 * int(text[k * 6 + 3]) + int(text[k * 6 + 4])
        tmp = S[k][row * 16 + column]
        for j in range(4):
            r2[4 * k + j] = int2bit(tmp)[j]
    return r2

def p_place(text):
    r3 = [0 for i in range(32)]
    for j in range(32):  # p盒置换
        r3[j] = text[P[j] - 1]
    return r3

def ip_ni(text):  # 逆置换
    MIWEN = [0 for i in range(64)]
    for i in range(64):
        MIWEN[i] = text[IP_NI[i] - 1]
    return MIWEN

def jiami(MING, mi):
    MING1 = ip(MING)
    l = MING1[:32]
    r = MING1[32:]
    allkey = miyao(mi)
    for i in range(16):  # 16轮运算
        l1 = [j for j in l]
        for j in range(32):
            l[j] = r[j]
        r_k = extend(r)  # 扩展
        r1 = yihuo(r_k, allkey[i])  # 异或
        r2 = s_place(r1)
        r3 = p_place(r2)
        r = yihuo(r3, l1)
    MING2 = l + r
    MIWEN = ip_ni(MING2)

    a = ''.join(MIWEN)
    return a

def jiemi(MIWEN, mi):
    MING1 = ip(MIWEN)
    l = MING1[:32]
    r = MING1[32:]
    allkey = miyao(mi)
    for i in range(16):
        r_1 = [j for j in r]
        for j in range(32):
            r[j] = l[j]
        r_k = extend(r)  # 扩展
        r1 = yihuo(r_k, allkey[15 - i])  # 异或
        r2 = s_place(r1)
        r3 = p_place(r2)
        l = yihuo(r3, r_1)
    MING2 = l + r
    MING = ip_ni(MING2)
    return ''.join(MING)

def threedesjia(ming):
    jia_miwen = jiami(ming, mi1)
    jia_ming2 = jiemi(jia_miwen, mi2)
    jia_miwen2 = jiami(jia_ming2, mi3)
    return jia_miwen2

def threedesjie(jia_miwen2):
    jie_ming = jiemi(jia_miwen2, mi3)
    jie_miwen = jiami(jie_ming, mi2)
    jie_ming2 = jiemi(jie_miwen, mi1)
    return jie_ming2

def read_out_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        mess = f.read()
    print("文件读取成功！")
    res = ''
    for i in mess:
        tmp = bin(ord(i))[2:]  # 将每个字符转化成二进制
        tmp = str('0' * (16 - len(tmp))) + tmp  # 补齐16位
        res += tmp
    if len(res) % 64 != 0:
        count = 64 - len(res) % 64  # 不够64位补充0
    else:
        count = 0
    res += '0' * count
    return res
# 字符串转化为二进制

def write_in_file(mess, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(mess)
        print('文件写入成功！')

import re

# 二进制转化为字符串
def bin2str(bin_str):
    res = ""
    tmp = re.findall(r'.{16}', bin_str)
    for i in tmp:
        res += chr(int(i, 2))
    print("要写入的数据为：")
    print(res)
    return res
IV='0100100110100110001011100001100100100001000010001111100001100101'
def alljiami(filename):
    message = read_out_file(filename)
    tmp = re.findall(r'.{64}', message)
    mi = ''
    global IV
    for i in range(len(tmp)):
        if i==0:
            tmp[i]=yihuo(tmp[i],IV)
        else:
            tmp[i]=yihuo(tmp[i],miwen)
        tmp[i]=''.join(tmp[i])
        miwen = threedesjia(tmp[i])
        mi += miwen
    MI = bin2str(mi)
    write_in_file(MI, filename)

def alljiemi(filename):
    message = read_out_file(filename)
    tmp = re.findall(r'.{64}', message)
    ming = ''
    global IV
    for i in range(len(tmp)):
        mingwen = threedesjie(tmp[i])
        if i==0:
            mingwen=yihuo(mingwen,IV)
        else:
            mingwen=yihuo(tmp[i-1],mingwen)
        mingwen=''.join(mingwen)
        ming += mingwen
    bu = ming[-64:]
    ming = ming[:-64] + bu.replace('0000000000000000', '')
    MING = bin2str(ming)
    write_in_file(MING, filename)

def threemiyao():
    global mi1, mi2, mi3
    mi = ['0', '0', '0']
    for i in range(0, 3):
        mi[i] = str(input("请输入第{}个密钥：".format(i + 1)))
        res = ''
        for j in mi[i]:
            tmp = bin(ord(j))[2:]  # 将每个字符转化成二进制
            tmp = str('0' * (16 - len(tmp))) + tmp  # 补齐8位
            res += tmp
        if len(res) < 64:
            res = res + '0' * (64 - len(res))
        else:
            res = res[:64]
        mi[i] = res
    mi1 = mi[0]
    mi2 = mi[1]
    mi3 = mi[2]

import os

if __name__ == '__main__':
    while 1:
        filename = input('请输入要加密/解密的文件:')
        if os.path.isfile('./' + filename) == False:
            print("代码同级目录下没有该文件！")
            continue
        while 1:
            number = str(input('选择加密（1）还是解密（2）：'))
            if number == '1':
                threemiyao()
                alljiami(filename)
                break
            elif number == '2':
                threemiyao()
                alljiemi(filename)
                break
            else:
                print('输入格式错误！')
        xz=str(input("按1退出，其它继续："))
        if xz=='1':
            print("欢迎再次使用")
            break