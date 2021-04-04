
import timeit
import zlib


def getFiles():
    tusen_byte=''
    tio_tusen_byte=''
    hundra_kb = ''
    en_mb=''
    tio_mb=''
    with open('1000byte.txt', "r", encoding="utf-8") as file:
        for row in file:
            tusen_byte=tusen_byte+row

    with open('10_000byte.txt', "r", encoding="utf-8") as file:
        for row in file:
            tio_tusen_byte=tusen_byte+row


    with open('100_000byte.txt', "r", encoding="utf-8") as file:
        for row in file:
            hundra_kb = hundra_kb + row

    with open('1_000_000byte.txt', "r", encoding="utf-8") as file:
        for row in file:
            en_mb = en_mb + row

    with open('10_000_000byte.txt', "r", encoding="utf-8") as file:
        for row in file:
            tio_mb = tio_mb + row
    return tusen_byte, tio_tusen_byte, hundra_kb, en_mb, tio_mb


def time_adler(en_kb, tio_kb, hundra_kb, en_mb, tio_mb):
    en_kb_byte=en_kb.encode()
    tio_kb_byte = tio_kb.encode()
    hundra_kb_byte = hundra_kb.encode()
    en_mb_byte = en_mb.encode()
    tio_mb_byte = tio_mb.encode()



    print("Adler32 med 1 kb tog",timeit.timeit(stmt=lambda: zlib.adler32(en_kb_byte)) , "sekunder")
    print("Adler32 med 10 kb tog", timeit.timeit(stmt=lambda: zlib.adler32(tio_kb_byte)), "sekunder")
    print("Adler32 med 100 kb tog", timeit.timeit(stmt=lambda: zlib.adler32(hundra_kb_byte)), "sekunder")
    print("Adler32 med 1 Mb tog", timeit.timeit(stmt=lambda: zlib.adler32(en_mb_byte)), "sekunder")
    print("Adler32 med 10 Mb tog", timeit.timeit(stmt=lambda: zlib.adler32(tio_mb_byte)), "sekunder")

if __name__ == '__main__':
    en_kb, tio_kb, hundra_kb, en_mb, tio_mb=getFiles()
    time_adler(en_kb, tio_kb, hundra_kb, en_mb, tio_mb)
