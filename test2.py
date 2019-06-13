password = "pbkdf2:sha256:150000$St9g87AI$e8b7ea6a77cf01bbaae4b641133fd46667938ad7e664214722b38cc42b4dff7f"

p = "miguel"

from werkzeug.security import generate_password_hash, check_password_hash

if check_password_hash(password, p):
    print "OK"
else:
    print "Not Ok"


class Hola:
    def __init__(self):
        print "Hola"