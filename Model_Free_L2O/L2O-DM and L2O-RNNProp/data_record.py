from datetime import datetime

now = datetime.now()

# UTC Timezone used
current_time = now.strftime("%Y_%m_%d_%H_%M")


# print("Current Time =", current_time)


def create_file():
    file_obj = open("./dump/{}.text".format(current_time), 'a')
    return file_obj


def add_log(file_obj, content):
    file_obj.write(content)


def close_file(file_obj):
    file_obj.close()
