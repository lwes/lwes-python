#!/usr/bin/env python

"""
setup.py file for LWES binding
"""

from distutils.core import setup, Extension
import commands

def pkgconfig(*packages, **kw):
	flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
	for token in commands.getoutput("pkg-config --libs --cflags %s" % ' '.join(packages)).split():
		if flag_map.has_key(token[:2]):
			kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
		else:
			kw.setdefault('extra_link_args', []).append(token)
	for k, v in kw.iteritems():
		kw[k] = list(set(v))
	return kw	

lwes_module = Extension('_lwes',
                        sources=['lwes_wrap.c'],
			**pkgconfig('lwes-0')
                       )

setup (name='lwes',
       version = '0.0.1',
       author = "Michael P. Lum",
       description = """Python bindings for the Light Weight Event System""",
       ext_modules = [lwes_module],
       py_modules = ["lwes"],
      )

