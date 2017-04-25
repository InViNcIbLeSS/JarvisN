from winreg import *
import itertools
aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', 0, KEY_READ)

for i in itertools.count():
	try:
		subname = EnumKey(aKey, i)
	except WindowsError:
		break
	print(subname)
	subkey = OpenKey(aKey, subname, 0, KEY_READ)
	print(subkey)
	pathname, regtype = QueryValueEx(subkey, r"InstallLocation")
	print(subname, pathname)
	CloseKey(subkey)