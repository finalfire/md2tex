class Preamble:
    
    @staticmethod
    def head():
        return "\\documentclass{article}\n" + "\\title{}\n" + "\\author{}\n" + "\\begin{document}\n" + "\\maketitle\n"

    @staticmethod
    def tail():
        return "\n\\end{document}"


class Parser:
 
    def __init__(self, to_attach=None):
        self.filename = to_attach
        self.content = list()
        self.document = list()

    # get methods
    def filename(self):
        return self.filename

    def md_content(self):
        return self.md_content or []

    def document(self):
        return self.document or []

    # operational methods
    def open(self):
        with open(self.filename) as infile:
            self.content = [l.strip() for l in infile]
    
    def create_element(self, e):
        if not e:
            return '\n'

        tokens = e.split(' ')

        if tokens[0] == '#':
            return '\\section{' + ' '.join(tokens[1:]) + '}'
         
        if tokens[0] == '##':
            return '\\subsection{' + ' '.join(tokens[1:]) + '}'

        if tokens[0] == '###':
            return '\\subsubsection{' + ' '.join(tokens[1:]) + '}'

        if tokens[0] == '####':
            return '\\paragraph{' + ' '.join(tokens[1:]) + '}'

        # here we have a paragraph
        return e

    def parse(self):
        for element in self.content:
            latex_element = self.create_element(element)
            self.document.append(latex_element)

    def latex(self):
        return Preamble.head() + '\n'.join(self.document) + Preamble.tail()