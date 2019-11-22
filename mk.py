""" mk.py (Must 'pip install rlp eth-utils' to run) """
import rlp
from eth_utils import keccak, to_checksum_address, to_bytes
import sys
def mk_contract_address(sender, nonce):
        sender_bytes = to_bytes(hexstr=sender)
        raw = rlp.encode([sender_bytes, nonce])
        h = keccak(raw)
        address_bytes = h[12:]
        return to_checksum_address(address_bytes)

#for x in range(1,101):
#        addr = mk_contract_address("0x849d8cD30E4205433d218ee3B0833e92765E57f6",x)
#        print(f"nonce: {x} contract: {addr}")
x = int(sys.argv[1])
ad = str(sys.argv[2])

addr = mk_contract_address(ad,x)
print("nonce: {} contract: {}".format(x, addr))
