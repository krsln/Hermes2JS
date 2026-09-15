.PHONY: prepare-96 prepare-98 decompile-96 decompile-98

# hermes-disassembler | hermes-dec
DISASSEMBLER ?= hermes-disassembler

prepare-96: VERSION=96
prepare-96: FUNCTION_RANGE=15042..15216
prepare-96: prepare

prepare-98: VERSION=98
prepare-98: FUNCTION_RANGE=9446..9542
prepare-98: prepare

decompile-96: VERSION=96
decompile-96: decompile

decompile-98: VERSION=98
decompile-98: decompile

prepare:
	## Step 1 — Disassemble
#	python scripts/run-hermes-disassembler.py \
#		apps/testy/$(VERSION)/index.android.bundle \
#		apps/testy/$(VERSION)/output/disassembler-output.hasm
ifeq ($(DISASSEMBLER),hermes-dec)
	python vendor/hermes-dec/src/hermes_dec/disassembly/hbc_disassembler.py \
		apps/testy/$(VERSION)/index.android.bundle \
		apps/testy/$(VERSION)/output/disassembler-output.hasm
else ifeq ($(DISASSEMBLER),hermes-disassembler)
	python scripts/run-hermes-disassembler.py \
		apps/testy/$(VERSION)/index.android.bundle \
		apps/testy/$(VERSION)/output/disassembler-output.hasm
else
	$(error Unknown DISASSEMBLER: $(DISASSEMBLER). Use 'hermes-disassembler' or 'hermes-dec')
endif

	## Step 2 — Split
	rm -rf apps/testy/$(VERSION)/output/sections
	python scripts/split_output_file.py \
		-i apps/testy/$(VERSION)/output/disassembler-output.hasm \
		-o apps/testy/$(VERSION)/output/sections

	## Step 3 — Copy sections to fixtures
	rm -f apps/demo/fixtures/$(VERSION)/sections/*
	cp apps/testy/$(VERSION)/output/sections/function_{$(FUNCTION_RANGE)}_*.hasm \
		apps/demo/fixtures/$(VERSION)/sections/

decompile:
	## Decompile sections
	PYTHONPATH=. python scripts/decompile_sections.py \
		-i apps/demo/fixtures/$(VERSION)/sections \
		-o apps/demo/fixtures/$(VERSION)/results

