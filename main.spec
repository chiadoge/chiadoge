# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
project_path = C:\\
python_path = C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39

a = Analysis([
        'project_path\\chiadoge\\main.py',
        'project_path\\chiadoge\\scheduler_device\\scheduler_swarm.py',
        'project_path\\chiadoge\\scheduler_device\\node_notification.py',
        'project_path\\chiadoge\\scheduler_device\\add_scheduler_job.py',
        'project_path\\chiadoge\\server_api\\http_function.py',
        'project_path\\chiadoge\\log\\log.py',
        'project_path\\chiadoge\\config\\db_config.py',
        'project_path\\chiadoge\\config\\email_config.py',
        'project_path\\chiadoge\\config\\log_config.py',
        'project_path\\chiadoge\\config\\config.py'
        ],
             pathex=[
             'python_path\\Lib\\site-packages',
             'C:\\Windows\\System32\\downlevel',
             'project_path\\chiadoge'
             ],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='chiadoge',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='project_path\\chiadoge\\sources\\images\\favicon.ico'
          )