# Generated from /home/antonio/Documents/Tareas/gramatica/Ejemplo.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,24,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,3,2,22,8,2,1,2,0,0,3,0,2,4,0,0,22,
        0,6,1,0,0,0,2,17,1,0,0,0,4,21,1,0,0,0,6,7,5,1,0,0,7,8,3,2,1,0,8,
        9,3,4,2,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,5,2,0,0,12,18,5,3,0,0,
        13,14,5,4,0,0,14,15,3,4,2,0,15,16,5,5,0,0,16,18,1,0,0,0,17,11,1,
        0,0,0,17,13,1,0,0,0,18,3,1,0,0,0,19,22,5,6,0,0,20,22,1,0,0,0,21,
        19,1,0,0,0,21,20,1,0,0,0,22,5,1,0,0,0,2,17,21
    ]

class EjemploParser ( Parser ):

    grammarFileName = "Ejemplo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'bas'", "'big'", "'boss'", 
                     "'c'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS" ]

    RULE_s = 0
    RULE_b = 1
    RULE_c = 2

    ruleNames =  [ "s", "b", "c" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def b(self):
            return self.getTypedRuleContext(EjemploParser.BContext,0)


        def c(self):
            return self.getTypedRuleContext(EjemploParser.CContext,0)


        def EOF(self):
            return self.getToken(EjemploParser.EOF, 0)

        def getRuleIndex(self):
            return EjemploParser.RULE_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = EjemploParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(EjemploParser.T__0)
            self.state = 7
            self.b()
            self.state = 8
            self.c()
            self.state = 9
            self.match(EjemploParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def c(self):
            return self.getTypedRuleContext(EjemploParser.CContext,0)


        def getRuleIndex(self):
            return EjemploParser.RULE_b

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB" ):
                return visitor.visitB(self)
            else:
                return visitor.visitChildren(self)




    def b(self):

        localctx = EjemploParser.BContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_b)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(EjemploParser.T__1)
                self.state = 12
                self.match(EjemploParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(EjemploParser.T__3)
                self.state = 14
                self.c()
                self.state = 15
                self.match(EjemploParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EjemploParser.RULE_c

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC" ):
                return visitor.visitC(self)
            else:
                return visitor.visitChildren(self)




    def c(self):

        localctx = EjemploParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_c)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(EjemploParser.T__5)
                pass
            elif token in [-1, 5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





