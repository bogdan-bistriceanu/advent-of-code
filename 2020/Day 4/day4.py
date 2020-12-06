import re

hair_reeeeeee = re.compile('^#[0-9a-f]{6}$')

required_fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
passport_list = []
passport = {}
part_1_count = 0
part_2_count = 0

def check_height(data):
    if data[:-2].isdigit() and data.endswith("cm") and 150 <= int(data[:-2]) <= 193: 
        return True
    
    if data[:-2].isdigit() and data.endswith("in") and 59 <= int(data[:-2]) <= 76:
        return True
    
    return False

def check_passport(data):
    
    byr = data.get('byr')
    iyr = data.get('iyr')
    eyr = data.get('eyr')
    hgt = data.get('hgt')
    hcl = data.get('hcl')
    ecl = data.get('ecl')
    pid = data.get('pid')

    if byr == None:
        byr = False
    elif len(byr) == 4 and 1920 <= int(byr) <= 2002:
        byr = True

    if iyr == None:
        iyr = False
    elif len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
        iyr = True
        
    if eyr == None:
        eyr = False
    elif len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
        eyr = True
        
    if hcl == None:
        hcl = False
    elif bool(hair_reeeeeee.match(hcl)):
        hcl = True

    if ecl == None:
        ecl = False
    elif ecl in {"amb","blu","brn","gry","grn","hzl","oth"}:
        ecl = True

    if pid == None:
        pid = False
    elif len(pid) == 9 and pid.isdigit():
        pid = True
        
    if hgt == None:
        hgt = False
    elif check_height(hgt):
        hgt = True 
    
    print(byr)
    
    if byr == True and iyr == True and eyr == True and hcl == True and ecl == True and pid == True and hgt == True:
        return True
    else:
        return False
        
    #   print('Yes:', yes)
    #print('No:', no)


with open('input.txt') as input_file:
    x = input_file.readlines()
    x.append('')
    for line in x:
        line = line.strip()
        if line:
            passport.update([line.split(':') for line in line.split(' ')])
            #print(line)
            #print(passport)
        else:
            passport_list.append(passport)
            passport = {}
            #print('Blank')

input_file.close()

for item in passport_list:
    if required_fields.issubset(item):
        part_1_count += 1
        
    if check_passport(item) == True:
        part_2_count += 1
        
print('Part 1:', part_1_count)
print('Part 2:', part_2_count)