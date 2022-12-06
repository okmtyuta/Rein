runserver:
	@echo "開発用サーバーを起動します"
	@python3 packages/manage.py
	
push:
	@echo "gitへの自動pushを開始します"
	git add .
	git commit -m "make push"
	git push origin HEAD