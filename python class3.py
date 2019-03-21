Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name= "Nikki"
>>> age= "10"
>>> print(%s is %d years old."%(name,age)
	  
SyntaxError: invalid syntax
>>> phrase = "Akirachix"
	  
>>> print(phrase)
	  
Akirachix
>>> print("   /|")
	  
   /|
>>> print("   /|")
	  
   /|
>>> print
	  
<built-in function print>
>>> first name = "James"
	  
SyntaxError: invalid syntax
>>> balance=1000
	  
>>> print("   /|")
	  
   /|
>>> print("   /|")
	  
   /|
>>> first_name= "James"
	  
>>> balance= "1000"
	  
>>> second_name= "Jane"
	  
>>> balance= "1000"
	  
>>> print("Hello'{},'your balance is'{}".format(first_name,balance))
	  
Hello'James,'your balance is'1000
>>> print("Hello'{},'your balance is'{}".format(second_name,balance))
	  
Hello'Jane,'your balance is'1000
>>> name_1= "SUSAN"
	  
>>> type(a)
	  
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> a="car"
	  
>>> type(a)
	  
<class 'str'>
>>> b="10"
	  
>>> type(b)
	  
<class 'str'>
>>> s="Akirachix"
	  
>>> s.upper()
	  
'AKIRACHIX'
>>> s.lower()
	  
'akirachix'
>>> s.capitalise()
	  
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.capitalise()
AttributeError: 'str' object has no attribute 'capitalise'
>>> s.endswith(x)
	  
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.endswith(x)
NameError: name 'x' is not defined
>>> s.endswith("x")
	  
True
>>> s.endswith("k")
	  
False
>>> s.startswith("a")
	  
False
>>> s.startswith("A")
	  
True
>>> s.startswith("b")
	  
False
>>> s.is lower()
	  
SyntaxError: invalid syntax
>>> s.islower()
	  
False
>>> b.islower()
	  
False
>>> b.isupper()
	  
False
>>> b.isalpha()
	  
False
>>> b.isalnum()
	  
True
>>> b.isalpha()
	  
False
>>> s.replace("Akirachix","Codehive")
	  
'Codehive'
>>> s.replace("Codehive","Akirchix")
	  
'Akirachix'
>>> 
	  
>>> 
	  
>>> 
	  
>>> 
	  
>>> 'Akirachix'
	  
'Akirachix'
>>> s[0]
	  
'A'
>>> s[4]
	  
'a'
>>> s[7]
	  
'i'
>>> s[9]
	  
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s[9]
IndexError: string index out of range
>>> 
s[-9]
	  
'A'
>>> s[-1]
	  
'x'
>>> len(s)
	  
9
>>> s.len()
	  
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.len()
AttributeError: 'str' object has no attribute 'len'
>>> s[0:4]
	  
'Akir'
>>> s[2:7]
	  
'irach'
>>> s[5:8]
	  
'chi'
>>> s[5:9]
	  
'chix'
>>> s[5:10]
	  
'chix'
>>> s[5:11]
	  
'chix'
>>> s[3:]
	  
'rachix'
>>> s[:4]
	  
'Akir'
>>> s[-9:-6]
	  
'Aki'
>>> s-6:-9]
SyntaxError: invalid syntax
>>> s[-6:-9]
''
>>> s[-9:-5]
'Akir'
>>> s[0:4]==s[-9:-5]
True
>>> s[5:8]==s[-4:-1]
True
>>> s[5:9]==s[-4:0]
False
>>> s[3:]==s[-6:]
True
>>> s[5:9]
'chix'
>>> s[-4:0]
''
>>> s[5:9]==s[-4:]
True
>>> s[:4]==s[:-5]
True
>>> s[:4]!=s[:-5]
False
>>> first_name= "Nikki"
>>> second_name= "Antonine"
>>> fullname={}\t{}.format(first_name,second_name)
SyntaxError: unexpected character after line continuation character
>>> fullname= "{}\t{}".format(first_name,second_name)
>>> print(fullname)
Nikki	Antonine
>>> a=fullname[0:5]
>>> b=fullname[4:12]
>>> a==first_name
True
>>> b==second_name
False
>>> b=fullname[5:13]
>>> b==second_name
False
>>> b=fullname[5:]
>>> b==second_name
False
>>> b=fullname[4:]
>>> b==second_name
False
>>> b=fullname[5:]
>>> b==second_name[5:]
False
>>> b=fullname[5:13]
>>> b==secondname
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    b==secondname
NameError: name 'secondname' is not defined
>>> b=fullname[4:12]
>>> b==second_name
False
>>> b=fullname[4:13]
>>> b==secondname
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    b==secondname
NameError: name 'secondname' is not defined
>>> b=fullname[4:]
>>> b==secondname
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    b==secondname
NameError: name 'secondname' is not defined
>>> File "<pyshell#105>", line 1, in <module>b=fullname[4:13]
SyntaxError: invalid syntax
>>> b=fullname[5:13]
>>> b==second_name
False
>>> b=fullname[6:]
>>> b==second_name
True
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          atexit              http                runpy
__main__            audioop             hyperparser         runscript
_abc                autocomplete        idle                sched
_ast                autocomplete_w      idle_test           scrolledlist
_asyncio            autoexpand          idlelib             search
_bisect             base64              imaplib             searchbase
_blake2             bdb                 imghdr              searchengine
_bootlocale         binascii            imp                 secrets
_bz2                binhex              importlib           select
_codecs             bisect              inspect             selectors
_codecs_cn          browser             io                  setuptools
_codecs_hk          builtins            iomenu              shelve
_codecs_iso2022     bz2                 ipaddress           shlex
_codecs_jp          cProfile            itertools           shutil
_codecs_kr          calendar            json                signal
_codecs_tw          calltip             keyword             site
_collections        calltip_w           lib2to3             smtpd
_collections_abc    cgi                 linecache           smtplib
_compat_pickle      cgitb               locale              sndhdr
_compression        chunk               logging             socket
_contextvars        cmath               lzma                socketserver
_csv                cmd                 macosx              sqlite3
_ctypes             code                macpath             squeezer
_ctypes_test        codecontext         mailbox             sre_compile
_datetime           codecs              mailcap             sre_constants
_decimal            codeop              mainmenu            sre_parse
_dummy_thread       collections         marshal             ssl
_elementtree        colorizer           math                stackviewer
_functools          colorsys            mimetypes           stat
_hashlib            compileall          mmap                statistics
_heapq              concurrent          modulefinder        statusbar
_imp                config              msilib              string
_io                 config_key          msvcrt              stringprep
_json               configdialog        multicall           struct
_locale             configparser        multiprocessing     subprocess
_lsprof             contextlib          netrc               sunau
_lzma               contextvars         nntplib             symbol
_markupbase         copy                nt                  symtable
_md5                copyreg             ntpath              sys
_msi                crypt               nturl2path          sysconfig
_multibytecodec     csv                 numbers             tabnanny
_multiprocessing    ctypes              opcode              tarfile
_opcode             curses              operator            telnetlib
_operator           dataclasses         optparse            tempfile
_osx_support        datetime            os                  test
_overlapped         dbm                 outwin              textview
_pickle             debugger            paragraph           textwrap
_py_abc             debugger_r          parenmatch          this
_pydecimal          debugobj            parser              threading
_pyio               debugobj_r          pathbrowser         time
_queue              decimal             pathlib             timeit
_random             delegator           pdb                 tkinter
_sha1               difflib             percolator          token
_sha256             dis                 pickle              tokenize
_sha3               distutils           pickletools         tooltip
_sha512             doctest             pip                 trace
_signal             dummy_threading     pipes               traceback
_sitebuiltins       dynoption           pkg_resources       tracemalloc
_socket             easy_install        pkgutil             tree
_sqlite3            editor              platform            tty
_sre                email               plistlib            turtle
_ssl                encodings           poplib              turtledemo
_stat               ensurepip           posixpath           types
_string             enum                pprint              typing
_strptime           errno               profile             undo
_struct             faulthandler        pstats              unicodedata
_symtable           filecmp             pty                 unittest
_testbuffer         fileinput           py_compile          urllib
_testcapi           filelist            pyclbr              uu
_testconsole        fnmatch             pydoc               uuid
_testimportmultiple formatter           pydoc_data          venv
_testmultiphase     fractions           pyexpat             warnings
_thread             ftplib              pyparse             wave
_threading_local    functools           pyshell             weakref
_tkinter            gc                  python class3       webbrowser
_tracemalloc        genericpath         python lesson       window
_warnings           getopt              python2             winreg
_weakref            getpass             query               winsound
_weakrefset         gettext             queue               wsgiref
_winapi             glob                quopri              xdrlib
abc                 grep                random              xml
aifc                gzip                re                  xmlrpc
antigravity         hashlib             redirector          xxsubtype
argparse            heapq               replace             zipapp
array               help                reprlib             zipfile
ast                 help_about          rlcompleter         zipimport
asynchat            history             rpc                 zlib
asyncio             hmac                rstrip              zoomheight
asyncore            html                run                 zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help>





