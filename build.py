import PyInstaller.__main__

PyInstaller.__main__.run([
    "main.py",
    "--clean",
    "--onefile",
    "--console",
    "--distpath",
    "./",
    "--name",
    "crpl",
    "--icon",
    "icon.ico",
    "--log-level",
    "DEBUG",
])