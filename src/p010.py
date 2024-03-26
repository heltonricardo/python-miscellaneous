import sys
import fitz


fname = sys.argv[1]
doc = fitz.open(fname)

for page in doc:
    pix = page.get_pixmap(dpi=300)
    pix.save("page-%i.png" % page.number)
