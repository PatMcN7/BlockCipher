#this program made by Patrick James McNaughton. Contact me at patmcn300@outlook.com, Github: PatMcN7

#padding the message (breaking it into chunks)
def pad_message(message, block_size = 4):
    message_list = []
    chunk = 0
    block_count = len(message) // block_size + 1
    for c in range(block_count * block_size):
        chunk = chunk << 8
        if c < len(message):
            chunk += ord(message[c])
        else:
            chunk += 0
    return message_list

#rebuilding the message
def rebuild_message(message_list, block_size = 4):
    message = ''
    for i in range(len(message_list)):
        chunk = message_list[i]
        for c in range(block_size):
            number = (chunk >> (8 * (block_size - 1 - c))) % 2 ** 8
            message += chr(number)
    return message

#Shifting the blocks
def apply_rotate(message_list, key, block_size = 4):
    cipher_list = []
    bit_max = block_size * 8
    for i in range(len(message_list)):
        chunk = message_list
        carry = chunk % 2 ** key
        carry = carry <<  (bit_max - key)
        cipher = (chunk >> key) + carry
        cipher_list.append(cipher)
    return cipher_list

def undo_shift(cipher_list, key, block_size=4):
    message_list = []
    bit_max = block_size * 8
    for i in range(len(cipher_list)):
        chunk = cipher_list[i]
        carry = chunk % (2 ** (bit_max - key))
        carry = carry << key
        number = (chunk >> (bit_max - key)) + carry
        message_list.append(number)
    return message_list


