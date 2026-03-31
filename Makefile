SRCS     := $(wildcard documents/src/*.md)
PDFS     := $(SRCS:documents/src/%.md=documents/dist/%.pdf)
TEMPLATE := documents/src/resinsight-template.latex
LOGO     := documents/src/logo.png   # place your logo here (optional)

PANDOC_FLAGS := \
  --pdf-engine=xelatex \
  --template=$(TEMPLATE) \
  --toc

# Inject logo path if the file exists
ifneq (,$(wildcard $(LOGO)))
  PANDOC_FLAGS += --variable logopath=$(LOGO)
endif

.PHONY: all clean

all: $(PDFS)

documents/dist/%.pdf: documents/src/%.md $(TEMPLATE)
	@mkdir -p documents/dist
	pandoc $< $(PANDOC_FLAGS) --resource-path="$(dir $<):." -o $@

clean:
	rm -rf documents/dist/
