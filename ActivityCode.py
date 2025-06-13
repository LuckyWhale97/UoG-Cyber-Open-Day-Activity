ciphertexts = {
    "A": "Kh pdufkhg eudyhob lqwr wkh vwrup.",
    "B": "AABAAAAAAAAAABAAABBBAAABAAABBBAAAAAABABBABABBAABAAABBABAABBAAABAABAAABAABAABABABAABAAAAAAAABABBAABAAAAABBAAAAAAABBBABAAAAAABBAAABBAABAAABBABBAABABAABBBAAABAABAAABBABAABBABAABBAABBB",
    "C": "Vmmxw eeepnib dlc krasild ggdc ukpjc.",
    "D": "Oltrx lugvm hloevh dszg yifgv ulixv xzmmlg.",
    "E": "OHLIIEDVESESCXEHATPHXRIQWEOXTLUHREX ",
    "F": "BABBAABAAABAABAAAABBABBBAABBAAAABBBABAAAAAABBAABAABAABAABAAAABBABABBBBABABBAAAAAABAAAABBABBAABAABAAAAABBAAABBBBAABBAABABABBBABAAABBAABBAABBBAABAAABBBBAAAAABAABBABAAAAABAAABBABBAABB",
    "G": "Vykpuhyf tlu kylht vm leayhvykpuhyf aopunz.",
    "H": "Ivzorgb yvmwh dsvm rnztrmzgrlm gzpvh levi.",
    "I": "LNHSTAIETOTGSOREHTLIATADETTRSS",
    "J": "Zfrrrjg npua afch pvry mqgk xbpvj tq pvzd uaocx."
}

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def atbash_decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(base + (25 - (ord(char) - base)))
        else:
            result += char
    return result

def vigenere_decrypt(text, keyword):
    result = ""
    keyword = keyword.upper()
    k_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[k_index % len(keyword)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift + 26) % 26 + base)
            k_index += 1
        else:
            result += char
    return result

def bacon_decrypt(text):
    bacon_map = {
        "AAAAA": "A", "AAAAB": "B", "AAABA": "C", "AAABB": "D",
        "AABAA": "E", "AABAB": "F", "AABBA": "G", "AABBB": "H",
        "ABAAA": "I", "ABAAB": "J", "ABABA": "K", "ABABB": "L",
        "ABBAA": "M", "ABBAB": "N", "ABBBA": "O", "ABBBB": "P",
        "BAAAA": "Q", "BAAAB": "R", "BAABA": "S", "BAABB": "T",
        "BABAA": "U", "BABAB": "V", "BABBA": "W", "BABBB": "X",
        "BBAAA": "Y", "BBAAB": "Z"
    }
    result = ""
    filtered_text = ''.join([c for c in text if c in "AB"])
    for i in range(0, len(filtered_text), 5):
        chunk = filtered_text[i:i+5]
        if chunk in bacon_map:
            result += bacon_map[chunk]
    return result

def columnar_decrypt(text, num_cols):
    text = text.replace(" ", "").upper()
    num_rows = len(text) // num_cols
    cols = [text[i * num_rows:(i + 1) * num_rows] for i in range(num_cols)]
    result = ''
    for i in range(num_rows):
        for col in cols:
            if i < len(col):
                result += col[i]
    return result

print("Select a ciphertext label (A-J) to see the encrypted message.")

while True:
    choice = input("Enter ciphertext label (A-J) or 'exit' to quit: ").upper()
    if choice == "EXIT":
        break
    elif choice in ciphertexts:
        print(f"\nCiphertext {choice}:")
        print(ciphertexts[choice])
        
        print("\nSelect a decryption method:")
        print("1. Caesar")
        print("2. Atbash")
        print("3. Vigenere")
        print("4. Baconian")
        print("5. Columnar Transposition")
        
        method_choice = input("Enter the number of the decryption method (1-5): ")
        decrypted_text = ""
        
        if method_choice == "1":
            shift = int(input("Enter the Caesar shift (0-25): "))
            decrypted_text = caesar_decrypt(ciphertexts[choice], shift)
        elif method_choice == "2":
            decrypted_text = atbash_decrypt(ciphertexts[choice])
        elif method_choice == "3":
            keyword = input("Enter the Vigenere keyword: ").upper()
            decrypted_text = vigenere_decrypt(ciphertexts[choice], keyword)
        elif method_choice == "4":
            decrypted_text = bacon_decrypt(ciphertexts[choice])
        elif method_choice == "5":
            num_cols = int(input("Enter the number of columns for Columnar Transposition: "))
            decrypted_text = columnar_decrypt(ciphertexts[choice], num_cols)
        else:
            print("Invalid choice.")
            continue
        
        print(f"\nDecrypted message using method {method_choice}:")
        print(decrypted_text)
        
    else:
        print("Please enter a letter from A to J, or 'exit' to quit.")
