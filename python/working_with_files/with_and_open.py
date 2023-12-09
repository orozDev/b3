

# file_for_write = open('text.txt', 'w')
# file_for_write.write('Nursultan loves Kyrgystan')
# file_for_write.close()
#
# file_for_read = open('text.txt', 'r')
# text_after_reading = file_for_read.read()
# print(text_after_reading)
# file_for_read.close()


# with open('text.txt', 'r') as file_for_read:
#     text_after_reading = file_for_read.read()
#     print(text_after_reading)
#
# with open('text.txt', 'w') as file_for_write:
#     file_for_write.write('Nursultan loves Kyrgystan')

with open('text.txt', 'r+') as file:
    text = file.read()
    print(text)
    file.write('Nursultan loves Kyrgystan')
    text = file.read()
    print(text)

