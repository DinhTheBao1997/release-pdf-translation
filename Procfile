web: gunicorn main.wsgi --timeout 600 --log-file -
# release: bash release.sh
# beat: celery -A main.celeryapp:app beat -S redbeat.RedBeatScheduler  --loglevel=DEBUG --pidfile /tmp/celerybeat.pid
# worker: celery -A main.celeryapp:app  worker -Q default -n main.%%h --without-gossip --without-mingle --without-heartbeat --loglevel=INFO --max-memory-per-child=512000 --concurrency=1
