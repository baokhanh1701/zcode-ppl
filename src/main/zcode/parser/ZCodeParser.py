# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01d9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\7\2b\n\2\f\2\16\2e\13\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\5\4r\n\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\5\5y\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u0087\n\7\3\7\3\7\5\7\u008b\n\7\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u0091\n\b\3\t\3\t\3\t\3\t\5\t\u0097\n\t")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u009d\n\n\3\n\3\n\5\n\u00a1\n\n\3")
        buf.write("\n\3\n\5\n\u00a5\n\n\3\n\3\n\5\n\u00a9\n\n\5\n\u00ab\n")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\5\13\u00b2\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00bb\n\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00c4\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00cf\n\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00da\n\21\3\21\3\21\5\21\u00de")
        buf.write("\n\21\3\21\3\21\5\21\u00e2\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u00e9\n\22\3\22\3\22\5\22\u00ed\n\22\3\22\3\22")
        buf.write("\3\22\5\22\u00f2\n\22\3\23\3\23\5\23\u00f6\n\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0101\n\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u010b\n")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0113\n\26\3\27")
        buf.write("\3\27\5\27\u0117\n\27\3\30\3\30\3\30\5\30\u011c\n\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0125\n\31\3\32")
        buf.write("\3\32\3\32\5\32\u012a\n\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0133\n\33\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u013a\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0159\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\7\36\u0164\n\36\f\36\16\36\u0167\13\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0172\n\37\f\37")
        buf.write("\16\37\u0175\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \7 \u0183\n \f \16 \u0186\13 \3!\3!\3!\5!\u018b\n!\3")
        buf.write("\"\3\"\3\"\5\"\u0190\n\"\3#\3#\3#\3#\5#\u0196\n#\3#\5")
        buf.write("#\u0199\n#\3#\3#\5#\u019d\n#\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\5$\u01a9\n$\3%\3%\3%\3%\3&\3&\3&\5&\u01b2\n&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\5\'\u01bb\n\'\3(\3(\3(\3(\3)\3)")
        buf.write("\3)\3)\3)\5)\u01c6\n)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\6\60\u01d5\n\60\r\60\16\60\u01d6\3\60\2\5:<")
        buf.write(">\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\b\3\2\31\32\3\2\3\4\3")
        buf.write("\2\5\7\3\2\26\30\3\2%&\4\2\31\37!$\2\u01f4\2c\3\2\2\2")
        buf.write("\4m\3\2\2\2\6q\3\2\2\2\bx\3\2\2\2\nz\3\2\2\2\f\177\3\2")
        buf.write("\2\2\16\u0090\3\2\2\2\20\u0092\3\2\2\2\22\u0098\3\2\2")
        buf.write("\2\24\u00b1\3\2\2\2\26\u00b3\3\2\2\2\30\u00c3\3\2\2\2")
        buf.write("\32\u00ce\3\2\2\2\34\u00d0\3\2\2\2\36\u00d2\3\2\2\2 \u00d4")
        buf.write("\3\2\2\2\"\u00f1\3\2\2\2$\u00f3\3\2\2\2&\u00f9\3\2\2\2")
        buf.write("(\u010a\3\2\2\2*\u010f\3\2\2\2,\u0114\3\2\2\2.\u0118\3")
        buf.write("\2\2\2\60\u0124\3\2\2\2\62\u0126\3\2\2\2\64\u0132\3\2")
        buf.write("\2\2\66\u0139\3\2\2\28\u0158\3\2\2\2:\u015a\3\2\2\2<\u0168")
        buf.write("\3\2\2\2>\u0176\3\2\2\2@\u018a\3\2\2\2B\u018f\3\2\2\2")
        buf.write("D\u019c\3\2\2\2F\u01a8\3\2\2\2H\u01aa\3\2\2\2J\u01ae\3")
        buf.write("\2\2\2L\u01ba\3\2\2\2N\u01bc\3\2\2\2P\u01c5\3\2\2\2R\u01c7")
        buf.write("\3\2\2\2T\u01c9\3\2\2\2V\u01cb\3\2\2\2X\u01cd\3\2\2\2")
        buf.write("Z\u01cf\3\2\2\2\\\u01d1\3\2\2\2^\u01d4\3\2\2\2`b\7\60")
        buf.write("\2\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2df\3\2\2\2")
        buf.write("ec\3\2\2\2fg\5\4\3\2gh\7\2\2\3h\3\3\2\2\2ij\5\6\4\2jk")
        buf.write("\5\4\3\2kn\3\2\2\2ln\5\6\4\2mi\3\2\2\2ml\3\2\2\2n\5\3")
        buf.write("\2\2\2or\5\22\n\2pr\5\b\5\2qo\3\2\2\2qp\3\2\2\2rs\3\2")
        buf.write("\2\2st\5^\60\2t\7\3\2\2\2uy\5\n\6\2vy\5\f\7\2wy\5\20\t")
        buf.write("\2xu\3\2\2\2xv\3\2\2\2xw\3\2\2\2y\t\3\2\2\2z{\7\t\2\2")
        buf.write("{|\7.\2\2|}\7 \2\2}~\5\66\34\2~\13\3\2\2\2\177\u0086\5")
        buf.write("T+\2\u0080\u0087\7.\2\2\u0081\u0082\7.\2\2\u0082\u0083")
        buf.write("\7)\2\2\u0083\u0084\5\16\b\2\u0084\u0085\7*\2\2\u0085")
        buf.write("\u0087\3\2\2\2\u0086\u0080\3\2\2\2\u0086\u0081\3\2\2\2")
        buf.write("\u0087\u008a\3\2\2\2\u0088\u0089\7 \2\2\u0089\u008b\5")
        buf.write("\66\34\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\r\3\2\2\2\u008c\u008d\7/\2\2\u008d\u008e\7+\2\2\u008e")
        buf.write("\u0091\5\16\b\2\u008f\u0091\7/\2\2\u0090\u008c\3\2\2\2")
        buf.write("\u0090\u008f\3\2\2\2\u0091\17\3\2\2\2\u0092\u0093\7\n")
        buf.write("\2\2\u0093\u0096\7.\2\2\u0094\u0095\7 \2\2\u0095\u0097")
        buf.write("\5\66\34\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\21\3\2\2\2\u0098\u0099\7\13\2\2\u0099\u009a\7.\2\2\u009a")
        buf.write("\u009c\7\'\2\2\u009b\u009d\5\24\13\2\u009c\u009b\3\2\2")
        buf.write("\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00aa")
        buf.write("\7(\2\2\u009f\u00a1\5^\60\2\u00a0\u009f\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00ab\5*\26\2")
        buf.write("\u00a3\u00a5\5^\60\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00ab\5\62\32\2\u00a7")
        buf.write("\u00a9\5^\60\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00ab\3\2\2\2\u00aa\u00a0\3\2\2\2\u00aa\u00a4\3")
        buf.write("\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\23\3\2\2\2\u00ac\u00ad")
        buf.write("\5\26\f\2\u00ad\u00ae\7+\2\2\u00ae\u00af\5\24\13\2\u00af")
        buf.write("\u00b2\3\2\2\2\u00b0\u00b2\5\26\f\2\u00b1\u00ac\3\2\2")
        buf.write("\2\u00b1\u00b0\3\2\2\2\u00b2\25\3\2\2\2\u00b3\u00ba\5")
        buf.write("T+\2\u00b4\u00bb\7.\2\2\u00b5\u00b6\7.\2\2\u00b6\u00b7")
        buf.write("\7)\2\2\u00b7\u00b8\5\16\b\2\u00b8\u00b9\7*\2\2\u00b9")
        buf.write("\u00bb\3\2\2\2\u00ba\u00b4\3\2\2\2\u00ba\u00b5\3\2\2\2")
        buf.write("\u00bb\27\3\2\2\2\u00bc\u00bd\5\32\16\2\u00bd\u00be\5")
        buf.write("^\60\2\u00be\u00bf\5\30\r\2\u00bf\u00c4\3\2\2\2\u00c0")
        buf.write("\u00c1\5\32\16\2\u00c1\u00c2\5^\60\2\u00c2\u00c4\3\2\2")
        buf.write("\2\u00c3\u00bc\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c4\31\3")
        buf.write("\2\2\2\u00c5\u00cf\5\34\17\2\u00c6\u00cf\5,\27\2\u00c7")
        buf.write("\u00cf\5&\24\2\u00c8\u00cf\5 \21\2\u00c9\u00cf\5(\25\2")
        buf.write("\u00ca\u00cf\5\36\20\2\u00cb\u00cf\5*\26\2\u00cc\u00cf")
        buf.write("\5.\30\2\u00cd\u00cf\5\62\32\2\u00ce\u00c5\3\2\2\2\u00ce")
        buf.write("\u00c6\3\2\2\2\u00ce\u00c7\3\2\2\2\u00ce\u00c8\3\2\2\2")
        buf.write("\u00ce\u00c9\3\2\2\2\u00ce\u00ca\3\2\2\2\u00ce\u00cb\3")
        buf.write("\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\33")
        buf.write("\3\2\2\2\u00d0\u00d1\5\b\5\2\u00d1\35\3\2\2\2\u00d2\u00d3")
        buf.write("\7\20\2\2\u00d3\37\3\2\2\2\u00d4\u00d5\7\21\2\2\u00d5")
        buf.write("\u00d6\7\'\2\2\u00d6\u00d7\5\66\34\2\u00d7\u00d9\7(\2")
        buf.write("\2\u00d8\u00da\5^\60\2\u00d9\u00d8\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd\5\32\16\2\u00dc")
        buf.write("\u00de\5^\60\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df\u00e1\5\"\22\2\u00e0\u00e2")
        buf.write("\5$\23\2\u00e1\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("!\3\2\2\2\u00e3\u00e4\7\23\2\2\u00e4\u00e5\7\'\2\2\u00e5")
        buf.write("\u00e6\5\66\34\2\u00e6\u00e8\7(\2\2\u00e7\u00e9\5^\60")
        buf.write("\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00ec\5\32\16\2\u00eb\u00ed\5^\60\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00ef\5\"\22\2\u00ef\u00f2\3\2\2\2\u00f0\u00f2")
        buf.write("\3\2\2\2\u00f1\u00e3\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2")
        buf.write("#\3\2\2\2\u00f3\u00f5\7\22\2\2\u00f4\u00f6\5^\60\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\u00f8\5\32\16\2\u00f8%\3\2\2\2\u00f9\u00fa\7\f")
        buf.write("\2\2\u00fa\u00fb\7.\2\2\u00fb\u00fc\7\r\2\2\u00fc\u00fd")
        buf.write("\5\66\34\2\u00fd\u00fe\7\16\2\2\u00fe\u0100\5\66\34\2")
        buf.write("\u00ff\u0101\5^\60\2\u0100\u00ff\3\2\2\2\u0100\u0101\3")
        buf.write("\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103\5\32\16\2\u0103")
        buf.write("\'\3\2\2\2\u0104\u010b\7.\2\2\u0105\u0106\7.\2\2\u0106")
        buf.write("\u0107\7)\2\2\u0107\u0108\5\64\33\2\u0108\u0109\7*\2\2")
        buf.write("\u0109\u010b\3\2\2\2\u010a\u0104\3\2\2\2\u010a\u0105\3")
        buf.write("\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\7 \2\2\u010d\u010e")
        buf.write("\5\66\34\2\u010e)\3\2\2\2\u010f\u0112\7\b\2\2\u0110\u0113")
        buf.write("\5\66\34\2\u0111\u0113\5.\30\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113+\3\2\2\2\u0114")
        buf.write("\u0116\7\17\2\2\u0115\u0117\5^\60\2\u0116\u0115\3\2\2")
        buf.write("\2\u0116\u0117\3\2\2\2\u0117-\3\2\2\2\u0118\u0119\7.\2")
        buf.write("\2\u0119\u011b\7\'\2\2\u011a\u011c\5\60\31\2\u011b\u011a")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\u011e\7(\2\2\u011e/\3\2\2\2\u011f\u0120\5\66\34\2\u0120")
        buf.write("\u0121\7+\2\2\u0121\u0122\5\60\31\2\u0122\u0125\3\2\2")
        buf.write("\2\u0123\u0125\5\66\34\2\u0124\u011f\3\2\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125\61\3\2\2\2\u0126\u0127\7\24\2\2\u0127\u0129")
        buf.write("\5^\60\2\u0128\u012a\5\30\r\2\u0129\u0128\3\2\2\2\u0129")
        buf.write("\u012a\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7\25\2")
        buf.write("\2\u012c\63\3\2\2\2\u012d\u012e\5\66\34\2\u012e\u012f")
        buf.write("\7+\2\2\u012f\u0130\5\64\33\2\u0130\u0133\3\2\2\2\u0131")
        buf.write("\u0133\5\66\34\2\u0132\u012d\3\2\2\2\u0132\u0131\3\2\2")
        buf.write("\2\u0133\65\3\2\2\2\u0134\u0135\58\35\2\u0135\u0136\7")
        buf.write("%\2\2\u0136\u0137\58\35\2\u0137\u013a\3\2\2\2\u0138\u013a")
        buf.write("\58\35\2\u0139\u0134\3\2\2\2\u0139\u0138\3\2\2\2\u013a")
        buf.write("\67\3\2\2\2\u013b\u013c\5:\36\2\u013c\u013d\7\36\2\2\u013d")
        buf.write("\u013e\5:\36\2\u013e\u0159\3\2\2\2\u013f\u0140\5:\36\2")
        buf.write("\u0140\u0141\7&\2\2\u0141\u0142\5:\36\2\u0142\u0159\3")
        buf.write("\2\2\2\u0143\u0144\5:\36\2\u0144\u0145\7\37\2\2\u0145")
        buf.write("\u0146\5:\36\2\u0146\u0159\3\2\2\2\u0147\u0148\5:\36\2")
        buf.write("\u0148\u0149\7!\2\2\u0149\u014a\5:\36\2\u014a\u0159\3")
        buf.write("\2\2\2\u014b\u014c\5:\36\2\u014c\u014d\7#\2\2\u014d\u014e")
        buf.write("\5:\36\2\u014e\u0159\3\2\2\2\u014f\u0150\5:\36\2\u0150")
        buf.write("\u0151\7\"\2\2\u0151\u0152\5:\36\2\u0152\u0159\3\2\2\2")
        buf.write("\u0153\u0154\5:\36\2\u0154\u0155\7$\2\2\u0155\u0156\5")
        buf.write(":\36\2\u0156\u0159\3\2\2\2\u0157\u0159\5:\36\2\u0158\u013b")
        buf.write("\3\2\2\2\u0158\u013f\3\2\2\2\u0158\u0143\3\2\2\2\u0158")
        buf.write("\u0147\3\2\2\2\u0158\u014b\3\2\2\2\u0158\u014f\3\2\2\2")
        buf.write("\u0158\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u01599\3\2\2")
        buf.write("\2\u015a\u015b\b\36\1\2\u015b\u015c\5<\37\2\u015c\u0165")
        buf.write("\3\2\2\2\u015d\u015e\f\5\2\2\u015e\u015f\7\27\2\2\u015f")
        buf.write("\u0164\5<\37\2\u0160\u0161\f\4\2\2\u0161\u0162\7\30\2")
        buf.write("\2\u0162\u0164\5<\37\2\u0163\u015d\3\2\2\2\u0163\u0160")
        buf.write("\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166;\3\2\2\2\u0167\u0165\3\2\2\2\u0168")
        buf.write("\u0169\b\37\1\2\u0169\u016a\5> \2\u016a\u0173\3\2\2\2")
        buf.write("\u016b\u016c\f\5\2\2\u016c\u016d\7\31\2\2\u016d\u0172")
        buf.write("\5> \2\u016e\u016f\f\4\2\2\u016f\u0170\7\32\2\2\u0170")
        buf.write("\u0172\5> \2\u0171\u016b\3\2\2\2\u0171\u016e\3\2\2\2\u0172")
        buf.write("\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174=\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\b \1\2")
        buf.write("\u0177\u0178\5@!\2\u0178\u0184\3\2\2\2\u0179\u017a\f\6")
        buf.write("\2\2\u017a\u017b\7\33\2\2\u017b\u0183\5@!\2\u017c\u017d")
        buf.write("\f\5\2\2\u017d\u017e\7\34\2\2\u017e\u0183\5@!\2\u017f")
        buf.write("\u0180\f\4\2\2\u0180\u0181\7\35\2\2\u0181\u0183\5@!\2")
        buf.write("\u0182\u0179\3\2\2\2\u0182\u017c\3\2\2\2\u0182\u017f\3")
        buf.write("\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185?\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188")
        buf.write("\7\26\2\2\u0188\u018b\5@!\2\u0189\u018b\5B\"\2\u018a\u0187")
        buf.write("\3\2\2\2\u018a\u0189\3\2\2\2\u018bA\3\2\2\2\u018c\u018d")
        buf.write("\t\2\2\2\u018d\u0190\5B\"\2\u018e\u0190\5D#\2\u018f\u018c")
        buf.write("\3\2\2\2\u018f\u018e\3\2\2\2\u0190C\3\2\2\2\u0191\u0199")
        buf.write("\7.\2\2\u0192\u0193\7.\2\2\u0193\u0195\7\'\2\2\u0194\u0196")
        buf.write("\5\60\31\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u0199\7(\2\2\u0198\u0191\3\2\2\2")
        buf.write("\u0198\u0192\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019d\5")
        buf.write("H%\2\u019b\u019d\5F$\2\u019c\u0198\3\2\2\2\u019c\u019b")
        buf.write("\3\2\2\2\u019dE\3\2\2\2\u019e\u01a9\5N(\2\u019f\u01a9")
        buf.write("\5J&\2\u01a0\u01a9\7/\2\2\u01a1\u01a9\5R*\2\u01a2\u01a9")
        buf.write("\7-\2\2\u01a3\u01a9\7.\2\2\u01a4\u01a5\7\'\2\2\u01a5\u01a6")
        buf.write("\5\66\34\2\u01a6\u01a7\7(\2\2\u01a7\u01a9\3\2\2\2\u01a8")
        buf.write("\u019e\3\2\2\2\u01a8\u019f\3\2\2\2\u01a8\u01a0\3\2\2\2")
        buf.write("\u01a8\u01a1\3\2\2\2\u01a8\u01a2\3\2\2\2\u01a8\u01a3\3")
        buf.write("\2\2\2\u01a8\u01a4\3\2\2\2\u01a9G\3\2\2\2\u01aa\u01ab")
        buf.write("\7)\2\2\u01ab\u01ac\5\64\33\2\u01ac\u01ad\7*\2\2\u01ad")
        buf.write("I\3\2\2\2\u01ae\u01af\7.\2\2\u01af\u01b1\7\'\2\2\u01b0")
        buf.write("\u01b2\5\60\31\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2")
        buf.write("\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\7(\2\2\u01b4K\3\2\2")
        buf.write("\2\u01b5\u01bb\7\3\2\2\u01b6\u01bb\7\4\2\2\u01b7\u01bb")
        buf.write("\7/\2\2\u01b8\u01bb\7-\2\2\u01b9\u01bb\5N(\2\u01ba\u01b5")
        buf.write("\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbM\3\2\2\2\u01bc")
        buf.write("\u01bd\7)\2\2\u01bd\u01be\5\64\33\2\u01be\u01bf\7*\2\2")
        buf.write("\u01bfO\3\2\2\2\u01c0\u01c1\5L\'\2\u01c1\u01c2\7+\2\2")
        buf.write("\u01c2\u01c3\5P)\2\u01c3\u01c6\3\2\2\2\u01c4\u01c6\5L")
        buf.write("\'\2\u01c5\u01c0\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6Q\3")
        buf.write("\2\2\2\u01c7\u01c8\t\3\2\2\u01c8S\3\2\2\2\u01c9\u01ca")
        buf.write("\t\4\2\2\u01caU\3\2\2\2\u01cb\u01cc\t\4\2\2\u01ccW\3\2")
        buf.write("\2\2\u01cd\u01ce\t\5\2\2\u01ceY\3\2\2\2\u01cf\u01d0\t")
        buf.write("\6\2\2\u01d0[\3\2\2\2\u01d1\u01d2\t\7\2\2\u01d2]\3\2\2")
        buf.write("\2\u01d3\u01d5\7\60\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("_\3\2\2\2\64cmqx\u0086\u008a\u0090\u0096\u009c\u00a0\u00a4")
        buf.write("\u00a8\u00aa\u00b1\u00ba\u00c3\u00ce\u00d9\u00dd\u00e1")
        buf.write("\u00e8\u00ec\u00f1\u00f5\u0100\u010a\u0112\u0116\u011b")
        buf.write("\u0124\u0129\u0132\u0139\u0158\u0163\u0165\u0171\u0173")
        buf.write("\u0182\u0184\u018a\u018f\u0195\u0198\u019c\u01a8\u01b1")
        buf.write("\u01ba\u01c5\u01d6")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "''\"'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB_AND_NEG", "MUL", 
                      "DIV", "MOD", "EQ", "NEQ", "ASSIGN", "LESS_THAN", 
                      "LESS_THAN_EQUAL", "GREATER_THAN", "GREATER_THAN_EQUAL", 
                      "STRING_CONCAT", "STRING_EQUAL", "LP", "RP", "LB", 
                      "RB", "CM", "INSIDE_QUOTE", "STRINGLIT", "IDENTIFIER", 
                      "ZNUM", "NEWLINE", "COMMENTS", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_variables = 3
    RULE_implicit_keyword_variable = 4
    RULE_defined_type_variable = 5
    RULE_int_lst = 6
    RULE_implicit_dynamic_variable = 7
    RULE_functions = 8
    RULE_param_lst = 9
    RULE_param = 10
    RULE_lst_stms = 11
    RULE_stm = 12
    RULE_declare_stm = 13
    RULE_continue_stm = 14
    RULE_if_stm = 15
    RULE_elif_stm = 16
    RULE_else_stm = 17
    RULE_for_stm = 18
    RULE_assign_stm = 19
    RULE_return_stm = 20
    RULE_break_stm = 21
    RULE_call_stm = 22
    RULE_arg_lst = 23
    RULE_block_stm = 24
    RULE_exp_list = 25
    RULE_exp0 = 26
    RULE_exp1 = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_exp5 = 31
    RULE_exp6 = 32
    RULE_exp7 = 33
    RULE_exp8 = 34
    RULE_index = 35
    RULE_call_function = 36
    RULE_literal = 37
    RULE_array_lit = 38
    RULE_lst_literal = 39
    RULE_boolean_type = 40
    RULE_common_data_type = 41
    RULE_array_type = 42
    RULE_boolean_operator = 43
    RULE_string_operator = 44
    RULE_number_operator = 45
    RULE_ignored_newline = 46

    ruleNames =  [ "program", "decl_list", "decl", "variables", "implicit_keyword_variable", 
                   "defined_type_variable", "int_lst", "implicit_dynamic_variable", 
                   "functions", "param_lst", "param", "lst_stms", "stm", 
                   "declare_stm", "continue_stm", "if_stm", "elif_stm", 
                   "else_stm", "for_stm", "assign_stm", "return_stm", "break_stm", 
                   "call_stm", "arg_lst", "block_stm", "exp_list", "exp0", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "index", "call_function", "literal", "array_lit", 
                   "lst_literal", "boolean_type", "common_data_type", "array_type", 
                   "boolean_operator", "string_operator", "number_operator", 
                   "ignored_newline" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB_AND_NEG=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    NEQ=29
    ASSIGN=30
    LESS_THAN=31
    LESS_THAN_EQUAL=32
    GREATER_THAN=33
    GREATER_THAN_EQUAL=34
    STRING_CONCAT=35
    STRING_EQUAL=36
    LP=37
    RP=38
    LB=39
    RB=40
    CM=41
    INSIDE_QUOTE=42
    STRINGLIT=43
    IDENTIFIER=44
    ZNUM=45
    NEWLINE=46
    COMMENTS=47
    WS=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 94
                self.match(ZCodeParser.NEWLINE)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.decl_list()
            self.state = 101
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.decl()
                self.state = 104
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignored_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,0)


        def functions(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionsContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.state = 109
                self.functions()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 110
                self.variables()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 113
            self.ignored_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_keyword_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_keyword_variableContext,0)


        def defined_type_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Defined_type_variableContext,0)


        def implicit_dynamic_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamic_variableContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.implicit_keyword_variable()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.defined_type_variable()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.implicit_dynamic_variable()
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


    class Implicit_keyword_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_keyword_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_keyword_variable" ):
                return visitor.visitImplicit_keyword_variable(self)
            else:
                return visitor.visitChildren(self)




    def implicit_keyword_variable(self):

        localctx = ZCodeParser.Implicit_keyword_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_keyword_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ZCodeParser.VAR)
            self.state = 121
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 122
            self.match(ZCodeParser.ASSIGN)
            self.state = 123
            self.exp0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Defined_type_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_data_type(self):
            return self.getTypedRuleContext(ZCodeParser.Common_data_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def int_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Int_lstContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_defined_type_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefined_type_variable" ):
                return visitor.visitDefined_type_variable(self)
            else:
                return visitor.visitChildren(self)




    def defined_type_variable(self):

        localctx = ZCodeParser.Defined_type_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_defined_type_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.common_data_type()
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 126
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 127
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 128
                self.match(ZCodeParser.LB)
                self.state = 129
                self.int_lst()
                self.state = 130
                self.match(ZCodeParser.RB)
                pass


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 134
                self.match(ZCodeParser.ASSIGN)
                self.state = 135
                self.exp0()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZNUM(self):
            return self.getToken(ZCodeParser.ZNUM, 0)

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def int_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Int_lstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_int_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lst" ):
                return visitor.visitInt_lst(self)
            else:
                return visitor.visitChildren(self)




    def int_lst(self):

        localctx = ZCodeParser.Int_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_int_lst)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(ZCodeParser.ZNUM)
                self.state = 139
                self.match(ZCodeParser.CM)
                self.state = 140
                self.int_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(ZCodeParser.ZNUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamic_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic_variable" ):
                return visitor.visitImplicit_dynamic_variable(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic_variable(self):

        localctx = ZCodeParser.Implicit_dynamic_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicit_dynamic_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.DYNAMIC)
            self.state = 145
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 146
                self.match(ZCodeParser.ASSIGN)
                self.state = 147
                self.exp0()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def return_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmContext,0)


        def block_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmContext,0)


        def param_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Param_lstContext,0)


        def ignored_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = ZCodeParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ZCodeParser.FUNC)
            self.state = 151
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 152
            self.match(ZCodeParser.LP)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 153
                self.param_lst()


            self.state = 156
            self.match(ZCodeParser.RP)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 157
                    self.ignored_newline()


                self.state = 160
                self.return_stm()
                pass

            elif la_ == 2:
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 161
                    self.ignored_newline()


                self.state = 164
                self.block_stm()
                pass

            elif la_ == 3:
                self.state = 166
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 165
                    self.ignored_newline()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def param_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Param_lstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lst" ):
                return visitor.visitParam_lst(self)
            else:
                return visitor.visitChildren(self)




    def param_lst(self):

        localctx = ZCodeParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_lst)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.param()
                self.state = 171
                self.match(ZCodeParser.CM)
                self.state = 172
                self.param_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_data_type(self):
            return self.getTypedRuleContext(ZCodeParser.Common_data_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def int_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Int_lstContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.common_data_type()
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 178
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 179
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 180
                self.match(ZCodeParser.LB)
                self.state = 181
                self.int_lst()
                self.state = 182
                self.match(ZCodeParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lst_stmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def ignored_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,0)


        def lst_stms(self):
            return self.getTypedRuleContext(ZCodeParser.Lst_stmsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lst_stms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst_stms" ):
                return visitor.visitLst_stms(self)
            else:
                return visitor.visitChildren(self)




    def lst_stms(self):

        localctx = ZCodeParser.Lst_stmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lst_stms)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.stm()
                self.state = 187
                self.ignored_newline()
                self.state = 188
                self.lst_stms()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.stm()
                self.state = 191
                self.ignored_newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Declare_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmContext,0)


        def for_stm(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmContext,0)


        def if_stm(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmContext,0)


        def assign_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmContext,0)


        def block_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stm)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.declare_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.break_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.for_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 198
                self.if_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 199
                self.assign_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 200
                self.continue_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 201
                self.return_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 202
                self.call_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 203
                self.block_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_stm" ):
                return visitor.visitDeclare_stm(self)
            else:
                return visitor.visitChildren(self)




    def declare_stm(self):

        localctx = ZCodeParser.Declare_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declare_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.variables()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = ZCodeParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def elif_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmContext,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def else_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmContext,0)


        def ignored_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Ignored_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = ZCodeParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ZCodeParser.IF)

            self.state = 211
            self.match(ZCodeParser.LP)
            self.state = 212
            self.exp0()
            self.state = 213
            self.match(ZCodeParser.RP)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 214
                self.ignored_newline()



            self.state = 217
            self.stm()
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 218
                self.ignored_newline()


            self.state = 221
            self.elif_stm()
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 222
                self.else_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmContext,0)


        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def ignored_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Ignored_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stm" ):
                return visitor.visitElif_stm(self)
            else:
                return visitor.visitChildren(self)




    def elif_stm(self):

        localctx = ZCodeParser.Elif_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_elif_stm)
        self._la = 0 # Token type
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(ZCodeParser.ELIF)
                self.state = 226
                self.match(ZCodeParser.LP)
                self.state = 227
                self.exp0()
                self.state = 228
                self.match(ZCodeParser.RP)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 229
                    self.ignored_newline()


                self.state = 232
                self.stm()
                self.state = 234
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 233
                    self.ignored_newline()


                self.state = 236
                self.elif_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def ignored_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stm" ):
                return visitor.visitElse_stm(self)
            else:
                return visitor.visitChildren(self)




    def else_stm(self):

        localctx = ZCodeParser.Else_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_else_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.ELSE)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 242
                self.ignored_newline()


            self.state = 245
            self.stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp0Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp0Context,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def ignored_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = ZCodeParser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_for_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ZCodeParser.FOR)
            self.state = 248
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 249
            self.match(ZCodeParser.UNTIL)
            self.state = 250
            self.exp0()
            self.state = 251
            self.match(ZCodeParser.BY)
            self.state = 252
            self.exp0()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 253
                self.ignored_newline()


            self.state = 256
            self.stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stm" ):
                return visitor.visitAssign_stm(self)
            else:
                return visitor.visitChildren(self)




    def assign_stm(self):

        localctx = ZCodeParser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 259
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 260
                self.match(ZCodeParser.LB)
                self.state = 261
                self.exp_list()
                self.state = 262
                self.match(ZCodeParser.RB)
                pass


            self.state = 266
            self.match(ZCodeParser.ASSIGN)
            self.state = 267
            self.exp0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def call_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = ZCodeParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.RETURN)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 270
                self.exp0()

            elif la_ == 2:
                self.state = 271
                self.call_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignored_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = ZCodeParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(ZCodeParser.BREAK)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 275
                self.ignored_newline()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def arg_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_lstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stm" ):
                return visitor.visitCall_stm(self)
            else:
                return visitor.visitChildren(self)




    def call_stm(self):

        localctx = ZCodeParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 279
            self.match(ZCodeParser.LP)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB_AND_NEG) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.ZNUM))) != 0):
                self.state = 280
                self.arg_lst()


            self.state = 283
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def arg_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_lstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_lst" ):
                return visitor.visitArg_lst(self)
            else:
                return visitor.visitChildren(self)




    def arg_lst(self):

        localctx = ZCodeParser.Arg_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arg_lst)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.exp0()
                self.state = 286
                self.match(ZCodeParser.CM)
                self.state = 287
                self.arg_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignored_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Ignored_newlineContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def lst_stms(self):
            return self.getTypedRuleContext(ZCodeParser.Lst_stmsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stm" ):
                return visitor.visitBlock_stm(self)
            else:
                return visitor.visitChildren(self)




    def block_stm(self):

        localctx = ZCodeParser.Block_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ZCodeParser.BEGIN)
            self.state = 293
            self.ignored_newline()
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 294
                self.lst_stms()


            self.state = 297
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = ZCodeParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp_list)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.exp0()
                self.state = 300
                self.match(ZCodeParser.CM)
                self.state = 301
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def STRING_CONCAT(self):
            return self.getToken(ZCodeParser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = ZCodeParser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp0)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.exp1()
                self.state = 307
                self.match(ZCodeParser.STRING_CONCAT)
                self.state = 308
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def STRING_EQUAL(self):
            return self.getToken(ZCodeParser.STRING_EQUAL, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_THAN_EQUAL, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp1)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.exp2(0)
                self.state = 314
                self.match(ZCodeParser.EQ)
                self.state = 315
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.exp2(0)
                self.state = 318
                self.match(ZCodeParser.STRING_EQUAL)
                self.state = 319
                self.exp2(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.exp2(0)
                self.state = 322
                self.match(ZCodeParser.NEQ)
                self.state = 323
                self.exp2(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.exp2(0)
                self.state = 326
                self.match(ZCodeParser.LESS_THAN)
                self.state = 327
                self.exp2(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.exp2(0)
                self.state = 330
                self.match(ZCodeParser.GREATER_THAN)
                self.state = 331
                self.exp2(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 333
                self.exp2(0)
                self.state = 334
                self.match(ZCodeParser.LESS_THAN_EQUAL)
                self.state = 335
                self.exp2(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 337
                self.exp2(0)
                self.state = 338
                self.match(ZCodeParser.GREATER_THAN_EQUAL)
                self.state = 339
                self.exp2(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 341
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 353
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 347
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 348
                        self.match(ZCodeParser.AND)
                        self.state = 349
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 350
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 351
                        self.match(ZCodeParser.OR)
                        self.state = 352
                        self.exp3(0)
                        pass

             
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB_AND_NEG(self):
            return self.getToken(ZCodeParser.SUB_AND_NEG, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 367
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 361
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 362
                        self.match(ZCodeParser.ADD)
                        self.state = 363
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 364
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 365
                        self.match(ZCodeParser.SUB_AND_NEG)
                        self.state = 366
                        self.exp4(0)
                        pass

             
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 384
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 375
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 376
                        self.match(ZCodeParser.MUL)
                        self.state = 377
                        self.exp5()
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 378
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 379
                        self.match(ZCodeParser.DIV)
                        self.state = 380
                        self.exp5()
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 381
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 382
                        self.match(ZCodeParser.MOD)
                        self.state = 383
                        self.exp5()
                        pass

             
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp5)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(ZCodeParser.NOT)
                self.state = 390
                self.exp5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB_AND_NEG, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER, ZCodeParser.ZNUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.exp6()
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def SUB_AND_NEG(self):
            return self.getToken(ZCodeParser.SUB_AND_NEG, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp6)
        self._la = 0 # Token type
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB_AND_NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB_AND_NEG):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 395
                self.exp6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER, ZCodeParser.ZNUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.exp7()
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index(self):
            return self.getTypedRuleContext(ZCodeParser.IndexContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def arg_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_lstContext,0)


        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 399
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 400
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 401
                    self.match(ZCodeParser.LP)
                    self.state = 403
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB_AND_NEG) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.ZNUM))) != 0):
                        self.state = 402
                        self.arg_lst()


                    self.state = 405
                    self.match(ZCodeParser.RP)
                    pass


                self.state = 408
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def call_function(self):
            return self.getTypedRuleContext(ZCodeParser.Call_functionContext,0)


        def ZNUM(self):
            return self.getToken(ZCodeParser.ZNUM, 0)

        def boolean_type(self):
            return self.getTypedRuleContext(ZCodeParser.Boolean_typeContext,0)


        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp8)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.array_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.call_function()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.match(ZCodeParser.ZNUM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.boolean_type()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 416
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 417
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 418
                self.match(ZCodeParser.LP)
                self.state = 419
                self.exp0()
                self.state = 420
                self.match(ZCodeParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = ZCodeParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(ZCodeParser.LB)
            self.state = 425
            self.exp_list()
            self.state = 426
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def arg_lst(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_lstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_function" ):
                return visitor.visitCall_function(self)
            else:
                return visitor.visitChildren(self)




    def call_function(self):

        localctx = ZCodeParser.Call_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_call_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 429
            self.match(ZCodeParser.LP)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB_AND_NEG) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.ZNUM))) != 0):
                self.state = 430
                self.arg_lst()


            self.state = 433
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def ZNUM(self):
            return self.getToken(ZCodeParser.ZNUM, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literal)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.ZNUM]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(ZCodeParser.ZNUM)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.array_lit()
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


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(ZCodeParser.LB)
            self.state = 443
            self.exp_list()
            self.state = 444
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lst_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def lst_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Lst_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lst_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst_literal" ):
                return visitor.visitLst_literal(self)
            else:
                return visitor.visitChildren(self)




    def lst_literal(self):

        localctx = ZCodeParser.Lst_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_lst_literal)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.literal()
                self.state = 447
                self.match(ZCodeParser.CM)
                self.state = 448
                self.lst_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_type" ):
                return visitor.visitBoolean_type(self)
            else:
                return visitor.visitChildren(self)




    def boolean_type(self):

        localctx = ZCodeParser.Boolean_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_boolean_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE or _la==ZCodeParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Common_data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_common_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommon_data_type" ):
                return visitor.visitCommon_data_type(self)
            else:
                return visitor.visitChildren(self)




    def common_data_type(self):

        localctx = ZCodeParser.Common_data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_common_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = ZCodeParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_operator" ):
                return visitor.visitBoolean_operator(self)
            else:
                return visitor.visitChildren(self)




    def boolean_operator(self):

        localctx = ZCodeParser.Boolean_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_boolean_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.AND) | (1 << ZCodeParser.OR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_CONCAT(self):
            return self.getToken(ZCodeParser.STRING_CONCAT, 0)

        def STRING_EQUAL(self):
            return self.getToken(ZCodeParser.STRING_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_operator" ):
                return visitor.visitString_operator(self)
            else:
                return visitor.visitChildren(self)




    def string_operator(self):

        localctx = ZCodeParser.String_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_string_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.STRING_CONCAT or _la==ZCodeParser.STRING_EQUAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB_AND_NEG(self):
            return self.getToken(ZCodeParser.SUB_AND_NEG, 0)

        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_THAN_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_number_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_operator" ):
                return visitor.visitNumber_operator(self)
            else:
                return visitor.visitChildren(self)




    def number_operator(self):

        localctx = ZCodeParser.Number_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_number_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB_AND_NEG) | (1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD) | (1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_THAN_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.GREATER_THAN_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ignored_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignored_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnored_newline" ):
                return visitor.visitIgnored_newline(self)
            else:
                return visitor.visitChildren(self)




    def ignored_newline(self):

        localctx = ZCodeParser.Ignored_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_ignored_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 465
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 468 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.exp2_sempred
        self._predicates[29] = self.exp3_sempred
        self._predicates[30] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




