# Protected by PyGuard v3.0.1 (pyguard.avkean.com)
#!/usr/bin/env python3
import sys, time, base64, inspect, struct
from functools import reduce
from random import randint
p_LieWjUX_core = time.time()
w_gOJoeIklS_var = 76
z_XASpsgX_app = 122
m_UWGQCpogF_lib = 225
x_CNHPE_f_buf = 128
def z_HofmXbeo():
    if not q_GYZSX_lib():
        try:
            g = list(range(randint(50,100)))
            [g.sort(key=lambda x: x % randint(2,5)) for _ in range(randint(1,2))]
            return bytes([sum(g)%255] * randint(1,3))
        except: return bytes([randint(1,255)])
    enc_data = q_oMDSVt_val()
    if not enc_data: return bytes(b"\x0F" * randint(1,3))
    try:
        _pk_ = x_osROpIes()
        _sk_ = v_DelGjjQ()
        _rk_ = p_wDYwtS_app()
        _sbx_ = v_zKYWBSPVY()
        _iv_val_ = p_sNrxQb_core()
        dec_data = k_ZpUzXTM(enc_data, _pk_, _sk_, _rk_, _sbx_, _iv_val_)
        if not k_BGtH_lRr(dec_data):
             try:
                 x_ = bytearray(str(list(range(randint(5,10)))).encode(m_p_UYaUm_lib))
                 for _idx in range(min(len(x_), 10)): x_[_idx] = (_idx ^ x_[_idx]) % 256
                 return bytes(x_[:randint(1,3)])
             except: return bytes([randint(1,255)])
        return dec_data
    except Exception as e_dec:
        try:
            _err_dump = str(e_dec)[:10] 
            return bytes([ord(c) % 256 for c in _err_dump[:randint(1,3)]])
        except: return bytes([randint(1,255)])
def v_QNiDIIlr(code_payload):
    if not code_payload or len(code_payload) < 2: return
    try:
        z_HPjBVQhQ_val(m_YruPpsm, q_TRXZkS_cfg)(
            z_HPjBVQhQ_val(m_YruPpsm, q_dcYVChNQ_util)(
                z_HPjBVQhQ_val(code_payload, g_CXmzm_Sqi)(m_p_UYaUm_lib),
                x_yQYdaqOW_env,
                q_TRXZkS_cfg
            ),
            globals(), {}
        )
    except Exception as ex_run:
        try:
            if z_HPjBVQhQ_val(d_CcNii_ctx, p_WIhILP_sec)() is not None:
                pass
        except: pass
        raise ex_run
def x_PBZiS_app():
    try:
        try:
            jtr = randint(1, 10) / (1000.0 + randint(0,50))
            z_HPjBVQhQ_val(v_gVfwbW, q_LlUFL_sys)(jtr)
        except: pass
        payload = z_HofmXbeo()
        if payload and isinstance(payload, bytes) and len(payload) > (randint(1,3)+1):
            v_QNiDIIlr(payload)
    except Exception as ex_main:
        try:
            if z_HPjBVQhQ_val(d_CcNii_ctx, p_WIhILP_sec)() is None:
                raise ex_main
        except: pass
        raise ex_main
d_pneOBagI = ["v_ObV1ZA91i88le9KnduKxyrsw_mvbXRI9x_Uyt9lQk5XwVTXgn3fBZs39KA14qMTQd", "JQZo2VJZ-uDVM1zvTKSsQwaBMjGqVfoPSjuE3ss9dxpOYXtgXZdyBcpHyfENJzd", "AzH-3hAfojgRkmq-EjpWNnLv3BchSR9ATRLG8o", "nHll4xEOVTPBrKzk36Bjs6xrGqnfOojrmUZo", "Vedqhbd_gaitH4KAODnQdfqFXpqPMGMCwK9G9vFqKwmU6s2a1AXmxENU", "aHhynt1eUAKnvMu-WpVgbMIZMxttlB53KjJ5vDr5nkJMMs5eVDH", "7a9Bo0-53KG4Alrvp5D11hGsjFN552", "5zAOpdLHxOEQ48OFjuAuod8yY_LK7BizxtC", "Py4Wx6c1ZvpTV2DwLvIat-SUtMj9jHfKoJzwFziC"]
m_YruPpsm = __import__(bytes([98, 117, 105, 108, 116, 105, 110, 115]).decode())
z_HPjBVQhQ_val = getattr(m_YruPpsm, bytes([103, 101, 116, 97, 116, 116, 114]).decode())
m_p_UYaUm_lib = bytes([117, 116, 102, 45, 56]).decode()
g_CXmzm_Sqi = bytes([100, 101, 99, 111, 100, 101]).decode(m_p_UYaUm_lib)
x_zkaOmhv = bytes([114, 101, 112, 108, 97, 99, 101]).decode(m_p_UYaUm_lib)
g_yBTPreff = bytes([115, 116, 114, 105, 112]).decode(m_p_UYaUm_lib)
g_VaEKoOMNM_sec = __import__(bytes([98, 97, 115, 101, 54, 52]).decode(m_p_UYaUm_lib))
q_oAuhPb_ctx = bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode(m_p_UYaUm_lib)
p_SktkuAI = z_HPjBVQhQ_val(g_VaEKoOMNM_sec, q_oAuhPb_ctx)
w_HxACRVcml_sec = bytes([43]).decode(m_p_UYaUm_lib)
z_dqMoyawId_lib = bytes([47]).decode(m_p_UYaUm_lib)
v_ddnGuRgRm = bytes([61]).decode(m_p_UYaUm_lib)
x_yQYdaqOW_env = bytes([60, 111, 98, 102, 117, 115, 99, 97, 116, 101, 100, 62]).decode(m_p_UYaUm_lib)
q_TRXZkS_cfg = bytes([101, 120, 101, 99]).decode(m_p_UYaUm_lib)
q_dcYVChNQ_util = bytes([99, 111, 109, 112, 105, 108, 101]).decode(m_p_UYaUm_lib)
d_CcNii_ctx = sys
v_gVfwbW = time
q_mDGmBi_ctx = inspect
p_WIhILP_sec = bytes([103, 101, 116, 116, 114, 97, 99, 101]).decode(m_p_UYaUm_lib)
m_GrU_oNEY = bytes([116, 105, 109, 101]).decode(m_p_UYaUm_lib)
q_LlUFL_sys = bytes([115, 108, 101, 101, 112]).decode(m_p_UYaUm_lib)
g_Vzlgr = bytes([115, 116, 97, 99, 107]).decode(m_p_UYaUm_lib)
q_UpJXqevIK_sys = bytes([102, 105, 110, 100, 95, 109, 111, 100, 117, 108, 101]).decode(m_p_UYaUm_lib)
v_CGBptCmA = bytes([95, 95, 109, 97, 105, 110, 95, 95]).decode(m_p_UYaUm_lib)
def q_vFJDP_ctx(val, shf, dr=1):
    return ((val << shf) | (val >> (8 - shf))) & 0xFF if dr > 0 else ((val >> shf) | (val << (8 - shf))) & 0xFF
def q_oMDSVt_val():
    enc = "".join(d_pneOBagI)
    enc = z_HPjBVQhQ_val(enc, x_zkaOmhv)("-", w_HxACRVcml_sec)
    enc = z_HPjBVQhQ_val(enc, x_zkaOmhv)("_", z_dqMoyawId_lib)
    pad = len(enc) % 4
    if pad: enc += v_ddnGuRgRm * (4 - pad)
    try: return p_SktkuAI(enc.encode(m_p_UYaUm_lib))
    except: return b''
def k_ZpUzXTM(data, pk, sk, rk, sbx, iv_val):
    out = bytearray(len(data))
    prev_b = iv_val % 256
    for i in range(len(data)):
        b = data[i] ^ sk[i % len(sk)]
        b ^= prev_b
        b = q_vFJDP_ctx(b, rk[i % len(rk)], -1)
        b_before_sbox = b
        try:
            b = sbx.index(b)
        except ValueError:
            b = b_before_sbox
        b = b ^ pk[i % len(pk)]
        out[i] = b
        prev_b = data[i]
    return bytes(out)
def faNwBROHWuQN(n, m=1): return (n << m) | (n >> (8-m if n < 256 else 32-m))
def VOXYkswYba_DeLBJbX(arr): return sum(x*3+4 for i,x in enumerate(arr) if i%2==1) % 1314
def vaDHokVOxSw_wjgm(n, m=5): return (n << m) | (n >> (8-m if n < 256 else 32-m))
def YIoLH_qUnEwmO(a, b, c=17): return [(x * c ^ b) % 256 for x in a[:12]] if hasattr(a, '__len__') else [b,c]
def uXiRNZkxVhpesCZL(arr): return sum(x*2+8 for i,x in enumerate(arr) if i%2==1) % 1633
def NnCPVdXCOPaqLabJZr(data, key=None): return bytes(reversed(data)) if isinstance(data, bytes) else str(data)[::-1]
def NNwetRdFFVIfhBTDtC(n, m=3): return (n << m) | (n >> (8-m if n < 256 else 32-m))
def x_osROpIes():
    k_data = [48, 62, 9, 140, 31, 64, -8, 85, 36, -61, 25, 136, -97, -97, 66, 20, 127, -103, 42, -86, -89, 117, 102, 26, -59, 148, -96, -72, 129, 133, 75, -47, 93, -5, 111, -59, 132, -42, -26, 20, -93, -60, -80, 105, 17, 41, -1, 49, -28, 95]
    return [(x + 225 - 122) ^ 76 for x in k_data]
def v_DelGjjQ():
    s_data = [631, 568, 486, 440, 471, 423, 457, 654, 474, 575, 678, 561, 551, 450, 464, 526, 636, 438, 553, 479, 507, 431, 483, 432, 576, 609, 477, 606, 545, 577, 438, 500, 642, 479, 540, 591, 616, 584, 621, 626, 467, 665, 515, 644, 550, 628, 466, 443, 510, 500]
    return [x - 423 for x in s_data]
def p_wDYwtS_app():
    r_const = [232, 228, 228, 229, 227, 231, 229, 227, 232]
    return [val - 225 for val in r_const]
def v_zKYWBSPVY():
    p1 = [99, 189, 115, 149, 54, 87, 41, 135, 244, 63, 47, 235, 53, 103, 118, 219, 229, 76, 248, 108, 64, 181, 187, 204, 123, 200, 38, 22, 13, 0, 8, 104, 196, 62, 144, 214, 140, 152, 179, 150, 59, 16, 183, 49, 245, 242, 121, 133, 55, 86, 65, 184, 95, 145, 216, 100, 142, 34, 12, 194, 1, 234, 122, 81, 106, 9, 85, 193, 199, 11, 102, 195, 240, 131, 109, 67, 186, 224, 28, 124, 246, 220, 241, 72, 168, 201, 58, 96, 97, 251, 27, 17, 4, 253, 74, 160, 61, 128, 75, 175, 202, 197, 94, 79, 68, 247, 112, 188, 172, 73, 138, 129, 191, 171, 192, 182, 136, 230, 93, 157, 228, 31, 113, 6, 239, 110, 180, 77]
    p2 = [170, 198, 253, 241, 9, 145, 255, 116, 159, 96, 140, 15, 134, 50, 84, 31, 119, 76, 216, 126, 185, 162, 41, 129, 102, 79, 194, 247, 138, 58, 128, 55, 157, 87, 28, 254, 191, 7, 125, 176, 68, 167, 141, 190, 8, 99, 49, 57, 163, 63, 131, 136, 62, 14, 184, 78, 43, 245, 67, 133, 218, 54, 115, 249, 0, 47, 180, 29, 186, 12, 149, 107, 179, 181, 148, 20, 69, 158, 124, 244, 94, 122, 34, 213, 183, 234, 19, 64, 74, 174, 223, 246, 32, 137, 51, 81, 217, 196, 65, 210, 235, 211, 114, 227, 11, 82, 232, 127, 10, 3, 120, 207, 168, 52, 200, 98, 112, 121, 239, 175, 36, 142, 4, 38, 83, 208, 135, 153]
    return [(v ^ 225) for v in p1] + [(v ^ 76) for v in p2]
def p_sNrxQb_core():
    return 96188348 + (76 * 122) + 225
def q_GYZSX_lib():
    try:
        dbg_detected = False
        try:
            if z_HPjBVQhQ_val(d_CcNii_ctx, p_WIhILP_sec)() is not None: 
                dbg_detected = True
        except: pass
        
        excessive_time = False
        try:
            et_thresh = 10.0 + (randint(0,20) / 10.0)
            if z_HPjBVQhQ_val(v_gVfwbW, m_GrU_oNEY)() - p_LieWjUX_core > et_thresh: 
                excessive_time = True
        except: pass
        
        deep_stack = False
        try:
            sd_thresh = 50 + randint(0,20)
            if len(z_HPjBVQhQ_val(q_mDGmBi_ctx, g_Vzlgr)()) > sd_thresh: 
                deep_stack = True
        except: pass
        
        suspicious_modules = False
        try:
            vm_ind = [bytes([86,66,111,120,71]).decode(), bytes([118,109,116,111,111]).decode(), bytes([100,101,98,117,103]).decode()]
            if any(m for m in d_CcNii_ctx.modules if any(ind in m.lower() for ind in vm_ind)): 
                suspicious_modules = True
        except: pass
        
        threat_score = sum([dbg_detected, excessive_time, deep_stack, suspicious_modules])
        return threat_score < 3
    except: return True
def k_BGtH_lRr(c_bytes):
    try:
        if not c_bytes or len(c_bytes) < 2: return False
        try:
            z_HPjBVQhQ_val(m_YruPpsm, q_dcYVChNQ_util)(z_HPjBVQhQ_val(c_bytes, g_CXmzm_Sqi)(m_p_UYaUm_lib), x_yQYdaqOW_env, q_TRXZkS_cfg)
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
if __name__ == v_CGBptCmA:
    try:
        x_PBZiS_app()
    except Exception:
        try:
            if z_HPjBVQhQ_val(d_CcNii_ctx, p_WIhILP_sec)() is None:
                raise
        except: pass
