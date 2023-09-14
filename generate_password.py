import random
import string

total_log = string.ascii_lowercase + string.ascii_uppercase + string.digits
total_pass = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
length = 16

login = ''. join((random.sample(total_log, 10)))
password = ''.join(random.sample(total_pass, length))
print('login:  {}\nPassword: {}'.format(login, password))



