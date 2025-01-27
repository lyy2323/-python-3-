# 8.9 消息
def show_massages(massages):
    for massage in massages:
        mag = f"Hello,{massage.title()}"
        print(mag)
m = ["adfasf", "fadaf", "aeqrqe"]
show_massages(m)

print()

# 8.10 发送消息

def send_massages(send, sent):
    while send:
        send_m = send.pop()
        print(f"打印了{send_m}")
        sent.append(send_m)

def show_massages(sent):
    print(f"转过来了：")
    for i in sent:
        print(i)


send = ["asfda", "3423", "sfaf"]
sent = []
send_massages(send, sent)
show_massages(sent)

print("\n以下是8.11\n")
# 8.11 归档消息（在上段的基础上，增加一个切片即可）

def send_massages(send, sent):
    while send:
        send_m = send.pop()
        print(f"打印了{send_m}")
        sent.append(send_m)

def show_massages(sent):
    print(f"转过来了：")
    for i in sent:
        print(i)


send = ["asfda", "3423", "sfaf"]
sent = []
send_massages(send[:], sent)
show_massages(sent)

print("原始的send:")
print(send)
print("调用后的sent:")
print(sent)