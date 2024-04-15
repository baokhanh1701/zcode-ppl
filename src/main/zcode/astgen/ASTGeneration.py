from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visit(self, ctx: ZCodeParser.ProgramContext):
        return ctx.accept(self)

    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        # print("reach visitProgram")

        return Program(self.visit(ctx.decl_list()))

    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        # print("reach visitDecl_list")
        if (ctx.decl_list()):
            return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())
        return [self.visit(ctx.decl())]

    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        # print("reach visitDecl")
        if (ctx.functions()):
            return self.visit(ctx.functions())
        return self.visit(ctx.variables())

    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        # print("reach visitVariables")
        if (ctx.implicit_keyword_variable()):
            return self.visit(ctx.implicit_keyword_variable())
        if (ctx.defined_type_variable()):
            return self.visit(ctx.defined_type_variable())
        return self.visit(ctx.implicit_dynamic_variable())


    # Visit a parse tree produced by ZCodeParser#implicit_keyword_variable.
    def visitImplicit_keyword_variable(self, ctx:ZCodeParser.Implicit_keyword_variableContext):
        # print("reach visitImplicit_keyword_variable")
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.VAR().getText(), self.visit(ctx.exp0()))
        

    # defined_type_variable: common_data_type (IDENTIFIER | (IDENTIFIER LB int_lst RB)) (ASSIGN exp0)?;
    def visitDefined_type_variable(self, ctx:ZCodeParser.Defined_type_variableContext):
        # print("reach visitDefined_type_variable")
        if (ctx.exp0()):
            if (ctx.int_lst()):
                return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType((self.visit(ctx.int_lst())), self.visit(ctx.common_data_type())), None, self.visit(ctx.exp0()))
            else:
                return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.common_data_type()), None, self.visit(ctx.exp0()))
        else:
            if (ctx.int_lst()):
                return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType((self.visit(ctx.int_lst())), self.visit(ctx.common_data_type())), None, None)
            else:
                return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.common_data_type()), None, None)
        # return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.common_data_type()), )
        

    # Visit a parse tree produced by ZCodeParser#int_lst.
    def visitInt_lst(self, ctx:ZCodeParser.Int_lstContext):
        # print("reach visitInt_lst")
        if (ctx.int_lst()):
            return [float(ctx.ZNUM().getText())] + self.visit(ctx.int_lst())
        return [float(ctx.ZNUM().getText())]

    # Visit a parse tree produced by ZCodeParser#implicit_dynamic_variable.
    def visitImplicit_dynamic_variable(self, ctx:ZCodeParser.Implicit_dynamic_variableContext):
        # print("reach visitImplicit_dynamic_variable")
        if (ctx.exp0()):
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.DYNAMIC().getText(), self.visit(ctx.exp0()))
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.DYNAMIC().getText(),None)

    # Visit a parse tree produced by ZCodeParser#functions.
    def visitFunctions(self, ctx:ZCodeParser.FunctionsContext):
        # print("reach visitFunctions")
        if (ctx.param_lst()):
            if (ctx.return_stm()):
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_lst()), self.visit(ctx.return_stm()))
            if (ctx.block_stm()):
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_lst()), self.visit(ctx.block_stm()))
            else:
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_lst()), None)
        else:
            if (ctx.return_stm()):
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), [], self.visit(ctx.return_stm()))
            if (ctx.block_stm()):
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), [], self.visit(ctx.block_stm()))
            else:
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), [], None)
        
    # Visit a parse tree produced by ZCodeParser#param_lst.
    def visitParam_lst(self, ctx:ZCodeParser.Param_lstContext):
        # print("reach visitParam_lst")
        if (ctx.param_lst()):
            return [self.visit(ctx.param())] + self.visit(ctx.param_lst())
        return [self.visit(ctx.param())]


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        # print("reach visitParam")
        if (ctx.int_lst()):
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType((self.visit(ctx.int_lst())), self.visit(ctx.common_data_type())), None, None)
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.common_data_type()), None, None)
    
    # Visit a parse tree produced by ZCodeParser#lst_stms.
    def visitLst_stms(self, ctx:ZCodeParser.Lst_stmsContext):
        # print("reach visitLst_stms")
        if (ctx.lst_stms()):
            return [self.visit(ctx.stm())] + self.visit(ctx.lst_stms())
        return [self.visit(ctx.stm())]

    # Visit a parse tree produced by ZCodeParser#stm.
    def visitStm(self, ctx:ZCodeParser.StmContext):
        # print("reach visitStm")
        if (ctx.declare_stm()):
            return self.visit(ctx.declare_stm())
        if (ctx.break_stm()):
            return self.visit(ctx.break_stm())
        if (ctx.for_stm()):
            return self.visit(ctx.for_stm())
        if (ctx.if_stm()):
            return self.visit(ctx.if_stm())
        if (ctx.assign_stm()):
            return self.visit(ctx.assign_stm())
        if (ctx.continue_stm()):
            return self.visit(ctx.continue_stm())
        if (ctx.return_stm()):
            return self.visit(ctx.return_stm())
        if (ctx.call_stm()):
            return self.visit(ctx.call_stm())
        if (ctx.block_stm()):
            return self.visit(ctx.block_stm())

    # Visit a parse tree produced by ZCodeParser#declare_stm.
    def visitDeclare_stm(self, ctx:ZCodeParser.Declare_stmContext):
        # print("reach visitDeclare_stm")
        
        return self.visit(ctx.variables())


    # Visit a parse tree produced by ZCodeParser#continue_stm.
    def visitContinue_stm(self, ctx:ZCodeParser.Continue_stmContext):
        # print("reach visitContinue_stm")

        return Continue()


    # Visit a parse tree produced by ZCodeParser#if_stm.
    def visitIf_stm(self, ctx:ZCodeParser.If_stmContext):
        # print("reach visitIf_stm")
        if not ctx.else_stm():
            return If(  self.visit(ctx.exp0()),
                        self.visit(ctx.stm()),
                        self.visit(ctx.elif_stm()),
                        None
                    )
        return If(  self.visit(ctx.exp0()),
                    self.visit(ctx.stm()),
                    self.visit(ctx.elif_stm()),
                    self.visit(ctx.else_stm())
                )


    # Visit a parse tree produced by ZCodeParser#elif_stm.
    def visitElif_stm(self, ctx:ZCodeParser.Elif_stmContext):
        # print("reach visitElif_stm - must return elifStmt: List[Tuple[Expr, Stmt]]")
        if ctx.elif_stm():
            return [tuple(  
                            [
                                self.visit(ctx.exp0()), 
                                self.visit(ctx.stm())
                            ]
                        )
                    ] + self.visit(ctx.elif_stm())
        return []


    # Visit a parse tree produced by ZCodeParser#else_stm.
    def visitElse_stm(self, ctx:ZCodeParser.Else_stmContext):
        # print("reach visitElse_stm")
        return self.visit(ctx.stm())


    # Visit a parse tree produced by ZCodeParser#for_stm.
    def visitFor_stm(self, ctx:ZCodeParser.For_stmContext):
        # print("reach visitFor_stm")
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exp0()[0]), self.visit(ctx.exp0()[1]), self.visit(ctx.stm()))


    # Visit a parse tree produced by ZCodeParser#assign_stm.
    def visitAssign_stm(self, ctx:ZCodeParser.Assign_stmContext):
        # print("reach visitAssign_stm")
        
        if (ctx.exp_list()):
            return Assign(ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exp_list())), self.visit(ctx.exp0()))
        else:
            return Assign(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exp0()))

    # Visit a parse tree produced by ZCodeParser#return_stm.
    def visitReturn_stm(self, ctx:ZCodeParser.Return_stmContext):
        # print("reach visitReturn_stm")
        if (ctx.exp0()):
            return Return(self.visit(ctx.exp0()))
        elif (ctx.call_stm()):
            return Return(self.visit(ctx.call_stm()))
        return Return()        

    # Visit a parse tree produced by ZCodeParser#break_stm.
    def visitBreak_stm(self, ctx:ZCodeParser.Break_stmContext):
        # print("reach visitBreak_stm")
        return Break()

    # Visit a parse tree produced by ZCodeParser#call_stm.
    def visitCall_stm(self, ctx:ZCodeParser.Call_stmContext):
        # print("reach visitCall_stm")
        if (ctx.arg_lst()):
            return CallStmt(Id(ctx.IDENTIFIER().getText()), list(self.visit(ctx.arg_lst())))
        else:
            return CallStmt(Id(ctx.IDENTIFIER().getText()), [])


    # Visit a parse tree produced by ZCodeParser#arg_lst.
    def visitArg_lst(self, ctx:ZCodeParser.Arg_lstContext):
        # print("reach visitArg_lst")
        if (ctx.arg_lst()):
            return [self.visit(ctx.exp0())] + self.visit(ctx.arg_lst())
        return [self.visit(ctx.exp0())]

    # Visit a parse tree produced by ZCodeParser#block_stm.
    def visitBlock_stm(self, ctx:ZCodeParser.Block_stmContext):
        # print("reach visitBlock_stm")
        if (ctx.lst_stms()):
            return Block(self.visit(ctx.lst_stms()))
        else:
            return Block([])


    # Visit a parse tree produced by ZCodeParser#exp_list.
    def visitExp_list(self, ctx:ZCodeParser.Exp_listContext):
        # print("reach visitExp_list")
        
        if (ctx.exp_list()):
            return [self.visit(ctx.exp0())] + self.visit(ctx.exp_list())
        return [self.visit(ctx.exp0())]


    # Visit a parse tree produced by ZCodeParser#exp0.
    def visitExp0(self, ctx:ZCodeParser.Exp0Context):
        # print("reach visitExp0")        
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp1()[0])
        
        operator = ctx.STRING_CONCAT().getText()
        lhs = self.visit(ctx.exp1()[0])
        rhs = self.visit(ctx.exp1()[1])
        return BinaryOp(operator,lhs,rhs)


    # Visit a parse tree produced by ZCodeParser#exp1.
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        # print("reach visitExp1")
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp2()[0])
        
        operator = ''
        if (ctx.EQ()):
            operator = ctx.EQ().getText()
        elif (ctx.STRING_EQUAL()):
            operator = ctx.STRING_EQUAL().getText()
        elif (ctx.NEQ()):
            operator = ctx.NEQ().getText()
        elif (ctx.LESS_THAN()):
            operator = ctx.LESS_THAN().getText()
        elif (ctx.GREATER_THAN()):
            operator = ctx.GREATER_THAN().getText()
        elif (ctx.LESS_THAN_EQUAL()):
            operator = ctx.LESS_THAN_EQUAL().getText()
        elif (ctx.GREATER_THAN_EQUAL()):
            operator = ctx.GREATER_THAN_EQUAL().getText()
        
        lhs = self.visit(ctx.exp2()[0])
        rhs = self.visit(ctx.exp2()[1])
        
        return BinaryOp(operator, lhs, rhs)


    # Visit a parse tree produced by ZCodeParser#exp2.
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        # print("reach visitExp2")
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp3())
        
        operator = ''
        if (ctx.AND()):
            operator = ctx.AND().getText()
        elif (ctx.OR()):
            operator = ctx.OR().getText()
        
        lhs = self.visit(ctx.exp2())
        rhs = self.visit(ctx.exp3())
        
        return BinaryOp(operator, lhs, rhs)


    # Visit a parse tree produced by ZCodeParser#exp3.
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        # print("reach visitExp3")        
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp4())
        
        operator = ''
        if (ctx.ADD()):
            operator = ctx.ADD().getText()
        elif (ctx.SUB_AND_NEG()):
            operator = ctx.SUB_AND_NEG().getText()
        
        lhs = self.visit(ctx.exp3())
        rhs = self.visit(ctx.exp4())
        
        return BinaryOp(operator, lhs, rhs)


    # Visit a parse tree produced by ZCodeParser#exp4.
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        # print("reach visitExp4")
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp5())
        
        operator = ''
        if (ctx.MUL()):
            operator = ctx.MUL().getText()
        elif (ctx.DIV()):
            operator = ctx.DIV().getText()
        elif (ctx.MOD()):
            operator = ctx.MOD().getText()
        
        lhs = self.visit(ctx.exp4())
        rhs = self.visit(ctx.exp5())
        
        return BinaryOp(operator, lhs, rhs)


    # Visit a parse tree produced by ZCodeParser#exp5.
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        # print("reach visitExp5")        
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp6())

        operator = ''
        if (ctx.NOT()):
            operator = ctx.NOT().getText()
        
        operand = self.visit(ctx.exp5())
        return UnaryOp(operator, operand)

    # Visit a parse tree produced by ZCodeParser#exp6.
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        # print("reach visitExp6")        
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp7())
        
        operator = ''
        if (ctx.SUB_AND_NEG()):
            operator = ctx.SUB_AND_NEG().getText()
        elif (ctx.ADD()):
            operator = ctx.ADD().getText()
        
        operand = self.visit(ctx.exp6())
        return UnaryOp(operator, operand)


    # Visit a parse tree produced by ZCodeParser#exp7.
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        # print("reach visitExp7")        
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp8())
        elif (ctx.getChildCount() == 2):
            # print("reach condition ctx.getChildCount() == 4")
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.index()))
        elif (ctx.arg_lst()):
            # print("reach condition len(ctx.index()) == 2")
            return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.arg_lst())), self.visit(ctx.index()))
        
        return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()), []), self.visit(ctx.index()))

    # Visit a parse tree produced by ZCodeParser#exp8.
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        # print("reach visitExp8")        
        if (ctx.array_lit()):
            return self.visit(ctx.array_lit())
        elif (ctx.call_function()):
            return self.visit(ctx.call_function())
        elif (ctx.ZNUM()):
            return NumberLiteral(float(ctx.ZNUM().getText()))
        elif (ctx.boolean_type()):
            return self.visit(ctx.boolean_type())
        elif (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())
        elif (ctx.IDENTIFIER()):
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.exp0())
        


    # Visit a parse tree produced by ZCodeParser#index.
    def visitIndex(self, ctx:ZCodeParser.IndexContext):
        # print("reach visitIndex")
        
        return self.visit(ctx.exp_list())


    # Visit a parse tree produced by ZCodeParser#call_function.
    def visitCall_function(self, ctx:ZCodeParser.Call_functionContext):
        # print("reach visitCall_function")        
        if (ctx.arg_lst()):
            return CallExpr(Id(ctx.IDENTIFIER().getText()), list(self.visit(ctx.arg_lst())))
        else:
            return CallExpr(Id(ctx.IDENTIFIER().getText()), [])


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        # print("reach visitLiteral")

        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        # print("reach visitArray_lit")

        return ArrayLiteral(self.visit(ctx.exp_list()))


    # Visit a parse tree produced by ZCodeParser#lst_literal.
    def visitLst_literal(self, ctx:ZCodeParser.Lst_literalContext):
        # print("reach visitLst_literal")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolean_type.
    def visitBoolean_type(self, ctx:ZCodeParser.Boolean_typeContext):
        # print("reach visitBoolean_type")

        if (ctx.TRUE()):
            return BooleanLiteral(True)
        else:
            return BooleanLiteral(False)


    # Visit a parse tree produced by ZCodeParser#common_data_type.
    def visitCommon_data_type(self, ctx:ZCodeParser.Common_data_typeContext):
        # print("reach visitCommon_data_type")
        
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()


    # Visit a parse tree produced by ZCodeParser#boolean_operator.
    def visitBoolean_operator(self, ctx:ZCodeParser.Boolean_operatorContext):
        # print("reach visitBoolean_operator")

        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_operator.
    def visitString_operator(self, ctx:ZCodeParser.String_operatorContext):
        # print("reach visitString_operator")
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_operator.
    def visitNumber_operator(self, ctx:ZCodeParser.Number_operatorContext):
        # print("reach visitNumber_operator")
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignored_newline.
    def visitIgnored_newline(self, ctx:ZCodeParser.Ignored_newlineContext):
        # print("reach visitIgnored_newline")
        
        return self.visitChildren(ctx)