# Generated from /home/antonio/Documents/Tareas/gramatica/Ejemplo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EjemploParser import EjemploParser
else:
    from EjemploParser import EjemploParser

# This class defines a complete generic visitor for a parse tree produced by EjemploParser.

class EjemploVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EjemploParser#s.
    def visitS(self, ctx:EjemploParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EjemploParser#b.
    def visitB(self, ctx:EjemploParser.BContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EjemploParser#c.
    def visitC(self, ctx:EjemploParser.CContext):
        return self.visitChildren(ctx)



del EjemploParser