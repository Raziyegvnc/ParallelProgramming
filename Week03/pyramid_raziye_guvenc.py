def calculate_pyramid_height(number_of_blocks: int) -> int:
    height = 0
    blocks_used = 0
    
    while blocks_used + (height + 1) <= number_of_blocks:
        height += 1
        blocks_used += height
    return height
