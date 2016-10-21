import base64
import subprocess

def crypt_b64(validation_key, flag):
    if len(validation_key) < len(flag):
        return
    return bytes(flag) + b'_' + \
           base64.b64encode(bytes([a^b for a,b in zip(validation_key, flag)]))

def make_bin(user, challenge):
    path = "challenges/bin/" + challenge.name
    encflag = challenge.getEncryptedFlag(user)
    binary = subprocess.check_output("make -s -C{} _FLAG_={} _ID_={}" \
                   .format(path, encflag.decode(), user.pk), shell=True)
    subprocess.run("make -s clean -C" + path, shell=True)
    return binary
