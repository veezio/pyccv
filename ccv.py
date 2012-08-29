import platform
from ctypes import *

def _get_system_extension():
    extensions = {
        "Windows": "dll",
        "Linux": "so.0",
        "Darwin": "dylib",
    }
    import platform
    return extensions[platform.system()]


_libraries = {}
_libraries['libccv'] = CDLL('libccv.%s' % _get_system_extension())
STRING = c_char_p
WSTRING = c_wchar_p


_CS_POSIX_V7_LPBIG_OFFBIG_LINTFLAGS = 1147
_CS_POSIX_V7_LPBIG_OFFBIG_LDFLAGS = 1145
_CS_POSIX_V7_LPBIG_OFFBIG_CFLAGS = 1144
_SC_2_C_DEV = 48
_CS_POSIX_V7_LP64_OFF64_LIBS = 1142
_CS_POSIX_V7_LP64_OFF64_CFLAGS = 1140
_CS_POSIX_V7_ILP32_OFFBIG_LINTFLAGS = 1139
_CS_POSIX_V7_ILP32_OFFBIG_LDFLAGS = 1137
_CS_POSIX_V7_ILP32_OFFBIG_CFLAGS = 1136
_CS_POSIX_V7_ILP32_OFF32_LINTFLAGS = 1135
_CS_POSIX_V7_ILP32_OFF32_LDFLAGS = 1133
_SC_XOPEN_REALTIME = 130
_CS_POSIX_V7_ILP32_OFF32_CFLAGS = 1132
_CS_POSIX_V6_LPBIG_OFFBIG_LINTFLAGS = 1131
_CS_POSIX_V6_LPBIG_OFFBIG_LIBS = 1130
_CS_POSIX_V6_LPBIG_OFFBIG_LDFLAGS = 1129
_CS_POSIX_V6_LPBIG_OFFBIG_CFLAGS = 1128
_CS_POSIX_V6_LP64_OFF64_LIBS = 1126
_CS_POSIX_V6_LP64_OFF64_CFLAGS = 1124
_CS_POSIX_V6_ILP32_OFFBIG_LINTFLAGS = 1123
_CS_POSIX_V6_ILP32_OFFBIG_LIBS = 1122
_CS_POSIX_V6_ILP32_OFFBIG_LDFLAGS = 1121
_SC_XBS5_LPBIG_OFFBIG = 128
_CS_POSIX_V6_ILP32_OFF32_LINTFLAGS = 1119
_CS_POSIX_V6_ILP32_OFF32_LIBS = 1118
_CS_POSIX_V6_ILP32_OFF32_CFLAGS = 1116
_CS_XBS5_LPBIG_OFFBIG_LINTFLAGS = 1115
_SC_XBS5_LP64_OFF64 = 127
_CS_XBS5_LPBIG_OFFBIG_LDFLAGS = 1113
_CS_POSIX_V7_LPBIG_OFFBIG_LIBS = 1146
_CS_XBS5_LP64_OFF64_LIBS = 1110
_CS_XBS5_LP64_OFF64_LDFLAGS = 1109
_SC_XBS5_ILP32_OFFBIG = 126
_CS_XBS5_LP64_OFF64_CFLAGS = 1108
_CS_XBS5_ILP32_OFFBIG_LINTFLAGS = 1107
_CS_XBS5_ILP32_OFFBIG_LIBS = 1106
_CS_XBS5_ILP32_OFFBIG_LDFLAGS = 1105
_CS_XBS5_ILP32_OFFBIG_CFLAGS = 1104
_CS_XBS5_ILP32_OFF32_LINTFLAGS = 1103
_SC_XBS5_ILP32_OFF32 = 125
_CS_XBS5_ILP32_OFF32_LDFLAGS = 1101
_CS_XBS5_ILP32_OFF32_CFLAGS = 1100
_CS_LFS64_LINTFLAGS = 1007
_CS_LFS64_LIBS = 1006
_CS_LFS64_LDFLAGS = 1005
_CS_LFS64_CFLAGS = 1004
_CS_LFS_LINTFLAGS = 1003
_CS_POSIX_V7_LP64_OFF64_LINTFLAGS = 1143
_CS_LFS_LIBS = 1002
_CS_LFS_LDFLAGS = 1001
_CS_V7_WIDTH_RESTRICTED_ENVS = 5
_SC_NL_SETMAX = 123
_CS_V5_WIDTH_RESTRICTED_ENVS = 4
_SC_NL_NMAX = 122
_CS_POSIX_V7_LP64_OFF64_LDFLAGS = 1141
_SC_2_VERSION = 46
_SC_NL_MSGMAX = 121
CCV_MATRIX_CSC = 524288
_SC_NL_ARGMAX = 119
_CS_POSIX_V7_ILP32_OFFBIG_LIBS = 1138
CCV_MATRIX_SPARSE = 131072
_SC_ULONG_MAX = 117
CCV_MATRIX_DENSE = 65536
_SC_SELECT = 59
_CS_POSIX_V7_ILP32_OFF32_LIBS = 1134
_SC_SHRT_MAX = 113
_SC_SCHAR_MIN = 112
_SC_RE_DUP_MAX = 44
_CS_GNU_LIBC_VERSION = 2
_SC_SCHAR_MAX = 111
_SC_MB_LEN_MAX = 108
_CS_POSIX_V6_LP64_OFF64_LINTFLAGS = 1127
_CS_V6_WIDTH_RESTRICTED_ENVS = 1
_CS_POSIX_V6_LP64_OFF64_LDFLAGS = 1125
_SC_INT_MIN = 105
_CS_GNU_LIBPTHREAD_VERSION = 3
_SC_INT_MAX = 104
_CS_PATH = 0
_CS_POSIX_V6_ILP32_OFFBIG_CFLAGS = 1120
_SC_2_PBS_CHECKPOINT = 175
_CS_POSIX_V6_ILP32_OFF32_LDFLAGS = 1117
_CS_XBS5_LPBIG_OFFBIG_LIBS = 1114
_CS_XBS5_LPBIG_OFFBIG_CFLAGS = 1112
_CS_XBS5_LP64_OFF64_LINTFLAGS = 1111
_PC_2_SYMLINKS = 20
_SC_XOPEN_STREAMS = 246
_SC_TRACE_USER_EVENT_MAX = 245
_SC_TRACE_NAME_MAX = 243
_SC_XOPEN_XCU_VERSION = 90
_SC_TRACE_EVENT_NAME_MAX = 242
_SC_V7_LPBIG_OFFBIG = 240
_SC_LEVEL3_CACHE_LINESIZE = 196
_SC_PASS_MAX = 88
_SC_LEVEL3_CACHE_ASSOC = 195
_SC_LEVEL1_DCACHE_LINESIZE = 190
_SC_LEVEL1_DCACHE_SIZE = 188
_SC_LEVEL1_ICACHE_LINESIZE = 187
_SC_TRACE_LOG = 184
_SC_AVPHYS_PAGES = 86
_SC_TRACE_INHERIT = 183
_SC_2_PBS_TRACK = 172
_SC_TRACE = 181
_SC_HOST_NAME_MAX = 180
_SC_V6_LPBIG_OFFBIG = 179
_SC_V6_LP64_OFF64 = 178
_SC_PHYS_PAGES = 85
_SC_V6_ILP32_OFFBIG = 177
_SC_V6_ILP32_OFF32 = 176
_SC_SYMLOOP_MAX = 173
_CS_XBS5_ILP32_OFF32_LIBS = 1102
_SC_2_PBS_ACCOUNTING = 169
_SC_USER_GROUPS_R = 167
_SC_USER_GROUPS = 166
_SC_NPROCESSORS_CONF = 83
_SC_TYPED_MEMORY_OBJECTS = 165
_SC_SYSTEM_DATABASE_R = 163
_SC_THREAD_SPORADIC_SERVER = 161
_PC_ALLOC_SIZE_MIN = 18
_SC_THREAD_PROCESS_SHARED = 82
_SC_SIGNALS = 158
_SC_SHELL = 157
_SC_SPIN_LOCKS = 154
_SC_READER_WRITER_LOCKS = 153
_SC_2_PBS_MESSAGE = 171
_SC_NETWORKING = 152
_SC_SINGLE_PROCESS = 151
_SC_MULTI_PROCESS = 150
_SC_MONOTONIC_CLOCK = 149
_SC_THREAD_PRIO_INHERIT = 80
_SC_FILE_LOCKING = 147
_SC_FILE_ATTRIBUTES = 146
_SC_FIFO = 144
_SC_DEVICE_SPECIFIC = 141
_SC_THREAD_CPUTIME = 139
_SC_CPUTIME = 138
_SC_CLOCK_SELECTION = 137
_SC_THREAD_ATTR_STACKSIZE = 78
_SC_C_LANG_SUPPORT_R = 136
_SC_BASE = 134
_SC_ADVISORY_INFO = 132
_PC_REC_XFER_ALIGN = 17
_SC_XOPEN_REALTIME_THREADS = 131
_SC_THREAD_ATTR_STACKADDR = 77
_SC_XOPEN_LEGACY = 129
_SC_THREAD_THREADS_MAX = 76
_SC_NL_TEXTMAX = 124
_SC_2_PBS_LOCATE = 170
_SC_NL_LANGMAX = 120
_SC_USHRT_MAX = 118
_SC_UINT_MAX = 116
_SC_UCHAR_MAX = 115
_SC_SHRT_MIN = 114
_CS_LFS_CFLAGS = 1000
_SC_SSIZE_MAX = 110
_SC_NZERO = 109
_SC_WORD_BIT = 107
_SC_LONG_BIT = 106
_SC_CHAR_MIN = 103
_SC_CHAR_MAX = 102
_SC_CHAR_BIT = 101
_SC_XOPEN_XPG4 = 100
_SC_XOPEN_XPG3 = 99
_SC_XOPEN_XPG2 = 98
_SC_2_UPE = 97
_SC_2_C_VERSION = 96
_SC_2_CHAR_TERM = 95
_SC_XOPEN_SHM = 94
_SC_XOPEN_ENH_I18N = 93
_SC_XOPEN_CRYPT = 92
_SC_XOPEN_UNIX = 91
_SC_ATEXIT_MAX = 87
_SC_NPROCESSORS_ONLN = 84
_SC_GETGR_R_SIZE_MAX = 69
_SC_THREAD_PRIO_PROTECT = 81
_SC_THREAD_PRIORITY_SCHEDULING = 79
_SC_THREAD_STACK_MIN = 75
_SC_THREAD_KEYS_MAX = 74
_SC_THREAD_DESTRUCTOR_ITERATIONS = 73
_SC_TTY_NAME_MAX = 72
_SC_LOGIN_NAME_MAX = 71
_SC_GETPW_R_SIZE_MAX = 70
_SC_THREAD_SAFE_FUNCTIONS = 68
_SC_THREADS = 67
_SC_T_IOV_MAX = 66
_SC_PII_OSI_M = 65
_SC_PII_OSI_CLTS = 64
_SC_2_PBS = 168
_SC_PII_INTERNET_DGRAM = 62
_SC_PII_INTERNET_STREAM = 61
_SC_UIO_MAXIOV = 60
_SC_PII_OSI = 57
_SC_PII_INTERNET = 56
_SC_PII_SOCKET = 55
_SC_PII = 53
_SC_2_FORT_DEV = 49
_SC_PII_OSI_COTS = 63
_PC_REC_INCR_XFER_SIZE = 14
_SC_LINE_MAX = 43
_SC_EXPR_NEST_MAX = 42
_SC_EQUIV_CLASS_MAX = 41
_SC_COLL_WEIGHTS_MAX = 40
_SC_BC_STRING_MAX = 39
_XOPEN_ = 1
_SC_BC_SCALE_MAX = 38
_SC_BC_DIM_MAX = 37
_SC_BC_BASE_MAX = 36
_SC_TIMER_MAX = 35
_SC_SIGQUEUE_MAX = 34
_SC_SEM_VALUE_MAX = 33
_SVID_ = 0
_SC_SEM_NSEMS_MAX = 32
_SC_RTSIG_MAX = 31
CCV_NO_PADDING = 0
_SC_IOV_MAX = 60
_SC_PAGESIZE = 30
_PC_FILESIZEBITS = 13
_SC_POLL = 58
_SC_PII_XTI = 54
_SC_2_LOCALEDEF = 52
_SC_2_SW_DEV = 51
_SC_2_FORT_RUN = 50
_PC_PRIO_IO = 11
_SC_2_C_BIND = 47
_SC_AIO_LISTIO_MAX = 23
CCV_INTER_LINEAR = 2
_SC_CHARCLASS_NAME_MAX = 45
_SC_SHARED_MEMORY_OBJECTS = 22
_SC_VERSION = 29
_SC_MQ_PRIO_MAX = 28
_SC_MQ_OPEN_MAX = 27
_SC_DELAYTIMER_MAX = 26
_SC_SEMAPHORES = 21
_PC_REC_MIN_XFER_SIZE = 16
_PC_REC_MAX_XFER_SIZE = 15
_PC_SOCK_MAXBUF = 12
_SC_FSYNC = 15
_PC_ASYNC_IO = 10
_SC_PRIORITIZED_IO = 13
_SC_ASYNCHRONOUS_IO = 12
_PC_PIPE_BUF = 5
_PC_NAME_MAX = 3
_PC_MAX_CANON = 1
_SC_CLK_TCK = 2
_SC_CHILD_MAX = 1
_SC_MESSAGE_PASSING = 20
_SC_MEMORY_PROTECTION = 19
_PC_CHOWN_RESTRICTED = 6
_SC_SPAWN = 159
_SC_MEMLOCK_RANGE = 18
CCV_MATRIX_CSR = 262144
_PC_PATH_MAX = 4
_ISOC_ = 3
_IEEE_ = -1
CCV_DAISY_NORMAL_PARTIAL = 1
_SC_REGEXP = 155
_PC_NO_TRUNC = 7
CCV_DAISY_NORMAL_FULL = 2
CCV_FLIP_Y = 2
CCV_FLIP_X = 1
CCV_INTER_LANCZOS = 4
CCV_INTER_CUBIC = 3
_PC_LINK_MAX = 0
CCV_INTER_AREA = 1
CCV_C_TRANSPOSE = 4
CCV_UNSIGNED = 1
CCV_PADDING_EXTEND = 2
CCV_PADDING_ZERO = 1
__codecvt_noconv = 3
__codecvt_partial = 1
__codecvt_ok = 0
CCV_POSITIVE = 0
CCV_NEGATIVE = 8
CCV_GSEDT = 4
CCV_L1_NORM = 2
CCV_L2_NORM = 1
CCV_IO_ATTEMPTED = 3
CCV_IO_ERROR = 2
CCV_IO_CONTINUE = 1
CCV_IO_FINAL = 0
CCV_IO_BINARY_FILE = 36
CCV_IO_PNG_FILE = 35
CCV_IO_JPEG_FILE = 34
CCV_IO_BMP_FILE = 33
CCV_IO_ANY_FILE = 32
CCV_IO_JPEG_STREAM = 19
CCV_IO_DEFLATE_STREAM = 18
CCV_IO_ANY_STREAM = 16
CCV_IO_GRAY = 256
CCV_SPARSE_COL_MAJOR = 1
CCV_SPARSE_ROW_MAJOR = 0
CCV_UNMANAGED = 536870912
CCV_REUSABLE = 1073741824
CCV_GARBAGE = -2147483648
CCV_64F = 4096
CCV_B_TRANSPOSE = 2
_SC_STREAM_MAX = 5
CCV_SIGNED = 0
CCV_DPM_NO_NESTED = 268435456
_SC_THREAD_ROBUST_PRIO_PROTECT = 248
_SC_OPEN_MAX = 4
_SC_THREAD_ROBUST_PRIO_INHERIT = 247
_SC_NGROUPS_MAX = 3
__codecvt_error = 2
CCV_DAISY_NORMAL_SIFT = 3
_SC_LEVEL4_CACHE_ASSOC = 198
_SC_SS_REPL_MAX = 241
_MM_HINT_NTA = 0
_SC_V7_LP64_OFF64 = 239
CCV_IO_PNG_STREAM = 20
_MM_HINT_T2 = 1
CCV_IO_PLAIN_STREAM = 17
CCV_IO_COLOR = 768
_SC_AIO_PRIO_DELTA_MAX = 25
_MM_HINT_T1 = 2
_SC_AIO_MAX = 24
_MM_HINT_T0 = 3
_PC_SYMLINK_MAX = 19
_SC_LEVEL4_CACHE_SIZE = 197
_SC_RAW_SOCKETS = 236
_SC_MEMLOCK = 17
_SC_MAPPED_FILES = 16
_SC_BARRIERS = 133
_SC_SYNCHRONIZED_IO = 14
_PC_SYNC_IO = 9
_PC_VDISABLE = 8
_SC_TIMERS = 11
_SC_PRIORITY_SCHEDULING = 10
_SC_REALTIME_SIGNALS = 9
_SC_SAVED_IDS = 8
_SC_JOB_CONTROL = 7
_POSIX_ = 2
_SC_TZNAME_MAX = 6
CCV_A_TRANSPOSE = 1
_PC_MAX_INPUT = 2
CCV_C4 = 4
_SC_ARG_MAX = 0
_SC_TRACE_SYS_MAX = 244
CCV_DENSE_VECTOR = 2097152
FP_SUBNORMAL = 3
CCV_SPARSE_VECTOR = 1048576
_SC_XOPEN_VERSION = 89
CCV_64S = 2048
CCV_32F = 1024
CCV_32S = 512
CCV_8U = 256
CCV_C3 = 3
_SC_V7_ILP32_OFFBIG = 238
_SC_V7_ILP32_OFF32 = 237
FP_NORMAL = 4
FP_ZERO = 2
FP_INFINITE = 1
FP_NAN = 0
CCV_C2 = 2
_SC_IPV6 = 235
_SC_LEVEL4_CACHE_LINESIZE = 199
CCV_C1 = 1
_SC_LEVEL2_CACHE_LINESIZE = 193
_SC_LEVEL2_CACHE_SIZE = 191
_SC_LEVEL2_CACHE_ASSOC = 192
CCV_BBF_NO_NESTED = 268435456
CCV_BBF_FLOAT_OPT = 2
CCV_BBF_GENETIC_OPT = 1
_SC_STREAMS = 174
_SC_LEVEL1_DCACHE_ASSOC = 189
_SC_TIMEOUTS = 164
_SC_SYSTEM_DATABASE = 162
_SC_SPORADIC_SERVER = 160
_SC_REGEX_VERSION = 156
_SC_LEVEL3_CACHE_SIZE = 194
_SC_LEVEL1_ICACHE_ASSOC = 186
_SC_FILE_SYSTEM = 148
_SC_PIPE = 145
_SC_FD_MGMT = 143
_SC_DEVICE_SPECIFIC_R = 142
_SC_LEVEL1_ICACHE_SIZE = 185
_SC_DEVICE_IO = 140
_SC_C_LANG_SUPPORT = 135
_SC_TRACE_EVENT_FILTER = 182
CCV_PADDING_MIRROR = 4

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration
class ccv_matrix_cell_t(Union):
    pass
int64_t = c_int64
ccv_matrix_cell_t._fields_ = [
    ('u8', POINTER(c_ubyte)),
    ('i32', POINTER(c_int)),
    ('f32', POINTER(c_float)),
    ('i64', POINTER(int64_t)),
    ('f64', POINTER(c_double)),
]
class N18ccv_dense_matrix_t4DOT_36E(Union):
    pass
N18ccv_dense_matrix_t4DOT_36E._fields_ = [
    ('u8', c_ubyte),
    ('i32', c_int),
    ('f32', c_float),
    ('i64', int64_t),
    ('f64', c_double),
    ('p', c_void_p),
]
class ccv_dense_matrix_t(Structure):
    pass
uint64_t = c_uint64
ccv_dense_matrix_t._fields_ = [
    ('type', c_int),
    ('sig', uint64_t),
    ('refcount', c_int),
    ('rows', c_int),
    ('cols', c_int),
    ('step', c_int),
    ('tag', N18ccv_dense_matrix_t4DOT_36E),
    ('data', ccv_matrix_cell_t),
]

# values for unnamed enumeration
class ccv_dense_vector_t(Structure):
    pass
ccv_dense_vector_t._fields_ = [
    ('step', c_int),
    ('length', c_int),
    ('index', c_int),
    ('prime', c_int),
    ('load_factor', c_int),
    ('data', ccv_matrix_cell_t),
    ('indice', POINTER(c_int)),
    ('next', POINTER(ccv_dense_vector_t)),
]

# values for unnamed enumeration
class N19ccv_sparse_matrix_t4DOT_40E(Union):
    pass
N19ccv_sparse_matrix_t4DOT_40E._fields_ = [
    ('chr', c_ubyte),
    ('i', c_int),
    ('fl', c_float),
    ('l', int64_t),
    ('db', c_double),
]
class ccv_sparse_matrix_t(Structure):
    pass
ccv_sparse_matrix_t._fields_ = [
    ('type', c_int),
    ('sig', uint64_t),
    ('refcount', c_int),
    ('rows', c_int),
    ('cols', c_int),
    ('major', c_int),
    ('prime', c_int),
    ('load_factor', c_int),
    ('tag', N19ccv_sparse_matrix_t4DOT_40E),
    ('vector', POINTER(ccv_dense_vector_t)),
]
_ccv_get_sparse_prime = (c_int * 0).in_dll(_libraries['libccv'], '_ccv_get_sparse_prime')
ccv_matrix_t = None
ccv_cache_index_free_f = CFUNCTYPE(None, c_void_p)
class N17ccv_cache_index_t4DOT_42E(Structure):
    pass
N17ccv_cache_index_t4DOT_42E._fields_ = [
    ('bitmap', uint64_t),
    ('set', uint64_t),
    ('age', uint64_t),
]
class N17ccv_cache_index_t4DOT_43E(Structure):
    pass
N17ccv_cache_index_t4DOT_43E._fields_ = [
    ('sign', uint64_t),
    ('off', uint64_t),
    ('type', uint64_t),
]
class ccv_cache_index_t(Union):
    pass
ccv_cache_index_t._fields_ = [
    ('branch', N17ccv_cache_index_t4DOT_42E),
    ('terminal', N17ccv_cache_index_t4DOT_43E),
]
class ccv_cache_t(Structure):
    pass
uint32_t = c_uint32
size_t = c_ulong
ccv_cache_t._fields_ = [
    ('origin', ccv_cache_index_t),
    ('rnum', uint32_t),
    ('age', uint32_t),
    ('up', size_t),
    ('size', size_t),
    ('ffree', ccv_cache_index_free_f * 16),
]
ccv_cache_init = _libraries['libccv'].ccv_cache_init
ccv_cache_init.restype = None
ccv_cache_init.argtypes = [POINTER(ccv_cache_t), size_t, c_int, ccv_cache_index_free_f]
uint8_t = c_uint8
ccv_cache_get = _libraries['libccv'].ccv_cache_get
ccv_cache_get.restype = c_void_p
ccv_cache_get.argtypes = [POINTER(ccv_cache_t), uint64_t, POINTER(uint8_t)]
ccv_cache_put = _libraries['libccv'].ccv_cache_put
ccv_cache_put.restype = c_int
ccv_cache_put.argtypes = [POINTER(ccv_cache_t), uint64_t, c_void_p, uint32_t, uint8_t]
ccv_cache_out = _libraries['libccv'].ccv_cache_out
ccv_cache_out.restype = c_void_p
ccv_cache_out.argtypes = [POINTER(ccv_cache_t), uint64_t, POINTER(uint8_t)]
ccv_cache_delete = _libraries['libccv'].ccv_cache_delete
ccv_cache_delete.restype = c_int
ccv_cache_delete.argtypes = [POINTER(ccv_cache_t), uint64_t]
ccv_cache_cleanup = _libraries['libccv'].ccv_cache_cleanup
ccv_cache_cleanup.restype = None
ccv_cache_cleanup.argtypes = [POINTER(ccv_cache_t)]
ccv_cache_close = _libraries['libccv'].ccv_cache_close
ccv_cache_close.restype = None
ccv_cache_close.argtypes = [POINTER(ccv_cache_t)]
class N30ccv_compressed_sparse_matrix_t4DOT_46E(Union):
    pass
N30ccv_compressed_sparse_matrix_t4DOT_46E._fields_ = [
    ('chr', c_ubyte),
    ('i', c_int),
    ('fl', c_float),
    ('l', int64_t),
    ('db', c_double),
]
class ccv_compressed_sparse_matrix_t(Structure):
    pass
ccv_compressed_sparse_matrix_t._fields_ = [
    ('type', c_int),
    ('sig', uint64_t),
    ('refcount', c_int),
    ('rows', c_int),
    ('cols', c_int),
    ('nnz', c_int),
    ('tag', N30ccv_compressed_sparse_matrix_t4DOT_46E),
    ('index', POINTER(c_int)),
    ('offset', POINTER(c_int)),
    ('data', ccv_matrix_cell_t),
]
ccv_dense_matrix_renew = _libraries['libccv'].ccv_dense_matrix_renew
ccv_dense_matrix_renew.restype = POINTER(ccv_dense_matrix_t)
ccv_dense_matrix_renew.argtypes = [POINTER(ccv_dense_matrix_t), c_int, c_int, c_int, c_int, uint64_t]
ccv_dense_matrix_new = _libraries['libccv'].ccv_dense_matrix_new
ccv_dense_matrix_new.restype = POINTER(ccv_dense_matrix_t)
ccv_dense_matrix_new.argtypes = [c_int, c_int, c_int, c_void_p, uint64_t]
ccv_dense_matrix = _libraries['libccv'].ccv_dense_matrix
ccv_dense_matrix.restype = ccv_dense_matrix_t
ccv_dense_matrix.argtypes = [c_int, c_int, c_int, c_void_p, uint64_t]
ccv_make_matrix_mutable = _libraries['libccv'].ccv_make_matrix_mutable
ccv_make_matrix_mutable.restype = None
ccv_make_matrix_mutable.argtypes = [POINTER(ccv_matrix_t)]
ccv_make_matrix_immutable = _libraries['libccv'].ccv_make_matrix_immutable
ccv_make_matrix_immutable.restype = None
ccv_make_matrix_immutable.argtypes = [POINTER(ccv_matrix_t)]
ccv_sparse_matrix_new = _libraries['libccv'].ccv_sparse_matrix_new
ccv_sparse_matrix_new.restype = POINTER(ccv_sparse_matrix_t)
ccv_sparse_matrix_new.argtypes = [c_int, c_int, c_int, c_int, uint64_t]
ccv_matrix_free_immediately = _libraries['libccv'].ccv_matrix_free_immediately
ccv_matrix_free_immediately.restype = None
ccv_matrix_free_immediately.argtypes = [POINTER(ccv_matrix_t)]
ccv_matrix_free = _libraries['libccv'].ccv_matrix_free
ccv_matrix_free.restype = None
ccv_matrix_free.argtypes = [POINTER(ccv_matrix_t)]
ccv_cache_generate_signature = _libraries['libccv'].ccv_cache_generate_signature
ccv_cache_generate_signature.restype = uint64_t
ccv_cache_generate_signature.argtypes = [STRING, c_int, uint64_t]
ccv_drain_cache = _libraries['libccv'].ccv_drain_cache
ccv_drain_cache.restype = None
ccv_drain_cache.argtypes = []
ccv_disable_cache = _libraries['libccv'].ccv_disable_cache
ccv_disable_cache.restype = None
ccv_disable_cache.argtypes = []
ccv_enable_default_cache = _libraries['libccv'].ccv_enable_default_cache
ccv_enable_default_cache.restype = None
ccv_enable_default_cache.argtypes = []
ccv_enable_cache = _libraries['libccv'].ccv_enable_cache
ccv_enable_cache.restype = None
ccv_enable_cache.argtypes = [size_t]

# values for unnamed enumeration

# values for unnamed enumeration
#ccv_read = _libraries['libccv'].ccv_read
#ccv_read.restype = c_int
#ccv_read.argtypes = [STRING, POINTER(POINTER(ccv_dense_matrix_t)), c_int]
ccv_write = _libraries['libccv'].ccv_write
ccv_write.restype = c_int
ccv_write.argtypes = [POINTER(ccv_dense_matrix_t), STRING, POINTER(c_int), c_int, c_void_p]
ccv_trace = _libraries['libccv'].ccv_trace
ccv_trace.restype = c_double
ccv_trace.argtypes = [POINTER(ccv_matrix_t)]

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration
ccv_norm = _libraries['libccv'].ccv_norm
ccv_norm.restype = c_double
ccv_norm.argtypes = [POINTER(ccv_matrix_t), c_int]
ccv_normalize = _libraries['libccv'].ccv_normalize
ccv_normalize.restype = c_double
ccv_normalize.argtypes = [POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int, c_int]
ccv_sat = _libraries['libccv'].ccv_sat
ccv_sat.restype = None
ccv_sat.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int]
ccv_sum = _libraries['libccv'].ccv_sum
ccv_sum.restype = c_double
ccv_sum.argtypes = [POINTER(ccv_matrix_t), c_int]
ccv_multiply = _libraries['libccv'].ccv_multiply
ccv_multiply.restype = None
ccv_multiply.argtypes = [POINTER(ccv_matrix_t), POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int]
ccv_subtract = _libraries['libccv'].ccv_subtract
ccv_subtract.restype = None
ccv_subtract.argtypes = [POINTER(ccv_matrix_t), POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int]

# values for unnamed enumeration
ccv_gemm = _libraries['libccv'].ccv_gemm
ccv_gemm.restype = None
ccv_gemm.argtypes = [POINTER(ccv_matrix_t), POINTER(ccv_matrix_t), c_double, POINTER(ccv_matrix_t), c_double, c_int, POINTER(POINTER(ccv_matrix_t)), c_int]
ccv_get_dense_matrix = _libraries['libccv'].ccv_get_dense_matrix
ccv_get_dense_matrix.restype = POINTER(ccv_dense_matrix_t)
ccv_get_dense_matrix.argtypes = [POINTER(ccv_matrix_t)]
ccv_get_sparse_matrix = _libraries['libccv'].ccv_get_sparse_matrix
ccv_get_sparse_matrix.restype = POINTER(ccv_sparse_matrix_t)
ccv_get_sparse_matrix.argtypes = [POINTER(ccv_matrix_t)]
ccv_get_sparse_matrix_vector = _libraries['libccv'].ccv_get_sparse_matrix_vector
ccv_get_sparse_matrix_vector.restype = POINTER(ccv_dense_vector_t)
ccv_get_sparse_matrix_vector.argtypes = [POINTER(ccv_sparse_matrix_t), c_int]
ccv_get_sparse_matrix_cell = _libraries['libccv'].ccv_get_sparse_matrix_cell
ccv_get_sparse_matrix_cell.restype = ccv_matrix_cell_t
ccv_get_sparse_matrix_cell.argtypes = [POINTER(ccv_sparse_matrix_t), c_int, c_int]
ccv_set_sparse_matrix_cell = _libraries['libccv'].ccv_set_sparse_matrix_cell
ccv_set_sparse_matrix_cell.restype = None
ccv_set_sparse_matrix_cell.argtypes = [POINTER(ccv_sparse_matrix_t), c_int, c_int, c_void_p]
ccv_compress_sparse_matrix = _libraries['libccv'].ccv_compress_sparse_matrix
ccv_compress_sparse_matrix.restype = None
ccv_compress_sparse_matrix.argtypes = [POINTER(ccv_sparse_matrix_t), POINTER(POINTER(ccv_compressed_sparse_matrix_t))]
ccv_decompress_sparse_matrix = _libraries['libccv'].ccv_decompress_sparse_matrix
ccv_decompress_sparse_matrix.restype = None
ccv_decompress_sparse_matrix.argtypes = [POINTER(ccv_compressed_sparse_matrix_t), POINTER(POINTER(ccv_sparse_matrix_t))]
ccv_move = _libraries['libccv'].ccv_move
ccv_move.restype = None
ccv_move.argtypes = [POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int, c_int, c_int]
ccv_matrix_eq = _libraries['libccv'].ccv_matrix_eq
ccv_matrix_eq.restype = c_int
ccv_matrix_eq.argtypes = [POINTER(ccv_matrix_t), POINTER(ccv_matrix_t)]
ccv_slice = _libraries['libccv'].ccv_slice
ccv_slice.restype = None
ccv_slice.argtypes = [POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int, c_int, c_int, c_int, c_int]
ccv_visualize = _libraries['libccv'].ccv_visualize
ccv_visualize.restype = None
ccv_visualize.argtypes = [POINTER(ccv_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int]
ccv_flatten = _libraries['libccv'].ccv_flatten
ccv_flatten.restype = None
ccv_flatten.argtypes = [POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int, c_int]
ccv_zero = _libraries['libccv'].ccv_zero
ccv_zero.restype = None
ccv_zero.argtypes = [POINTER(ccv_matrix_t)]
ccv_shift = _libraries['libccv'].ccv_shift
ccv_shift.restype = None
ccv_shift.argtypes = [POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int, c_int, c_int]
ccv_any_nan = _libraries['libccv'].ccv_any_nan
ccv_any_nan.restype = c_int
ccv_any_nan.argtypes = [POINTER(ccv_matrix_t)]
class ccv_size_t(Structure):
    pass
ccv_size_t._fields_ = [
    ('width', c_int),
    ('height', c_int),
]
class ccv_rect_t(Structure):
    pass
ccv_rect_t._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
]
class ccv_array_t(Structure):
    pass
ccv_array_t._fields_ = [
    ('type', c_int),
    ('sig', uint64_t),
    ('refcount', c_int),
    ('rnum', c_int),
    ('size', c_int),
    ('rsize', c_int),
    ('data', c_void_p),
]
ccv_array_new = _libraries['libccv'].ccv_array_new
ccv_array_new.restype = POINTER(ccv_array_t)
ccv_array_new.argtypes = [c_int, c_int, uint64_t]
ccv_array_push = _libraries['libccv'].ccv_array_push
ccv_array_push.restype = None
ccv_array_push.argtypes = [POINTER(ccv_array_t), c_void_p]
ccv_array_group_f = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
ccv_array_group = _libraries['libccv'].ccv_array_group
ccv_array_group.restype = c_int
ccv_array_group.argtypes = [POINTER(ccv_array_t), POINTER(POINTER(ccv_array_t)), ccv_array_group_f, c_void_p]
ccv_make_array_immutable = _libraries['libccv'].ccv_make_array_immutable
ccv_make_array_immutable.restype = None
ccv_make_array_immutable.argtypes = [POINTER(ccv_array_t)]
ccv_make_array_mutable = _libraries['libccv'].ccv_make_array_mutable
ccv_make_array_mutable.restype = None
ccv_make_array_mutable.argtypes = [POINTER(ccv_array_t)]
ccv_array_zero = _libraries['libccv'].ccv_array_zero
ccv_array_zero.restype = None
ccv_array_zero.argtypes = [POINTER(ccv_array_t)]
ccv_array_clear = _libraries['libccv'].ccv_array_clear
ccv_array_clear.restype = None
ccv_array_clear.argtypes = [POINTER(ccv_array_t)]
ccv_array_free_immediately = _libraries['libccv'].ccv_array_free_immediately
ccv_array_free_immediately.restype = None
ccv_array_free_immediately.argtypes = [POINTER(ccv_array_t)]
ccv_array_free = _libraries['libccv'].ccv_array_free
ccv_array_free.restype = None
ccv_array_free.argtypes = [POINTER(ccv_array_t)]
class ccv_point_t(Structure):
    pass
ccv_point_t._fields_ = [
    ('x', c_int),
    ('y', c_int),
]
class ccv_contour_t(Structure):
    pass
ccv_contour_t._fields_ = [
    ('rect', ccv_rect_t),
    ('size', c_int),
    ('set', POINTER(ccv_array_t)),
    ('m10', c_long),
    ('m01', c_long),
    ('m11', c_long),
    ('m20', c_long),
    ('m02', c_long),
]
ccv_contour_new = _libraries['libccv'].ccv_contour_new
ccv_contour_new.restype = POINTER(ccv_contour_t)
ccv_contour_new.argtypes = [c_int]
ccv_contour_push = _libraries['libccv'].ccv_contour_push
ccv_contour_push.restype = None
ccv_contour_push.argtypes = [POINTER(ccv_contour_t), ccv_point_t]
ccv_contour_free = _libraries['libccv'].ccv_contour_free
ccv_contour_free.restype = None
ccv_contour_free.argtypes = [POINTER(ccv_contour_t)]
ccv_invert = _libraries['libccv'].ccv_invert
ccv_invert.restype = None
ccv_invert.argtypes = [POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int]
ccv_solve = _libraries['libccv'].ccv_solve
ccv_solve.restype = None
ccv_solve.argtypes = [POINTER(ccv_matrix_t), POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int]
ccv_eigen = _libraries['libccv'].ccv_eigen
ccv_eigen.restype = None
ccv_eigen.argtypes = [POINTER(ccv_matrix_t), POINTER(ccv_matrix_t), POINTER(POINTER(ccv_matrix_t)), c_int]
class ccv_minimize_param_t(Structure):
    pass
ccv_minimize_param_t._fields_ = [
    ('interp', c_double),
    ('extrap', c_double),
    ('max_iter', c_int),
    ('ratio', c_double),
    ('rho', c_double),
    ('sig', c_double),
]
ccv_minimize_f = CFUNCTYPE(c_int, POINTER(ccv_dense_matrix_t), POINTER(c_double), POINTER(ccv_dense_matrix_t), c_void_p)
ccv_minimize = _libraries['libccv'].ccv_minimize
ccv_minimize.restype = None
ccv_minimize.argtypes = [POINTER(ccv_dense_matrix_t), c_int, c_double, ccv_minimize_f, ccv_minimize_param_t, c_void_p]
ccv_filter = _libraries['libccv'].ccv_filter
ccv_filter.restype = None
ccv_filter.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int]
ccv_filter_kernel_f = CFUNCTYPE(c_double, c_double, c_double, c_void_p)
ccv_filter_kernel = _libraries['libccv'].ccv_filter_kernel
ccv_filter_kernel.restype = None
ccv_filter_kernel.argtypes = [POINTER(ccv_dense_matrix_t), ccv_filter_kernel_f, c_void_p]
ccv_distance_transform = _libraries['libccv'].ccv_distance_transform
ccv_distance_transform.restype = None
ccv_distance_transform.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, POINTER(POINTER(ccv_dense_matrix_t)), c_int, POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_double, c_double, c_double, c_double, c_int]
ccv_sobel = _libraries['libccv'].ccv_sobel
ccv_sobel.restype = None
ccv_sobel.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int, c_int]
ccv_gradient = _libraries['libccv'].ccv_gradient
ccv_gradient.restype = None
ccv_gradient.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int, c_int]

# values for unnamed enumeration
ccv_resample = _libraries['libccv'].ccv_resample
ccv_resample.restype = None
ccv_resample.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int, c_int, c_int]
ccv_sample_down = _libraries['libccv'].ccv_sample_down
ccv_sample_down.restype = None
ccv_sample_down.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int, c_int]
ccv_sample_up = _libraries['libccv'].ccv_sample_up
ccv_sample_up.restype = None
ccv_sample_up.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int, c_int]

# values for unnamed enumeration
ccv_flip = _libraries['libccv'].ccv_flip
ccv_flip.restype = None
ccv_flip.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int]
ccv_blur = _libraries['libccv'].ccv_blur
ccv_blur.restype = None
ccv_blur.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_double]
ccv_hog = _libraries['libccv'].ccv_hog
ccv_hog.restype = None
ccv_hog.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int, c_int]
ccv_canny = _libraries['libccv'].ccv_canny
ccv_canny.restype = None
ccv_canny.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, c_int, c_double, c_double]
ccv_otsu = _libraries['libccv'].ccv_otsu
ccv_otsu.restype = c_int
ccv_otsu.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(c_double), c_int]
class ccv_daisy_param_t(Structure):
    pass
ccv_daisy_param_t._fields_ = [
    ('radius', c_double),
    ('rad_q_no', c_int),
    ('th_q_no', c_int),
    ('hist_th_q_no', c_int),
    ('normalize_threshold', c_float),
    ('normalize_method', c_int),
]

# values for unnamed enumeration
ccv_daisy = _libraries['libccv'].ccv_daisy
ccv_daisy.restype = None
ccv_daisy.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, ccv_daisy_param_t]
class N14ccv_keypoint_t4DOT_64E(Union):
    pass
class N14ccv_keypoint_t4DOT_644DOT_65E(Structure):
    pass
N14ccv_keypoint_t4DOT_644DOT_65E._fields_ = [
    ('a', c_double),
    ('b', c_double),
    ('c', c_double),
    ('d', c_double),
]
class N14ccv_keypoint_t4DOT_644DOT_66E(Structure):
    pass
N14ccv_keypoint_t4DOT_644DOT_66E._fields_ = [
    ('scale', c_double),
    ('angle', c_double),
]
N14ccv_keypoint_t4DOT_64E._fields_ = [
    ('affine', N14ccv_keypoint_t4DOT_644DOT_65E),
    ('regular', N14ccv_keypoint_t4DOT_644DOT_66E),
]
class ccv_keypoint_t(Structure):
    pass
ccv_keypoint_t._anonymous_ = ['_0']
ccv_keypoint_t._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('octave', c_int),
    ('level', c_int),
    ('_0', N14ccv_keypoint_t4DOT_64E),
]
class ccv_sift_param_t(Structure):
    pass
ccv_sift_param_t._fields_ = [
    ('up2x', c_int),
    ('noctaves', c_int),
    ('nlevels', c_int),
    ('edge_threshold', c_float),
    ('peak_threshold', c_float),
    ('norm_threshold', c_float),
]
ccv_sift = _libraries['libccv'].ccv_sift
ccv_sift.restype = None
ccv_sift.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_array_t)), POINTER(POINTER(ccv_dense_matrix_t)), c_int, ccv_sift_param_t]
class ccv_mser_param_t(Structure):
    pass
ccv_mser_param_t._fields_ = [
    ('delta', c_int),
    ('min_area', c_int),
    ('max_area', c_int),
    ('max_variance', c_double),
    ('min_diversity', c_double),
    ('area_threshold', c_double),
    ('min_margin', c_double),
    ('max_evolution', c_int),
    ('edge_blur_sigma', c_double),
]
class ccv_mser_keypoint_t(Structure):
    pass
ccv_mser_keypoint_t._fields_ = [
    ('rect', ccv_rect_t),
    ('size', c_int),
    ('m10', c_long),
    ('m01', c_long),
    ('m11', c_long),
    ('m20', c_long),
    ('m02', c_long),
    ('keypoint', ccv_point_t),
]
ccv_mser = _libraries['libccv'].ccv_mser
ccv_mser.restype = POINTER(ccv_array_t)
ccv_mser.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, ccv_mser_param_t]
class ccv_swt_param_t(Structure):
    pass
ccv_swt_param_t._fields_ = [
    ('up2x', c_int),
    ('direction', c_int),
    ('size', c_int),
    ('low_thresh', c_double),
    ('high_thresh', c_double),
    ('max_height', c_int),
    ('min_height', c_int),
    ('aspect_ratio', c_double),
    ('variance_ratio', c_double),
    ('thickness_ratio', c_double),
    ('height_ratio', c_double),
    ('intensity_thresh', c_int),
    ('distance_ratio', c_double),
    ('intersect_ratio', c_double),
    ('elongate_ratio', c_double),
    ('letter_thresh', c_int),
    ('breakdown', c_int),
    ('breakdown_ratio', c_double),
]
ccv_swt = _libraries['libccv'].ccv_swt
ccv_swt.restype = None
ccv_swt.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dense_matrix_t)), c_int, ccv_swt_param_t]
ccv_swt_detect_words = _libraries['libccv'].ccv_swt_detect_words
ccv_swt_detect_words.restype = POINTER(ccv_array_t)
ccv_swt_detect_words.argtypes = [POINTER(ccv_dense_matrix_t), ccv_swt_param_t]
class ccv_comp_t(Structure):
    pass
ccv_comp_t._fields_ = [
    ('rect', ccv_rect_t),
    ('neighbors', c_int),
    ('id', c_int),
    ('confidence', c_float),
]
class ccv_root_comp_t(Structure):
    pass
ccv_root_comp_t._fields_ = [
    ('rect', ccv_rect_t),
    ('neighbors', c_int),
    ('id', c_int),
    ('confidence', c_float),
    ('pnum', c_int),
    ('part', ccv_comp_t * 10),
]
class ccv_dpm_part_classifier_t(Structure):
    pass
ccv_dpm_part_classifier_t._fields_ = [
    ('w', POINTER(ccv_dense_matrix_t)),
    ('dx', c_double),
    ('dy', c_double),
    ('dxx', c_double),
    ('dyy', c_double),
    ('x', c_int),
    ('y', c_int),
    ('z', c_int),
    ('counterpart', c_int),
    ('alpha', c_float * 6),
]
class ccv_dpm_root_classifier_t(Structure):
    pass
ccv_dpm_root_classifier_t._fields_ = [
    ('count', c_int),
    ('root', ccv_dpm_part_classifier_t),
    ('part', POINTER(ccv_dpm_part_classifier_t)),
    ('alpha', c_float * 3),
    ('beta', c_float),
]
class ccv_dpm_mixture_model_t(Structure):
    pass
ccv_dpm_mixture_model_t._fields_ = [
    ('count', c_int),
    ('root', POINTER(ccv_dpm_root_classifier_t)),
]
class ccv_dpm_param_t(Structure):
    pass
ccv_dpm_param_t._fields_ = [
    ('interval', c_int),
    ('min_neighbors', c_int),
    ('flags', c_int),
    ('threshold', c_float),
]
class ccv_dpm_new_param_t(Structure):
    pass
ccv_dpm_new_param_t._fields_ = [
    ('components', c_int),
    ('parts', c_int),
    ('grayscale', c_int),
    ('symmetric', c_int),
    ('min_area', c_int),
    ('max_area', c_int),
    ('iterations', c_int),
    ('data_minings', c_int),
    ('relabels', c_int),
    ('negative_cache_size', c_int),
    ('include_overlap', c_double),
    ('alpha', c_double),
    ('alpha_ratio', c_double),
    ('balance', c_double),
    ('C', c_double),
    ('percentile_breakdown', c_double),
    ('detector', ccv_dpm_param_t),
]

# values for unnamed enumeration
ccv_dpm_mixture_model_new = _libraries['libccv'].ccv_dpm_mixture_model_new
ccv_dpm_mixture_model_new.restype = None
ccv_dpm_mixture_model_new.argtypes = [POINTER(STRING), POINTER(ccv_rect_t), c_int, POINTER(STRING), c_int, c_int, STRING, ccv_dpm_new_param_t]
ccv_dpm_detect_objects = _libraries['libccv'].ccv_dpm_detect_objects
ccv_dpm_detect_objects.restype = POINTER(ccv_array_t)
ccv_dpm_detect_objects.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_dpm_mixture_model_t)), c_int, ccv_dpm_param_t]
ccv_load_dpm_mixture_model = _libraries['libccv'].ccv_load_dpm_mixture_model
ccv_load_dpm_mixture_model.restype = POINTER(ccv_dpm_mixture_model_t)
ccv_load_dpm_mixture_model.argtypes = [STRING]
ccv_dpm_mixture_model_free = _libraries['libccv'].ccv_dpm_mixture_model_free
ccv_dpm_mixture_model_free.restype = None
ccv_dpm_mixture_model_free.argtypes = [POINTER(ccv_dpm_mixture_model_t)]
class ccv_bbf_feature_t(Structure):
    pass
ccv_bbf_feature_t._fields_ = [
    ('size', c_int),
    ('px', c_int * 8),
    ('py', c_int * 8),
    ('pz', c_int * 8),
    ('nx', c_int * 8),
    ('ny', c_int * 8),
    ('nz', c_int * 8),
]
class ccv_bbf_stage_classifier_t(Structure):
    pass
ccv_bbf_stage_classifier_t._fields_ = [
    ('count', c_int),
    ('threshold', c_float),
    ('feature', POINTER(ccv_bbf_feature_t)),
    ('alpha', POINTER(c_float)),
]
class ccv_bbf_classifier_cascade_t(Structure):
    pass
ccv_bbf_classifier_cascade_t._fields_ = [
    ('count', c_int),
    ('size', ccv_size_t),
    ('stage_classifier', POINTER(ccv_bbf_stage_classifier_t)),
]

# values for unnamed enumeration
class ccv_bbf_param_t(Structure):
    pass
ccv_bbf_param_t._fields_ = [
    ('interval', c_int),
    ('min_neighbors', c_int),
    ('flags', c_int),
    ('accurate', c_int),
    ('size', ccv_size_t),
]
class ccv_bbf_new_param_t(Structure):
    pass
ccv_bbf_new_param_t._fields_ = [
    ('pos_crit', c_double),
    ('neg_crit', c_double),
    ('balance_k', c_double),
    ('layer', c_int),
    ('feature_number', c_int),
    ('optimizer', c_int),
    ('detector', ccv_bbf_param_t),
]

# values for unnamed enumeration
ccv_bbf_classifier_cascade_new = _libraries['libccv'].ccv_bbf_classifier_cascade_new
ccv_bbf_classifier_cascade_new.restype = None
ccv_bbf_classifier_cascade_new.argtypes = [POINTER(POINTER(ccv_dense_matrix_t)), c_int, POINTER(STRING), c_int, c_int, ccv_size_t, STRING, ccv_bbf_new_param_t]
ccv_bbf_detect_objects = _libraries['libccv'].ccv_bbf_detect_objects
ccv_bbf_detect_objects.restype = POINTER(ccv_array_t)
ccv_bbf_detect_objects.argtypes = [POINTER(ccv_dense_matrix_t), POINTER(POINTER(ccv_bbf_classifier_cascade_t)), c_int, ccv_bbf_param_t]
ccv_load_bbf_classifier_cascade = _libraries['libccv'].ccv_load_bbf_classifier_cascade
ccv_load_bbf_classifier_cascade.restype = POINTER(ccv_bbf_classifier_cascade_t)
ccv_load_bbf_classifier_cascade.argtypes = [STRING]
ccv_bbf_classifier_cascade_read_binary = _libraries['libccv'].ccv_bbf_classifier_cascade_read_binary
ccv_bbf_classifier_cascade_read_binary.restype = POINTER(ccv_bbf_classifier_cascade_t)
ccv_bbf_classifier_cascade_read_binary.argtypes = [STRING]
ccv_bbf_classifier_cascade_write_binary = _libraries['libccv'].ccv_bbf_classifier_cascade_write_binary
ccv_bbf_classifier_cascade_write_binary.restype = c_int
ccv_bbf_classifier_cascade_write_binary.argtypes = [POINTER(ccv_bbf_classifier_cascade_t), STRING, c_int]
ccv_bbf_classifier_cascade_free = _libraries['libccv'].ccv_bbf_classifier_cascade_free
ccv_bbf_classifier_cascade_free.restype = None
ccv_bbf_classifier_cascade_free.argtypes = [POINTER(ccv_bbf_classifier_cascade_t)]
class _G_fpos_t(Structure):
    pass
__off_t = c_long
class __mbstate_t(Structure):
    pass
class N11__mbstate_t3DOT_5E(Union):
    pass
N11__mbstate_t3DOT_5E._fields_ = [
    ('__wch', c_uint),
    ('__wchb', c_char * 4),
]
__mbstate_t._fields_ = [
    ('__count', c_int),
    ('__value', N11__mbstate_t3DOT_5E),
]
_G_fpos_t._fields_ = [
    ('__pos', __off_t),
    ('__state', __mbstate_t),
]
class _G_fpos64_t(Structure):
    pass
__off64_t = c_long
_G_fpos64_t._fields_ = [
    ('__pos', __off64_t),
    ('__state', __mbstate_t),
]
_G_int16_t = c_short
_G_int32_t = c_int
_G_uint16_t = c_ushort
_G_uint32_t = c_uint

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration
acosl = _libraries['libccv'].acosl
acosl.restype = c_longdouble
acosl.argtypes = [c_longdouble]
acos = _libraries['libccv'].acos
acos.restype = c_double
acos.argtypes = [c_double]
acosf = _libraries['libccv'].acosf
acosf.restype = c_float
acosf.argtypes = [c_float]
asinf = _libraries['libccv'].asinf
asinf.restype = c_float
asinf.argtypes = [c_float]
asinl = _libraries['libccv'].asinl
asinl.restype = c_longdouble
asinl.argtypes = [c_longdouble]
asin = _libraries['libccv'].asin
asin.restype = c_double
asin.argtypes = [c_double]
atanl = _libraries['libccv'].atanl
atanl.restype = c_longdouble
atanl.argtypes = [c_longdouble]
atanf = _libraries['libccv'].atanf
atanf.restype = c_float
atanf.argtypes = [c_float]
atan = _libraries['libccv'].atan
atan.restype = c_double
atan.argtypes = [c_double]
atan2f = _libraries['libccv'].atan2f
atan2f.restype = c_float
atan2f.argtypes = [c_float, c_float]
atan2l = _libraries['libccv'].atan2l
atan2l.restype = c_longdouble
atan2l.argtypes = [c_longdouble, c_longdouble]
atan2 = _libraries['libccv'].atan2
atan2.restype = c_double
atan2.argtypes = [c_double, c_double]
cosf = _libraries['libccv'].cosf
cosf.restype = c_float
cosf.argtypes = [c_float]
cos = _libraries['libccv'].cos
cos.restype = c_double
cos.argtypes = [c_double]
cosl = _libraries['libccv'].cosl
cosl.restype = c_longdouble
cosl.argtypes = [c_longdouble]
sinf = _libraries['libccv'].sinf
sinf.restype = c_float
sinf.argtypes = [c_float]
sinl = _libraries['libccv'].sinl
sinl.restype = c_longdouble
sinl.argtypes = [c_longdouble]
sin = _libraries['libccv'].sin
sin.restype = c_double
sin.argtypes = [c_double]
tan = _libraries['libccv'].tan
tan.restype = c_double
tan.argtypes = [c_double]
tanf = _libraries['libccv'].tanf
tanf.restype = c_float
tanf.argtypes = [c_float]
tanl = _libraries['libccv'].tanl
tanl.restype = c_longdouble
tanl.argtypes = [c_longdouble]
coshf = _libraries['libccv'].coshf
coshf.restype = c_float
coshf.argtypes = [c_float]
cosh = _libraries['libccv'].cosh
cosh.restype = c_double
cosh.argtypes = [c_double]
coshl = _libraries['libccv'].coshl
coshl.restype = c_longdouble
coshl.argtypes = [c_longdouble]
sinh = _libraries['libccv'].sinh
sinh.restype = c_double
sinh.argtypes = [c_double]
sinhf = _libraries['libccv'].sinhf
sinhf.restype = c_float
sinhf.argtypes = [c_float]
sinhl = _libraries['libccv'].sinhl
sinhl.restype = c_longdouble
sinhl.argtypes = [c_longdouble]
tanh = _libraries['libccv'].tanh
tanh.restype = c_double
tanh.argtypes = [c_double]
tanhl = _libraries['libccv'].tanhl
tanhl.restype = c_longdouble
tanhl.argtypes = [c_longdouble]
tanhf = _libraries['libccv'].tanhf
tanhf.restype = c_float
tanhf.argtypes = [c_float]
acoshl = _libraries['libccv'].acoshl
acoshl.restype = c_longdouble
acoshl.argtypes = [c_longdouble]
acosh = _libraries['libccv'].acosh
acosh.restype = c_double
acosh.argtypes = [c_double]
acoshf = _libraries['libccv'].acoshf
acoshf.restype = c_float
acoshf.argtypes = [c_float]
asinhl = _libraries['libccv'].asinhl
asinhl.restype = c_longdouble
asinhl.argtypes = [c_longdouble]
asinhf = _libraries['libccv'].asinhf
asinhf.restype = c_float
asinhf.argtypes = [c_float]
asinh = _libraries['libccv'].asinh
asinh.restype = c_double
asinh.argtypes = [c_double]
atanhf = _libraries['libccv'].atanhf
atanhf.restype = c_float
atanhf.argtypes = [c_float]
atanh = _libraries['libccv'].atanh
atanh.restype = c_double
atanh.argtypes = [c_double]
atanhl = _libraries['libccv'].atanhl
atanhl.restype = c_longdouble
atanhl.argtypes = [c_longdouble]
expl = _libraries['libccv'].expl
expl.restype = c_longdouble
expl.argtypes = [c_longdouble]
expf = _libraries['libccv'].expf
expf.restype = c_float
expf.argtypes = [c_float]
exp = _libraries['libccv'].exp
exp.restype = c_double
exp.argtypes = [c_double]
frexpf = _libraries['libccv'].frexpf
frexpf.restype = c_float
frexpf.argtypes = [c_float, POINTER(c_int)]
frexp = _libraries['libccv'].frexp
frexp.restype = c_double
frexp.argtypes = [c_double, POINTER(c_int)]
frexpl = _libraries['libccv'].frexpl
frexpl.restype = c_longdouble
frexpl.argtypes = [c_longdouble, POINTER(c_int)]
ldexpl = _libraries['libccv'].ldexpl
ldexpl.restype = c_longdouble
ldexpl.argtypes = [c_longdouble, c_int]
ldexpf = _libraries['libccv'].ldexpf
ldexpf.restype = c_float
ldexpf.argtypes = [c_float, c_int]
ldexp = _libraries['libccv'].ldexp
ldexp.restype = c_double
ldexp.argtypes = [c_double, c_int]
logl = _libraries['libccv'].logl
logl.restype = c_longdouble
logl.argtypes = [c_longdouble]
logf = _libraries['libccv'].logf
logf.restype = c_float
logf.argtypes = [c_float]
log = _libraries['libccv'].log
log.restype = c_double
log.argtypes = [c_double]
log10l = _libraries['libccv'].log10l
log10l.restype = c_longdouble
log10l.argtypes = [c_longdouble]
log10f = _libraries['libccv'].log10f
log10f.restype = c_float
log10f.argtypes = [c_float]
log10 = _libraries['libccv'].log10
log10.restype = c_double
log10.argtypes = [c_double]
modf = _libraries['libccv'].modf
modf.restype = c_double
modf.argtypes = [c_double, POINTER(c_double)]
modfl = _libraries['libccv'].modfl
modfl.restype = c_longdouble
modfl.argtypes = [c_longdouble, POINTER(c_longdouble)]
modff = _libraries['libccv'].modff
modff.restype = c_float
modff.argtypes = [c_float, POINTER(c_float)]
expm1f = _libraries['libccv'].expm1f
expm1f.restype = c_float
expm1f.argtypes = [c_float]
expm1 = _libraries['libccv'].expm1
expm1.restype = c_double
expm1.argtypes = [c_double]
expm1l = _libraries['libccv'].expm1l
expm1l.restype = c_longdouble
expm1l.argtypes = [c_longdouble]
log1pf = _libraries['libccv'].log1pf
log1pf.restype = c_float
log1pf.argtypes = [c_float]
log1pl = _libraries['libccv'].log1pl
log1pl.restype = c_longdouble
log1pl.argtypes = [c_longdouble]
log1p = _libraries['libccv'].log1p
log1p.restype = c_double
log1p.argtypes = [c_double]
logbf = _libraries['libccv'].logbf
logbf.restype = c_float
logbf.argtypes = [c_float]
logbl = _libraries['libccv'].logbl
logbl.restype = c_longdouble
logbl.argtypes = [c_longdouble]
logb = _libraries['libccv'].logb
logb.restype = c_double
logb.argtypes = [c_double]
exp2f = _libraries['libccv'].exp2f
exp2f.restype = c_float
exp2f.argtypes = [c_float]
exp2l = _libraries['libccv'].exp2l
exp2l.restype = c_longdouble
exp2l.argtypes = [c_longdouble]
exp2 = _libraries['libccv'].exp2
exp2.restype = c_double
exp2.argtypes = [c_double]
log2f = _libraries['libccv'].log2f
log2f.restype = c_float
log2f.argtypes = [c_float]
log2l = _libraries['libccv'].log2l
log2l.restype = c_longdouble
log2l.argtypes = [c_longdouble]
__log2 = _libraries['libccv'].__log2
__log2.restype = c_double
__log2.argtypes = [c_double]
log2 = _libraries['libccv'].log2
log2.restype = c_double
log2.argtypes = [c_double]
powf = _libraries['libccv'].powf
powf.restype = c_float
powf.argtypes = [c_float, c_float]
pow = _libraries['libccv'].pow
pow.restype = c_double
pow.argtypes = [c_double, c_double]
powl = _libraries['libccv'].powl
powl.restype = c_longdouble
powl.argtypes = [c_longdouble, c_longdouble]
sqrtf = _libraries['libccv'].sqrtf
sqrtf.restype = c_float
sqrtf.argtypes = [c_float]
sqrtl = _libraries['libccv'].sqrtl
sqrtl.restype = c_longdouble
sqrtl.argtypes = [c_longdouble]
sqrt = _libraries['libccv'].sqrt
sqrt.restype = c_double
sqrt.argtypes = [c_double]
hypot = _libraries['libccv'].hypot
hypot.restype = c_double
hypot.argtypes = [c_double, c_double]
hypotf = _libraries['libccv'].hypotf
hypotf.restype = c_float
hypotf.argtypes = [c_float, c_float]
hypotl = _libraries['libccv'].hypotl
hypotl.restype = c_longdouble
hypotl.argtypes = [c_longdouble, c_longdouble]
cbrtf = _libraries['libccv'].cbrtf
cbrtf.restype = c_float
cbrtf.argtypes = [c_float]
cbrtl = _libraries['libccv'].cbrtl
cbrtl.restype = c_longdouble
cbrtl.argtypes = [c_longdouble]
cbrt = _libraries['libccv'].cbrt
cbrt.restype = c_double
cbrt.argtypes = [c_double]
ceil = _libraries['libccv'].ceil
ceil.restype = c_double
ceil.argtypes = [c_double]
ceill = _libraries['libccv'].ceill
ceill.restype = c_longdouble
ceill.argtypes = [c_longdouble]
ceilf = _libraries['libccv'].ceilf
ceilf.restype = c_float
ceilf.argtypes = [c_float]
fabsf = _libraries['libccv'].fabsf
fabsf.restype = c_float
fabsf.argtypes = [c_float]
fabsl = _libraries['libccv'].fabsl
fabsl.restype = c_longdouble
fabsl.argtypes = [c_longdouble]
fabs = _libraries['libccv'].fabs
fabs.restype = c_double
fabs.argtypes = [c_double]
floorl = _libraries['libccv'].floorl
floorl.restype = c_longdouble
floorl.argtypes = [c_longdouble]
floorf = _libraries['libccv'].floorf
floorf.restype = c_float
floorf.argtypes = [c_float]
floor = _libraries['libccv'].floor
floor.restype = c_double
floor.argtypes = [c_double]
fmodf = _libraries['libccv'].fmodf
fmodf.restype = c_float
fmodf.argtypes = [c_float, c_float]
fmodl = _libraries['libccv'].fmodl
fmodl.restype = c_longdouble
fmodl.argtypes = [c_longdouble, c_longdouble]
fmod = _libraries['libccv'].fmod
fmod.restype = c_double
fmod.argtypes = [c_double, c_double]
__isinf = _libraries['libccv'].__isinf
__isinf.restype = c_int
__isinf.argtypes = [c_double]
__isinff = _libraries['libccv'].__isinff
__isinff.restype = c_int
__isinff.argtypes = [c_float]
isinf = _libraries['libccv'].isinf
isinf.restype = c_int
isinf.argtypes = [c_double]
finite = _libraries['libccv'].finite
finite.restype = c_int
finite.argtypes = [c_double]
drem = _libraries['libccv'].drem
drem.restype = c_double
drem.argtypes = [c_double, c_double]
significand = _libraries['libccv'].significand
significand.restype = c_double
significand.argtypes = [c_double]
copysign = _libraries['libccv'].copysign
copysign.restype = c_double
copysign.argtypes = [c_double, c_double]
copysignf = _libraries['libccv'].copysignf
copysignf.restype = c_float
copysignf.argtypes = [c_float, c_float]
copysignl = _libraries['libccv'].copysignl
copysignl.restype = c_longdouble
copysignl.argtypes = [c_longdouble, c_longdouble]
nanf = _libraries['libccv'].nanf
nanf.restype = c_float
nanf.argtypes = [STRING]
nan = _libraries['libccv'].nan
nan.restype = c_double
nan.argtypes = [STRING]
nanl = _libraries['libccv'].nanl
nanl.restype = c_longdouble
nanl.argtypes = [STRING]
__nan = _libraries['libccv'].__nan
__nan.restype = c_double
__nan.argtypes = [STRING]
__isnanf = _libraries['libccv'].__isnanf
__isnanf.restype = c_int
__isnanf.argtypes = [c_float]
__isnan = _libraries['libccv'].__isnan
__isnan.restype = c_int
__isnan.argtypes = [c_double]
isnan = _libraries['libccv'].isnan
isnan.restype = c_int
isnan.argtypes = [c_double]
j0 = _libraries['libccv'].j0
j0.restype = c_double
j0.argtypes = [c_double]
j1 = _libraries['libccv'].j1
j1.restype = c_double
j1.argtypes = [c_double]
jn = _libraries['libccv'].jn
jn.restype = c_double
jn.argtypes = [c_int, c_double]
y0 = _libraries['libccv'].y0
y0.restype = c_double
y0.argtypes = [c_double]
y1 = _libraries['libccv'].y1
y1.restype = c_double
y1.argtypes = [c_double]
yn = _libraries['libccv'].yn
yn.restype = c_double
yn.argtypes = [c_int, c_double]
erff = _libraries['libccv'].erff
erff.restype = c_float
erff.argtypes = [c_float]
erf = _libraries['libccv'].erf
erf.restype = c_double
erf.argtypes = [c_double]
erfl = _libraries['libccv'].erfl
erfl.restype = c_longdouble
erfl.argtypes = [c_longdouble]
erfc = _libraries['libccv'].erfc
erfc.restype = c_double
erfc.argtypes = [c_double]
erfcf = _libraries['libccv'].erfcf
erfcf.restype = c_float
erfcf.argtypes = [c_float]
erfcl = _libraries['libccv'].erfcl
erfcl.restype = c_longdouble
erfcl.argtypes = [c_longdouble]
lgammal = _libraries['libccv'].lgammal
lgammal.restype = c_longdouble
lgammal.argtypes = [c_longdouble]
lgamma = _libraries['libccv'].lgamma
lgamma.restype = c_double
lgamma.argtypes = [c_double]
lgammaf = _libraries['libccv'].lgammaf
lgammaf.restype = c_float
lgammaf.argtypes = [c_float]
tgammaf = _libraries['libccv'].tgammaf
tgammaf.restype = c_float
tgammaf.argtypes = [c_float]
tgammal = _libraries['libccv'].tgammal
tgammal.restype = c_longdouble
tgammal.argtypes = [c_longdouble]
tgamma = _libraries['libccv'].tgamma
tgamma.restype = c_double
tgamma.argtypes = [c_double]
gamma = _libraries['libccv'].gamma
gamma.restype = c_double
gamma.argtypes = [c_double]
lgammaf_r = _libraries['libccv'].lgammaf_r
lgammaf_r.restype = c_float
lgammaf_r.argtypes = [c_float, POINTER(c_int)]
lgamma_r = _libraries['libccv'].lgamma_r
lgamma_r.restype = c_double
lgamma_r.argtypes = [c_double, POINTER(c_int)]
lgammal_r = _libraries['libccv'].lgammal_r
lgammal_r.restype = c_longdouble
lgammal_r.argtypes = [c_longdouble, POINTER(c_int)]
rint = _libraries['libccv'].rint
rint.restype = c_double
rint.argtypes = [c_double]
rintf = _libraries['libccv'].rintf
rintf.restype = c_float
rintf.argtypes = [c_float]
rintl = _libraries['libccv'].rintl
rintl.restype = c_longdouble
rintl.argtypes = [c_longdouble]
nextafterl = _libraries['libccv'].nextafterl
nextafterl.restype = c_longdouble
nextafterl.argtypes = [c_longdouble, c_longdouble]
nextafterf = _libraries['libccv'].nextafterf
nextafterf.restype = c_float
nextafterf.argtypes = [c_float, c_float]
nextafter = _libraries['libccv'].nextafter
nextafter.restype = c_double
nextafter.argtypes = [c_double, c_double]
nexttowardf = _libraries['libccv'].nexttowardf
nexttowardf.restype = c_float
nexttowardf.argtypes = [c_float, c_longdouble]
nexttowardl = _libraries['libccv'].nexttowardl
nexttowardl.restype = c_longdouble
nexttowardl.argtypes = [c_longdouble, c_longdouble]
nexttoward = _libraries['libccv'].nexttoward
nexttoward.restype = c_double
nexttoward.argtypes = [c_double, c_longdouble]
remainder = _libraries['libccv'].remainder
remainder.restype = c_double
remainder.argtypes = [c_double, c_double]
remainderl = _libraries['libccv'].remainderl
remainderl.restype = c_longdouble
remainderl.argtypes = [c_longdouble, c_longdouble]
remainderf = _libraries['libccv'].remainderf
remainderf.restype = c_float
remainderf.argtypes = [c_float, c_float]
scalbn = _libraries['libccv'].scalbn
scalbn.restype = c_double
scalbn.argtypes = [c_double, c_int]
scalbnf = _libraries['libccv'].scalbnf
scalbnf.restype = c_float
scalbnf.argtypes = [c_float, c_int]
scalbnl = _libraries['libccv'].scalbnl
scalbnl.restype = c_longdouble
scalbnl.argtypes = [c_longdouble, c_int]
ilogbf = _libraries['libccv'].ilogbf
ilogbf.restype = c_int
ilogbf.argtypes = [c_float]
ilogbl = _libraries['libccv'].ilogbl
ilogbl.restype = c_int
ilogbl.argtypes = [c_longdouble]
ilogb = _libraries['libccv'].ilogb
ilogb.restype = c_int
ilogb.argtypes = [c_double]
scalblnf = _libraries['libccv'].scalblnf
scalblnf.restype = c_float
scalblnf.argtypes = [c_float, c_long]
scalbln = _libraries['libccv'].scalbln
scalbln.restype = c_double
scalbln.argtypes = [c_double, c_long]
scalblnl = _libraries['libccv'].scalblnl
scalblnl.restype = c_longdouble
scalblnl.argtypes = [c_longdouble, c_long]
nearbyintf = _libraries['libccv'].nearbyintf
nearbyintf.restype = c_float
nearbyintf.argtypes = [c_float]
nearbyintl = _libraries['libccv'].nearbyintl
nearbyintl.restype = c_longdouble
nearbyintl.argtypes = [c_longdouble]
nearbyint = _libraries['libccv'].nearbyint
nearbyint.restype = c_double
nearbyint.argtypes = [c_double]
roundl = _libraries['libccv'].roundl
roundl.restype = c_longdouble
roundl.argtypes = [c_longdouble]
round = _libraries['libccv'].round
round.restype = c_double
round.argtypes = [c_double]
roundf = _libraries['libccv'].roundf
roundf.restype = c_float
roundf.argtypes = [c_float]
truncl = _libraries['libccv'].truncl
truncl.restype = c_longdouble
truncl.argtypes = [c_longdouble]
truncf = _libraries['libccv'].truncf
truncf.restype = c_float
truncf.argtypes = [c_float]
trunc = _libraries['libccv'].trunc
trunc.restype = c_double
trunc.argtypes = [c_double]
remquo = _libraries['libccv'].remquo
remquo.restype = c_double
remquo.argtypes = [c_double, c_double, POINTER(c_int)]
remquol = _libraries['libccv'].remquol
remquol.restype = c_longdouble
remquol.argtypes = [c_longdouble, c_longdouble, POINTER(c_int)]
remquof = _libraries['libccv'].remquof
remquof.restype = c_float
remquof.argtypes = [c_float, c_float, POINTER(c_int)]
lrintf = _libraries['libccv'].lrintf
lrintf.restype = c_long
lrintf.argtypes = [c_float]
lrintl = _libraries['libccv'].lrintl
lrintl.restype = c_long
lrintl.argtypes = [c_longdouble]
lrint = _libraries['libccv'].lrint
lrint.restype = c_long
lrint.argtypes = [c_double]
llrint = _libraries['libccv'].llrint
llrint.restype = c_longlong
llrint.argtypes = [c_double]
llrintf = _libraries['libccv'].llrintf
llrintf.restype = c_longlong
llrintf.argtypes = [c_float]
llrintl = _libraries['libccv'].llrintl
llrintl.restype = c_longlong
llrintl.argtypes = [c_longdouble]
lround = _libraries['libccv'].lround
lround.restype = c_long
lround.argtypes = [c_double]
lroundf = _libraries['libccv'].lroundf
lroundf.restype = c_long
lroundf.argtypes = [c_float]
lroundl = _libraries['libccv'].lroundl
lroundl.restype = c_long
lroundl.argtypes = [c_longdouble]
llroundf = _libraries['libccv'].llroundf
llroundf.restype = c_longlong
llroundf.argtypes = [c_float]
llround = _libraries['libccv'].llround
llround.restype = c_longlong
llround.argtypes = [c_double]
llroundl = _libraries['libccv'].llroundl
llroundl.restype = c_longlong
llroundl.argtypes = [c_longdouble]
fdimf = _libraries['libccv'].fdimf
fdimf.restype = c_float
fdimf.argtypes = [c_float, c_float]
fdiml = _libraries['libccv'].fdiml
fdiml.restype = c_longdouble
fdiml.argtypes = [c_longdouble, c_longdouble]
fdim = _libraries['libccv'].fdim
fdim.restype = c_double
fdim.argtypes = [c_double, c_double]
fmax = _libraries['libccv'].fmax
fmax.restype = c_double
fmax.argtypes = [c_double, c_double]
fmaxf = _libraries['libccv'].fmaxf
fmaxf.restype = c_float
fmaxf.argtypes = [c_float, c_float]
fmaxl = _libraries['libccv'].fmaxl
fmaxl.restype = c_longdouble
fmaxl.argtypes = [c_longdouble, c_longdouble]
fmin = _libraries['libccv'].fmin
fmin.restype = c_double
fmin.argtypes = [c_double, c_double]
fminl = _libraries['libccv'].fminl
fminl.restype = c_longdouble
fminl.argtypes = [c_longdouble, c_longdouble]
fminf = _libraries['libccv'].fminf
fminf.restype = c_float
fminf.argtypes = [c_float, c_float]
__fpclassifyf = _libraries['libccv'].__fpclassifyf
__fpclassifyf.restype = c_int
__fpclassifyf.argtypes = [c_float]
__fpclassify = _libraries['libccv'].__fpclassify
__fpclassify.restype = c_int
__fpclassify.argtypes = [c_double]
fma = _libraries['libccv'].fma
fma.restype = c_double
fma.argtypes = [c_double, c_double, c_double]
fmaf = _libraries['libccv'].fmaf
fmaf.restype = c_float
fmaf.argtypes = [c_float, c_float, c_float]
fmal = _libraries['libccv'].fmal
fmal.restype = c_longdouble
fmal.argtypes = [c_longdouble, c_longdouble, c_longdouble]
scalb = _libraries['libccv'].scalb
scalb.restype = c_double
scalb.argtypes = [c_double, c_double]
float_t = c_float
double_t = c_double
__signbitf = _libraries['libccv'].__signbitf
__signbitf.restype = c_int
__signbitf.argtypes = [c_float]
__signbitl = _libraries['libccv'].__signbitl
__signbitl.restype = c_int
__signbitl.argtypes = [c_longdouble]
pthread_t = c_ulong
class pthread_attr_t(Union):
    pass
pthread_attr_t._fields_ = [
    ('__size', c_char * 56),
    ('__align', c_long),
]
class __pthread_internal_list(Structure):
    pass
__pthread_internal_list._fields_ = [
    ('__prev', POINTER(__pthread_internal_list)),
    ('__next', POINTER(__pthread_internal_list)),
]
__pthread_list_t = __pthread_internal_list
class __pthread_mutex_s(Structure):
    pass
__pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_int),
    ('__list', __pthread_list_t),
]
class pthread_mutex_t(Union):
    pass
pthread_mutex_t._fields_ = [
    ('__data', __pthread_mutex_s),
    ('__size', c_char * 40),
    ('__align', c_long),
]
class pthread_mutexattr_t(Union):
    pass
pthread_mutexattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
class N14pthread_cond_t4DOT_20E(Structure):
    pass
N14pthread_cond_t4DOT_20E._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', c_void_p),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]
class pthread_cond_t(Union):
    pass
pthread_cond_t._fields_ = [
    ('__data', N14pthread_cond_t4DOT_20E),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]
class pthread_condattr_t(Union):
    pass
pthread_condattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
pthread_key_t = c_uint
pthread_once_t = c_int
class N16pthread_rwlock_t4DOT_23E(Structure):
    pass
N16pthread_rwlock_t4DOT_23E._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__writer', c_int),
    ('__shared', c_int),
    ('__pad1', c_ulong),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]
class pthread_rwlock_t(Union):
    pass
pthread_rwlock_t._fields_ = [
    ('__data', N16pthread_rwlock_t4DOT_23E),
    ('__size', c_char * 56),
    ('__align', c_long),
]
class pthread_rwlockattr_t(Union):
    pass
pthread_rwlockattr_t._fields_ = [
    ('__size', c_char * 8),
    ('__align', c_long),
]
pthread_spinlock_t = c_int
class pthread_barrier_t(Union):
    pass
pthread_barrier_t._fields_ = [
    ('__size', c_char * 32),
    ('__align', c_long),
]
class pthread_barrierattr_t(Union):
    pass
pthread_barrierattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
class __va_list_tag(Structure):
    pass
vprintf = _libraries['libccv'].vprintf
vprintf.restype = c_int
vprintf.argtypes = [STRING, POINTER(__va_list_tag)]
getchar = _libraries['libccv'].getchar
getchar.restype = c_int
getchar.argtypes = []
class _IO_FILE(Structure):
    pass
FILE = _IO_FILE
getc_unlocked = _libraries['libccv'].getc_unlocked
getc_unlocked.restype = c_int
getc_unlocked.argtypes = [POINTER(FILE)]
getchar_unlocked = _libraries['libccv'].getchar_unlocked
getchar_unlocked.restype = c_int
getchar_unlocked.argtypes = []
putchar = _libraries['libccv'].putchar
putchar.restype = c_int
putchar.argtypes = [c_int]
putc_unlocked = _libraries['libccv'].putc_unlocked
putc_unlocked.restype = c_int
putc_unlocked.argtypes = [c_int, POINTER(FILE)]
putchar_unlocked = _libraries['libccv'].putchar_unlocked
putchar_unlocked.restype = c_int
putchar_unlocked.argtypes = [c_int]
__ssize_t = c_long
getline = _libraries['libccv'].getline
getline.restype = __ssize_t
getline.argtypes = [POINTER(STRING), POINTER(size_t), POINTER(FILE)]
feof_unlocked = _libraries['libccv'].feof_unlocked
feof_unlocked.restype = c_int
feof_unlocked.argtypes = [POINTER(FILE)]
ferror_unlocked = _libraries['libccv'].ferror_unlocked
ferror_unlocked.restype = c_int
ferror_unlocked.argtypes = [POINTER(FILE)]
sys_nerr = (c_int).in_dll(_libraries['libccv'], 'sys_nerr')
sys_errlist = (STRING * 0).in_dll(_libraries['libccv'], 'sys_errlist')
class timeval(Structure):
    pass
__time_t = c_long
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
__u_char = c_ubyte
__u_short = c_ushort
__u_int = c_uint
__u_long = c_ulong
__int8_t = c_byte
__uint8_t = c_ubyte
__int16_t = c_short
__uint16_t = c_ushort
__int32_t = c_int
__uint32_t = c_uint
__int64_t = c_long
__uint64_t = c_ulong
__quad_t = c_long
__u_quad_t = c_ulong
__dev_t = c_ulong
__uid_t = c_uint
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = c_ulong
__mode_t = c_uint
__nlink_t = c_ulong
__pid_t = c_int
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__clock_t = c_long
__rlim_t = c_ulong
__rlim64_t = c_ulong
__id_t = c_uint
__useconds_t = c_uint
__daddr_t = c_int
__swblk_t = c_long
__key_t = c_int
__clockid_t = c_int
__timer_t = c_void_p
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = c_long
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = c_ulong
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = c_ulong
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_long
__socklen_t = c_uint
class wait(Union):
    pass
class N4wait3DOT_9E(Structure):
    pass
N4wait3DOT_9E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait4DOT_10E(Structure):
    pass
N4wait4DOT_10E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
wait._fields_ = [
    ('w_status', c_int),
    ('__wait_terminated', N4wait3DOT_9E),
    ('__wait_stopped', N4wait4DOT_10E),
]
optarg = (STRING).in_dll(_libraries['libccv'], 'optarg')
optind = (c_int).in_dll(_libraries['libccv'], 'optind')
opterr = (c_int).in_dll(_libraries['libccv'], 'opterr')
optopt = (c_int).in_dll(_libraries['libccv'], 'optopt')
getopt = _libraries['libccv'].getopt
getopt.restype = c_int
getopt.argtypes = [c_int, POINTER(STRING), STRING]
class _IO_jump_t(Structure):
    pass
_IO_jump_t._fields_ = [
]
_IO_lock_t = None
class _IO_marker(Structure):
    pass
_IO_marker._fields_ = [
    ('_next', POINTER(_IO_marker)),
    ('_sbuf', POINTER(_IO_FILE)),
    ('_pos', c_int),
]

# values for enumeration '__codecvt_result'
__codecvt_result = c_int # enum
_IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', STRING),
    ('_IO_read_end', STRING),
    ('_IO_read_base', STRING),
    ('_IO_write_base', STRING),
    ('_IO_write_ptr', STRING),
    ('_IO_write_end', STRING),
    ('_IO_buf_base', STRING),
    ('_IO_buf_end', STRING),
    ('_IO_save_base', STRING),
    ('_IO_backup_base', STRING),
    ('_IO_save_end', STRING),
    ('_markers', POINTER(_IO_marker)),
    ('_chain', POINTER(_IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_byte),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', c_void_p),
    ('__pad2', c_void_p),
    ('__pad3', c_void_p),
    ('__pad4', c_void_p),
    ('__pad5', size_t),
    ('_mode', c_int),
    ('_unused2', c_char * 20),
]
class _IO_FILE_plus(Structure):
    pass
_IO_FILE_plus._fields_ = [
]
__io_read_fn = CFUNCTYPE(__ssize_t, c_void_p, STRING, size_t)
__io_write_fn = CFUNCTYPE(__ssize_t, c_void_p, STRING, size_t)
__io_seek_fn = CFUNCTYPE(c_int, c_void_p, POINTER(__off64_t), c_int)
__io_close_fn = CFUNCTYPE(c_int, c_void_p)
cookie_read_function_t = __io_read_fn
cookie_write_function_t = __io_write_fn
cookie_seek_function_t = __io_seek_fn
cookie_close_function_t = __io_close_fn
class _IO_cookie_io_functions_t(Structure):
    pass
_IO_cookie_io_functions_t._fields_ = [
    ('read', POINTER(__io_read_fn)),
    ('write', POINTER(__io_write_fn)),
    ('seek', POINTER(__io_seek_fn)),
    ('close', POINTER(__io_close_fn)),
]
cookie_io_functions_t = _IO_cookie_io_functions_t
class _IO_cookie_file(Structure):
    pass
_IO_cookie_file._fields_ = [
]
signgam = (c_int).in_dll(_libraries['libccv'], 'signgam')

# values for unnamed enumeration

# values for enumeration '_LIB_VERSION_TYPE'
_LIB_VERSION_TYPE = c_int # enum
class __exception(Structure):
    pass
__exception._fields_ = [
    ('type', c_int),
    ('name', STRING),
    ('arg1', c_double),
    ('arg2', c_double),
    ('retval', c_double),
]
matherr = _libraries['libccv'].matherr
matherr.restype = c_int
matherr.argtypes = [POINTER(__exception)]
int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
uint16_t = c_uint16
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
uintptr_t = c_ulong
intmax_t = c_long
uintmax_t = c_ulong
__FILE = _IO_FILE
__va_list_tag._fields_ = [
]
__gnuc_va_list = __va_list_tag * 1
va_list = __gnuc_va_list
fpos_t = _G_fpos_t
fpos64_t = _G_fpos64_t
remove = _libraries['libccv'].remove
remove.restype = c_int
remove.argtypes = [STRING]
rename = _libraries['libccv'].rename
rename.restype = c_int
rename.argtypes = [STRING, STRING]
tmpfile = _libraries['libccv'].tmpfile
tmpfile.restype = POINTER(FILE)
tmpfile.argtypes = []
tmpnam = _libraries['libccv'].tmpnam
tmpnam.restype = STRING
tmpnam.argtypes = [STRING]
tempnam = _libraries['libccv'].tempnam
tempnam.restype = STRING
tempnam.argtypes = [STRING, STRING]
fclose = _libraries['libccv'].fclose
fclose.restype = c_int
fclose.argtypes = [POINTER(FILE)]
fflush = _libraries['libccv'].fflush
fflush.restype = c_int
fflush.argtypes = [POINTER(FILE)]
fopen = _libraries['libccv'].fopen
fopen.restype = POINTER(FILE)
fopen.argtypes = [STRING, STRING]
freopen = _libraries['libccv'].freopen
freopen.restype = POINTER(FILE)
freopen.argtypes = [STRING, STRING, POINTER(FILE)]
fdopen = _libraries['libccv'].fdopen
fdopen.restype = POINTER(FILE)
fdopen.argtypes = [c_int, STRING]
setbuf = _libraries['libccv'].setbuf
setbuf.restype = None
setbuf.argtypes = [POINTER(FILE), STRING]
setvbuf = _libraries['libccv'].setvbuf
setvbuf.restype = c_int
setvbuf.argtypes = [POINTER(FILE), STRING, c_int, size_t]
setbuffer = _libraries['libccv'].setbuffer
setbuffer.restype = None
setbuffer.argtypes = [POINTER(FILE), STRING, size_t]
setlinebuf = _libraries['libccv'].setlinebuf
setlinebuf.restype = None
setlinebuf.argtypes = [POINTER(FILE)]
fprintf = _libraries['libccv'].fprintf
fprintf.restype = c_int
fprintf.argtypes = [POINTER(FILE), STRING]
printf = _libraries['libccv'].printf
printf.restype = c_int
printf.argtypes = [STRING]
sprintf = _libraries['libccv'].sprintf
sprintf.restype = c_int
sprintf.argtypes = [STRING, STRING]
vfprintf = _libraries['libccv'].vfprintf
vfprintf.restype = c_int
vfprintf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vsprintf = _libraries['libccv'].vsprintf
vsprintf.restype = c_int
vsprintf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
snprintf = _libraries['libccv'].snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
vsnprintf = _libraries['libccv'].vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
vasprintf = _libraries['libccv'].vasprintf
vasprintf.restype = c_int
vasprintf.argtypes = [POINTER(STRING), STRING, POINTER(__va_list_tag)]
asprintf = _libraries['libccv'].asprintf
asprintf.restype = c_int
asprintf.argtypes = [POINTER(STRING), STRING]
vdprintf = _libraries['libccv'].vdprintf
vdprintf.restype = c_int
vdprintf.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
dprintf = _libraries['libccv'].dprintf
dprintf.restype = c_int
dprintf.argtypes = [c_int, STRING]
fscanf = _libraries['libccv'].fscanf
fscanf.restype = c_int
fscanf.argtypes = [POINTER(FILE), STRING]
scanf = _libraries['libccv'].scanf
scanf.restype = c_int
scanf.argtypes = [STRING]
sscanf = _libraries['libccv'].sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
vfscanf = _libraries['libccv'].vfscanf
vfscanf.restype = c_int
vfscanf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vscanf = _libraries['libccv'].vscanf
vscanf.restype = c_int
vscanf.argtypes = [STRING, POINTER(__va_list_tag)]
vsscanf = _libraries['libccv'].vsscanf
vsscanf.restype = c_int
vsscanf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
fgetc = _libraries['libccv'].fgetc
fgetc.restype = c_int
fgetc.argtypes = [POINTER(FILE)]
getc = _libraries['libccv'].getc
getc.restype = c_int
getc.argtypes = [POINTER(FILE)]
fputc = _libraries['libccv'].fputc
fputc.restype = c_int
fputc.argtypes = [c_int, POINTER(FILE)]
putc = _libraries['libccv'].putc
putc.restype = c_int
putc.argtypes = [c_int, POINTER(FILE)]
getw = _libraries['libccv'].getw
getw.restype = c_int
getw.argtypes = [POINTER(FILE)]
putw = _libraries['libccv'].putw
putw.restype = c_int
putw.argtypes = [c_int, POINTER(FILE)]
fgets = _libraries['libccv'].fgets
fgets.restype = STRING
fgets.argtypes = [STRING, c_int, POINTER(FILE)]
gets = _libraries['libccv'].gets
gets.restype = STRING
gets.argtypes = [STRING]
getdelim = _libraries['libccv'].getdelim
getdelim.restype = __ssize_t
getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
fputs = _libraries['libccv'].fputs
fputs.restype = c_int
fputs.argtypes = [STRING, POINTER(FILE)]
puts = _libraries['libccv'].puts
puts.restype = c_int
puts.argtypes = [STRING]
ungetc = _libraries['libccv'].ungetc
ungetc.restype = c_int
ungetc.argtypes = [c_int, POINTER(FILE)]
fread = _libraries['libccv'].fread
fread.restype = size_t
fread.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fwrite = _libraries['libccv'].fwrite
fwrite.restype = size_t
fwrite.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fseek = _libraries['libccv'].fseek
fseek.restype = c_int
fseek.argtypes = [POINTER(FILE), c_long, c_int]
ftell = _libraries['libccv'].ftell
ftell.restype = c_long
ftell.argtypes = [POINTER(FILE)]
rewind = _libraries['libccv'].rewind
rewind.restype = None
rewind.argtypes = [POINTER(FILE)]
fseeko = _libraries['libccv'].fseeko
fseeko.restype = c_int
fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
ftello = _libraries['libccv'].ftello
ftello.restype = __off_t
ftello.argtypes = [POINTER(FILE)]
fgetpos = _libraries['libccv'].fgetpos
fgetpos.restype = c_int
fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fsetpos = _libraries['libccv'].fsetpos
fsetpos.restype = c_int
fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
clearerr = _libraries['libccv'].clearerr
clearerr.restype = None
clearerr.argtypes = [POINTER(FILE)]
feof = _libraries['libccv'].feof
feof.restype = c_int
feof.argtypes = [POINTER(FILE)]
ferror = _libraries['libccv'].ferror
ferror.restype = c_int
ferror.argtypes = [POINTER(FILE)]
clearerr_unlocked = _libraries['libccv'].clearerr_unlocked
clearerr_unlocked.restype = None
clearerr_unlocked.argtypes = [POINTER(FILE)]
perror = _libraries['libccv'].perror
perror.restype = None
perror.argtypes = [STRING]
fileno = _libraries['libccv'].fileno
fileno.restype = c_int
fileno.argtypes = [POINTER(FILE)]
fileno_unlocked = _libraries['libccv'].fileno_unlocked
fileno_unlocked.restype = c_int
fileno_unlocked.argtypes = [POINTER(FILE)]
popen = _libraries['libccv'].popen
popen.restype = POINTER(FILE)
popen.argtypes = [STRING, STRING]
pclose = _libraries['libccv'].pclose
pclose.restype = c_int
pclose.argtypes = [POINTER(FILE)]
ctermid = _libraries['libccv'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
class obstack(Structure):
    pass
obstack._fields_ = [
]
flockfile = _libraries['libccv'].flockfile
flockfile.restype = None
flockfile.argtypes = [POINTER(FILE)]
ftrylockfile = _libraries['libccv'].ftrylockfile
ftrylockfile.restype = c_int
ftrylockfile.argtypes = [POINTER(FILE)]
funlockfile = _libraries['libccv'].funlockfile
funlockfile.restype = None
funlockfile.argtypes = [POINTER(FILE)]
class div_t(Structure):
    pass
div_t._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]
class ldiv_t(Structure):
    pass
ldiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
class lldiv_t(Structure):
    pass
lldiv_t._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]
strtod = _libraries['libccv'].strtod
strtod.restype = c_double
strtod.argtypes = [STRING, POINTER(STRING)]
strtof = _libraries['libccv'].strtof
strtof.restype = c_float
strtof.argtypes = [STRING, POINTER(STRING)]
strtold = _libraries['libccv'].strtold
strtold.restype = c_longdouble
strtold.argtypes = [STRING, POINTER(STRING)]
strtol = _libraries['libccv'].strtol
strtol.restype = c_long
strtol.argtypes = [STRING, POINTER(STRING), c_int]
strtoul = _libraries['libccv'].strtoul
strtoul.restype = c_ulong
strtoul.argtypes = [STRING, POINTER(STRING), c_int]
strtoq = _libraries['libccv'].strtoq
strtoq.restype = c_longlong
strtoq.argtypes = [STRING, POINTER(STRING), c_int]
strtouq = _libraries['libccv'].strtouq
strtouq.restype = c_ulonglong
strtouq.argtypes = [STRING, POINTER(STRING), c_int]
strtoll = _libraries['libccv'].strtoll
strtoll.restype = c_longlong
strtoll.argtypes = [STRING, POINTER(STRING), c_int]
strtoull = _libraries['libccv'].strtoull
strtoull.restype = c_ulonglong
strtoull.argtypes = [STRING, POINTER(STRING), c_int]
class __locale_struct(Structure):
    pass
__locale_t = POINTER(__locale_struct)
strtol_l = _libraries['libccv'].strtol_l
strtol_l.restype = c_long
strtol_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoul_l = _libraries['libccv'].strtoul_l
strtoul_l.restype = c_ulong
strtoul_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoll_l = _libraries['libccv'].strtoll_l
strtoll_l.restype = c_longlong
strtoll_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoull_l = _libraries['libccv'].strtoull_l
strtoull_l.restype = c_ulonglong
strtoull_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtod_l = _libraries['libccv'].strtod_l
strtod_l.restype = c_double
strtod_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtof_l = _libraries['libccv'].strtof_l
strtof_l.restype = c_float
strtof_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtold_l = _libraries['libccv'].strtold_l
strtold_l.restype = c_longdouble
strtold_l.argtypes = [STRING, POINTER(STRING), __locale_t]
atof = _libraries['libccv'].atof
atof.restype = c_double
atof.argtypes = [STRING]
atoi = _libraries['libccv'].atoi
atoi.restype = c_int
atoi.argtypes = [STRING]
atol = _libraries['libccv'].atol
atol.restype = c_long
atol.argtypes = [STRING]
atoll = _libraries['libccv'].atoll
atoll.restype = c_longlong
atoll.argtypes = [STRING]
l64a = _libraries['libccv'].l64a
l64a.restype = STRING
l64a.argtypes = [c_long]
a64l = _libraries['libccv'].a64l
a64l.restype = c_long
a64l.argtypes = [STRING]
random = _libraries['libccv'].random
random.restype = c_long
random.argtypes = []
srandom = _libraries['libccv'].srandom
srandom.restype = None
srandom.argtypes = [c_uint]
initstate = _libraries['libccv'].initstate
initstate.restype = STRING
initstate.argtypes = [c_uint, STRING, size_t]
setstate = _libraries['libccv'].setstate
setstate.restype = STRING
setstate.argtypes = [STRING]
class random_data(Structure):
    pass
random_data._fields_ = [
    ('fptr', POINTER(int32_t)),
    ('rptr', POINTER(int32_t)),
    ('state', POINTER(int32_t)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(int32_t)),
]
rand = _libraries['libccv'].rand
rand.restype = c_int
rand.argtypes = []
srand = _libraries['libccv'].srand
srand.restype = None
srand.argtypes = [c_uint]
rand_r = _libraries['libccv'].rand_r
rand_r.restype = c_int
rand_r.argtypes = [POINTER(c_uint)]
drand48 = _libraries['libccv'].drand48
drand48.restype = c_double
drand48.argtypes = []
erand48 = _libraries['libccv'].erand48
erand48.restype = c_double
erand48.argtypes = [POINTER(c_ushort)]
lrand48 = _libraries['libccv'].lrand48
lrand48.restype = c_long
lrand48.argtypes = []
nrand48 = _libraries['libccv'].nrand48
nrand48.restype = c_long
nrand48.argtypes = [POINTER(c_ushort)]
mrand48 = _libraries['libccv'].mrand48
mrand48.restype = c_long
mrand48.argtypes = []
jrand48 = _libraries['libccv'].jrand48
jrand48.restype = c_long
jrand48.argtypes = [POINTER(c_ushort)]
srand48 = _libraries['libccv'].srand48
srand48.restype = None
srand48.argtypes = [c_long]
seed48 = _libraries['libccv'].seed48
seed48.restype = POINTER(c_ushort)
seed48.argtypes = [POINTER(c_ushort)]
lcong48 = _libraries['libccv'].lcong48
lcong48.restype = None
lcong48.argtypes = [POINTER(c_ushort)]
class drand48_data(Structure):
    pass
drand48_data._fields_ = [
    ('__x', c_ushort * 3),
    ('__old_x', c_ushort * 3),
    ('__c', c_ushort),
    ('__init', c_ushort),
    ('__a', c_ulonglong),
]
malloc = _libraries['libccv'].malloc
malloc.restype = c_void_p
malloc.argtypes = [size_t]
calloc = _libraries['libccv'].calloc
calloc.restype = c_void_p
calloc.argtypes = [size_t, size_t]
realloc = _libraries['libccv'].realloc
realloc.restype = c_void_p
realloc.argtypes = [c_void_p, size_t]
free = _libraries['libccv'].free
free.restype = None
free.argtypes = [c_void_p]
valloc = _libraries['libccv'].valloc
valloc.restype = c_void_p
valloc.argtypes = [size_t]
abort = _libraries['libccv'].abort
abort.restype = None
abort.argtypes = []
atexit = _libraries['libccv'].atexit
atexit.restype = c_int
atexit.argtypes = [CFUNCTYPE(None)]
exit = _libraries['libccv'].exit
exit.restype = None
exit.argtypes = [c_int]
_Exit = _libraries['libccv']._Exit
_Exit.restype = None
_Exit.argtypes = [c_int]
getenv = _libraries['libccv'].getenv
getenv.restype = STRING
getenv.argtypes = [STRING]
putenv = _libraries['libccv'].putenv
putenv.restype = c_int
putenv.argtypes = [STRING]
setenv = _libraries['libccv'].setenv
setenv.restype = c_int
setenv.argtypes = [STRING, STRING, c_int]
unsetenv = _libraries['libccv'].unsetenv
unsetenv.restype = c_int
unsetenv.argtypes = [STRING]
mktemp = _libraries['libccv'].mktemp
mktemp.restype = STRING
mktemp.argtypes = [STRING]
mkstemp = _libraries['libccv'].mkstemp
mkstemp.restype = c_int
mkstemp.argtypes = [STRING]
mkstemps = _libraries['libccv'].mkstemps
mkstemps.restype = c_int
mkstemps.argtypes = [STRING, c_int]
mkdtemp = _libraries['libccv'].mkdtemp
mkdtemp.restype = STRING
mkdtemp.argtypes = [STRING]
system = _libraries['libccv'].system
system.restype = c_int
system.argtypes = [STRING]
realpath = _libraries['libccv'].realpath
realpath.restype = STRING
realpath.argtypes = [STRING, STRING]
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
bsearch = _libraries['libccv'].bsearch
bsearch.restype = c_void_p
bsearch.argtypes = [c_void_p, c_void_p, size_t, size_t, __compar_fn_t]
qsort = _libraries['libccv'].qsort
qsort.restype = None
qsort.argtypes = [c_void_p, size_t, size_t, __compar_fn_t]
qsort_r = _libraries['libccv'].qsort_r
qsort_r.restype = None
qsort_r.argtypes = [c_void_p, size_t, size_t, __compar_d_fn_t, c_void_p]
abs = _libraries['libccv'].abs
abs.restype = c_int
abs.argtypes = [c_int]
labs = _libraries['libccv'].labs
labs.restype = c_long
labs.argtypes = [c_long]
llabs = _libraries['libccv'].llabs
llabs.restype = c_longlong
llabs.argtypes = [c_longlong]
div = _libraries['libccv'].div
div.restype = div_t
div.argtypes = [c_int, c_int]
ldiv = _libraries['libccv'].ldiv
ldiv.restype = ldiv_t
ldiv.argtypes = [c_long, c_long]
lldiv = _libraries['libccv'].lldiv
lldiv.restype = lldiv_t
lldiv.argtypes = [c_longlong, c_longlong]
ecvt = _libraries['libccv'].ecvt
ecvt.restype = STRING
ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
fcvt = _libraries['libccv'].fcvt
fcvt.restype = STRING
fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
gcvt = _libraries['libccv'].gcvt
gcvt.restype = STRING
gcvt.argtypes = [c_double, c_int, STRING]
mblen = _libraries['libccv'].mblen
mblen.restype = c_int
mblen.argtypes = [STRING, size_t]
mbtowc = _libraries['libccv'].mbtowc
mbtowc.restype = c_int
mbtowc.argtypes = [WSTRING, STRING, size_t]
wctomb = _libraries['libccv'].wctomb
wctomb.restype = c_int
wctomb.argtypes = [STRING, c_wchar]
mbstowcs = _libraries['libccv'].mbstowcs
mbstowcs.restype = size_t
mbstowcs.argtypes = [WSTRING, STRING, size_t]
wcstombs = _libraries['libccv'].wcstombs
wcstombs.restype = size_t
wcstombs.argtypes = [STRING, WSTRING, size_t]
getsubopt = _libraries['libccv'].getsubopt
getsubopt.restype = c_int
getsubopt.argtypes = [POINTER(STRING), POINTER(STRING), POINTER(STRING)]
setkey = _libraries['libccv'].setkey
setkey.restype = None
setkey.argtypes = [STRING]
posix_openpt = _libraries['libccv'].posix_openpt
posix_openpt.restype = c_int
posix_openpt.argtypes = [c_int]
grantpt = _libraries['libccv'].grantpt
grantpt.restype = c_int
grantpt.argtypes = [c_int]
unlockpt = _libraries['libccv'].unlockpt
unlockpt.restype = c_int
unlockpt.argtypes = [c_int]
ptsname = _libraries['libccv'].ptsname
ptsname.restype = STRING
ptsname.argtypes = [c_int]
getloadavg = _libraries['libccv'].getloadavg
getloadavg.restype = c_int
getloadavg.argtypes = [POINTER(c_double), c_int]
memcpy = _libraries['libccv'].memcpy
memcpy.restype = c_void_p
memcpy.argtypes = [c_void_p, c_void_p, size_t]
memmove = _libraries['libccv'].memmove
memmove.restype = c_void_p
memmove.argtypes = [c_void_p, c_void_p, size_t]
memccpy = _libraries['libccv'].memccpy
memccpy.restype = c_void_p
memccpy.argtypes = [c_void_p, c_void_p, c_int, size_t]
memset = _libraries['libccv'].memset
memset.restype = c_void_p
memset.argtypes = [c_void_p, c_int, size_t]
memcmp = _libraries['libccv'].memcmp
memcmp.restype = c_int
memcmp.argtypes = [c_void_p, c_void_p, size_t]
memchr = _libraries['libccv'].memchr
memchr.restype = c_void_p
memchr.argtypes = [c_void_p, c_int, size_t]
memchr = _libraries['libccv'].memchr
memchr.restype = c_void_p
memchr.argtypes = [c_void_p, c_int, size_t]
strcpy = _libraries['libccv'].strcpy
strcpy.restype = STRING
strcpy.argtypes = [STRING, STRING]
strncpy = _libraries['libccv'].strncpy
strncpy.restype = STRING
strncpy.argtypes = [STRING, STRING, size_t]
strcat = _libraries['libccv'].strcat
strcat.restype = STRING
strcat.argtypes = [STRING, STRING]
strncat = _libraries['libccv'].strncat
strncat.restype = STRING
strncat.argtypes = [STRING, STRING, size_t]
strcmp = _libraries['libccv'].strcmp
strcmp.restype = c_int
strcmp.argtypes = [STRING, STRING]
strncmp = _libraries['libccv'].strncmp
strncmp.restype = c_int
strncmp.argtypes = [STRING, STRING, size_t]
strcoll = _libraries['libccv'].strcoll
strcoll.restype = c_int
strcoll.argtypes = [STRING, STRING]
strxfrm = _libraries['libccv'].strxfrm
strxfrm.restype = size_t
strxfrm.argtypes = [STRING, STRING, size_t]
strcoll_l = _libraries['libccv'].strcoll_l
strcoll_l.restype = c_int
strcoll_l.argtypes = [STRING, STRING, __locale_t]
strxfrm_l = _libraries['libccv'].strxfrm_l
strxfrm_l.restype = size_t
strxfrm_l.argtypes = [STRING, STRING, size_t, __locale_t]
strdup = _libraries['libccv'].strdup
strdup.restype = STRING
strdup.argtypes = [STRING]
strndup = _libraries['libccv'].strndup
strndup.restype = STRING
strndup.argtypes = [STRING, size_t]
strchr = _libraries['libccv'].strchr
strchr.restype = STRING
strchr.argtypes = [STRING, c_int]
strchr = _libraries['libccv'].strchr
strchr.restype = STRING
strchr.argtypes = [STRING, c_int]
strrchr = _libraries['libccv'].strrchr
strrchr.restype = STRING
strrchr.argtypes = [STRING, c_int]
strrchr = _libraries['libccv'].strrchr
strrchr.restype = STRING
strrchr.argtypes = [STRING, c_int]
strcspn = _libraries['libccv'].strcspn
strcspn.restype = size_t
strcspn.argtypes = [STRING, STRING]
strspn = _libraries['libccv'].strspn
strspn.restype = size_t
strspn.argtypes = [STRING, STRING]
strpbrk = _libraries['libccv'].strpbrk
strpbrk.restype = STRING
strpbrk.argtypes = [STRING, STRING]
strpbrk = _libraries['libccv'].strpbrk
strpbrk.restype = STRING
strpbrk.argtypes = [STRING, STRING]
strstr = _libraries['libccv'].strstr
strstr.restype = STRING
strstr.argtypes = [STRING, STRING]
strstr = _libraries['libccv'].strstr
strstr.restype = STRING
strstr.argtypes = [STRING, STRING]
strtok = _libraries['libccv'].strtok
strtok.restype = STRING
strtok.argtypes = [STRING, STRING]
strtok_r = _libraries['libccv'].strtok_r
strtok_r.restype = STRING
strtok_r.argtypes = [STRING, STRING, POINTER(STRING)]
strcasestr = _libraries['libccv'].strcasestr
strcasestr.restype = STRING
strcasestr.argtypes = [STRING, STRING]
strcasestr = _libraries['libccv'].strcasestr
strcasestr.restype = STRING
strcasestr.argtypes = [STRING, STRING]
memmem = _libraries['libccv'].memmem
memmem.restype = c_void_p
memmem.argtypes = [c_void_p, size_t, c_void_p, size_t]
strlen = _libraries['libccv'].strlen
strlen.restype = size_t
strlen.argtypes = [STRING]
strnlen = _libraries['libccv'].strnlen
strnlen.restype = size_t
strnlen.argtypes = [STRING, size_t]
strerror = _libraries['libccv'].strerror
strerror.restype = STRING
strerror.argtypes = [c_int]
strerror_r = _libraries['libccv'].strerror_r
strerror_r.restype = STRING
strerror_r.argtypes = [c_int, STRING, size_t]
__bzero = _libraries['libccv'].__bzero
__bzero.restype = None
__bzero.argtypes = [c_void_p, size_t]
bcopy = _libraries['libccv'].bcopy
bcopy.restype = None
bcopy.argtypes = [c_void_p, c_void_p, size_t]
bzero = _libraries['libccv'].bzero
bzero.restype = None
bzero.argtypes = [c_void_p, size_t]
bcmp = _libraries['libccv'].bcmp
bcmp.restype = c_int
bcmp.argtypes = [c_void_p, c_void_p, size_t]
index = _libraries['libccv'].index
index.restype = STRING
index.argtypes = [STRING, c_int]
index = _libraries['libccv'].index
index.restype = STRING
index.argtypes = [STRING, c_int]
rindex = _libraries['libccv'].rindex
rindex.restype = STRING
rindex.argtypes = [STRING, c_int]
rindex = _libraries['libccv'].rindex
rindex.restype = STRING
rindex.argtypes = [STRING, c_int]
ffs = _libraries['libccv'].ffs
ffs.restype = c_int
ffs.argtypes = [c_int]
ffsl = _libraries['libccv'].ffsl
ffsl.restype = c_int
ffsl.argtypes = [c_long]
strcasecmp = _libraries['libccv'].strcasecmp
strcasecmp.restype = c_int
strcasecmp.argtypes = [STRING, STRING]
strncasecmp = _libraries['libccv'].strncasecmp
strncasecmp.restype = c_int
strncasecmp.argtypes = [STRING, STRING, size_t]
strcasecmp_l = _libraries['libccv'].strcasecmp_l
strcasecmp_l.restype = c_int
strcasecmp_l.argtypes = [STRING, STRING, __locale_t]
strncasecmp_l = _libraries['libccv'].strncasecmp_l
strncasecmp_l.restype = c_int
strncasecmp_l.argtypes = [STRING, STRING, size_t, __locale_t]
strsep = _libraries['libccv'].strsep
strsep.restype = STRING
strsep.argtypes = [POINTER(STRING), STRING]
strsignal = _libraries['libccv'].strsignal
strsignal.restype = STRING
strsignal.argtypes = [c_int]
stpcpy = _libraries['libccv'].stpcpy
stpcpy.restype = STRING
stpcpy.argtypes = [STRING, STRING]
stpncpy = _libraries['libccv'].stpncpy
stpncpy.restype = STRING
stpncpy.argtypes = [STRING, STRING, size_t]
basename = _libraries['libccv'].basename
basename.restype = STRING
basename.argtypes = [STRING]
basename = _libraries['libccv'].basename
basename.restype = STRING
basename.argtypes = [STRING]
sigset_t = __sigset_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
fd_mask = __fd_mask
select = _libraries['libccv'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]
pselect = _libraries['libccv'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
u_char = __u_char
u_short = __u_short
u_int = __u_int
u_long = __u_long
quad_t = __quad_t
u_quad_t = __u_quad_t
fsid_t = __fsid_t
loff_t = __loff_t
ino_t = __ino_t
ino64_t = __ino64_t
dev_t = __dev_t
mode_t = __mode_t
nlink_t = __nlink_t
id_t = __id_t
daddr_t = __daddr_t
caddr_t = __caddr_t
key_t = __key_t
suseconds_t = __suseconds_t
ulong = c_ulong
ushort = c_ushort
uint = c_uint
u_int8_t = c_ubyte
u_int16_t = c_ushort
u_int32_t = c_uint
u_int64_t = c_ulong
register_t = c_long
blksize_t = __blksize_t
blkcnt_t = __blkcnt_t
fsblkcnt_t = __fsblkcnt_t
fsfilcnt_t = __fsfilcnt_t
blkcnt64_t = __blkcnt64_t
fsblkcnt64_t = __fsblkcnt64_t
fsfilcnt64_t = __fsfilcnt64_t
clock_t = __clock_t
time_t = __time_t
clockid_t = __clockid_t
timer_t = __timer_t
ssize_t = __ssize_t
gid_t = __gid_t
uid_t = __uid_t
off_t = __off_t
off64_t = __off64_t
useconds_t = __useconds_t
pid_t = __pid_t
intptr_t = __intptr_t
socklen_t = __socklen_t
access = _libraries['libccv'].access
access.restype = c_int
access.argtypes = [STRING, c_int]
lseek = _libraries['libccv'].lseek
lseek.restype = __off_t
lseek.argtypes = [c_int, __off_t, c_int]
close = _libraries['libccv'].close
close.restype = c_int
close.argtypes = [c_int]
read = _libraries['libccv'].read
read.restype = ssize_t
read.argtypes = [c_int, c_void_p, size_t]
write = _libraries['libccv'].write
write.restype = ssize_t
write.argtypes = [c_int, c_void_p, size_t]
pread = _libraries['libccv'].pread
pread.restype = ssize_t
pread.argtypes = [c_int, c_void_p, size_t, __off_t]
pwrite = _libraries['libccv'].pwrite
pwrite.restype = ssize_t
pwrite.argtypes = [c_int, c_void_p, size_t, __off_t]
pipe = _libraries['libccv'].pipe
pipe.restype = c_int
pipe.argtypes = [POINTER(c_int)]
alarm = _libraries['libccv'].alarm
alarm.restype = c_uint
alarm.argtypes = [c_uint]
sleep = _libraries['libccv'].sleep
sleep.restype = c_uint
sleep.argtypes = [c_uint]
ualarm = _libraries['libccv'].ualarm
ualarm.restype = __useconds_t
ualarm.argtypes = [__useconds_t, __useconds_t]
usleep = _libraries['libccv'].usleep
usleep.restype = c_int
usleep.argtypes = [__useconds_t]
pause = _libraries['libccv'].pause
pause.restype = c_int
pause.argtypes = []
chown = _libraries['libccv'].chown
chown.restype = c_int
chown.argtypes = [STRING, __uid_t, __gid_t]
fchown = _libraries['libccv'].fchown
fchown.restype = c_int
fchown.argtypes = [c_int, __uid_t, __gid_t]
lchown = _libraries['libccv'].lchown
lchown.restype = c_int
lchown.argtypes = [STRING, __uid_t, __gid_t]
chdir = _libraries['libccv'].chdir
chdir.restype = c_int
chdir.argtypes = [STRING]
fchdir = _libraries['libccv'].fchdir
fchdir.restype = c_int
fchdir.argtypes = [c_int]
getcwd = _libraries['libccv'].getcwd
getcwd.restype = STRING
getcwd.argtypes = [STRING, size_t]
getwd = _libraries['libccv'].getwd
getwd.restype = STRING
getwd.argtypes = [STRING]
dup = _libraries['libccv'].dup
dup.restype = c_int
dup.argtypes = [c_int]
dup2 = _libraries['libccv'].dup2
dup2.restype = c_int
dup2.argtypes = [c_int, c_int]
execve = _libraries['libccv'].execve
execve.restype = c_int
execve.argtypes = [STRING, POINTER(STRING), POINTER(STRING)]
execv = _libraries['libccv'].execv
execv.restype = c_int
execv.argtypes = [STRING, POINTER(STRING)]
execle = _libraries['libccv'].execle
execle.restype = c_int
execle.argtypes = [STRING, STRING]
execl = _libraries['libccv'].execl
execl.restype = c_int
execl.argtypes = [STRING, STRING]
execvp = _libraries['libccv'].execvp
execvp.restype = c_int
execvp.argtypes = [STRING, POINTER(STRING)]
execlp = _libraries['libccv'].execlp
execlp.restype = c_int
execlp.argtypes = [STRING, STRING]
nice = _libraries['libccv'].nice
nice.restype = c_int
nice.argtypes = [c_int]
_exit = _libraries['libccv']._exit
_exit.restype = None
_exit.argtypes = [c_int]
pathconf = _libraries['libccv'].pathconf
pathconf.restype = c_long
pathconf.argtypes = [STRING, c_int]
fpathconf = _libraries['libccv'].fpathconf
fpathconf.restype = c_long
fpathconf.argtypes = [c_int, c_int]
sysconf = _libraries['libccv'].sysconf
sysconf.restype = c_long
sysconf.argtypes = [c_int]
confstr = _libraries['libccv'].confstr
confstr.restype = size_t
confstr.argtypes = [c_int, STRING, size_t]
getpid = _libraries['libccv'].getpid
getpid.restype = __pid_t
getpid.argtypes = []
getppid = _libraries['libccv'].getppid
getppid.restype = __pid_t
getppid.argtypes = []
getpgrp = _libraries['libccv'].getpgrp
getpgrp.restype = __pid_t
getpgrp.argtypes = []
getpgid = _libraries['libccv'].getpgid
getpgid.restype = __pid_t
getpgid.argtypes = [__pid_t]
setpgid = _libraries['libccv'].setpgid
setpgid.restype = c_int
setpgid.argtypes = [__pid_t, __pid_t]
setpgrp = _libraries['libccv'].setpgrp
setpgrp.restype = c_int
setpgrp.argtypes = []
setsid = _libraries['libccv'].setsid
setsid.restype = __pid_t
setsid.argtypes = []
getsid = _libraries['libccv'].getsid
getsid.restype = __pid_t
getsid.argtypes = [__pid_t]
getuid = _libraries['libccv'].getuid
getuid.restype = __uid_t
getuid.argtypes = []
geteuid = _libraries['libccv'].geteuid
geteuid.restype = __uid_t
geteuid.argtypes = []
getgid = _libraries['libccv'].getgid
getgid.restype = __gid_t
getgid.argtypes = []
getegid = _libraries['libccv'].getegid
getegid.restype = __gid_t
getegid.argtypes = []
getgroups = _libraries['libccv'].getgroups
getgroups.restype = c_int
getgroups.argtypes = [c_int, POINTER(__gid_t)]
setuid = _libraries['libccv'].setuid
setuid.restype = c_int
setuid.argtypes = [__uid_t]
setreuid = _libraries['libccv'].setreuid
setreuid.restype = c_int
setreuid.argtypes = [__uid_t, __uid_t]
seteuid = _libraries['libccv'].seteuid
seteuid.restype = c_int
seteuid.argtypes = [__uid_t]
setgid = _libraries['libccv'].setgid
setgid.restype = c_int
setgid.argtypes = [__gid_t]
setregid = _libraries['libccv'].setregid
setregid.restype = c_int
setregid.argtypes = [__gid_t, __gid_t]
setegid = _libraries['libccv'].setegid
setegid.restype = c_int
setegid.argtypes = [__gid_t]
fork = _libraries['libccv'].fork
fork.restype = __pid_t
fork.argtypes = []
vfork = _libraries['libccv'].vfork
vfork.restype = __pid_t
vfork.argtypes = []
ttyname = _libraries['libccv'].ttyname
ttyname.restype = STRING
ttyname.argtypes = [c_int]
ttyname_r = _libraries['libccv'].ttyname_r
ttyname_r.restype = c_int
ttyname_r.argtypes = [c_int, STRING, size_t]
isatty = _libraries['libccv'].isatty
isatty.restype = c_int
isatty.argtypes = [c_int]
ttyslot = _libraries['libccv'].ttyslot
ttyslot.restype = c_int
ttyslot.argtypes = []
link = _libraries['libccv'].link
link.restype = c_int
link.argtypes = [STRING, STRING]
symlink = _libraries['libccv'].symlink
symlink.restype = c_int
symlink.argtypes = [STRING, STRING]
readlink = _libraries['libccv'].readlink
readlink.restype = ssize_t
readlink.argtypes = [STRING, STRING, size_t]
unlink = _libraries['libccv'].unlink
unlink.restype = c_int
unlink.argtypes = [STRING]
rmdir = _libraries['libccv'].rmdir
rmdir.restype = c_int
rmdir.argtypes = [STRING]
tcgetpgrp = _libraries['libccv'].tcgetpgrp
tcgetpgrp.restype = __pid_t
tcgetpgrp.argtypes = [c_int]
tcsetpgrp = _libraries['libccv'].tcsetpgrp
tcsetpgrp.restype = c_int
tcsetpgrp.argtypes = [c_int, __pid_t]
getlogin = _libraries['libccv'].getlogin
getlogin.restype = STRING
getlogin.argtypes = []
getlogin_r = _libraries['libccv'].getlogin_r
getlogin_r.restype = c_int
getlogin_r.argtypes = [STRING, size_t]
setlogin = _libraries['libccv'].setlogin
setlogin.restype = c_int
setlogin.argtypes = [STRING]
gethostname = _libraries['libccv'].gethostname
gethostname.restype = c_int
gethostname.argtypes = [STRING, size_t]
sethostname = _libraries['libccv'].sethostname
sethostname.restype = c_int
sethostname.argtypes = [STRING, size_t]
sethostid = _libraries['libccv'].sethostid
sethostid.restype = c_int
sethostid.argtypes = [c_long]
getdomainname = _libraries['libccv'].getdomainname
getdomainname.restype = c_int
getdomainname.argtypes = [STRING, size_t]
setdomainname = _libraries['libccv'].setdomainname
setdomainname.restype = c_int
setdomainname.argtypes = [STRING, size_t]
revoke = _libraries['libccv'].revoke
revoke.restype = c_int
revoke.argtypes = [STRING]
#profil = _libraries['libccv'].profil
#profil.restype = c_int
#profil.argtypes = [POINTER(c_ushort), size_t, size_t, c_uint]
acct = _libraries['libccv'].acct
acct.restype = c_int
acct.argtypes = [STRING]
getusershell = _libraries['libccv'].getusershell
getusershell.restype = STRING
getusershell.argtypes = []
endusershell = _libraries['libccv'].endusershell
endusershell.restype = None
endusershell.argtypes = []
setusershell = _libraries['libccv'].setusershell
setusershell.restype = None
setusershell.argtypes = []
daemon = _libraries['libccv'].daemon
daemon.restype = c_int
daemon.argtypes = [c_int, c_int]
chroot = _libraries['libccv'].chroot
chroot.restype = c_int
chroot.argtypes = [STRING]
getpass = _libraries['libccv'].getpass
getpass.restype = STRING
getpass.argtypes = [STRING]
fsync = _libraries['libccv'].fsync
fsync.restype = c_int
fsync.argtypes = [c_int]
gethostid = _libraries['libccv'].gethostid
gethostid.restype = c_long
gethostid.argtypes = []
sync = _libraries['libccv'].sync
sync.restype = None
sync.argtypes = []
getpagesize = _libraries['libccv'].getpagesize
getpagesize.restype = c_int
getpagesize.argtypes = []
getdtablesize = _libraries['libccv'].getdtablesize
getdtablesize.restype = c_int
getdtablesize.argtypes = []
truncate = _libraries['libccv'].truncate
truncate.restype = c_int
truncate.argtypes = [STRING, __off_t]
ftruncate = _libraries['libccv'].ftruncate
ftruncate.restype = c_int
ftruncate.argtypes = [c_int, __off_t]
brk = _libraries['libccv'].brk
brk.restype = c_int
brk.argtypes = [c_void_p]
sbrk = _libraries['libccv'].sbrk
sbrk.restype = c_void_p
sbrk.argtypes = [intptr_t]
syscall = _libraries['libccv'].syscall
syscall.restype = c_long
syscall.argtypes = [c_long]
lockf = _libraries['libccv'].lockf
lockf.restype = c_int
lockf.argtypes = [c_int, c_int, __off_t]
fdatasync = _libraries['libccv'].fdatasync
fdatasync.restype = c_int
fdatasync.argtypes = [c_int]
crypt = _libraries['libccv'].crypt
crypt.restype = STRING
crypt.argtypes = [STRING, STRING]
encrypt = _libraries['libccv'].encrypt
encrypt.restype = None
encrypt.argtypes = [STRING, c_int]
swab = _libraries['libccv'].swab
swab.restype = None
swab.argtypes = [c_void_p, c_void_p, ssize_t]
class locale_data(Structure):
    pass
__locale_struct._fields_ = [
    ('__locales', POINTER(locale_data) * 13),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', STRING * 13),
]
locale_data._fields_ = [
]
locale_t = __locale_t
posix_memalign = _libraries['libccv'].posix_memalign
posix_memalign.restype = c_int
posix_memalign.argtypes = [POINTER(c_void_p), size_t, size_t]

# values for enumeration '_mm_hint'
_mm_hint = c_int # enum
__all__ = ['ccv_dpm_param_t', '__uint16_t', '_SC_SYSTEM_DATABASE',
           'cbrtf', 'nearbyint', 'ccv_visualize', 'ccv_resample',
           'getc_unlocked', 'cbrtl', 'nearbyintf', 'int_fast32_t',
           'acosl', 'memset', 'ldexpl',
           '_CS_V7_WIDTH_RESTRICTED_ENVS', 'ccv_normalize',
           '_CS_POSIX_V6_ILP32_OFFBIG_LINTFLAGS', '_SC_XOPEN_LEGACY',
           'ldexpf', '_SC_XOPEN_VERSION', '_SC_BC_DIM_MAX',
           'N14pthread_cond_t4DOT_20E', 'uint8_t', 'fpos_t', 'setsid',
           'log2l', 'CCV_IO_ANY_FILE',
           '_CS_POSIX_V7_ILP32_OFFBIG_LINTFLAGS', 'ftell', 'CCV_C4',
           'ccv_bbf_new_param_t', 'CCV_C1', 'CCV_C2', 'CCV_C3',
           '_G_int16_t', 'getline', 'execle', 'getenv', 'ffs',
           'rand_r', '_SC_NZERO', 'scalbnf', 'fclose',
           '_SC_NPROCESSORS_CONF', 'scalbnl', 'getc', 'getloadavg',
           '_CS_LFS64_LINTFLAGS', 'seteuid',
           '_CS_POSIX_V6_LP64_OFF64_LIBS', '__time_t',
           '_SC_ULONG_MAX', '__pid_t', 'CCV_UNMANAGED',
           'CCV_C_TRANSPOSE', 'ccv_sparse_matrix_t',
           'ccv_swt_param_t', 'mbstowcs', '_SC_EQUIV_CLASS_MAX',
           'fmod', '_SC_V6_ILP32_OFFBIG', 'fileno_unlocked',
           'N16pthread_rwlock_t4DOT_23E', '_CS_LFS_LINTFLAGS',
           '_CS_LFS_LDFLAGS', 'pthread_rwlock_t', 'tanf', 'sleep',
           'atoi', 'fdatasync', 'round', 'ccv_minimize_f', 'expm1f',
           'cosf', 'getlogin_r', '__uint64_t', 'nexttoward',
           '_CS_POSIX_V6_LP64_OFF64_LINTFLAGS', 'snprintf',
           'getpagesize', '__va_list_tag', '__off64_t', 'sync',
           'cosh', '_CS_POSIX_V6_ILP32_OFF32_LINTFLAGS',
           '_SC_PII_INTERNET_STREAM', 'strcasestr', 'acosf',
           '_POSIX_', 'u_int32_t', '_SC_THREADS', 'strsep',
           'ccv_bbf_param_t', '__nan', 'asin',
           '_CS_POSIX_V7_ILP32_OFFBIG_LDFLAGS', 'ccv_shift',
           '_SC_INT_MIN', 'atexit', '_SC_UINT_MAX', '_SC_PASS_MAX',
           'erf', 'nanf', 'access', '_SC_XOPEN_XCU_VERSION',
           '_SC_SS_REPL_MAX', 'abs', '_PC_SOCK_MAXBUF', 'id_t',
           '_SC_THREAD_KEYS_MAX', 'CCV_DPM_NO_NESTED', 'ualarm',
           'expm1l', '__codecvt_partial', 'llroundf', '_MM_HINT_T1',
           '_MM_HINT_T0', '_MM_HINT_T2', '_SC_2_PBS', 'fmax',
           'matherr', 'copysign', '_SC_TRACE_INHERIT',
           '_IO_cookie_io_functions_t', '_SC_REGEXP',
           'CCV_IO_ATTEMPTED', 'log2f', 'drem', '_SC_NL_NMAX',
           '_CS_POSIX_V6_LP64_OFF64_CFLAGS', '_SC_V7_ILP32_OFFBIG',
           'sinf', '_SC_LEVEL4_CACHE_LINESIZE', 'getsid', 'trunc',
           'ccv_comp_t', 'lroundf', 'gethostname', 'strtok',
           'CCV_IO_BINARY_FILE', 'popen', '_SC_XOPEN_CRYPT',
           'lroundl', 'pthread_t', 'vsscanf', '_SC_POLL',
           '_PC_CHOWN_RESTRICTED', 'nextafter',
           'CCV_SPARSE_ROW_MAJOR', 'ccv_sample_up', 'vfork', 'strtof',
           'uint_fast8_t', 'ccv_set_sparse_matrix_cell',
           '__io_read_fn', 'cbrt', '__mode_t', 'malloc',
           'CCV_DENSE_VECTOR', 'CCV_IO_DEFLATE_STREAM',
           '_SC_MB_LEN_MAX', '_mm_hint', 'brk', '_SC_MQ_PRIO_MAX',
           'unlockpt', '_LIB_VERSION_TYPE', 'select', 'getchar',
           'labs', '_SC_BARRIERS', 'u_quad_t', '_MM_HINT_NTA',
           'fdimf', '__loff_t', '_SC_STREAMS', 'fdiml',
           '_SC_FILE_LOCKING', 'CCV_GSEDT', '_SC_2_LOCALEDEF',
           '_SC_STREAM_MAX', 'uint_least32_t', 'int_least64_t',
           'srand', 'unlink', 'CCV_IO_BMP_FILE', 'CCV_B_TRANSPOSE',
           'ccv_load_dpm_mixture_model',
           '_CS_POSIX_V7_ILP32_OFF32_LIBS', 'ssize_t', 'nexttowardf',
           'ferror_unlocked', '__int8_t', 'strtoll_l',
           '__fsblkcnt64_t', 'nexttowardl', 'ccv_contour_push',
           'strtold', 'llrintl', 'CCV_BBF_FLOAT_OPT', '_SC_WORD_BIT',
           'ccv_array_new', 'CCV_NO_PADDING', 'pthread_barrierattr_t',
           '_CS_XBS5_ILP32_OFF32_LIBS', 'ulong', 'chdir',
           '_PC_REC_MIN_XFER_SIZE', '_PC_PATH_MAX',
           '_SC_SPORADIC_SERVER', '_SC_PII_SOCKET', 'strerror',
           'ccv_get_sparse_matrix_vector', 'strtoq', '__fsfilcnt64_t',
           '_SC_NPROCESSORS_ONLN', '_CS_POSIX_V6_LPBIG_OFFBIG_LIBS',
           '_PC_MAX_INPUT', '_IO_FILE', 'mktemp', 'pthread_key_t',
           'fprintf', 'roundl', '_SC_VERSION', '__locale_struct',
           '_SC_CLK_TCK', 'CCV_32F', '_SC_THREAD_ROBUST_PRIO_PROTECT',
           'lockf', 'sysconf', 'atof', 'pclose', 'off_t',
           '_SC_AIO_MAX', 'ttyname_r', 'abort', 'CCV_32S', 'strtoll',
           '_CS_XBS5_ILP32_OFFBIG_LIBS', '__fpclassifyf', 'tan',
           '__locale_t', 'feof', 'ccv_distance_transform', 'strncat',
           '__pthread_list_t', '_SC_THREAD_PRIO_INHERIT', 'chroot',
           'clearerr', 'atanf', '_PC_2_SYMLINKS', 'lcong48',
           'lrand48', 'atanh', 'ccv_bbf_classifier_cascade_free',
           'atanl', 'write', 'signgam', '_IEEE_', 'rewind',
           '_CS_XBS5_LP64_OFF64_CFLAGS', 'erfc', 'putc_unlocked',
           'sin', 'bsearch', 'flockfile', 'CCV_A_TRANSPOSE', 'atan',
           'setuid', '_SC_SPAWN', 'getppid',
           '_CS_POSIX_V7_ILP32_OFF32_LDFLAGS',
           '_SC_THREAD_PRIO_PROTECT', '_SC_TRACE_EVENT_NAME_MAX',
           'key_t', 'ccv_contour_t', 'uint', 'valloc', 'drand48_data',
           'pthread_rwlockattr_t', '__swblk_t', 'strcasecmp',
           '_CS_LFS64_LDFLAGS', 'ccv_matrix_cell_t',
           '_CS_POSIX_V6_LPBIG_OFFBIG_CFLAGS', 'ccv_cache_init',
           '__rlim64_t', '_SC_TRACE_SYS_MAX', 'strerror_r',
           '_SC_NL_ARGMAX', 'ccv_sobel', 'CCV_L2_NORM', '__u_int',
           'atan2', 'setpgrp', 'ccv_enable_default_cache',
           '_SC_LEVEL3_CACHE_ASSOC', 'CCV_SPARSE_VECTOR',
           'N4wait3DOT_9E', '__clock_t', 'fcvt', '__fsfilcnt_t',
           '_SC_USER_GROUPS', 'endusershell', 'coshf', 'ccv_multiply',
           'getdomainname', 'ccv_array_free_immediately',
           'ccv_dpm_new_param_t', '_SC_AIO_PRIO_DELTA_MAX', 'revoke',
           'CCV_PADDING_MIRROR', 'strtouq', '_SC_MONOTONIC_CLOCK',
           '_SC_PII_OSI_M', '_SC_LEVEL3_CACHE_SIZE', 'strcasecmp_l',
           'FILE', '_SC_XOPEN_ENH_I18N', 'size_t', 'y0', 'pathconf',
           'seed48', 'CCV_DAISY_NORMAL_PARTIAL', 'ccv_slice',
           'strtol_l', 'ccv_point_t', 'fwrite',
           '_SC_MEMORY_PROTECTION', '_SC_T_IOV_MAX', 'roundf',
           'fdopen', 'uint_least16_t', 'ccv_get_sparse_matrix',
           'ccv_bbf_stage_classifier_t', 'asprintf', 'setgid',
           'feof_unlocked', '__qaddr_t', '__FILE', 'getlogin',
           'remquo', 'ccv_canny', 'CCV_POSITIVE', 'ccv_cache_out',
           'yn', 'N14ccv_keypoint_t4DOT_644DOT_65E', 'bcopy',
           '_SC_SPIN_LOCKS', '__bzero',
           '_CS_POSIX_V7_LP64_OFF64_LINTFLAGS', 'strcoll_l',
           '_SC_XOPEN_SHM', 'fpos64_t', '_SC_PRIORITY_SCHEDULING',
           'uid_t', 'cookie_write_function_t', '_exit',
           'getchar_unlocked', 'u_int16_t', 'strcoll', 'execl',
           'ccv_matrix_t', 'gets', '_SC_SEM_NSEMS_MAX',
           '_SC_LEVEL1_ICACHE_SIZE', 'ccv_bbf_detect_objects',
           'strchr', 'gcvt', '_CS_V5_WIDTH_RESTRICTED_ENVS',
           '__int32_t', 'getpgid', 'ccv_any_nan', '_SC_FSYNC',
           '_SC_GETGR_R_SIZE_MAX', '_SC_PII_INTERNET_DGRAM',
           '__u_short', 'execv', 'getw', '__uint32_t', 'memchr',
           'pthread_spinlock_t', '_SC_TRACE_NAME_MAX',
           '_SC_BC_BASE_MAX', 'sqrtl', 'ccv_dpm_detect_objects',
           '__fd_mask', '_CS_XBS5_LP64_OFF64_LINTFLAGS', 'logf',
           '_SC_XOPEN_STREAMS', 'logb', 'sinhf',
           '_SC_DEVICE_SPECIFIC', '_SC_GETPW_R_SIZE_MAX', 'clock_t',
           'logl', 'ccv_dense_matrix', '_SC_CPUTIME', 'sinhl',
           'fchdir', 'uint_fast16_t', '__useconds_t', 'vasprintf',
           '_SC_XBS5_ILP32_OFFBIG', '_IO_jump_t',
           'ccv_minimize_param_t', 'ccv_otsu', '_SC_INT_MAX', 'div_t',
           '_SC_TRACE_EVENT_FILTER', 'profil', '__log2',
           '_SC_PII_OSI_COTS', 'sprintf', 'atan2l', 'vscanf',
           'strrchr', '_SC_THREAD_ATTR_STACKADDR', 'atan2f',
           'uint_least8_t', '_SC_CHAR_MAX', 'pthread_barrier_t',
           'usleep', '_SC_OPEN_MAX', 'log2', 'fmaxf',
           '_SC_2_FORT_RUN', 'fileno', '_SC_LEVEL1_ICACHE_LINESIZE',
           '__pthread_internal_list', 'setlogin', 'getcwd',
           'N30ccv_compressed_sparse_matrix_t4DOT_46E',
           'CCV_UNSIGNED', 'getusershell', '_SC_RE_DUP_MAX',
           'N18ccv_dense_matrix_t4DOT_36E', 'copysignf',
           '__gnuc_va_list', '_CS_POSIX_V6_ILP32_OFF32_LDFLAGS',
           'nice', 'mode_t', 'qsort_r', '_SC_2_PBS_CHECKPOINT',
           'remainder', 'realpath', 'CCV_GARBAGE', 'expm1', 'fseeko',
           '_SC_TIMERS', 'CCV_IO_JPEG_STREAM', 'atoll',
           '_SC_XBS5_LPBIG_OFFBIG', 'ccv_decompress_sparse_matrix',
           'fsync', '_SC_SHARED_MEMORY_OBJECTS', '_SC_XOPEN_XPG4',
           'erff', 'jrand48', 'setkey', 'CCV_DAISY_NORMAL_FULL',
           'pthread_attr_t', '_SC_XOPEN_XPG2', '_SC_XOPEN_XPG3',
           'fmodf', 'ferror', 'erfl', 'ino_t', '_PC_ALLOC_SIZE_MIN',
           'N14ccv_keypoint_t4DOT_644DOT_66E',
           '_SC_READER_WRITER_LOCKS', '_SC_NETWORKING',
           '_ccv_get_sparse_prime', 'rint', 'ccv_dense_matrix_t',
           'floorl', '_SC_MEMLOCK_RANGE', '_SC_PII_INTERNET',
           '_SC_NL_LANGMAX', 'ldexp', 'calloc', '__blksize_t',
           'CCV_8U', '_PC_VDISABLE', 'acct', '_PC_MAX_CANON',
           'strncpy', '_SC_MEMLOCK', 'strtoull_l',
           '_SC_THREAD_THREADS_MAX', 'ecvt', '_SC_LOGIN_NAME_MAX',
           'exp2', 'scanf', 'qsort', 'system', 'ilogb', 'optind',
           '_SC_2_C_BIND', 'N4wait4DOT_10E', 'ino64_t',
           '_PC_NO_TRUNC', 'CCV_BBF_NO_NESTED', 'memcmp',
           '_SC_V7_ILP32_OFF32', 'ccv_compressed_sparse_matrix_t',
           'clearerr_unlocked', 'fma', '__mbstate_t', 'nearbyintl',
           '_SC_SHELL', 'confstr', 'ccv_mser', 'setbuffer',
           '_CS_POSIX_V7_ILP32_OFF32_LINTFLAGS',
           '_CS_GNU_LIBC_VERSION', '_SC_SINGLE_PROCESS', 'strcat',
           'CCV_IO_JPEG_FILE', 'ccv_filter_kernel_f',
           '_SC_SEM_VALUE_MAX', '_SC_C_LANG_SUPPORT_R',
           'CCV_IO_PLAIN_STREAM', '_SC_MQ_OPEN_MAX',
           'CCV_PADDING_ZERO', 'ccv_daisy_param_t',
           '_CS_POSIX_V7_ILP32_OFF32_CFLAGS', 'CCV_INTER_AREA',
           '_SC_CHAR_MIN', 'copysignl', 'N11__mbstate_t3DOT_5E',
           'quad_t', '_CS_XBS5_ILP32_OFF32_CFLAGS',
           'CCV_INTER_LANCZOS', 'va_list', '_SC_HOST_NAME_MAX',
           '_SC_THREAD_STACK_MIN', 'expl', '_SC_TIMEOUTS',
           'ccv_dpm_mixture_model_new', 'dup2', '_SC_IPV6',
           '_CS_XBS5_LPBIG_OFFBIG_LINTFLAGS', '_SC_CHILD_MAX',
           'vsnprintf', 'setusershell', 'pthread_cond_t',
           'ccv_array_free', 'remainderf', '_SC_2_PBS_MESSAGE',
           'strtok_r', '__caddr_t', 'getpass', '_SC_2_C_DEV',
           '_SC_TIMER_MAX', 'stpcpy', 'FP_ZERO', 'blkcnt_t',
           '__rlim_t', 'setstate', 'nlink_t', '__uint8_t',
           'strncasecmp', '_PC_REC_XFER_ALIGN', 'geteuid',
           'CCV_MATRIX_CSR', '_SC_REALTIME_SIGNALS', 'CCV_IO_FINAL',
           'timeval', '_SC_V6_LP64_OFF64', '__int64_t',
           'ccv_compress_sparse_matrix', 'frexpl', 'wctomb',
           '_SC_LEVEL2_CACHE_SIZE', '_SC_DEVICE_IO', 'CCV_MATRIX_CSC',
           '_SC_NL_MSGMAX', '__u_char', 'frexpf', 'printf',
           'ccv_dpm_root_classifier_t', '_SC_SCHAR_MIN',
           'CCV_MATRIX_DENSE', '_SC_SELECT', 'significand',
           '__clockid_t', 'powl', 'CCV_IO_ANY_STREAM',
           'ccv_dense_matrix_new', 'getpid',
           'ccv_bbf_classifier_cascade_new', 'ccv_array_group_f',
           'CCV_DAISY_NORMAL_SIFT', 'ccv_contour_new', '_PC_ASYNC_IO',
           'u_int', 'opterr', 'logbl', '_CS_LFS_CFLAGS',
           'ccv_disable_cache', 'nanl', 'dprintf', 'CCV_INTER_LINEAR',
           'ccv_cache_delete', 'srand48', 'ccv_array_zero',
           '_SC_NL_TEXTMAX', 'fsblkcnt_t', 'CCV_BBF_GENETIC_OPT',
           '_SC_MAPPED_FILES', 'suseconds_t', 'pipe',
           '_SC_PII_OSI_CLTS', '__quad_t', 'llrint', '__key_t',
           '_SC_NGROUPS_MAX', '_SC_DEVICE_SPECIFIC_R', 'ccv_flatten',
           'dev_t', '__uid_t', '_CS_POSIX_V6_LPBIG_OFFBIG_LINTFLAGS',
           '_CS_POSIX_V7_LPBIG_OFFBIG_CFLAGS', 'setvbuf', '_SVID_',
           '__pthread_mutex_s', '_SC_LEVEL4_CACHE_SIZE',
           '_SC_SEMAPHORES', '_CS_LFS64_CFLAGS', 'CCV_INTER_CUBIC',
           'a64l', 'random', 'fsfilcnt_t', 'putchar_unlocked',
           'ccv_make_array_mutable', 'strtoull', 'locale_data',
           'realloc', '_SC_C_LANG_SUPPORT', '_Exit', 'ccv_sum',
           'strtol', 'fputc', 'pause', 'fmodl',
           'ccv_make_array_immutable', 'ccv_matrix_free_immediately',
           'strtod', '_SC_TRACE_LOG', '__fpclassify', '_SC_CHAR_BIT',
           'mkstemps', 'frexp', 'coshl', 'off64_t', '_CS_LFS64_LIBS',
           'strtof_l', 'tcsetpgrp', '_SC_PIPE', 'llroundl',
           'ccv_mser_param_t', '_CS_POSIX_V6_LPBIG_OFFBIG_LDFLAGS',
           'intptr_t', 'l64a', 'lgammaf',
           '_CS_POSIX_V6_ILP32_OFF32_CFLAGS', 'CCV_IO_PNG_FILE',
           'tgamma', 'int_fast8_t', '_CS_XBS5_ILP32_OFF32_LINTFLAGS',
           '_SC_THREAD_DESTRUCTOR_ITERATIONS', 'lgammal', 'ceil',
           'N17ccv_cache_index_t4DOT_43E', 'bcmp',
           'ccv_make_matrix_mutable', 'strxfrm_l',
           'ccv_swt_detect_words', 'getpgrp', '_SC_BC_STRING_MAX',
           '_SC_UIO_MAXIOV', 'strtod_l', '_CS_XBS5_LPBIG_OFFBIG_LIBS',
           'memcpy', '_SC_2_SW_DEV', 'fmaf', 'ccv_invert', 'FP_NAN',
           'perror', 'srandom', 'locale_t', 'fscanf',
           'N17ccv_cache_index_t4DOT_42E', 'remove', '_G_fpos_t',
           'pthread_once_t', 'ccv_array_t', 'fd_mask', '_SC_ARG_MAX',
           '_SC_THREAD_PRIORITY_SCHEDULING', '__int16_t', '__timer_t',
           'cookie_close_function_t', 'mbtowc', 'nextafterl',
           'strtoul', '__ssize_t', 'comparison_fn_t', 'nextafterf',
           'atol', 'pthread_mutexattr_t', 'j0', 'j1',
           '_SC_THREAD_CPUTIME', 'y1',
           '_CS_POSIX_V7_ILP32_OFFBIG_LIBS', 'int16_t', 'div',
           'execlp', 'CCV_REUSABLE', 'wait', 'ccv_array_push',
           '_CS_POSIX_V6_ILP32_OFF32_LIBS', 'close', 'lgammaf_r',
           '__sigset_t', 'isnan', '_SC_SYNCHRONIZED_IO',
           'ccv_dense_vector_t', 'fgetpos', 'funlockfile', 'erand48',
           'encrypt', 'erfcf', 'posix_memalign',
           '_CS_POSIX_V6_LP64_OFF64_LDFLAGS', 'lgammal_r', 'erfcl',
           'ldiv_t', 'vdprintf', 'FP_INFINITE', 'strtold_l',
           'ccv_cache_index_t', 'scalbln', 'lrintl', 'CCV_L1_NORM',
           'isatty', 'timer_t', '_PC_FILESIZEBITS', 'ilogbl',
           'floorf', 'strdup', '__blkcnt64_t', 'ilogbf', 'setpgid',
           'atanhl', 'cos', 'uint64_t', '_IO_FILE_plus', 'CCV_FLIP_Y',
           'CCV_FLIP_X', 'atanhf', 'ushort', '_SC_USHRT_MAX', 'sinl',
           '_CS_XBS5_LPBIG_OFFBIG_CFLAGS', 'ccv_enable_cache',
           'ccv_dense_matrix_renew', 'clockid_t', '_SC_V7_LP64_OFF64',
           'fd_set', 'caddr_t', '_SC_SYMLOOP_MAX', 'uint16_t',
           'timespec', 'setregid', 'CCV_NEGATIVE', '_SC_XOPEN_UNIX',
           'sinh', 'ccv_size_t', 'ccv_array_group', 'double_t',
           'strxfrm', 'fmaxl', 'ccv_write', 'fmal', 'sys_nerr',
           'ccv_cache_cleanup', '__intptr_t', 'CCV_IO_CONTINUE',
           'ffsl', 'hypotf', 'getsubopt',
           '_CS_POSIX_V7_ILP32_OFFBIG_CFLAGS', 'puts', 'hypotl',
           'acoshl', 'obstack', '_CS_XBS5_ILP32_OFFBIG_LDFLAGS',
           'ccv_cache_close', '_SC_MULTI_PROCESS', 'fminf', 'putc',
           'acosh', '_SC_V7_LPBIG_OFFBIG', '_SC_NL_SETMAX',
           '_CS_POSIX_V7_LP64_OFF64_CFLAGS', 'rand', '__isnan',
           'fminl', '_SC_V6_LPBIG_OFFBIG', 'ccv_cache_put', 'asinl',
           '_SC_EXPR_NEST_MAX', 'pwrite', 'tmpnam',
           '_CS_POSIX_V6_ILP32_OFFBIG_CFLAGS', '__ino64_t',
           'u_int8_t', 'stpncpy', '__dev_t',
           '_CS_V6_WIDTH_RESTRICTED_ENVS', 'pselect', 'bzero',
           'execve', 'drand48', 'tanl', 'truncl', '__suseconds_t',
           '_SC_PAGESIZE', 'tanh', '_PC_REC_MAX_XFER_SIZE', 'fgetc',
           'u_long', 'scalblnl', 'truncf', 'lgamma',
           'ccv_dpm_part_classifier_t', 'N14ccv_keypoint_t4DOT_64E',
           '_SC_DELAYTIMER_MAX', 'ccv_daisy', 'vsprintf',
           'ccv_keypoint_t', '_SC_SHRT_MIN', 'rename', 'log10l',
           '_SC_LONG_BIT', 'scalblnf', 'ccv_eigen', 'sethostid',
           'log10f', 'uintmax_t', 'getwd',
           '_SC_LEVEL3_CACHE_LINESIZE', 'ccv_filter_kernel',
           'ccv_zero', 'int_fast16_t', 'ccv_gemm', 'initstate',
           '__blkcnt_t', '_SC_XBS5_LP64_OFF64', 'time_t', 'u_short',
           'CCV_IO_COLOR', 'ccv_bbf_feature_t', 'blksize_t', 'fabs',
           'strnlen', '_CS_POSIX_V7_LPBIG_OFFBIG_LIBS', 'sqrt',
           '_SC_SIGQUEUE_MAX', '_IO_marker', 'fsblkcnt64_t',
           'ccv_sift_param_t', 'finite', '_SC_TZNAME_MAX', 'optarg',
           '_CS_PATH', 'ceilf', '_SC_SYSTEM_DATABASE_R', 'ccv_rect_t',
           'ceill', '__io_write_fn', '_SC_SCHAR_MAX',
           'ccv_get_sparse_matrix_cell', '__ino_t', '_SC_PHYS_PAGES',
           '_IO_lock_t', 'setbuf', '_SC_MESSAGE_PASSING', 'fchown',
           'readlink', '_CS_XBS5_LPBIG_OFFBIG_LDFLAGS',
           '_SC_THREAD_SAFE_FUNCTIONS', 'acoshf', 'ttyslot',
           '_CS_POSIX_V7_LPBIG_OFFBIG_LINTFLAGS', 'uint_fast64_t',
           '_PC_NAME_MAX', 'cookie_seek_function_t', 'lldiv_t',
           'u_char', 'nrand48', '_SC_TRACE_USER_EVENT_MAX',
           'pthread_mutex_t', 'scalb', 'log', 'uint32_t', 'ccv_read',
           'ccv_sparse_matrix_new', 'powf', 'ccv_norm',
           'strncasecmp_l', 'rindex', '_SC_AVPHYS_PAGES', 'lseek',
           '_SC_RAW_SOCKETS', '_SC_LEVEL1_DCACHE_ASSOC', 'rintf',
           '_SC_2_C_VERSION', '__isinff', 'ccv_matrix_eq',
           '_SC_LEVEL1_DCACHE_SIZE', '_SC_RTSIG_MAX', 'rintl',
           'register_t', 'ccv_contour_free', 'pthread_condattr_t',
           '_SC_PRIORITIZED_IO', '_SC_LEVEL4_CACHE_ASSOC', '__fsid_t',
           '_ISOC_', 'u_int64_t', 'fflush', 'random_data', 'getegid',
           '_PC_REC_INCR_XFER_SIZE', 'fabsf', 'ccv_cache_t',
           '_CS_XBS5_ILP32_OFFBIG_CFLAGS', '_SC_XBS5_ILP32_OFF32',
           'sethostname', 'ldiv', '_XOPEN_', 'ptsname',
           '_SC_USER_GROUPS_R', '_CS_POSIX_V7_LP64_OFF64_LIBS',
           'optopt', 'lchown', 'setdomainname', 'pow', 'CCV_IO_ERROR',
           '__u_quad_t', 'ccv_flip', '_CS_GNU_LIBPTHREAD_VERSION',
           'int32_t', 'modff', 'loff_t', '_SC_2_PBS_LOCATE',
           '_SC_V6_ILP32_OFF32', 'free', 'read', 'int_least32_t',
           'scalbn', 'setreuid', 'strcspn', '_SC_PII_XTI',
           '_PC_SYNC_IO', 'FP_NORMAL', '_SC_2_UPE', '_PC_LINK_MAX',
           'fabsl', '_G_uint32_t', '_SC_SSIZE_MAX', '_SC_IOV_MAX',
           'daemon', 'strstr', 'fputs', '_SC_TRACE', 'memmove',
           '_G_fpos64_t', '_SC_UCHAR_MAX', 'float_t', 'CCV_SIGNED',
           '_SC_FIFO', 'mblen', 'setegid', 'sigset_t',
           '_CS_POSIX_V6_ILP32_OFFBIG_LDFLAGS', '_SC_FILE_ATTRIBUTES',
           'freopen', 'strcpy', '__nlink_t', '__compar_fn_t',
           '_CS_POSIX_V7_LPBIG_OFFBIG_LDFLAGS', 'strcmp', 'tanhl',
           'tempnam', 'tmpfile', 'ccv_make_matrix_immutable', 'lldiv',
           '__io_close_fn', 'ccv_hog', 'tanhf', '__off_t',
           'ccv_root_comp_t', 'getdelim', 'intmax_t',
           'CCV_PADDING_EXTEND', '__codecvt_ok', 'fgets', 'swab',
           '_SC_THREAD_SPORADIC_SERVER', '_SC_BASE', 'crypt',
           'ctermid', '__id_t', 'cookie_io_functions_t', 'llrintf',
           'exp2f', '_SC_LINE_MAX', 'gid_t', 'int_least8_t',
           'putchar', 'socklen_t', 'exp2l', 'fsetpos', '__signbitf',
           'exit', 'CCV_SPARSE_COL_MAJOR', '__signbitl',
           'int_least16_t', 'CCV_MATRIX_SPARSE', 'mkdtemp', 'log1pl',
           'basename', 'modf', 'tgammal',
           '_CS_XBS5_LP64_OFF64_LDFLAGS', '_G_uint16_t', 'log1pf',
           'tgammaf', 'putw', 'symlink', '_SC_SIGNALS',
           '__codecvt_result', 'FP_SUBNORMAL',
           '_SC_LEVEL1_DCACHE_LINESIZE', 'ccv_solve', 'strlen',
           '_SC_PII_OSI', '_CS_LFS_LIBS', 'ccv_blur', '__fsblkcnt_t',
           'ccv_move', '_CS_POSIX_V6_ILP32_OFFBIG_LIBS', 'strpbrk',
           'ccv_bbf_classifier_cascade_t', 'fseek',
           'ccv_cache_index_free_f', 'sys_errlist', '__compar_d_fn_t',
           'logbf', '_SC_2_FORT_DEV', '_SC_FILE_SYSTEM', 'fmin',
           'ccv_filter', '_SC_PII', 'acos', 'ccv_gradient', 'gamma',
           'ccv_drain_cache', '_SC_SHRT_MAX', 'remquol',
           '_SC_ATEXIT_MAX', 'ftruncate', 'jn', 'fsfilcnt64_t',
           '_SC_SAVED_IDS', 'ccv_minimize', '__u_long',
           'ccv_subtract', 'gethostid', 'fopen', 'sqrtf', '__gid_t',
           'truncate', 'memccpy', '__io_seek_fn', '_SC_2_PBS_TRACK',
           'putenv', '_SC_THREAD_PROCESS_SHARED', '_SC_JOB_CONTROL',
           'ccv_bbf_classifier_cascade_read_binary', 'lround',
           '_CS_XBS5_LP64_OFF64_LIBS', 'llround', 'getdtablesize',
           '_SC_LEVEL2_CACHE_ASSOC', 'ccv_matrix_free', '__daddr_t',
           'rmdir', '_IO_cookie_file', '__sig_atomic_t',
           '_SC_LEVEL1_ICACHE_ASSOC', 'CCV_IO_PNG_STREAM', 'log10',
           'remquof', '_SC_CHARCLASS_NAME_MAX', 'fork',
           '_CS_XBS5_ILP32_OFFBIG_LINTFLAGS', 'uintptr_t', 'CCV_64S',
           'vprintf', '_SC_ADVISORY_INFO', 'strtoul_l',
           '_SC_XOPEN_REALTIME_THREADS',
           'N19ccv_sparse_matrix_t4DOT_40E', '_PC_SYMLINK_MAX',
           'int8_t', '_SC_THREAD_ROBUST_PRIO_INHERIT', 'cosl', 'dup',
           'ccv_mser_keypoint_t', 'ccv_cache_get', 'link', 'vfprintf',
           'CCV_64F', 'ccv_sift', '_CS_XBS5_ILP32_OFF32_LDFLAGS',
           'getuid', '_SC_COLL_WEIGHTS_MAX', 'lrint',
           '_SC_CLOCK_SELECTION', 'ccv_get_dense_matrix',
           '_PC_PRIO_IO', 'sbrk', 'fdim', '_SC_XOPEN_REALTIME',
           'ccv_trace', 'strspn', '__exception',
           'cookie_read_function_t', 'ungetc', '_PC_PIPE_BUF',
           'execvp', 'strncmp', 'log1p', 'alarm', 'blkcnt64_t',
           'llabs', 'lrintf', 'tcgetpgrp', 'sscanf', '__isnanf',
           '_SC_2_PBS_ACCOUNTING', 'strndup', 'syscall', 'grantpt',
           'mrand48', 'fread', 'ftello', 'asinh',
           '_SC_LEVEL2_CACHE_LINESIZE', '_SC_FD_MGMT', 'lgamma_r',
           'int64_t', 'strsignal', 'ccv_swt', 'ccv_swt_manual', 'getgid', 'wcstombs',
           'posix_openpt', 'ccv_dpm_mixture_model_t', 'floor',
           'CCV_IO_GRAY', 'index', 'ttyname', 'nan',
           '_SC_THREAD_ATTR_STACKSIZE', 'daddr_t',
           '_SC_REGEX_VERSION', 'setenv',
           'ccv_load_bbf_classifier_cascade',
           'ccv_bbf_classifier_cascade_write_binary', '_SC_2_VERSION',
           'getopt', 'mkstemp', 'int_fast64_t', 'vfscanf',
           'ftrylockfile', 'modfl', 'fsid_t', 'ccv_array_clear',
           'unsetenv', 'exp', 'ccv_dpm_mixture_model_free', 'expf',
           'asinf', '__codecvt_error', '_SC_TYPED_MEMORY_OBJECTS',
           '_SC_ASYNCHRONOUS_IO', 'hypot', '_SC_2_CHAR_TERM',
           'ccv_sample_down', 'isinf', '_SC_AIO_LISTIO_MAX',
           'useconds_t', 'remainderl', 'getgroups', 'uint_least64_t',
           '_SC_BC_SCALE_MAX', 'setlinebuf', '__isinf',
           'uint_fast32_t', '__socklen_t', 'ccv_sat', 'pread',
           'fpathconf', 'chown', 'memmem', 'pid_t', 'asinhf',
           '__codecvt_noconv', '_G_int32_t',
           'ccv_cache_generate_signature',
           '_CS_POSIX_V7_LP64_OFF64_LDFLAGS', '_SC_TTY_NAME_MAX',
           'asinhl']
