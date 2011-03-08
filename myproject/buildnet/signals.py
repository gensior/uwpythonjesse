import random, string

set_qrcode = object()

def serial(length):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(length))