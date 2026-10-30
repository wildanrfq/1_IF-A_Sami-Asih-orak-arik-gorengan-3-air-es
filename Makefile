.PHONY: setup data pipeline test notebook demo clean

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

data:
	python scripts/download_data.py

pipeline:
	python scripts/run_pipeline.py

test:
	pytest -q

notebook:
	jupyter notebook notebooks/

demo:  ## uji cepat dengan data sintetis (bukan data asli)
	python scripts/make_synthetic_data.py
	python scripts/run_pipeline.py

clean:
	rm -rf data/processed/*.csv reports/figures/*.png reports/tables/* .pytest_cache
