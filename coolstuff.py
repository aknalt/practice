# Protected by PyGuard v3.0.1 (pyguard.akean.dev)
#!/usr/bin/env python3
import sys, time, base64, inspect, struct
from functools import reduce
from random import randint
x_RanYhqoZi = time.time()
v_DF_XsSA = 23
x_IVkqZfcPm = 135
x_NsqtRW_e_buf = 224
m_PZEDz_app = 128
def x_UcPUqDX_dat():
    try:
        dbg_detected = False
        try:
            if x_QfUNoDg_ctx(d_IqAzonfRr_dat, k_Wzgqnmca)() is not None: 
                dbg_detected = True
        except: pass
        
        excessive_time = False
        try:
            et_thresh = 10.0 + (randint(0,20) / 10.0)
            if x_QfUNoDg_ctx(z_iLvSXzf, g_vTPuRe)() - x_RanYhqoZi > et_thresh: 
                excessive_time = True
        except: pass
        
        deep_stack = False
        try:
            sd_thresh = 50 + randint(0,20)
            if len(x_QfUNoDg_ctx(g_jWuWkXa, d_fdXhGuH_val)()) > sd_thresh: 
                deep_stack = True
        except: pass
        
        suspicious_modules = False
        try:
            vm_ind = [bytes([86,66,111,120,71]).decode(), bytes([118,109,116,111,111]).decode(), bytes([100,101,98,117,103]).decode()]
            if any(m for m in d_IqAzonfRr_dat.modules if any(ind in m.lower() for ind in vm_ind)): 
                suspicious_modules = True
        except: pass
        
        threat_score = sum([dbg_detected, excessive_time, deep_stack, suspicious_modules])
        return threat_score < 3
    except: return True
def z_oPKXWcbNF(c_bytes):
    try:
        if not c_bytes or len(c_bytes) < 2: return False
        try:
            x_QfUNoDg_ctx(w_RdzVem_var, g_DLYisH_env)(x_QfUNoDg_ctx(c_bytes, m_gBAISX_var)(q_ugubJHkA), q_dIUEdALip_core, q_ZwcvvJOsx)
        except: return False
        l = len(c_bytes)
        if l == 0: return False
        try:
            chk = sum(c_bytes[i] ^ (i % (randint(1,7)+1)) for i in range(min(l, 100))) % (randint(100,200)+l)
            if l > 10 and chk < l // 4:
                 if sum(c_bytes[:20]) == 0: return False
        except: pass
        return True
    except: return False
v_RpYeVLctW_cfg = ["zcUBJMOJTrAg3bHZ5jqqUIozKb4nW3jvQtYTwCDcZcP2Pbx2ZVkZQbzNGJMIAw"]
w_RdzVem_var = __import__(bytes([98, 117, 105, 108, 116, 105, 110, 115]).decode())
x_QfUNoDg_ctx = getattr(w_RdzVem_var, bytes([103, 101, 116, 97, 116, 116, 114]).decode())
q_ugubJHkA = bytes([117, 116, 102, 45, 56]).decode()
m_gBAISX_var = bytes([100, 101, 99, 111, 100, 101]).decode(q_ugubJHkA)
d_kftVTYCHJ_val = bytes([114, 101, 112, 108, 97, 99, 101]).decode(q_ugubJHkA)
z_FPKKA_ctx = bytes([115, 116, 114, 105, 112]).decode(q_ugubJHkA)
v_lFKiB_env = __import__(bytes([98, 97, 115, 101, 54, 52]).decode(q_ugubJHkA))
v_BdVsj_sec = bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode(q_ugubJHkA)
x_VTFsEYD = x_QfUNoDg_ctx(v_lFKiB_env, v_BdVsj_sec)
m_JEZCA_sec = bytes([43]).decode(q_ugubJHkA)
v_tOSNIvvZp_var = bytes([47]).decode(q_ugubJHkA)
d_hnzTqtyu_cfg = bytes([61]).decode(q_ugubJHkA)
q_dIUEdALip_core = bytes([60, 111, 98, 102, 117, 115, 99, 97, 116, 101, 100, 62]).decode(q_ugubJHkA)
q_ZwcvvJOsx = bytes([101, 120, 101, 99]).decode(q_ugubJHkA)
g_DLYisH_env = bytes([99, 111, 109, 112, 105, 108, 101]).decode(q_ugubJHkA)
d_IqAzonfRr_dat = sys
z_iLvSXzf = time
g_jWuWkXa = inspect
k_Wzgqnmca = bytes([103, 101, 116, 116, 114, 97, 99, 101]).decode(q_ugubJHkA)
g_vTPuRe = bytes([116, 105, 109, 101]).decode(q_ugubJHkA)
v_nVsVZ_env = bytes([115, 108, 101, 101, 112]).decode(q_ugubJHkA)
d_fdXhGuH_val = bytes([115, 116, 97, 99, 107]).decode(q_ugubJHkA)
x_jHfriyjh = bytes([102, 105, 110, 100, 95, 109, 111, 100, 117, 108, 101]).decode(q_ugubJHkA)
v_ZWWVxUh_app = bytes([95, 95, 109, 97, 105, 110, 95, 95]).decode(q_ugubJHkA)
def EXypbqrQRsNESSZY(a, b, c=2): return [(x * c ^ b) % 256 for x in a[:14]] if hasattr(a, '__len__') else [b,c]
def eRthWSveun(s): return ''.join(chr(ord(c) + 3) for c in str(s) if ord(c) < 125)
def II_dmwOmIkhXjcC_(arr): return sum(x*2+10 for i,x in enumerate(arr) if i%2==0) % 1723
def qmSQsKrMbup(arr): return sum(x*5+4 for i,x in enumerate(arr) if i%2==1) % 1225
def mZAxOzGURRLoy(arr): return sum(x*3+5 for i,x in enumerate(arr) if i%2==0) % 1504
def qScRBH_cMuK(arr): return sum(x*4+6 for i,x in enumerate(arr) if i%2==0) % 1042
def ylyvgUfHudz(a, b, c=19): return [(x * c ^ b) % 256 for x in a[:15]] if hasattr(a, '__len__') else [b,c]
def k_MBFRHhEE(val, shf, dr=1):
    return ((val << shf) | (val >> (8 - shf))) & 0xFF if dr > 0 else ((val >> shf) | (val << (8 - shf))) & 0xFF
def x_QjTzket_dat():
    enc = "".join(v_RpYeVLctW_cfg)
    enc = x_QfUNoDg_ctx(enc, d_kftVTYCHJ_val)("-", m_JEZCA_sec)
    enc = x_QfUNoDg_ctx(enc, d_kftVTYCHJ_val)("_", v_tOSNIvvZp_var)
    pad = len(enc) % 4
    if pad: enc += d_hnzTqtyu_cfg * (4 - pad)
    try: return x_VTFsEYD(enc.encode(q_ugubJHkA))
    except: return b''
def g_IxuxtYv(data, pk, sk, rk, sbx, iv_val):
    out = bytearray(len(data))
    prev_b = iv_val % 256
    for i in range(len(data)):
        b = data[i] ^ sk[i % len(sk)]
        b ^= prev_b
        b = k_MBFRHhEE(b, rk[i % len(rk)], -1)
        b_before_sbox = b
        try:
            b = sbx.index(b)
        except ValueError:
            b = b_before_sbox
        b = b ^ pk[i % len(pk)]
        out[i] = b
        prev_b = data[i]
    return bytes(out)
def m_QaYjI_dat():
    if not x_UcPUqDX_dat():
        try:
            g = list(range(randint(50,100)))
            [g.sort(key=lambda x: x % randint(2,5)) for _ in range(randint(1,2))]
            return bytes([sum(g)%255] * randint(1,3))
        except: return bytes([randint(1,255)])
    enc_data = x_QjTzket_dat()
    if not enc_data: return bytes(b"\x0F" * randint(1,3))
    try:
        _pk_ = q_UejHdkjkB()
        _sk_ = p_ixVwZZtD_dat()
        _rk_ = k_JMFVxm_lib()
        _sbx_ = x_iZMitDoP()
        _iv_val_ = q__vUKpGrsB_lib()
        dec_data = g_IxuxtYv(enc_data, _pk_, _sk_, _rk_, _sbx_, _iv_val_)
        if not z_oPKXWcbNF(dec_data):
             try:
                 x_ = bytearray(str(list(range(randint(5,10)))).encode(q_ugubJHkA))
                 for _idx in range(min(len(x_), 10)): x_[_idx] = (_idx ^ x_[_idx]) % 256
                 return bytes(x_[:randint(1,3)])
             except: return bytes([randint(1,255)])
        return dec_data
    except Exception as e_dec:
        try:
            _err_dump = str(e_dec)[:10] 
            return bytes([ord(c) % 256 for c in _err_dump[:randint(1,3)]])
        except: return bytes([randint(1,255)])
def q_yCDNb_dLD(code_payload):
    if not code_payload or len(code_payload) < 2: return
    try:
        x_QfUNoDg_ctx(w_RdzVem_var, q_ZwcvvJOsx)(
            x_QfUNoDg_ctx(w_RdzVem_var, g_DLYisH_env)(
                x_QfUNoDg_ctx(code_payload, m_gBAISX_var)(q_ugubJHkA),
                q_dIUEdALip_core,
                q_ZwcvvJOsx
            ),
            globals(), {}
        )
    except Exception as ex_run:
        try:
            if x_QfUNoDg_ctx(d_IqAzonfRr_dat, k_Wzgqnmca)() is not None:
                pass
        except: pass
        raise ex_run
def p_bXZPoh_env():
    try:
        try:
            jtr = randint(1, 10) / (1000.0 + randint(0,50))
            x_QfUNoDg_ctx(z_iLvSXzf, v_nVsVZ_env)(jtr)
        except: pass
        payload = m_QaYjI_dat()
        if payload and isinstance(payload, bytes) and len(payload) > (randint(1,3)+1):
            q_yCDNb_dLD(payload)
    except Exception as ex_main:
        try:
            if x_QfUNoDg_ctx(d_IqAzonfRr_dat, k_Wzgqnmca)() is None:
                raise ex_main
        except: pass
        raise ex_main
def q_UejHdkjkB():
    k_data = [79, 131, 61, 162, 69, 1, 6, 133, -16, 38, 41, 40, -81, -82, -2, -82, -42, -64, 13, -18, -27, 82, 85, 124, 1, 51, -58, 18, -24, 62, 102, 99, 81, 23, 53, -79, 87, -43, 4, 101, 117, -21, -6]
    return [(x + 224 - 135) ^ 23 for x in k_data]
def p_ixVwZZtD_dat():
    s_data = [630, 391, 386, 561, 427, 616, 429, 549, 382, 397, 569, 569, 502, 559, 626, 452, 466, 601, 405, 547, 383, 509, 527, 562, 565, 559, 636, 467, 506, 599, 595, 382, 625, 457, 626, 599, 503, 432, 401, 431, 599, 398, 565]
    return [x - 382 for x in s_data]
def k_JMFVxm_lib():
    r_const = [230, 229, 226, 231, 227, 230, 228, 226, 230, 230, 226, 230, 231]
    return [val - 224 for val in r_const]
def x_iZMitDoP():
    p1 = [128, 113, 104, 26, 152, 94, 78, 38, 223, 192, 34, 8, 108, 187, 23, 4, 135, 68, 107, 141, 52, 197, 183, 2, 88, 35, 58, 97, 72, 162, 158, 212, 186, 139, 199, 144, 195, 235, 80, 0, 60, 83, 36, 70, 137, 57, 101, 99, 50, 246, 129, 27, 255, 174, 112, 31, 138, 177, 160, 63, 184, 136, 47, 210, 176, 17, 201, 116, 230, 245, 209, 15, 198, 111, 165, 237, 79, 228, 124, 150, 75, 243, 251, 191, 1, 253, 65, 163, 156, 28, 56, 43, 18, 71, 216, 147, 126, 89, 215, 39, 22, 98, 240, 194, 95, 12, 110, 172, 59, 225, 19, 159, 153, 207, 93, 118, 55, 64, 14, 148, 190, 222, 13, 121, 127, 167, 85, 9]
    p2 = [34, 201, 58, 113, 66, 187, 241, 60, 92, 63, 16, 86, 65, 44, 173, 145, 163, 227, 238, 115, 180, 165, 181, 151, 74, 18, 0, 68, 199, 223, 25, 102, 6, 90, 186, 143, 242, 13, 234, 244, 231, 106, 128, 95, 23, 117, 45, 138, 54, 98, 30, 69, 215, 67, 233, 202, 20, 31, 171, 217, 101, 61, 59, 144, 252, 166, 121, 218, 81, 160, 219, 109, 9, 29, 221, 154, 140, 120, 141, 46, 27, 11, 75, 239, 214, 5, 132, 36, 193, 108, 190, 57, 83, 178, 130, 51, 24, 161, 123, 240, 21, 94, 158, 210, 39, 93, 116, 96, 133, 3, 226, 189, 88, 114, 196, 42, 172, 14, 147, 222, 194, 198, 253, 157, 43, 78, 33, 15]
    return [(v ^ 224) for v in p1] + [(v ^ 23) for v in p2]
def q__vUKpGrsB_lib():
    return 16674938 + (23 * 135) + 224
if __name__ == v_ZWWVxUh_app:
    try:
        p_bXZPoh_env()
    except Exception:
        try:
            if x_QfUNoDg_ctx(d_IqAzonfRr_dat, k_Wzgqnmca)() is None:
                raise
        except: pass
