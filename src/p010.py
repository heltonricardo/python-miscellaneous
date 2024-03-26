import sys
import fitz


def show_help():
    print("This script converts a PDF file to PNG images.")
    print("Usage: python p010.py <path_to_pdf_file>")
    print("Example: python p010.py document.pdf")


if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
    show_help()
    sys.exit()

fname = sys.argv[1]
doc = fitz.open(fname)

for page in doc:
    pix = page.get_pixmap(dpi=300)
    pix.save("page-%i.png" % page.number)
