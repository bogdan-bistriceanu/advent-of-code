my_inputs = []

def tree_finder(char):
    if char == "#":
        return True
    else:
        return False
    
def pos_finder(current_pos, landscape_len):
    return current_pos % landscape_len

def downhill(a, b):
    tree_counter = 0
    try: 
        with open('input.txt') as input_file:
            
            my_inputs = [line.rstrip() for line in input_file]
            
            line_skip = 0
            
            pos_cnt = a
            
            for line in my_inputs[1:]:
                
                line_skip += 1
                
                if line_skip == b:
                    
                    landscape = list(line)
                    
                    if tree_finder(landscape[pos_finder(pos_cnt, len(landscape))]):
                        tree_counter = tree_counter + 1 
                        
                    pos_cnt = pos_cnt + a
                    
                    line_skip = 0
    finally:    
        input_file.close()
        return(tree_counter)

print("Part 1:", downhill(3,1))
print("Part 2:", downhill(1,1)*downhill(3,1)*downhill(5,1)*downhill(7,1)*downhill(1,2))
