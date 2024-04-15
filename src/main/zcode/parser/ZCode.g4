grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
// program: EOF;
program: NEWLINE* decl_list EOF;
decl_list:  decl decl_list |  decl;
decl: (functions | variables) ignored_newline;

//Variables
variables: implicit_keyword_variable | defined_type_variable | implicit_dynamic_variable;
implicit_keyword_variable: VAR IDENTIFIER ASSIGN exp0;

defined_type_variable: common_data_type (IDENTIFIER | (IDENTIFIER LB int_lst RB)) (ASSIGN exp0)?;
int_lst: ZNUM CM int_lst | ZNUM;

implicit_dynamic_variable: DYNAMIC IDENTIFIER (ASSIGN exp0)?;

//Functions
functions: 	FUNC IDENTIFIER LP param_lst? RP
			(	
				ignored_newline? return_stm 
				| ignored_newline? block_stm 
				| ignored_newline?
			);
param_lst: param CM param_lst | param;
param: common_data_type (IDENTIFIER | (IDENTIFIER LB int_lst RB));

lst_stms: (stm ignored_newline lst_stms) | (stm ignored_newline);
stm: declare_stm 
	| break_stm
	| for_stm
	| if_stm
	| assign_stm
	| continue_stm
	| return_stm
	| call_stm
	| block_stm
	;

declare_stm: variables;

continue_stm: CONTINUE;

if_stm: IF (LP exp0 RP ignored_newline?) (stm ignored_newline?) elif_stm else_stm?;
elif_stm: (ELIF LP exp0 RP ignored_newline? stm ignored_newline?) elif_stm | ;
else_stm: ELSE ignored_newline? stm;

for_stm: FOR IDENTIFIER UNTIL exp0 BY exp0 ignored_newline? stm;
assign_stm: (IDENTIFIER | (IDENTIFIER LB exp_list RB)) ASSIGN exp0;

return_stm: RETURN (exp0 | call_stm)?;
break_stm: BREAK ignored_newline?;

call_stm: IDENTIFIER LP arg_lst? RP;
arg_lst: exp0 CM arg_lst | exp0;

block_stm: 	BEGIN ignored_newline
			lst_stms?
			END;

// PARSER INTERFACES FOR LATER USES

exp_list: exp0 CM exp_list | exp0;
exp0: exp1 STRING_CONCAT exp1 | exp1;
exp1: 
	exp2 EQ exp2
	| exp2 STRING_EQUAL exp2
	| exp2 NEQ exp2
	| exp2 LESS_THAN exp2
	| exp2 GREATER_THAN exp2
	| exp2 LESS_THAN_EQUAL exp2
	| exp2 GREATER_THAN_EQUAL exp2
	| exp2;
exp2: 
	exp2 AND exp3
	| exp2 OR exp3
	| exp3;
exp3: 
	exp3 ADD exp4
	| exp3 SUB_AND_NEG exp4
	| exp4;
exp4: 
	exp4 MUL exp5
	| exp4 DIV exp5
	| exp4 MOD exp5
	| exp5;
exp5: NOT exp5 | exp6;
exp6: 
	(SUB_AND_NEG | ADD) exp6 
	| exp7;
exp7: (IDENTIFIER | (IDENTIFIER LP arg_lst? RP)) index | exp8;
exp8: array_lit | call_function | ZNUM | boolean_type | STRINGLIT | IDENTIFIER | LP exp0 RP; //! danger

index: LB exp_list RB;
call_function: IDENTIFIER LP arg_lst? RP;

// Literals
literal: TRUE | FALSE | ZNUM | STRINGLIT | array_lit;
array_lit: LB exp_list RB;
lst_literal: literal CM lst_literal | literal;

//Data type
// data_type:
// 	NUMBER
// 	| BOOL
// 	| STRING
// 	| array_type;

boolean_type: TRUE | FALSE;
common_data_type: NUMBER | BOOL | STRING;

array_type:
	NUMBER 
	| BOOL
	| STRING;

boolean_operator: NOT | AND | OR;
string_operator: STRING_CONCAT | STRING_EQUAL;
number_operator:
	ADD
	| SUB_AND_NEG
	| MUL
	| DIV
	| MOD
	| EQ
	| NEQ
	| GREATER_THAN
	| GREATER_THAN_EQUAL
	| LESS_THAN
	| LESS_THAN_EQUAL;

ignored_newline: NEWLINE+;
//LEXICAL STRUCTURES
// * Keywords ** Boolean
TRUE: 'true';
FALSE: 'false';

NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';

RETURN: 'return';

VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';

BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

// * Operators
NOT: 'not';
AND: 'and';
OR: 'or';

ADD: '+';
SUB_AND_NEG: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQ: '=';
NEQ: '!=';

ASSIGN: '<-';
LESS_THAN: '<';
LESS_THAN_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_EQUAL: '>=';

STRING_CONCAT: '...';
STRING_EQUAL: '==';

// * Separators
LP: '(';
RP: ')';
LB: '[';
RB: ']';
// LB: '{'; RB: '}';
CM: ',';

INSIDE_QUOTE: '\'"';

// INT: (DECIMAL) {self.text = self.text.replace('_','')};
// fragment DECIMAL     : ([1-9][0-9]*([_][0-9]+)*) | [0];
// // fragment HEXADECIMAL : [0][xX][0-9a-fA-F]+([_][0-9a-fA-F]+)*;
// // fragment OCTAL       : [0][oO]?[0-7]+([_][0-7]+)*;
// // fragment BINARY      : [0][bB][01]+([_][01]+)*;

STRINGLIT: '"' STRINGLIT_ '"' {self.text = self.text[1:-1];};
fragment STRINGLIT_: (
		~[\b\f\r\n\\"]
		| '\\' [bfrnt'\\]
		| INSIDE_QUOTE
	)*;

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

ZNUM: INTPART DECPART? | INTPART DECPART? EXPPART;
fragment INTPART: [0-9]+ '.'?;
fragment DECPART: [0-9]+;
fragment EXPPART: [eE] [+-]? [0-9]+;

NEWLINE: [\n];
COMMENTS: '##' ~[\n\r\f]* -> skip;
WS: [ \t\r]+ -> skip; // skip spaces, tabs, newlines

// BLANK: ' '; TAB: '\t'; FORM_FEED: '\f'; CARRIAGE_RETURN: '\r'; NEWLINE: '\n'; SINGLE_QUOTE: '\'';
// BACKSLASH: '\\';

ILLEGAL_ESCAPE:
	'"' (STRINGLIT_) ('\\' ~[bfrnt\\] | [\r\f\\] | ['] ~["]) {self.text = self.text[1:]; raise IllegalEscape(self.text)
		};
UNCLOSE_STRING:
	'"' (STRINGLIT_) ('\r\n' | '\n' | EOF) {raise UncloseString(self.text[1:].rstrip("\r\n"))};
ERROR_CHAR: . {raise ErrorToken(self.text)};