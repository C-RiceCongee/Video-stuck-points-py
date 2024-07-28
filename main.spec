# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],  # 如果没有隐藏的导入，可以保持为空
    hookspath=[],  # 如果没有自定义的 hook 脚本，可以保持为空
    hooksconfig={},  # 如果没有自定义的 hooks 配置，可以保持为空
    runtime_hooks=[],  # 如果没有运行时钩子，可以保持为空
    excludes=[],  # 如果没有要排除的模块，可以保持为空
    noarchive=False,  # 通常不需要更改
    optimize=0,  # 通常不需要更改
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,  # 如果你的应用已经准备好发布，可以关闭调试模式
    bootloader_ignore_signals=False,  # 通常不需要更改
    strip=False,  # 如果不需要剥离符号表，可以保持为 False
    upx=True,  # 如果不需要压缩可执行文件，可以设置为 False
    upx_exclude=[],  # 如果没有需要从 UPX 压缩中排除的文件，可以保持为空
    runtime_tmpdir=None,  # 通常不需要更改
    console=False,  # 如果你的应用是 GUI 应用，应该设置为 False
    disable_windowed_traceback=False,  # 如果不需要禁用窗口化的 traceback，可以保持为 False
    argv_emulation=False,  # 如果不需要模拟 argv，可以保持为 False
    target_arch=None,  # 通常不需要更改
    codesign_identity=None,  # 如果不需要代码签名，可以保持为 None
    entitlements_file=None,  # 如果不需要 entitlements 文件，可以保持为 None
)
app = BUNDLE(
    exe,
    name='main.app',
    icon=None,  # 如果没有图标文件，可以保持为 None
    bundle_identifier=None,  # 如果不需要设置 bundle identifier，可以保持为 None
)