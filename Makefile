
default:
	@echo "Please specify a make command. help command might be usefull"

reinstall_package:
	@pip uninstall -y brain-signals_api && pip install -e .

hard_uninstall:
	@pip uninstall -yr requirements.txt brain-signals_api

run_streamlit:
	@streamlit run Home.py
