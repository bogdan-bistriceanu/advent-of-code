import re

line = 0
sol_count_p1 = 0
sol_count_p2 = 0
my_inputs = []

def eval_part_1(pswd_txt, rule_min, rule_max, rule_chr):
    if rule_min <= pswd_txt.count(rule_chr) <= rule_max:
        return True
    else:
        return False
    
def eval_part_2(pswd_txt, rule_ps1, rule_ps2, rule_chr):
    srch_val = rule_chr
    word_arr = list(pswd_txt)
    
    if word_arr[rule_ps1-1] == srch_val and word_arr[rule_ps2-1] == srch_val:
        return False
    elif word_arr[rule_ps1-1] != srch_val and word_arr[rule_ps2-1] != srch_val:
        return False
    else:
        return True   
    
try: 
    with open('input.txt') as input_file:
        print('file opened')
        my_inputs = [line.rstrip() for line in input_file]
        for rule in my_inputs:
            line = line + 1
            
            rule = re.sub('(-|\:|\s)','_',rule)
            rule = re.sub('__','_', rule)
            
            rule_min = int(rule.split('_')[0])
            rule_max = int(rule.split('_')[1])
            rule_chr = rule.split('_')[2]
            pswd_txt = rule.split('_')[3]
            
            if eval_part_1(pswd_txt, rule_min, rule_max, rule_chr):
                sol_count_p1 = sol_count_p1 + 1
                
            if eval_part_2(pswd_txt, rule_min, rule_max, rule_chr):
                sol_count_p2 = sol_count_p2 + 1
finally:    
    input_file.close()
    print('Solution count part 1:', sol_count_p1)
    print('Solution count part 2:', sol_count_p2)
    print('file closed')