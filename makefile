.PHONY: all boundle run1 run2 dev

# 打包目标
boundle:
	@cd web && npm run build
	@pyinstaller build.spec
www:
	cd web && npm run dev
# 运行第一个脚本
run1:
	@echo "启动web"
	cd web && npm run dev

# 运行第二个脚本
run2:
	@echo "启动GUI"
	python3 main.py

# 异步运行两个脚本
dev:
	@echo "Setting environment variable and starting both scripts asynchronously"
	export appEnv="dev" && $(MAKE) run1 &
	export appEnv="dev" && $(MAKE) run2 &
	wait

install:
	pip3 install -r requirements.txt
	cd web && npm i