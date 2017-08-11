import os
import sys

from pathlib import Path

if sys.platform == 'win32':
    from cx_Freeze import setup, Executable
else:
    from distutils.core import setup

sys.path.insert(0, "src")

company_name = 'FAF Community'
product_name = 'FAF Launcher'

if sys.platform == 'win32':
    msi_version = os.getenv('faf_version')

build_exe_options = {
    'include_msvcr': True,
    'optimize': 2,
    'silent': True,
    'zip_include_packages': ["*"],     # Place source files in zip archive, like in cx_freeze 4.3.4
    'zip_exclude_packages': [],
}

shortcut_table = [
    ('DesktopShortcut',           # Shortcut
     'DesktopFolder',             # Directory_
     'FA Forever Launcher'        # Name
     'TARGETDIR',                 # Component_
     '[TARGETDIR]FAFLauncher.exe',# Target
     None,                        # Arguments
     None,                        # Description
     None,                        # Hotkey
     None,                        # Icon
     None,                        # IconIndex
     None,                        # ShowCmd
     'TARGETDIR'                  # WkDir
     )
]

target_dir = '[ProgramFilesFolder][ProductName]'
upgrade_code = '{487DA9B9-0BA7-4C11-BC0D-C97230747D55}'

bdist_msi_options = {
    'upgrade_code': upgrade_code,
    'initial_target_dir': target_dir,
    'add_to_path': False,
    'data': {'Shortcut': shortcut_table},
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

if sys.platform == 'win32':
    platform_options = {
        'executables': [Executable(
                          'src/__main__.py',
                          base=base,
                          targetName='FAFLauncher.exe',
                          icon='res/faf.ico'
                      )],
        'requires': ['cx_Freeze'],
        'options': {'build_exe': build_exe_options,
                 'bdist_msi': bdist_msi_options},
        'version': msi_version,
                 }
else:
    from setuptools import find_packages
    platform_options = {
        'packages': find_packages(),
        'version': os.getenv('FAFCLIENT_VERSION'),
        }

setup(
    name=product_name,
    description='Forged Alliance Forever - Lobby Launcher',
    long_description='FA Forever is a community project that allows you to play \
Supreme Commander and Supreme Commander: Forged Alliance online \
with people across the globe. Provides new game play modes, including cooperative play, \
ranked ladder play, and featured mods.',
    author='FA Forever Community',
    maintainer='Sheeo',
    url='http://www.faforever.com',
    license='GNU General Public License, Version 3',
    **platform_options
)
