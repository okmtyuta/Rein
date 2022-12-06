port=8000
action=runserver

runserver:
	@echo "開発用サーバーを起動します"
	@python3 packages/manage.py --action ${action} --port ${port}

comment="make"

commit:
	@echo "gitへの自動commitを開始します"
	git add .
	git commit -m ${comment}

push:
	@echo "gitへの自動pushを開始します"
	git add .
	git commit -m ${comment}
	git push origin HEAD