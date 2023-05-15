# 本项目仅做技术钻研，请勿用于非法用途
## 尝试攻击本校校园网

### 大致思路

1. 找到攻击方法
2. 获取用户信息
3. 编写批量脚本
4. 测试最终结果

### 1.

由于校园网在登录后会重定向到新的页面，故尝试使用重定向到的url在相同网络环境的非登录设备上点击下线

非常幸运，一次成功

这个结果说明校园网是在后端记录登录状态，来判定用户在线状态。

从重定向到的url来看

```16进制
36393738363435313865353335343564363830356165323564656162663861375f3137322e32342e32352e36325f3138343336363833333635
```

盲猜是16进制，转换成ASCII字节码

```ASCII
6978645818e53545d6805ae25deabf8a7_172.24.25.62_1843668****
```

即：固定前缀+ip+手机号

到这里思路就清晰了

### 2.

由于这里的内网ip和账号绑定，所以在编写脚本时只能让程序逐个尝试

用密码来尝试的话难度太大需要的时间太多，转而尝试直接访问url，这种方式来排查时，已上线的用户，只要排查到，就能在页面返回元素中得到username，讲username作为判定条件就能知道哪些ip+手机号的组合成功获取到了信息。

### 3.

批量下线只需要模拟网络请求就能完成

### 4.

查询上线人数即可测试最终结果
