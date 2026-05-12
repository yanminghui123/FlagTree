import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class FlagCXConfig:
    bitcode_path: str
    shared_lib_path: str

    def __post_init__(self):
        self.default_libdir = Path(__file__).parent / 'lib'
        self.bitcode_path = str(self.default_libdir / 'flagcx.bc')
        self.shared_lib_path = str(self.default_libdir / 'libflagcx.so')
        if not os.path.exists(self.bitcode_path):
            raise FileNotFoundError(f"FlagCX bitcode not found at {self.bitcode_path}")
        if not os.path.exists(self.shared_lib_path):
            raise FileNotFoundError(f"FlagCX shared library not found at {self.shared_lib_path}")


class Distributed:

    def __init__(self):
        self.is_use_flagcx = os.environ.get("USE_FLAGCX", "OFF") == "ON"
        self.extern_libs = {}
        if self.is_use_flagcx:
            self.extern_libs["flagcx"] = FlagCXConfig().bitcode_path

    def get_extern_libs(self):
        return self.extern_libs
