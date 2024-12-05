from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("twopage.pdf")
writer = PdfWriter()

page_indices = list(range(0, len(reader.pages)))

for index in page_indices:
    content_page = reader.pages[index]
    mediabox = content_page.mediabox

    reader_watermark = PdfReader("wtr.pdf")
    image_page = reader_watermark.pages[0]

    image_page.merge_page(content_page)
    image_page.media_box = mediabox

    writer.add_page(image_page)

    with open("twopage-watermarked.pdf", "wb") as file:
        writer.write(file)


print("Done")
