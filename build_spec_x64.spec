# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for Windows 11 RDP Manager (x64 64-bit)

block_cipher = None

a = Analysis(
    ['src/main_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('requirements.txt', '.'),
        ('README.md', '.'),
    ],
    hiddenimports=[
        'PyQt5.sip',
        'PyQt5.QtCore',
        'PyQt5.QtWidgets', 
        'PyQt5.QtGui',
        'requests',
        'urllib3',
        'certifi',
        'charset_normalizer',
        'idna',
        'github',
        'requests_oauthlib',
        'oauthlib',
        'cryptography',
        'psutil',
        'configparser',
        'json',
        'webbrowser',
        'threading',
        'http.server',
        'urllib.parse',
        'secrets',
        'base64',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
        'PIL.ImageShow',  # Exclude PIL image viewers
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Filter out unnecessary modules to reduce file size
a.datas = [x for x in a.datas if not x[1].startswith('tcl')]
a.datas = [x for x in a.datas if not x[1].startswith('tk')]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Windows11-RDP-Manager-x64',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Windows GUI application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='x64',  # 64-bit target
    codesign_identity=None,
    entitlements_file=None,
    icon='resources/app_icon.ico',  # Application icon
    version_file=None,  # Could add version info file here
    manifest=None,
)