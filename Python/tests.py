from pip._vendor.progress import counter
import pytest
from random import randint
from speck import SpeckCipher


# Official Test Vectors
class TestOfficialTestVectors:
    """
    Official Test Vector From the Original Paper
    "The SIMON and SPECK Families of Lightweight Block Ciphers"
    """
    def test_speck32_64(self):
        key = 0x1918111009080100
        plaintxt = 0x6574694c
        ciphertxt = 0xa86842f2
        block_size = 32
        key_size = 64
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck48_72(self):
        key = 0x1211100a0908020100
        plaintxt = 0x20796c6c6172
        ciphertxt = 0xc049a5385adc
        block_size = 48
        key_size = 72
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck48_96(self):
        key = 0x1a19181211100a0908020100
        plaintxt = 0x6d2073696874
        ciphertxt = 0x735e10b6445d
        block_size = 48
        key_size = 96
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck64_96(self):
        key = 0x131211100b0a090803020100
        plaintxt = 0x74614620736e6165
        ciphertxt = 0x9f7952ec4175946c
        block_size = 64
        key_size = 96
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck64_128(self):
        key = 0x1b1a1918131211100b0a090803020100
        plaintxt = 0x3b7265747475432d
        ciphertxt = 0x8c6fa548454e028b
        block_size = 64
        key_size = 128
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck96_96(self):
        key = 0x0d0c0b0a0908050403020100
        plaintxt = 0x65776f68202c656761737520
        ciphertxt = 0x9e4d09ab717862bdde8f79aa
        block_size = 96
        key_size = 96
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck96_144(self):
        key = 0x1514131211100d0c0b0a0908050403020100
        plaintxt = 0x656d6974206e69202c726576
        ciphertxt = 0x2bf31072228a7ae440252ee6
        block_size = 96
        key_size = 144
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck128_128(self):
        key = 0x0f0e0d0c0b0a09080706050403020100
        plaintxt = 0x6c617669757165207469206564616d20
        ciphertxt = 0xa65d9851797832657860fedf5c570d18
        block_size = 128
        key_size = 128
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck128_192(self):
        key = 0x17161514131211100f0e0d0c0b0a09080706050403020100
        plaintxt = 0x726148206665696843206f7420746e65
        ciphertxt = 0x1be4cf3a13135566f9bc185de03c1886
        block_size = 128
        key_size = 192
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt

    def test_speck128_256(self):
        key = 0x1f1e1d1c1b1a191817161514131211100f0e0d0c0b0a09080706050403020100
        plaintxt = 0x65736f6874206e49202e72656e6f6f70
        ciphertxt = 0x4109010405c0f53e4eeeb48d9c188f43
        block_size = 128
        key_size = 256
        c = SpeckCipher(key, key_size, block_size, 'ECB')
        assert c.encrypt(plaintxt) == ciphertxt
        assert c.decrypt(ciphertxt) == plaintxt



class TestRandomTestVectors:
    """
    Unofficial Test Vectors Randomly Generated
    Key/Plaintext are printed out with each test in case of failure
    """
    test_cnt = 500

    def test_speck32_64(self):
        block_size = 32
        key_size = 64
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck48_72(self):
        block_size = 48
        key_size = 72
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck48_96(self):
        block_size = 48
        key_size = 96
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck64_96(self):
        block_size = 64
        key_size = 96
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck64_128(self):
        block_size = 64
        key_size = 128
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck96_96(self):
        block_size = 96
        key_size = 96
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck96_144(self):
        block_size = 96
        key_size = 144
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck128_128(self):
        block_size = 128
        key_size = 128
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck128_192(self):
        block_size = 128
        key_size = 192
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt

    def test_speck128_256(self):
        block_size = 128
        key_size = 256
        for x in range(self.test_cnt):
            key = randint(0, (2**key_size) - 1)
            plaintxt = randint(0, (2**block_size) - 1)
            print(x, hex(key), hex(plaintxt))
            c = SpeckCipher(key, key_size, block_size, 'ECB')
            assert  c.decrypt(c.encrypt(plaintxt)) == plaintxt


class TestCipherInitialization:
    not_ints = [6.22, 'hello', bytearray(b'stuffandbytes'), bytearray([12, 34, 0xAA, 00, 0x00, 34]), '0x1234567']

    def test_bad_keys(self):
        for bad_key in self.not_ints:
            with pytest.raises(TypeError):
                SpeckCipher(bad_key)

    def test_bad_counters(self):
        for bad_counters in self.not_ints:
            with pytest.raises(TypeError):
                SpeckCipher(0, counter=bad_counters)

    def test_bad_ivs(self):
        for bad_iv in self.not_ints:
            with pytest.raises(TypeError):
                SpeckCipher(0,iv=bad_iv)

    not_block_modes = [7.1231, 'ERT', 11]

    def test_bad_modes(self):
        for bad_mode in self.not_block_modes:
            with pytest.raises(ValueError):
                SpeckCipher(0, mode=bad_mode)

    not_block_sizes = [10, 'steve', 11.8]

    def test_bad_blocksizes(self):
        for bad_bsize in self.not_block_sizes:
            with pytest.raises(KeyError):
                SpeckCipher(0, block_size=bad_bsize)

    not_key_sizes = [100000, 'eve', 11.8, 127]

    def test_bad_keysize_1(self):
        for bad_ksize in self.not_key_sizes:
            with pytest.raises(KeyError):
                SpeckCipher(0, key_size=bad_ksize)




class TestCipherModes:
    key = 0x1f1e1d1c1b1a191817161514131211100f0e0d0c0b0a09080706050403020100
    plaintxt = 0x65736f6874206e49202e72656e6f6f70
    iv = 0x123456789ABCDEF0
    counter = 0x1
    block_size = 128
    key_size = 256

    def test_ctr_mode_single(self):

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'CTR', init=self.iv, counter=self.counter)
        ctr_out = c.encrypt(self.plaintxt)

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'ECB')
        ecb_out = c.encrypt((self.iv << 64) + self.counter)
        ctr_equivalent = ecb_out ^ self.plaintxt
        assert ctr_out == ctr_equivalent

    def test_ctr_mode_chain(self):

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'CTR', init=self.iv, counter=self.counter)

        ctr_out = 0
        for x in range(1000):
            ctr_out = c.encrypt(self.plaintxt)
        c = SpeckCipher(self.key, self.key_size, self.block_size, 'ECB')

        ctr_equivalent = 0
        for x in range(1000):
            ecb_out = c.encrypt((self.iv << 64) + self.counter)
            self.counter += 1
            ctr_equivalent = ecb_out ^ self.plaintxt

        assert ctr_out == ctr_equivalent

    def test_cbc_mode_single(self):

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'CBC', init=self.iv)
        cbc_out = c.encrypt(self.plaintxt)

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'ECB')
        cbc_equivalent = c.encrypt(self.iv ^ self.plaintxt)
        assert cbc_out == cbc_equivalent

    def test_cbc_mode_chain(self):

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'CBC', init=self.iv)

        cbc_out = 0
        for x in range(1000):
            cbc_out = c.encrypt(self.plaintxt)

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'ECB')

        cbc_equivalent = self.iv
        for x in range(1000):
            cbc_input = self.plaintxt ^ cbc_equivalent
            cbc_equivalent = c.encrypt(cbc_input)

        assert cbc_out == cbc_equivalent

    def test_pcbc_mode_single(self):

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'PCBC', init=self.iv)
        pcbc_out = c.encrypt(self.plaintxt)

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'ECB')
        pcbc_equivalent = c.encrypt(self.iv ^ self.plaintxt)
        assert pcbc_out == pcbc_equivalent

    def test_pcbc_mode_chain(self):

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'PCBC', init=self.iv)

        cbc_out = 0
        for x in range(1000):
            cbc_out = c.encrypt(self.plaintxt)

        c = SpeckCipher(self.key, self.key_size, self.block_size, 'ECB')

        pcbc_equivalent = 0
        for x in range(1000):
            pcbc_input = self.plaintxt ^ self.iv
            pcbc_equivalent = c.encrypt(pcbc_input)
            self.iv = pcbc_equivalent ^ self.plaintxt

        assert cbc_out == pcbc_equivalent