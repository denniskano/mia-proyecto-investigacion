PDF = build/Plan_Tesis_Grupo9.2.pdf
MAIN = main.tex

.PHONY: pdf clean open

pdf:
	latexmk -pdf -outdir=build $(MAIN)
	@cp build/main.pdf $(PDF)

clean:
	latexmk -C -outdir=build
	rm -f $(PDF)

open: pdf
	open $(PDF)
