# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis([
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\main.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\scheduler_device\\scheduler_swarm.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\scheduler_device\\node_notification.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\scheduler_device\\add_scheduler_job.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\server_api\\http_function.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\log\\log.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\config\\db_config.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\config\\email_config.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\config\\log_config.py',
        'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\config\\config.py'
        ],
             pathex=[
             'C:\\Users\\xjhouc\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages',
             'C:\\Windows\\System32\\downlevel',
             'C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge'
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
          icon='C:\\idea_workspace\\guns\\crypto-swarm\\_data_script\\chiadoge\\sources\\images\\favicon.ico'
          )