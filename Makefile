PYTHON = python3
INPUT_FILE = main.py
OUTPUT_FILE = test.txt

main: $(INPUT_FILE)
	$(PYTHON) $(INPUT_FILE) > $(OUTPUT_FILE)

%:
	$(PYTHON) $(INPUT_FILE) $@ > $(OUTPUT_FILE)

clean:
	rm -f $(OUTPUT_FILE)