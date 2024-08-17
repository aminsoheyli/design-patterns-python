from abc import ABC, abstractmethod
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


class PresentationBuilder(ABC):
    @abstractmethod
    def add_slide(self, slide):
        pass


class PdfDocumentBuilder(PresentationBuilder):

    def __init__(self):
        self.document = PdfDocument()

    def add_slide(self, slide):
        self.document.add_page(slide)

    def get_pdf_document(self):
        return self.document


class MovieBuilder(PresentationBuilder):

    def __init__(self):
        self.movie = Movie()

    def add_slide(self, slide):
        self.movie.add_frame(slide, 3)

    def get_movie(self):
        return self.movie


class PdfDocument:
    def add_page(self, text):
        print('Adding a page to PDF')


class Movie:
    def add_frame(self, text, duration):
        print('Adding a frame to the movie')


class Presentation:
    def __init__(self):
        self.slides = []

    def add_slide(self, slide):
        self.slides.append(slide)

    def export(self, builder: PresentationBuilder):
        builder.add_slide('Copyright')
        for slide in self.slides:
            builder.add_slide(slide)


if __name__ == '__main__':
    presentation = Presentation()
    presentation.add_slide('Slide 1')
    presentation.add_slide('Slide 2')
    builder = MovieBuilder()
    presentation.export(builder)
    movie = builder.get_movie()
