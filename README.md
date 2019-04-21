# Raspi Auto Grow to keep your plants watered! 

## Setting things up

* Install python3
* Install modules listed in `requirements.txt`
* Notifications:
    * (After installing notify-run)
    * Run $ `notify-run register`
    * Scan QR Code with smartphone and register to nofications in browser
* Copy `raspi_auto_grow.py` to raspberry pi
* Make `raspi_auto_grow.py` executable
    * $ `chmod +x raspi_auto_grow.py`
* Copy `rag.service` to `/lib/systemd/system`
* Change `ExecStart=` command inside `rag.service` accordingly to path where `raspi_auto_grow.py` was copied
* Enable daemon process
    * $ `sudo systemctl daemon-reload`
    * $ `sudo systemctl enable rag.service`
    * $ `sudo systemctl start rag.service`

## Useful commands for process monitoring

* Check status
    * $ `sudo systemctl status rag.service`
* Start service
    * $ `sudo systemctl start rag.service`
* Stop service
    * $ `sudo systemctl stop rag.service`
* Check service's log
    * $ `sudo journalctl -f -u rag.service`