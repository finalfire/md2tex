#!/usr/bin/python
import Parser

if __name__ == '__main__':
    p = Parser.Parser(to_attach="sample.md")
    p.open()
    p.parse()

    #print(p.filename)
    #print(p.content)
    print(p.latex())