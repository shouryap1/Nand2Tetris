f1 = input("Insert file name or path: ")
finput = open(f1, "r")
foutput = open("new.asm", "w")
for line in finput:
    l1 = line.split("//")
    l1[0] = l1[0].replace(" ", "")
    if len(l1) > 1:
        l1[0] += "\n"
    if l1[0].rstrip():
        foutput.write(l1[0])

foutput.close()
finput.close()

file1 = open('new.asm', 'r')
Lines = file1.readlines() 
file1.close()
# print(Lines[4])
def comp_lookup(comp_str):
    p= {
        "0":   "0101010",
        "1":   "0111111",
        "-1":  "0111010",
        "D":   "0001100",
        "A":   "0110000",
        "M":   "1110000",
        "!D":  "0001101",
        "!A":  "0110001",
        "!M":  "1110001",
        "-D":  "0001111",
        "-A":  "0110011",
        "-M":  "1110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "M+1": "1110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "M-1": "1110010",
        "D+A": "0000010",
        "D+M": "1000010",
        "D-A": "0010011",
        "D-M": "1010011",
        "A-D": "0000111",
        "M-D": "1000111",
        "D&A": "0000000",
        "D&M": "1000000",
        "D|A": "0010101",
        "D|M": "1010101"
    }
    return p[comp_str]
# def replace_symbols(key,lines):
l= {
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4",
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "R10": "10",
    "R11": "11",
    "R12": "12",
    "R13": "13",
    "R14": "14",
    "R15": "15",
    "SCREEN": "16384",
    "KBD": "24576",
}


count=0
for line in Lines:
    if(line[0]=='('):
        a=[line[1:-2],count]
        l[line[1:-2]]=str(count)
    else:
        count=count+1
file2=open('new.asm','r')
Lines2=file2.readlines()
file2.close()
counter=16
for line in Lines2:
    if line[0]=='@' and (line[1:-1] not in l) and not (line[1]=='0' or line[1]=='1' or line[1]=='2' or line[1]=='3' or line[1]=='4' or line[1]=='5' or line[1]=='6' or line[1]=='7' or line[1]=='8' or line[1]=='9'):
        l[line[1:-1]]=str(counter)
        print('ponggame.0' in l)

        counter=counter+1
f=open('new.asm','r')
Lines=f.readlines()
# f=open('final.asm','w')
for line in Lines:
    if line[0]=='@' and not(line[1]=='0' or line[1]=='1' or line[1]=='2' or line[1]=='3' or line[1]=='4' or line[1]=='5' or line[1]=='6' or line[1]=='7' or line[1]=='8' or line[1]=='9'):
        # print(line[0])
        w='@'+l[line[1:-1]]+'\n'
        # line.replace(line,w)
        ff=open('new2.asm','a')
        ff.write(w)
    elif line[0]=='(':
        a=1
    else:
        ff=open('new2.asm','a')
        ff.write(line)
# ff.close()

# class Code(object):
#     def init(self):
#         pass
def check(line):
    # print(line)
    # print(line[2:])
    if(line[0]=='@'):
        a='0'+bin(int(line[1:]))[2:].zfill(15)+'\n'
        fbinary=open('binary1.txt','a')
        fbinary.write(a)
    else:
        def comp(a):
            # print("a-")
            print(a)        
            # print("\n")
            _comp_codes = { '0':'0101010',  '1':'0111111',  '-1':'0111010', 'D':'0001100', 
                    'A':'0110000',  '!D':'0001101', '!A':'0110001', '-D':'0001111', 
                    '-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110', 
                    'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111', 
                    'D&A':'0000000','D|A':'0010101',
                    '':'xxxxxxx',   '':'xxxxxxx',   '':'xxxxxxx',   '':'xxxxxxx', 
                    'M':'1110000',  '':'xxxxxxx',   '!M':'1110001', '':'xxxxxxx', 
                    '-M':'1110011', '':'xxxxxxx',   'M+1':'1110111','':'xxxxxxx', 
                    'M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111', 
                    'D&M':'1000000', 'D|M':'1010101' }
            print(_comp_codes[a])
            return _comp_codes[a]
        def dest(a):
            _dest_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
            print(bin(int(_dest_codes.index(a))).zfill(3))
            return bin(int(_dest_codes.index(a))).zfill(3)
        def jump(a): 
            _jump_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
            # print(bin(int(_jump_codes.index(a))).zfill(3))
            # print(a)
            # if a not in _jump_codes:
            #     return '000'
            return bin(int(_jump_codes.index(a))).zfill(3)
        if line[1]==';':
            a='111'+comp(line[0])+'000'+jump(line[2:-1])[2:].zfill(3)+'\n'
            print(a)
            fbinary=open('binary1.txt','a')
            fbinary.write(a)
        else:
            # print("jtsdfsd")
            # print("\n")
            # print(line[2:])
            # print(comp(line[2:]))
            if (line[0:2]=='AM' or line[0:2]=='AD'  or line[0:2]=='MD'):
                a='111'+comp(line[3:-1])+dest(line[0:2])[2:].zfill(3)+'000'+'\n'
                fbinary=open('binary1.txt','a')
                fbinary.write(a)
            elif line[0:3]=='AMD':
                a='111'+comp(line[4:-1])+dest(line[0:3])[2:].zfill(3)+'000'+'\n'
                fbinary=open('binary1.txt','a')
                fbinary.write(a)
            else:
                                  
                a='111'+comp(line[2:-1])+dest(line[0])[2:].zfill(3)+'000'+'\n'
            
                fbinary=open('binary1.txt','a')
                fbinary.write(a)



      


f3=open('new2.asm','r')

Lines=f3.readlines()
for line in Lines:

    print(line)
    check(line)   
# print("asdfasdfs")
# print(Lines[15])
# check(Lines[15])
# check(Lines[15])

# check('D;JGT') 
# check('D=M')