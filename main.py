#! /usr/bin/env python3
#
#   check all seeds for valid when one word unknown
#

from electrum.keystore import bip39_is_checksum_valid

def load_wordlist():
    text_file = open("srv/app/wordlist.txt")
    lines = text_file.readlines()
    text_file.close()
    return lines

def recreate_seed(known_words, all_possible_words):
    for w in words:
        for n in range(len(known_words)+1):
            chk = known[:n]+[w]+known[n:]
            is_checksum,_ = bip39_is_checksum_valid(' '.join(chk))
            if is_checksum:
                return ("".join(chk), n)
    return None

#TODO: Hier die wörter einfügen, die bekannt sind (mit leerzeichen dazwischen)
known = 'put your known words here just like this etc etc etc'.split()
words = load_wordlist()

print(f"versuche seed wiederherzustellen für folgende bekannte Wörter: {known}")

recreated_seed = recreate_seed(known, words)
if recreated_seed:
    print(f"Der Seed ist: {recreated_seed[0]}")
    print(f"Das fehlende Wort war: {recreated_seed[1]}")
else:
    print("Seed konnte nicht erstellt werden")
