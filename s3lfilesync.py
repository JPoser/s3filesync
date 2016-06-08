
import subprocess
import logbook


cfg_s3folder = 
cfg_localstorage = 
cfg_logname = 

loggerprefix = logbook.Logger('s3logsync log')
log = logbook.TimedRotatingFileHandler(cfg_logname, date_format='%Y-%m-%d')
log.push_application()

def sync_logs(s3folder, localstorage):
	try:	
		sync = subprocess.Popen(["/usr/local/bin/s4cmd.py", "sync","-s", s3folder, localstorage], stdout=subprocess.PIPE)
		out = sync.communicate()[0]
		sync.wait()
		logger.info(out.upper())
		logger.info('Sync completed.')
	except subprocess.CalledProcessError, fail:
		fail = logger.warn("Sync failed!, check error log.")

sync_logs(cfg_s3folder, cfg_localstorage)