
# Pre-requisites

- Windows / Windows + WSL(Ubuntu)
- [Python 3.7+](https://www.python.org/downloads/windows/)
- [Git](https://git-scm.com/downloads)
- Enabled `INFO` logs on your chia farmer

# Windows

## How to enable INFO logs on chia farmer?

First we'll set Chia's log level to `INFO`. This ensures that all logs necessary for `chiadoge` to operate are available
under `C:\Users\[YOUR-USER]\.chia\mainnet\log\debug.log`.

1. Open the file `C:\Users\[YOUR-USER]\.chia\mainnet\config\config.yaml` in your favorite text editor
2. Find the line that reads `log_level: DEBUG` (under the `farmer` section) and change this to `log_level: INFO`
3. Restart the GUI or run `chia start --restart farmer` from the command line


## Run `Chiadoge.exe`
> Download [chiadoge.zip](https://github.com/chiadoge/chiadoge/releases) from Github
> 
> Open zip,you will find `chiadoge.exe` and `config.yaml`
> 
> Extracted the zip to a directory and enter to it 
> 
> Run with: `chiadoge.exe --config config.yaml`

<img src="/sources/images/markdown/zip.png" >

<img src="/sources/images/markdown/windows_run.png" >



# Linux(Ubuntu)

## How to enable INFO logs on chia farmer?

**Reminder**: `INFO` level log in Chia must be enabled (`chia configure -log-level=INFO`)


## How to use Chiadoge
1. Download

```shell
git clone https://github.com/chiadoge/chiadoge.git
cd chiadoge
```

2. Run the install script.

```shell
chmod 777 install.sh
./install.sh
```

3. Open up `config_linux.yaml` in your editor and change some profiles to yourself


4. Run the start script
```shell
chmod 777 start.sh
./start.sh
```

