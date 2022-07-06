#chat
def read_file(filename):
    lines = []
    with open (filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    Simba_wc = 0
    Yuki_wc = 0
    KEVIN_wc = 0
    Simba_sc = 0
    Yuki_sc = 0
    KEVIN_sc = 0
    Simba_ic = 0
    Yuki_ic = 0
    KEVIN_ic = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Simba':
            if s[2] == '貼圖':
                Simba_sc += 1
            elif s[2] == '圖片':
                Simba_ic += 1
            else:
                for msg in s[2:]:
                    Simba_wc += len(msg)
        elif name == 'Yuki':
            if s[2] == '貼圖':
                Yuki_sc += 1
            elif s[2] == '圖片':
                Yuki_ic += 1
            else:
                for msg in s[2:]:
                    Yuki_wc += len(msg)
        elif name == 'KEVIN':
            if s[2] == '貼圖':
                KEVIN_sc += 1
            elif s[2] == '圖片':
                KEVIN_ic += 1
            else:
                for msg in s[2:]:
                    KEVIN_wc += len(msg)
    print ('Simba說了', Simba_wc, '個字')
    print ('Simba傳了', Simba_sc, '個貼圖') 
    print ('Simba傳了', Simba_ic, '張照片')
    print ('..............................')
    print ('Yuki說了', Yuki_wc, '個字')
    print ('Yuki傳了', Yuki_sc, '個貼圖')
    print ('Yuki傳了', Yuki_ic, '張照片')
    print ('..............................')
    print ('KEVIN說了', KEVIN_wc, '個字')
    print ('KEVIN傳了', KEVIN_sc, '個貼圖') 
    print ('KEVIN傳了', KEVIN_ic, '張照片')
 

def main():
    lines = read_file('[LINE]music.txt')
    lines = convert(lines)

main()