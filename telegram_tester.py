import rag_telegram_bot as rtb
import time
from multiprocessing import Process

p = Process(target=rtb.start_tb_listener())
p.run()

time.sleep(2)

rtb.send_message('This is a test output')
