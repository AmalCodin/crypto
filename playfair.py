def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")  
    key = "".join(dict.fromkeys(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ")) 
    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]  
    return matrix

def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
    return None

def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            b = 'X'  
            i += 1
        elif i + 1 < len(plaintext):
            b = plaintext[i + 1]
            i += 2
        else:
            b = 'X'  
            i += 1
        prepared += a + b
    return prepared

def encrypt_playfair(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:  
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext


key = "KEYWORD"
plaintext = "HELLO WORLD"
ciphertext = encrypt_playfair(plaintext, key)
print("Ciphertext:", ciphertext)
