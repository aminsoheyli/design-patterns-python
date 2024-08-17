from enum import Enum


class Slide:
    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text


class PresentationFormat(Enum):
    PDF = 1
    IMAGE = 2
    POWERPOINT = 3
    MOVIE = 4


class PdfDocument:
    def add_page(self, text):
        print('Adding a page to PDF')


class Movie:
    def add_frame(self, text, duration):
        print('Adding a frame to the movie')


class Presentation:
    def __init__(self):
        self._slides = []

    def add_slide(self, slide):
        self.slides.append(slide)

    def export(self, format):
        if format == PresentationFormat.PDF:
            pdf = PdfDocument()
            for slide in self._slides:
                pdf.add_page(slide.text)

        elif format == PresentationFormat.MOVIE:
            movie = Movie()
            for slide in self._slides:
                movie.add_frame(slide.text, duration=3)
