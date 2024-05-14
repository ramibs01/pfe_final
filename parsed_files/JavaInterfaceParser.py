# Generated from JavaInterface.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\5\2\24\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\3\5\5\5&\n\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\7\6.\n\6\f\6\16\6\61\13\6\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\2\2\n\2")
        buf.write("\4\6\b\n\f\16\20\2\2\2:\2\23\3\2\2\2\4\30\3\2\2\2\6\34")
        buf.write("\3\2\2\2\b%\3\2\2\2\n+\3\2\2\2\f\64\3\2\2\2\16\66\3\2")
        buf.write("\2\2\20<\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\23\24\3\2")
        buf.write("\2\2\24\25\3\2\2\2\25\26\5\b\5\2\26\27\7\2\2\3\27\3\3")
        buf.write("\2\2\2\30\31\7\3\2\2\31\32\5\6\4\2\32\33\7\4\2\2\33\5")
        buf.write("\3\2\2\2\34!\7\r\2\2\35\36\7\5\2\2\36 \7\r\2\2\37\35\3")
        buf.write("\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\7\3\2\2\2#!")
        buf.write("\3\2\2\2$&\7\6\2\2%$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\7")
        buf.write("\7\2\2()\7\r\2\2)*\5\n\6\2*\t\3\2\2\2+/\7\b\2\2,.\5\f")
        buf.write("\7\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62")
        buf.write("\3\2\2\2\61/\3\2\2\2\62\63\7\t\2\2\63\13\3\2\2\2\64\65")
        buf.write("\5\16\b\2\65\r\3\2\2\2\66\67\5\20\t\2\678\7\r\2\289\7")
        buf.write("\n\2\29:\7\13\2\2:;\7\4\2\2;\17\3\2\2\2<=\7\f\2\2=\21")
        buf.write("\3\2\2\2\6\23!%/")
        return buf.getvalue()


class JavaInterfaceParser ( Parser ):

    grammarFileName = "JavaInterface.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'package'", "';'", "'.'", "'public'", 
                     "'interface'", "'{'", "'}'", "'('", "')'", "'String'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "WS" ]

    RULE_compilationUnit = 0
    RULE_packageDeclaration = 1
    RULE_qualifiedName = 2
    RULE_interfaceDeclaration = 3
    RULE_interfaceBody = 4
    RULE_interfaceMember = 5
    RULE_interfaceMethod = 6
    RULE_type = 7

    ruleNames =  [ "compilationUnit", "packageDeclaration", "qualifiedName", 
                   "interfaceDeclaration", "interfaceBody", "interfaceMember", 
                   "interfaceMethod", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    IDENTIFIER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceDeclaration(self):
            return self.getTypedRuleContext(JavaInterfaceParser.InterfaceDeclarationContext,0)


        def EOF(self):
            return self.getToken(JavaInterfaceParser.EOF, 0)

        def packageDeclaration(self):
            return self.getTypedRuleContext(JavaInterfaceParser.PackageDeclarationContext,0)


        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = JavaInterfaceParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaInterfaceParser.T__0:
                self.state = 16
                self.packageDeclaration()


            self.state = 19
            self.interfaceDeclaration()
            self.state = 20
            self.match(JavaInterfaceParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(JavaInterfaceParser.QualifiedNameContext,0)


        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_packageDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageDeclaration" ):
                listener.enterPackageDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageDeclaration" ):
                listener.exitPackageDeclaration(self)




    def packageDeclaration(self):

        localctx = JavaInterfaceParser.PackageDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_packageDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(JavaInterfaceParser.T__0)
            self.state = 23
            self.qualifiedName()
            self.state = 24
            self.match(JavaInterfaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(JavaInterfaceParser.IDENTIFIER)
            else:
                return self.getToken(JavaInterfaceParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_qualifiedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedName" ):
                listener.enterQualifiedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedName" ):
                listener.exitQualifiedName(self)




    def qualifiedName(self):

        localctx = JavaInterfaceParser.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(JavaInterfaceParser.IDENTIFIER)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JavaInterfaceParser.T__2:
                self.state = 27
                self.match(JavaInterfaceParser.T__2)
                self.state = 28
                self.match(JavaInterfaceParser.IDENTIFIER)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(JavaInterfaceParser.IDENTIFIER, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(JavaInterfaceParser.InterfaceBodyContext,0)


        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_interfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDeclaration" ):
                listener.enterInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDeclaration" ):
                listener.exitInterfaceDeclaration(self)




    def interfaceDeclaration(self):

        localctx = JavaInterfaceParser.InterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interfaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaInterfaceParser.T__3:
                self.state = 34
                self.match(JavaInterfaceParser.T__3)


            self.state = 37
            self.match(JavaInterfaceParser.T__4)
            self.state = 38
            self.match(JavaInterfaceParser.IDENTIFIER)
            self.state = 39
            self.interfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaInterfaceParser.InterfaceMemberContext)
            else:
                return self.getTypedRuleContext(JavaInterfaceParser.InterfaceMemberContext,i)


        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_interfaceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceBody" ):
                listener.enterInterfaceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceBody" ):
                listener.exitInterfaceBody(self)




    def interfaceBody(self):

        localctx = JavaInterfaceParser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interfaceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(JavaInterfaceParser.T__5)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JavaInterfaceParser.T__9:
                self.state = 42
                self.interfaceMember()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(JavaInterfaceParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceMethod(self):
            return self.getTypedRuleContext(JavaInterfaceParser.InterfaceMethodContext,0)


        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_interfaceMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMember" ):
                listener.enterInterfaceMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMember" ):
                listener.exitInterfaceMember(self)




    def interfaceMember(self):

        localctx = JavaInterfaceParser.InterfaceMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_interfaceMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.interfaceMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(JavaInterfaceParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(JavaInterfaceParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_interfaceMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMethod" ):
                listener.enterInterfaceMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMethod" ):
                listener.exitInterfaceMethod(self)




    def interfaceMethod(self):

        localctx = JavaInterfaceParser.InterfaceMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_interfaceMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.type()
            self.state = 53
            self.match(JavaInterfaceParser.IDENTIFIER)
            self.state = 54
            self.match(JavaInterfaceParser.T__7)
            self.state = 55
            self.match(JavaInterfaceParser.T__8)
            self.state = 56
            self.match(JavaInterfaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaInterfaceParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type(self):

        localctx = JavaInterfaceParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(JavaInterfaceParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





