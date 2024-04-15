from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from abc import ABC


class ZCodeType(ABC):
    pass


class FuncType(ZCodeType):
    def __init__(self, params=[], typ=None, body=False):
        self.params = params
        self.typ = typ
        self.body = body


class VarType(ZCodeType):
    def __init__(self, typ=None):
        self.typ = typ



class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast, ):
        self.ast = ast
        self.ForBlockCounter = 0

        self.function = None  # ! hàm hiện tại đang được dùng để kiểm tra static
        self.Return = False  # ! kiểm tra hàm hiện tại có return hay không

        #! lưu danh sách các hàm dưới dạng Dict
        # self.listFunction = [{
        #     "readNumber": FuncType([], NumberType(), True),
        #     "readBool": FuncType([], BoolType(), True),
        #     "readString": FuncType([], StringType(), True),
        #     "writeNumber": FuncType([NumberType()], VoidType(), True),
        #     "writeBool": FuncType([BoolType()], VoidType(), True),
        #     "writeString": FuncType([StringType()], VoidType(), True)
        # }]

        self.list_of_function = [{}]

    # def setTypeArray(self, typeArray, typeArrayZcode):
    #     if typeArray.size[0] != len(typeArrayZcode.eleType):
    #         return False
        
    #     #* trường hợp bên trong array là các kiểu nguyên thủy (array 1 chiều)
    #        #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
    #        #^ nếu typeArrayZcode.eleType[i] là arrayZcode : trả về False (vì 1 chiều mà bắt gán 2 chiều :) )
    #     if len(typeArray.size) == 1:
    #         #TODO implement
    #         for i in typeArrayZcode.eleType:
    #             if (typeArrayZcode.eleType[i] is ZCodeType):
    #                 typeArrayZcode.eleType[i].typ = typeArray.eleType
    #             if (typeArrayZcode.eleType[i] is ArrayType):
    #                 return False
    #     #* trường hợp bên trong array là các arrayType (array >= 2 chiều)
    #        #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
    #        #^ nếu typeArrayZcode.eleType[i] là arrayZcode : gọi đệ quy self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i]) để vào bên trong xem có lỗi gì không       
    #     else: return False
    #         #TODO implement
            
    def debugLogs(self, ast, param, visit_name):
        print("-------------- Start state of " + visit_name + "--------------")
        print("ast: ", ast)
        print("param: ", param)

        print("list of function: ", self.list_of_function)

        # print("ForBlockCounter: ", self.ForBlockCounter)
        # print("function static check: ", self.function)
        # print("Return: ", self.Return)

        print("-------------- Debug --------------")

        print("|")
        print("|")
        print("|")
        print("V")

    def check(self):
        self.visit(self.ast, [{}])
        return ""

    def comparType(self, LHS, RHS):
        pass

    def comparListType(self, listLHS, listRHS):
        pass

    def visitProgram(self, ast, param):
        print("======================================")
        print("visitProgram")
        for i in ast.decl:
            self.visit(i, param)

        for funcdecl_key in self.list_of_function[0].keys():
            if (self.list_of_function[0][funcdecl_key].body == False):
                raise NoDefinition(funcdecl_key)

        main_function = self.list_of_function[0].get("main")

        if not main_function:
            print("No Entry Point due to not exists main")
            raise NoEntryPoint()
        else:
            if main_function.params:
                print("No Entry Point due to params")
                raise NoEntryPoint()
            if not isinstance(main_function.typ, VoidType):
                print("No Entry Point due to VoidType")
                raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, param):
        print("visitVarDecl", ast.name.name)

        if (param[0].get(ast.name.name) != None):
            raise Redeclared(Variable(), ast.name.name)

        
        param[0][ast.name.name] = VarType(ast.varType)
        # print("* varInit: ", ast.varInit)
        # print("* type(varInit): ", type(ast.varInit))
        # print("* name: ", ast.name)
        # print("* type(name): ", type(ast.name))
        print("param: ", param)
        if (ast.varInit):
            lhs = ast.varType
            rhs = self.visit(ast.varInit, param)
            
            print("lhs: ", lhs)
            print("rhs: ", rhs)
            if (lhs is None and rhs is None):
                raise TypeCannotBeInferred(ast)
            if (lhs is Type and rhs is ArrayType):
                raise TypeCannotBeInferred(ast)
            if (lhs is not Type and rhs is ArrayType):
                if (lhs is StringType or lhs is BoolType or lhs is NumberType):
                    raise TypeMismatchInStatement(ast)
                if (lhs is ArrayType):
                    checkArray = False

    def visitFuncDecl(self, ast: FuncDecl, param):
        print("visitFucnDecl", ast.name.name)

        check_exists_func = self.list_of_function[0].get(ast.name.name)

        if (check_exists_func != None):
            if (check_exists_func.body):
                raise Redeclared(Function(), ast.name.name)
            else:
                if (not ast.body):
                    raise Redeclared(Function(), ast.name.name)
        else:
            self.list_of_function[0][ast.name.name] = FuncType(
                params=None, typ=None, body=(True if ast.body else False)
            )

        self.function = self.list_of_function[0][ast.name.name]
        typeParam = []
        listParam = {}
        typeParamToString = []
        
        # for i in self.function.params:

        if (self.function.params):
            for i in self.function.params:
                typeParamToString.append(i.__str__())
            if (len(self.function.params) != len(ast.param)):
                raise Redeclared(Function(), ast.name.name)
            else:
                typeParamToString = sorted(typeParamToString)
                astParamToString = sorted([i.varType.__str__() for i in ast.param])
                if (typeParamToString != astParamToString):
                    raise Redeclared(Function(), ast.name.name)

        for i in ast.param:
            for j in listParam:
                if (j == i.name.name):
                    raise Redeclared(Parameter(), i.name.name)
            listParam[i.name.name] = VarType(i.varType)
            typeParam.append(i.varType)
            typeParamToString.append(i.varType.__str__())
        
        self.function.params = typeParam
        
        if (ast.body):
            self.visit(ast.body, [listParam] + param)
            self.function.body = True

        if (self.Return == False):
            self.function.typ = VoidType()
        self.Return = False  # ! kiểm tra hàm hiện tại có return hay không
        #! hàm này không có return
        # if not self.Return:
        #     #! type cũng chưa có luôn ta xác định nó VoidType
        #     if self.list_of_function[0][ast.name.name].typ is None:
        #         self.list_of_function[0][ast.name.name].typ = VoidType()
        #     #! type đã có so sánh nó với VoidType
        # elif not self.list_of_function[0][ast.name.name].typ == VoidType():
        #     raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast: Id, param):
        # self.debugLogs(ast, param, "visitId")
        print("visitId", ast.name)        
        check_exist = None
        founded = None
        
        for scope in param:
            founded = scope.get(ast.name)
            if (founded):
                if (isinstance(founded, VarType)):
                    check_exist = founded.typ
                    break
            else: continue
        
        if (founded is None):
            raise Undeclared(Identifier(), ast.name)

        print("check_exist: ", check_exist)
        return check_exist


    def visitCallExpr(self, ast, param):
        print("visitCallExpr")
        # self.debugLogs(ast, param, "visitCallExpr")
        """
            TODO kiểm tra xem name có trong self.listFunction nén lỗi Undeclared
            VD 1: đúng 
            func foo()
            func main()begin
                var a <- foo()
            end

            VD 2: Undeclared
            func foo()
            func main()begin
                var a <- foo1()
            end

        """
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ xét listLHS (là method.param) và listRHS (là ast.args)
                ^ nếu len khác nhau TypeMismatchInExpression
                ^ nếu self.comparType(LHS[i], RHS[i]) -> TypeMismatchInExpression
            ^ nếu FuncType.typ is None thì return FuncType
            ^ nếu comparType(FuncType.typ, VoidType()) -> TypeMismatchInExpression
            ^ còn lại return FuncType.typ (giống phần VarType)
        """

    def visitCallStmt(self, ast, param):
        print("visitCallStmt")
        # self.debugLogs(ast, param, "visitCallStmt")
        """như CallExpr chỉ khác ở chỗ not comparType(FuncType.typ, VoidType()) -> TypeMismatchInStatement"""
        print("* param: ", param)
        print("* list of function: ", self.list_of_function)
        
        if (self.list_of_function[0].get(ast.name.name) is None):
            raise Undeclared(Function(), ast.name.name)
        
        method = self.list_of_function[0].get(ast.name.name)

    def visitIf(self, ast, param):
        # self.debugLogs(ast, param, "visitIf")
        """
            TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ ast.expr có LHS = BoolType(), RHS = self.visit(ast.expr, param)
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """

        """
            TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ expr in ast.elifStmt có LHS = BoolType(), RHS = .... 
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """

        """
            TODO kiểm tra elseStmt
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """

    def visitFor(self, ast, param):
        self.debugLogs(ast, param, "visitFor")

        self.ForBlockCounter += 1  # ! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param)  # ! tăng tầm vực mới
        self.ForBlockCounter -= 1  # ! cút khỏi vòng for nào anh em

    def visitReturn(self, ast: Return, param):

        if (ast.expr):
            self.Return = True
            self.function.typ = NumberType()

        # self.list_of_function[0][param["name"]].typ = NumberType() #* Change later
        # if (ast.expr == None):
        #     self.list_of_function[0][param["name"]].typ = VoidType()

        # self.Return = False
        # return NumberType()

    def visitAssign(self, ast, param):
        # self.debugLogs(ast, param, "visitAssign")
        print("visitAssign")
        """
            TODO giống phần kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
        """

    def visitBinaryOp(self, ast, param):
        self.debugLogs(ast, param, "visitBinaryOp")

    def visitUnaryOp(self, ast, param):
        self.debugLogs(ast, param, "visitUnaryOp")

    def visitArrayCell(self, ast, param):
        self.debugLogs(ast, param, "visitArrayCell")

    def visitArrayLiteral(self, ast, param):
        # self.debugLogs(ast, param, "visitArrayLiteral")
        #! code chỉ mang tính tham khảo, do BTL này không yêu cầu lỗi khác nhau ArrayLiteral nên thầy ko cho TypeCannotBeInferred
        for item in ast.value:
            self.visit(item, param)
        typ = self.visit(ast.value[0], param)

        #! đệ quy
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)

    def visitBlock(self, ast: Block, param):
        print("visitBlock")
        # self.debugLogs(ast, param, "visitBlock")
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block:
                self.visit(item, [{}] + param)
            else:
                self.visit(item, param)

    def visitContinue(self, ast, param):
        # self.debugLogs(ast, param, "visitContinue")
        #! kiểm tra đang ở vòng for hay không
        if self.ForBlockCounter == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        # self.debugLogs(ast, param, "visitBreak")
        #! kiểm tra đang ở vòng for hay không
        if self.ForBlockCounter == 0:
            raise MustInLoop(ast)

    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()
