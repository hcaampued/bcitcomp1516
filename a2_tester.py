# jason wilder

import main
import os


import hashlib


def hash_file(filename):
    hasher = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)
            if chunk == b"":
                break
            hasher.update(chunk)

    return hasher.hexdigest()


hashes = {
    "a_a.txt":"ff1317739e4a233949d3fc77af2f960abec403915ef1250720427e903021df9b",
    "alternating.txt":"9a0afb75f205397c8bfcba40e053a8cf16a31a254112cc6c77dbd5dbcd641047",
    "city_town.txt":"37e845e97476374919978381bf01c515b9225a16e7efdfa25f67aad72e81c48b",
    "cons_cons_cons.txt":"69e8e47722bc67582fb47dca7dea47f69c4f3e9b61b650d525ea8b6c1a254a7d",
    "double.txt":"27c0466de3baa45be073d02fc5563fc6152da88613e2f16afcd8af3fa31df549",
    "hyphen.txt":"6c607e7924374bb5c1620a275b8d79e110e85cf4974b98ce56ca84fb5a31eeae",
    "i_before_e.txt":"5867cb401ef80221bd43ed137a35151bf28f25f0c12c7ccfa8a3268c5d0c6dd0",
    "multiple.txt":"b7b21642d9604fd044ba49863fcbe6eca198f857886de19f14651d4017a2fa77",
    "not_aeio.txt":"913e4385e15260d26ec1d031b414d5d27593e0a4dff0d820df670daa632cb10e",
    "not_start.txt":"71ffab9865f7664bc6e1c2cd7b9815d838853cefa025a1ef0493c43e2392ec0c",
    "notvowel_notvowel.txt":"aa83296ad16e97bd7f41a638439f2fd3c8a9f2ea63f66d1c65c8529fb87da7dc",
    "spaces.txt":"ec5e7c2d698f49908c74049644275b1ea4f1e7adec22c91583dc0927bb09ab0b",
    "vowel_vowel_vowel.txt":"1a392b4fd890303ed52ee81f1e8a6e1556dfc3670779d175dc62b4011e800cec",
    "weird.txt":"aa581ac95e8ce5e7a655a18a5fd562397aff4b8f1afb1c813ede26b0552ae884"
}

main.main()

if __name__ == '__main__':
    for file_name, hashcode in hashes.items():
        if not os.path.isfile(file_name):
            print("missing file: " + file_name)
        else:
            if hash_file(file_name) != hashcode:
                print("problem with file: " + file_name)
            else:
                print(file_name + " looks correct")
