tree_counter = 0
my_inputs = []

def tree_finder(char):
    if char == "#":
        return True
    else:
        return False
    
def pos_finder(current_pos, landscape_len):
    if current_pos % landscape_len == current_pos:
        return current_pos
    elif current_pos % landscape_len == 0:
        return landscape_len - 1
    else:
        return current_pos % landscape_len

try: 
    with open('input.txt') as input_file:
        
        print('file open')
        
        my_inputs = [line.rstrip() for line in input_file]
        
        pos_cnt = 3
        
        for line in my_inputs[1:]:
            
            landscape = list(line)
            print(len(landscape))
            
            if tree_finder(landscape[pos_finder(pos_cnt, len(landscape))]):
                tree_counter = tree_counter + 1 
            
            pos_cnt = pos_cnt + 3
            
finally:    
    input_file.close()
    print('Trees:', tree_counter)
    print('file closed')