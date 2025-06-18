from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        print("Preparing document for printing...")
        self.print()  # Виклик абстрактного методу


class PDFDocument(Document):
    def print(self):
        print("Printing PDF document...")


class WordDocument(Document):
    def print(self):
        print("Printing Word document...")


class ExcelDocument(Document):
    def print(self):
        print("Printing Excel document...")


class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "excel":
            return ExcelDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")


if __name__ == "__main__":
    pdf = DocumentFactory.create_document("pdf")
    word = DocumentFactory.create_document("word")
    excel = DocumentFactory.create_document("excel")

    # Використання документів
    print("PDF Document:")
    pdf.prepare_for_printing()

    print("\nWord Document:")
    word.prepare_for_printing()

    print("\nExcel Document:")
    excel.prepare_for_printing()