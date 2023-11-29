## DHKE
*代码文件为：main.py*
*运行结果为：运行结果.docx*
*运行原理为：*
1. **选择参数：** 选择两个大素数 \( p \) 和 \( g \)（通常 \( g \) 是 \( p \) 的原根）。

2. **密钥生成：** 每个通信方选择一个私有密钥。假设 Alice 选择私钥 \( a \)，而 Bob 选择私钥 \( b \)。

3. **计算公共值：** Alice 计算 \( A = g^a \mod p \)，Bob 计算 \( B = g^b \mod p \)。

4. **交换公共值：** Alice 和 Bob 通过不安全的通信渠道交换 \( A \) 和 \( B \)。

5. **计算共享密钥：** Alice 使用 Bob 发送的 \( B \) 计算共享密钥 \( K = B^a \mod p \)。同时，Bob 使用 Alice 发送的 \( A \) 计算共享密钥 \( K = A^b \mod p \)
