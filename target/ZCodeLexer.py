# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0177\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,")
        buf.write("\3-\3-\3-\3-\7-\u011f\n-\f-\16-\u0122\13-\3.\3.\7.\u0126")
        buf.write("\n.\f.\16.\u0129\13.\3/\3/\5/\u012d\n/\3/\3/\5/\u0131")
        buf.write("\n/\3/\3/\5/\u0135\n/\3\60\6\60\u0138\n\60\r\60\16\60")
        buf.write("\u0139\3\60\5\60\u013d\n\60\3\61\6\61\u0140\n\61\r\61")
        buf.write("\16\61\u0141\3\62\3\62\5\62\u0146\n\62\3\62\6\62\u0149")
        buf.write("\n\62\r\62\16\62\u014a\3\63\3\63\3\64\3\64\3\64\3\64\7")
        buf.write("\64\u0153\n\64\f\64\16\64\u0156\13\64\3\64\3\64\3\65\6")
        buf.write("\65\u015b\n\65\r\65\16\65\u015c\3\65\3\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\5\66\u0168\n\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u0171\n\67\3\67\3\67\38\38\3")
        buf.write("8\2\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y\2[.]/_\2a\2c\2e\60g\61i\62k\63m\64o\65\3")
        buf.write("\2\21\7\2\n\n\f\f\16\17$$^^\t\2))^^ddhhppttvv\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\3\2\f\f\4\2")
        buf.write("\f\f\16\17\5\2\13\13\17\17\"\"\b\2^^ddhhppttvv\4\2\16")
        buf.write("\17^^\3\2))\3\2$$\3\3\f\f\2\u0183\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3\2\2\2\5")
        buf.write("v\3\2\2\2\7|\3\2\2\2\t\u0083\3\2\2\2\13\u0088\3\2\2\2")
        buf.write("\r\u008f\3\2\2\2\17\u0096\3\2\2\2\21\u009a\3\2\2\2\23")
        buf.write("\u00a2\3\2\2\2\25\u00a7\3\2\2\2\27\u00ab\3\2\2\2\31\u00b1")
        buf.write("\3\2\2\2\33\u00b4\3\2\2\2\35\u00ba\3\2\2\2\37\u00c3\3")
        buf.write("\2\2\2!\u00c6\3\2\2\2#\u00cb\3\2\2\2%\u00d0\3\2\2\2\'")
        buf.write("\u00d6\3\2\2\2)\u00da\3\2\2\2+\u00de\3\2\2\2-\u00e2\3")
        buf.write("\2\2\2/\u00e5\3\2\2\2\61\u00e7\3\2\2\2\63\u00e9\3\2\2")
        buf.write("\2\65\u00eb\3\2\2\2\67\u00ed\3\2\2\29\u00ef\3\2\2\2;\u00f1")
        buf.write("\3\2\2\2=\u00f4\3\2\2\2?\u00f7\3\2\2\2A\u00f9\3\2\2\2")
        buf.write("C\u00fc\3\2\2\2E\u00fe\3\2\2\2G\u0101\3\2\2\2I\u0105\3")
        buf.write("\2\2\2K\u0108\3\2\2\2M\u010a\3\2\2\2O\u010c\3\2\2\2Q\u010e")
        buf.write("\3\2\2\2S\u0110\3\2\2\2U\u0112\3\2\2\2W\u0115\3\2\2\2")
        buf.write("Y\u0120\3\2\2\2[\u0123\3\2\2\2]\u0134\3\2\2\2_\u0137\3")
        buf.write("\2\2\2a\u013f\3\2\2\2c\u0143\3\2\2\2e\u014c\3\2\2\2g\u014e")
        buf.write("\3\2\2\2i\u015a\3\2\2\2k\u0160\3\2\2\2m\u016b\3\2\2\2")
        buf.write("o\u0174\3\2\2\2qr\7v\2\2rs\7t\2\2st\7w\2\2tu\7g\2\2u\4")
        buf.write("\3\2\2\2vw\7h\2\2wx\7c\2\2xy\7n\2\2yz\7u\2\2z{\7g\2\2")
        buf.write("{\6\3\2\2\2|}\7p\2\2}~\7w\2\2~\177\7o\2\2\177\u0080\7")
        buf.write("d\2\2\u0080\u0081\7g\2\2\u0081\u0082\7t\2\2\u0082\b\3")
        buf.write("\2\2\2\u0083\u0084\7d\2\2\u0084\u0085\7q\2\2\u0085\u0086")
        buf.write("\7q\2\2\u0086\u0087\7n\2\2\u0087\n\3\2\2\2\u0088\u0089")
        buf.write("\7u\2\2\u0089\u008a\7v\2\2\u008a\u008b\7t\2\2\u008b\u008c")
        buf.write("\7k\2\2\u008c\u008d\7p\2\2\u008d\u008e\7i\2\2\u008e\f")
        buf.write("\3\2\2\2\u008f\u0090\7t\2\2\u0090\u0091\7g\2\2\u0091\u0092")
        buf.write("\7v\2\2\u0092\u0093\7w\2\2\u0093\u0094\7t\2\2\u0094\u0095")
        buf.write("\7p\2\2\u0095\16\3\2\2\2\u0096\u0097\7x\2\2\u0097\u0098")
        buf.write("\7c\2\2\u0098\u0099\7t\2\2\u0099\20\3\2\2\2\u009a\u009b")
        buf.write("\7f\2\2\u009b\u009c\7{\2\2\u009c\u009d\7p\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7o\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1")
        buf.write("\7e\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4")
        buf.write("\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7e\2\2\u00a6\24")
        buf.write("\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7t\2\2\u00aa\26\3\2\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7n\2\2\u00b0\30\3\2\2\2\u00b1\u00b2\7d\2\2\u00b2\u00b3")
        buf.write("\7{\2\2\u00b3\32\3\2\2\2\u00b4\u00b5\7d\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9")
        buf.write("\7m\2\2\u00b9\34\3\2\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\36\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7h\2\2\u00c5 \3\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\"")
        buf.write("\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce")
        buf.write("\7k\2\2\u00ce\u00cf\7h\2\2\u00cf$\3\2\2\2\u00d0\u00d1")
        buf.write("\7d\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7i\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7p\2\2\u00d5&\3\2\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7f\2\2\u00d9(\3")
        buf.write("\2\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd*\3\2\2\2\u00de\u00df\7c\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7f\2\2\u00e1,\3\2\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7t\2\2\u00e4.\3\2\2\2\u00e5\u00e6")
        buf.write("\7-\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\7/\2\2\u00e8\62\3")
        buf.write("\2\2\2\u00e9\u00ea\7,\2\2\u00ea\64\3\2\2\2\u00eb\u00ec")
        buf.write("\7\61\2\2\u00ec\66\3\2\2\2\u00ed\u00ee\7\'\2\2\u00ee8")
        buf.write("\3\2\2\2\u00ef\u00f0\7?\2\2\u00f0:\3\2\2\2\u00f1\u00f2")
        buf.write("\7#\2\2\u00f2\u00f3\7?\2\2\u00f3<\3\2\2\2\u00f4\u00f5")
        buf.write("\7>\2\2\u00f5\u00f6\7/\2\2\u00f6>\3\2\2\2\u00f7\u00f8")
        buf.write("\7>\2\2\u00f8@\3\2\2\2\u00f9\u00fa\7>\2\2\u00fa\u00fb")
        buf.write("\7?\2\2\u00fbB\3\2\2\2\u00fc\u00fd\7@\2\2\u00fdD\3\2\2")
        buf.write("\2\u00fe\u00ff\7@\2\2\u00ff\u0100\7?\2\2\u0100F\3\2\2")
        buf.write("\2\u0101\u0102\7\60\2\2\u0102\u0103\7\60\2\2\u0103\u0104")
        buf.write("\7\60\2\2\u0104H\3\2\2\2\u0105\u0106\7?\2\2\u0106\u0107")
        buf.write("\7?\2\2\u0107J\3\2\2\2\u0108\u0109\7*\2\2\u0109L\3\2\2")
        buf.write("\2\u010a\u010b\7+\2\2\u010bN\3\2\2\2\u010c\u010d\7]\2")
        buf.write("\2\u010dP\3\2\2\2\u010e\u010f\7_\2\2\u010fR\3\2\2\2\u0110")
        buf.write("\u0111\7.\2\2\u0111T\3\2\2\2\u0112\u0113\7)\2\2\u0113")
        buf.write("\u0114\7$\2\2\u0114V\3\2\2\2\u0115\u0116\7$\2\2\u0116")
        buf.write("\u0117\5Y-\2\u0117\u0118\7$\2\2\u0118\u0119\b,\2\2\u0119")
        buf.write("X\3\2\2\2\u011a\u011f\n\2\2\2\u011b\u011c\7^\2\2\u011c")
        buf.write("\u011f\t\3\2\2\u011d\u011f\5U+\2\u011e\u011a\3\2\2\2\u011e")
        buf.write("\u011b\3\2\2\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121Z\3\2\2")
        buf.write("\2\u0122\u0120\3\2\2\2\u0123\u0127\t\4\2\2\u0124\u0126")
        buf.write("\t\5\2\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\\\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u012a\u012c\5_\60\2\u012b\u012d\5a\61\2")
        buf.write("\u012c\u012b\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u0135\3")
        buf.write("\2\2\2\u012e\u0130\5_\60\2\u012f\u0131\5a\61\2\u0130\u012f")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("\u0133\5c\62\2\u0133\u0135\3\2\2\2\u0134\u012a\3\2\2\2")
        buf.write("\u0134\u012e\3\2\2\2\u0135^\3\2\2\2\u0136\u0138\t\6\2")
        buf.write("\2\u0137\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u0137")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u013d\7\60\2\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2")
        buf.write("\2\u013d`\3\2\2\2\u013e\u0140\t\6\2\2\u013f\u013e\3\2")
        buf.write("\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142")
        buf.write("\3\2\2\2\u0142b\3\2\2\2\u0143\u0145\t\7\2\2\u0144\u0146")
        buf.write("\t\b\2\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0149\t\6\2\2\u0148\u0147\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3")
        buf.write("\2\2\2\u014bd\3\2\2\2\u014c\u014d\t\t\2\2\u014df\3\2\2")
        buf.write("\2\u014e\u014f\7%\2\2\u014f\u0150\7%\2\2\u0150\u0154\3")
        buf.write("\2\2\2\u0151\u0153\n\n\2\2\u0152\u0151\3\2\2\2\u0153\u0156")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\b\64\3")
        buf.write("\2\u0158h\3\2\2\2\u0159\u015b\t\13\2\2\u015a\u0159\3\2")
        buf.write("\2\2\u015b\u015c\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\b\65\3\2\u015f")
        buf.write("j\3\2\2\2\u0160\u0161\7$\2\2\u0161\u0167\5Y-\2\u0162\u0163")
        buf.write("\7^\2\2\u0163\u0168\n\f\2\2\u0164\u0168\t\r\2\2\u0165")
        buf.write("\u0166\t\16\2\2\u0166\u0168\n\17\2\2\u0167\u0162\3\2\2")
        buf.write("\2\u0167\u0164\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016a\b\66\4\2\u016al\3\2\2\2\u016b\u016c")
        buf.write("\7$\2\2\u016c\u0170\5Y-\2\u016d\u016e\7\17\2\2\u016e\u0171")
        buf.write("\7\f\2\2\u016f\u0171\t\20\2\2\u0170\u016d\3\2\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\b\67\5")
        buf.write("\2\u0173n\3\2\2\2\u0174\u0175\13\2\2\2\u0175\u0176\b8")
        buf.write("\6\2\u0176p\3\2\2\2\22\2\u011e\u0120\u0127\u012c\u0130")
        buf.write("\u0134\u0139\u013c\u0141\u0145\u014a\u0154\u015c\u0167")
        buf.write("\u0170\7\3,\2\b\2\2\3\66\3\3\67\4\38\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB_AND_NEG = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    NEQ = 29
    ASSIGN = 30
    LESS_THAN = 31
    LESS_THAN_EQUAL = 32
    GREATER_THAN = 33
    GREATER_THAN_EQUAL = 34
    STRING_CONCAT = 35
    STRING_EQUAL = 36
    LP = 37
    RP = 38
    LB = 39
    RB = 40
    CM = 41
    INSIDE_QUOTE = 42
    STRINGLIT = 43
    IDENTIFIER = 44
    ZNUM = 45
    NEWLINE = 46
    COMMENTS = 47
    WS = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "''\"'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB_AND_NEG", "MUL", "DIV", "MOD", "EQ", "NEQ", "ASSIGN", "LESS_THAN", 
            "LESS_THAN_EQUAL", "GREATER_THAN", "GREATER_THAN_EQUAL", "STRING_CONCAT", 
            "STRING_EQUAL", "LP", "RP", "LB", "RB", "CM", "INSIDE_QUOTE", 
            "STRINGLIT", "IDENTIFIER", "ZNUM", "NEWLINE", "COMMENTS", "WS", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB_AND_NEG", "MUL", "DIV", "MOD", 
                  "EQ", "NEQ", "ASSIGN", "LESS_THAN", "LESS_THAN_EQUAL", 
                  "GREATER_THAN", "GREATER_THAN_EQUAL", "STRING_CONCAT", 
                  "STRING_EQUAL", "LP", "RP", "LB", "RB", "CM", "INSIDE_QUOTE", 
                  "STRINGLIT", "STRINGLIT_", "IDENTIFIER", "ZNUM", "INTPART", 
                  "DECPART", "EXPPART", "NEWLINE", "COMMENTS", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[42] = self.STRINGLIT_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
            		
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:].rstrip("\r\n"))
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


