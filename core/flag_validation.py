import base64
import subprocess

def crypt_b64(user, challenge):
    key = user.validation_key.bytes
    flag = challenge.flag.encode()
    if len(key) < len(flag):
        return
    return base64.b64encode(bytes([a^b for a,b in zip(key, flag)]))

def make_bin(user, challenge):
    path = "challenges/bin/" + challenge.name
    encflag = crypt_b64(user, challenge)
    binary = subprocess.check_output("make -s -C{} _FLAG_={} _ID_={}" \
                   .format(path, encflag.decode(), user.pk), shell=True)
    subprocess.run("make -s clean -C" + path, shell=True)
    return binary
