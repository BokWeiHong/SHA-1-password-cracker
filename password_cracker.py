import hashlib

def crack_sha1_hash(hash, use_salts=False):
    salts = []
    if use_salts:
        # Get all known salts from file if use_salts is true
        with open("known-salts.txt") as salt_file:
            salts = salt_file.read().splitlines()

    with open("top-10000-passwords.txt", mode="r") as password_txt:
        # Get all passwords to check
        passwords = [p.strip() for p in password_txt]

        for password in passwords:
            # Password check without salts
            if not use_salts:
                cracked_password_hash = hashlib.sha1(password.encode("utf-8")).hexdigest()
                if cracked_password_hash == hash:
                    return password
            else:
                # Password check with salts
                for salt in salts:
                    for salted_password in (salt + password, password + salt):
                        cracked_password_hash = hashlib.sha1(salted_password.encode("utf-8")).hexdigest()
                        if cracked_password_hash == hash:
                            return password

    return "PASSWORD NOT IN DATABASE"
