PDF = build/Exposicion_Plan_Tesis_Grupo9.2-beamer.pdf
MAIN = exposicion_beamer.tex
OUT_COPY = ../Exposicion_Plan_Tesis_Grupo9.2-beamer.pdf
PPT = ../ppt/Exposicion_Plan_Tesis_Grupo9.2.pptx
VENV_PY = ../ppt/.venv/bin/python3

.PHONY: pdf clean open images

images:
	$(VENV_PY) extract_ppt_images.py

pdf: images
	latexmk -pdf -outdir=build $(MAIN)
	@cp build/exposicion_beamer.pdf $(PDF)
	@cp $(PDF) $(OUT_COPY)
	@echo "Copiado a $(OUT_COPY)"

clean:
	latexmk -C -outdir=build
	rm -f $(PDF) $(OUT_COPY)

open: pdf
	open $(PDF)
