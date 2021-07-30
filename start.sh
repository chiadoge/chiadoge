# Check chiadoge log path
home_path=`echo ${HOME}`
chiadoge_log_path="${home_path}/chiadoge/log"
if [ ! -d "$chiadoge_log_path" ]; then
    mkdir -p "$chiadoge_log_path"
fi

# Activate the virtual environment
. ./venv/bin/activate
echo Your Chiadoge log path "$chiadoge_log_path"

# Start the ChiaDoge
python3 main.py --config config_linux.yaml

# Start the ChiaDoge in background
#nohup python3 main.py --config config_linux.yaml > /dev/null 2>&1 &