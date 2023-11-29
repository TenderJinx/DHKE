from extended_function import extended_function


def DHKE(P, G, a, b):
    """
    迪菲-赫尔曼密钥交换机制(协议)
    :param P: 素数
    :param G: 原根
    :param a: 用户甲的私密整数
    :param b: 用户乙的私密整数
    :return: 用户甲、乙的公开数字及各自计算的会话密钥
    """
    A = pow(G, a) % P
    B = pow(G, b) % P

    Sa = pow(B, a) % P
    Sb = pow(A, b) % P

    return A, B, Sa, Sb


if __name__ == '__main__':
    P, G, a, b = 251, 6, 11, 13

    A, B, Sa, Sb = DHKE(P, G, a, b)
    print(f"素数为{P}")
    print(f"原根为{G}")

    print(f"用户甲的公开数字为{A}")
    print(f"用户乙的公开数字为{B}")

    if Sa == Sb:
        print(f"会话密钥为: {Sb}")
    else:
       print("密钥计算错误")

    text = "Hello,World!"
    key = Sa
    print(f"明文为: {text}")

    ciphertext = extended_function(text, key)
    print(f"密文为: {ciphertext}")

    plaintext = extended_function(ciphertext, key, True)
    print(f"解密后的明文为: {plaintext}")
