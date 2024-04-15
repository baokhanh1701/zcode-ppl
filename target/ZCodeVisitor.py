# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_keyword_variable.
    def visitImplicit_keyword_variable(self, ctx:ZCodeParser.Implicit_keyword_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#defined_type_variable.
    def visitDefined_type_variable(self, ctx:ZCodeParser.Defined_type_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#int_lst.
    def visitInt_lst(self, ctx:ZCodeParser.Int_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic_variable.
    def visitImplicit_dynamic_variable(self, ctx:ZCodeParser.Implicit_dynamic_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functions.
    def visitFunctions(self, ctx:ZCodeParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_lst.
    def visitParam_lst(self, ctx:ZCodeParser.Param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lst_stms.
    def visitLst_stms(self, ctx:ZCodeParser.Lst_stmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stm.
    def visitStm(self, ctx:ZCodeParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declare_stm.
    def visitDeclare_stm(self, ctx:ZCodeParser.Declare_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stm.
    def visitContinue_stm(self, ctx:ZCodeParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stm.
    def visitIf_stm(self, ctx:ZCodeParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stm.
    def visitElif_stm(self, ctx:ZCodeParser.Elif_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stm.
    def visitElse_stm(self, ctx:ZCodeParser.Else_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stm.
    def visitFor_stm(self, ctx:ZCodeParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stm.
    def visitAssign_stm(self, ctx:ZCodeParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stm.
    def visitReturn_stm(self, ctx:ZCodeParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stm.
    def visitBreak_stm(self, ctx:ZCodeParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_stm.
    def visitCall_stm(self, ctx:ZCodeParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg_lst.
    def visitArg_lst(self, ctx:ZCodeParser.Arg_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stm.
    def visitBlock_stm(self, ctx:ZCodeParser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp_list.
    def visitExp_list(self, ctx:ZCodeParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp0.
    def visitExp0(self, ctx:ZCodeParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp1.
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp2.
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp3.
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp4.
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp5.
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp6.
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp7.
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp8.
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index.
    def visitIndex(self, ctx:ZCodeParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_function.
    def visitCall_function(self, ctx:ZCodeParser.Call_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lst_literal.
    def visitLst_literal(self, ctx:ZCodeParser.Lst_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolean_type.
    def visitBoolean_type(self, ctx:ZCodeParser.Boolean_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#common_data_type.
    def visitCommon_data_type(self, ctx:ZCodeParser.Common_data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_type.
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolean_operator.
    def visitBoolean_operator(self, ctx:ZCodeParser.Boolean_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_operator.
    def visitString_operator(self, ctx:ZCodeParser.String_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_operator.
    def visitNumber_operator(self, ctx:ZCodeParser.Number_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignored_newline.
    def visitIgnored_newline(self, ctx:ZCodeParser.Ignored_newlineContext):
        return self.visitChildren(ctx)



del ZCodeParser