import random
import string

total_log = string.ascii_lowercase + string.ascii_uppercase + string.digits
total_pass = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
n = int(input('Press length login: '))
m = int(input('Press length password: '))

login = ''. join((random.sample(total_log, n)))
password = ''.join(random.sample(total_pass, m))
print('login:  {}\nPassword: {}'.format(login, password))



