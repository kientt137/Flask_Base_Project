from AesEverywhere import aes256
import bcrypt as bc
import json
import requests
from .Config import caches


def get_data_api(url):
    request = requests.get(url)
    data_json = request.json()
    return data_json


def put_json_api(url, **data):
    request = requests.put(url, json=data)
    data_json = request.json()
    return data_json


def post_json_api(url, **data):
    request = requests.post(url, json=data)
    data_json = request.json()
    return data_json


def delete_json_api(url, **data):
    request = requests.delete(url, json=data)
    data_json = request.json()
    return data_json


def get_cache(domain, id):
    return caches.get(domain + "-" + str(id))


def set_cache(domain, id, data):
    return caches.set(domain + "-" + str(id), data)


def update_cache(domain, id, new_data):
    caches.delete(domain + "-" + str(id))
    return caches.set(domain + "-" + str(id), new_data)


def delete_cache(domain, id):
    return caches.delete(domain + "-" + str(id))


def find_keys_cache(domain):
    k_prefix = caches.cache.key_prefix
    keys = caches.cache._write_client.keys(k_prefix + "*")
    keys = [k.decode("utf8") for k in keys]
    keys = [k.replace(k_prefix, "") for k in keys]
    result = list(filter(lambda x: (domain in x), keys))
    return result


def encrypt_bc(key):
    if isinstance(key, str):
        key = key.encode("utf-8")

    hashed = bc.hashpw(key, bc.gensalt())
    return hashed.decode("utf-8")


def check_bc(passwd, hashed):
    if isinstance(passwd, str) and isinstance(hashed, str):
        passwd = passwd.encode("utf-8")
        hashed = hashed.encode("utf-8")

    return bc.checkpw(passwd, hashed)


def encrypt_aes(values, salt):
    val = json.dumps(values)
    encrypted = aes256.encrypt(val, salt)
    return str(encrypted, "utf-8")


def decrypt_aes(values, salt):
    decrypted = aes256.decrypt(values, salt)
    return json.loads(decrypted)
