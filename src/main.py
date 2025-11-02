diff --git a/src/main.py b/src/main.py
index 5430e2d804073565ecb8dfaf1b1d544f63ed019a..6aa87b6cde9f70573bba73ca455bdea3ebf69625 100644
--- a/src/main.py
+++ b/src/main.py
@@ -1,62 +1,62 @@
 """Main file for UE4-DDS-Tools."""
 # std libs
 import argparse
 import json
 import os
 import time
 from contextlib import redirect_stdout
 import concurrent.futures
 import functools
 
 # my scripts
 from util import (compare, get_ext, get_temp_dir,
                   get_file_list, get_base_folder, remove_quotes,
                   check_python_version, is_windows)
 from unreal.uasset import Uasset, UASSET_EXT
 from directx.dds import DDS
 from directx.dxgi_format import DXGI_FORMAT
 from directx.texconv import Texconv
 
-TOOL_VERSION = "0.6.1"
+TOOL_VERSION = "0.6.2"
 
-# UE version: 4.0 ~ 5.4, ff7r, borderlands3
-UE_VERSIONS = ["4." + str(i) for i in range(28)] + ["5." + str(i) for i in range(5)] + ["ff7r", "borderlands3"]
+# UE version: 4.0 ~ 5.6, ff7r, borderlands3
+UE_VERSIONS = ["4." + str(i) for i in range(28)] + ["5." + str(i) for i in range(7)] + ["ff7r", "borderlands3"]
 
 # UE version for textures
 UTEX_VERSIONS = [
-    "5.4", "5.3", "5.2", "5.1", "5.0",
+    "5.6", "5.5", "5.4", "5.3", "5.2", "5.1", "5.0",
     "4.26 ~ 4.27", "4.24 ~ 4.25", "4.23", "4.20 ~ 4.22",
     "4.16 ~ 4.19", "4.15", "4.14", "4.12 ~ 4.13", "4.11", "4.10",
     "4.9", "4.8", "4.7", "4.4 ~ 4.6", "4.3", "4.0 ~ 4.2",
     "ff7r", "borderlands3"
 ]
 
 # Supported file extensions.
-TEXTURES = ["dds", "tga", "hdr"]
+TEXTURES = ["dds", "tga", "hdr", "png"]
 if is_windows():
-    TEXTURES += ["bmp", "jpg", "png"]
+    TEXTURES += ["bmp", "jpg"]
 
 # Supported image filters.
 IMAGE_FILTERS = ["point", "linear", "cubic"]
 
 
 def get_args():  # pragma: no cover
     parser = argparse.ArgumentParser()
     parser.add_argument("file", help="uasset, texture file, or folder")
     parser.add_argument("texture", nargs="?", help="texture file for injection mode.")
     parser.add_argument("--save_folder", default="output", type=str, help="output folder")
     parser.add_argument("--mode", default="inject", type=str,
                         help="valid, parse, inject, export, remove_mipmaps, check, convert, and copy are available.")
     parser.add_argument("--version", default=None, type=str,
                         help="UE version. it will overwrite the argument in config.json.")
     parser.add_argument("--export_as", default="dds", type=str,
                         help="format for export mode. dds, tga, png, jpg, and bmp are available.")
     parser.add_argument("--convert_to", default="tga", type=str,
                         help=("format for convert mode."
                               " tga, hdr, png, jpg, bmp, and DXGI formats (e.g. BC1_UNORM) are available."))
     parser.add_argument("--no_mipmaps", action="store_true",
                         help="force no mips to dds and uasset.")
     parser.add_argument("--force_uncompressed", action="store_true",
                         help="use uncompressed format for compressed texture assets.")
     parser.add_argument("--disable_tempfile", action="store_true",
                         help="store temporary files in the tool's directory.")
