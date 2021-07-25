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

#



