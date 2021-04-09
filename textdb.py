from os import listdir
from os.path import isfile, join, realpath, dirname
import codecs 

def makeCsv(file_path, csv_path):
    with open(file_path, 'rt', encoding='UTF-8') as f:
        read_file = f.read()
    f.close() 
    new_file = codecs.open(csv_path, 'w', encoding='UTF-8')
    new_file.write(read_file)
    
    #close file 
    new_file.close() 
    print(csv_path+'생성 시작...')

def replaceInFile(file_path, old, newstr):
    with open(file_path, 'rt', encoding='UTF-8') as f:
        read_file = f.read()
    f.close() 
    new_file = codecs.open(file_path, 'w', encoding='UTF-8')
    for line in read_file.split("\n"): 
        new_file.write(line.replace(old, newstr)) 
        new_file.write("\n")
    
    #close file 
    new_file.close() 

def changeHead(file_path):
    with open(file_path, 'rt', encoding='UTF-8') as f:
        read_file = f.read()
    f.close() 
    new_file = codecs.open(file_path, 'w', encoding='UTF-8')
    line = read_file.split("\n")
    new_file.write("f,gain,phase\n") 
    for body in line[1:]: 
        new_file.write(body) 
        new_file.write("\n")
    
    #close file 
    new_file.close() 
    print(file_path[:-3]+'csv 생성 완료')
    
mypath = dirname(realpath(__file__))
onlytxts = [ f for f in listdir(mypath) if (isfile(join(mypath,f))) and (f[-3:]=='txt') ] 
print('현재 경로에 있는 txt파일로 엑셀 csv 파일을 생성합니다.')
print('대상 파일 : ')
for fname in onlytxts: 
    print('\t'+fname)
print('프로그램이 강제 종료되면 txt파일을 한번 열어서 저장(Ctrl + S)한 후 닫고 다시 시도해보세요')
input('계속하려면 엔터 키를 누르세요')
for fname in onlytxts: 
    fpath = join(mypath,fname) 
    fcsvpath = fpath[:-3]+'csv'
    makeCsv(fpath,fcsvpath);
    replaceInFile(fcsvpath, "?", "");
    replaceInFile(fcsvpath, "dB", "");
    replaceInFile(fcsvpath, "(", "");
    replaceInFile(fcsvpath, "\t", ",");
    changeHead(fcsvpath);
input('종료하려면 엔터 키를 누르세요')

