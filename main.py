import hashlib

def transform(s):
    return hashlib.md5(s.encode()).hexdigest()[8:24]

def generate_activation_key(hardware_id):
    print("FinalShell-Keygenv1.0-DevelopedbyUltraPanda")
    print("*Onlyforeducationalpurpose*")
    print("请输入离线激活所提供的机器码:")
    hardware_id = input()
    advanced_key = transform('\uef79'+hardware_id+str(8552))
    pro_key = transform(str(2356)+hardware_id+str(13593))
    print("高级版激活码:{}\n专业版激活码:{}".format(advanced_key,pro_key))

if __name__ == '__main__':
    generate_activation_key('')
