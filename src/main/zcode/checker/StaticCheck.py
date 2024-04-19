from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

# from abc import ABC


class ZCodeType(Type):
    pass


class FuncZType(ZCodeType):
    def __init__(self, params=[], typ=None, body=False):
        self.params = params
        self.typ = typ
        self.body = body


class VarZType(ZCodeType):
    def __init__(self, typ=None):
        self.typ = typ


class ArrayZType(Type):
    def __init__(self, size, typ):
        self.size = size
        self.typ = typ


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast, ):
        self.ast = ast
        self.ForBlockCounter = 0

        self.function = None  # ! hàm hiện tại đang được dùng để kiểm tra static
        self.Return = False  # ! kiểm tra hàm hiện tại có return hay không

        #! lưu danh sách các hàm dưới dạng Dict
        # self.listFunction = [{
        #     "readNumber": FuncZType([], NumberType(), True),
        #     "readBool": FuncZType([], BoolType(), True),
        #     "readString": FuncZType([], StringType(), True),
        #     "writeNumber": FuncZType([NumberType()], VoidType(), True),
        #     "writeBool": FuncZType([BoolType()], VoidType(), True),
        #     "writeString": FuncZType([StringType()], VoidType(), True)
        # }]

        self.list_of_function = [{}]

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

    def prRed(self,skk): print("\033[91m {}\033[00m".format(skk))

    def prGreen(self,skk): print("\033[92m {}\033[00m".format(skk))

    def prYellow(self,skk): print("\033[93m {}\033[00m" .format(skk))

    def prLightPurple(self,skk): print("\033[94m {}\033[00m" .format(skk))

    def prPurple(self,skk): print("\033[95m {}\033[00m" .format(skk))

    def prCyan(self,skk): print("\033[96m {}\033[00m" .format(skk))

    def prLightGray(self,skk): print("\033[97m {}\033[00m" .format(skk))

    def prBlack(self,skk): print("\033[98m {}\033[00m" .format(skk))

    def check(self):
        self.visit(self.ast, [{}])
        return ""

    def compareTypeInDecl(self, lhs, rhs):
        if (lhs is None and rhs is None):
            return False
        elif (lhs is not None and rhs is None):
            return True
        elif (lhs is None and rhs is not None):
            return True
        else:
            if (isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType)):
                print("********* lhs.eleType: ", lhs.eleType)
                print("********* rhs.eleType: ", rhs.eleType)
                if (str(lhs.eleType) != str(rhs.eleType)):
                    return False
                size_left = lhs.size
                size_right = rhs.size

                if size_left != size_right:
                    return False
                else:
                    for i in range(len(size_right)):
                        if size_left[i] != size_right[i]:
                            return False
                    else:
                        return True
            else:
                return (str(lhs) == str(rhs))

    def comparListTypeInDecl(self, lhs, rhs):
        size_left = len(lhs)
        size_right = len(rhs)
        if size_left != size_right:
            return False
        else:
            for i in range(size_right):
                if not self.compareTypeInDecl(lhs[i], rhs[i]):
                    return False
            else:
                return True

    def visitProgram(self, ast, param):
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
                print("No Entry Point due to not being VoidType")
                raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, param):
        print("\n\n", "visitVarDecl", ast.name.name)
        # print("-----ast: ", ast)
        self.prCyan("ast: " + str(ast))
        # Redeclared error
        if (param[0].get(ast.name.name) is not None):
            raise Redeclared(Variable(), ast.name.name)

        # create a new param that has type is equal to current Type
        param[0][ast.name.name] = VarZType(ast.varType)

        # If exist variable initialization --> visit
        if (ast.varInit):
            lhs = param[0][ast.name.name].typ  # vardecl type object

            # If doesn't not exist type (var, dynamic) --> set LHS = ZCodeTye
            if (param[0][ast.name.name].typ is None):
                lhs = ZCodeType()

            # Get type of variable initialization --> visit to get varInit object (typ and name)
            rhs = self.visit(ast.varInit, param)

            if (isinstance(rhs, NumberType)
                    or
                    isinstance(rhs, BoolType)
                    or
                    isinstance(rhs, StringType)
                ):
                rhs = VarZType(rhs)

            # if (rhs is VarZType):
            elif (isinstance(rhs, ArrayType)):
                rhs = ArrayZType(rhs.size, ArrayType(rhs.size, rhs.eleType))
            elif (
                rhs.typ is None
            ):
                rhs.typ = ZCodeType()

            # Debug my ass
            # for key in param[0].keys():
            #     print("name of param: ", key)
            #     print("type of param:", param[0][key].typ)
            # print("lhs: ", lhs)
            # print("rhs: ", rhs)
            if (
                ast.varType is None  # ? Xet luon ast
                and
                isinstance(rhs.typ, ZCodeType)
            ):
                # Case 1: both size of vardecl doesn't have type or type cannot be infered.
                print("1-----case1")
                raise TypeCannotBeInferred(ast)
            # Case 2: LHS = Type, RHS = Array
            elif (
                    isinstance(lhs, ZCodeType)
                    and
                    isinstance(rhs.typ, ArrayZType)):
                print("2-----case2")
                raise TypeCannotBeInferred(ast)
            # Case 3: LHS not Type, RHS = Array
            elif (
                    not isinstance(lhs, ZCodeType)
                    and isinstance(rhs.typ, ArrayZType)):
                print("3-----case3")
                # Case 3.1: LHS is String, Bool, Num
                if (
                    isinstance(lhs, StringType)
                    or isinstance(lhs, BoolType)
                    or isinstance(lhs, NumberType)
                ):
                    print("case3.1")
                    raise TypeMismatchInStatement(ast)
                # Case 3.2: LHS is array Type
                elif (isinstance(lhs, ArrayType)):
                    print("case3.2")
                    # self.compareTypeInDecl()
                    # TODO Not yet implement
            # Case 4: LHS is ZCodeType (dynamic, var, haven't been infered), RHS: String, Bool, Num
            elif (isinstance(lhs, ZCodeType)
                  and
                  (isinstance(rhs.typ, StringType)
                   or isinstance(rhs.typ, BoolType)
                   or isinstance(rhs.typ, NumberType))):
                print("4-----case4: LHS is ZCodeType, RHS: String, Bool, Num")
                ast.varType = rhs.typ  # Set type of current ast to rhs's type
                lhs = ast.varType  # Update variable LHS
                param[0][ast.name.name].typ = rhs.typ  # Update in param
            # Case 5: RHS is ZCodeType, LHS: String, Bool, Num
            elif (
                    (
                    isinstance(lhs, StringType)
                    or isinstance(lhs, BoolType)
                    or isinstance(lhs, NumberType)
                    )
                    and
                    isinstance(rhs.typ, ZCodeType)):
                print("5-----case5")
                rhs.typ = lhs
            elif (
                not isinstance(ast.varType, ZCodeType)
                and
                not isinstance(rhs.typ, ZCodeType)
            ):
                print("6-----case6")
                print("--- ast.varTyoe", ast.varType)
                print("--- ast.varTyoe", rhs.typ)
                if not self.compareTypeInDecl(ast.varType, rhs.typ):
                    raise TypeMismatchInStatement(ast)
                ast.varType = rhs.typ
        print("-----param: ", param)

        print("```pass```")

        return None

    def visitFuncDecl(self, ast: FuncDecl, param):
        print("\n\nvisitFucnDecl", ast.name.name)

        check_exists_func = self.list_of_function[0].get(ast.name.name)

        # Check if exist in list of function
        if (check_exists_func):
            if (check_exists_func.body):
                raise Redeclared(Function(), ast.name.name)
            else:
                if (not ast.body):
                    raise Redeclared(Function(), ast.name.name)
        else:
            self.list_of_function[0][ast.name.name] = FuncZType(
                params=None, typ=None, body=(True if ast.body else False)
            )

        self.function = self.list_of_function[0][ast.name.name]
        typeParam = []
        listParam = {}
        typeParamToString = []

        # If have function params
        if (self.function.params):
            for i in self.function.params:
                typeParamToString.append(i.__str__())
            if (len(self.function.params) != len(ast.param)):
                raise Redeclared(Function(), ast.name.name)
            else:
                typeParamToString = sorted(typeParamToString)
                astParamToString = sorted(
                    [i.varType.__str__() for i in ast.param])
                if (typeParamToString != astParamToString):
                    raise Redeclared(Function(), ast.name.name)

        for i in ast.param:
            for j in listParam:
                if (j == i.name.name):
                    raise Redeclared(Parameter(), i.name.name)
            listParam[i.name.name] = VarZType(i.varType)
            typeParam.append(i.varType)
            typeParamToString.append(i.varType.__str__())

        self.function.params = typeParam

        if (ast.body):
            self.visit(ast.body, [listParam] + param)
            self.function.body = True
            if (not self.Return):
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

        for scope in param:
            founded = scope.get(ast.name)
            if (founded and isinstance(founded, VarZType)):
                check_exist = founded
                # Check var/dynamic
                if (not check_exist):
                    return ZCodeType()
                break
        else:
            raise Undeclared(Identifier(), ast.name)

        # print("founded: ", founded)
        # print("check_exist: ", check_exist)

        # if (founded is None):
        #     raise Undeclared(Identifier(), ast.name)

        return check_exist

    def visitCallExpr(self, ast: CallExpr, param):
        self.prYellow("\n\nvisitCallExpr:  " + str(ast.name.name))
        # self.debugLogs(ast, param, "visitCallExpr")
        if (not self.list_of_function[0].get(ast.name.name)):
            raise Undeclared(Function(), ast.name.name)

        call_to_function = self.list_of_function[0].get(ast.name.name)
        list_of_params = call_to_function.params
        list_of_args = ast.args

        print("call_to_function: ", call_to_function)
        print("list_of_params: ", list_of_params)
        print("list_of_args: ", list_of_args)

        if (len(list_of_params) != len(list_of_args)):
            raise TypeMismatchInExpression(ast)
        self.prGreen("PASS: length comparison args and params")

        for i in range(len(list_of_params)):
            func_args = self.visit(list_of_args[i], param)
            func_args = func_args.typ if isinstance(func_args, VarZType) else func_args
            self.prLightGray("func_args: " + str(func_args))
            self.prLightGray("list_of_params[i]: " + str(list_of_params[i]))
            self.prRed("check type: " + str(self.compareTypeInDecl(list_of_params[i], func_args)))
            if (not self.compareTypeInDecl(list_of_params[i], func_args)):
                raise TypeMismatchInExpression(ast)
        self.prGreen("PASS: not same types args and params")

        if call_to_function.typ is None:
            return call_to_function
                
        if self.compareTypeInDecl(call_to_function.typ, VoidType):
            raise TypeMismatchInExpression(ast)
    
        self.prGreen("PASS: Function called is VoidType")


        return VarZType(call_to_function.typ)

        # return call_to_function  # Trả về nguyên object expr để có gì gán type

    def visitCallStmt(self, ast, param):
        self.prYellow("\n\nvisitCallStmt:  " + str(ast.name.name))
        if (not self.list_of_function[0].get(ast.name.name)):
            raise Undeclared(Function(), ast.name.name)

        call_to_function = self.list_of_function[0].get(ast.name.name)
        list_of_params = call_to_function.params
        list_of_args = ast.args

        print("call_to_function: ", call_to_function)
        print("list_of_params: ", list_of_params)
        print("list_of_args: ", list_of_args)

        if (len(list_of_params) != len(list_of_args)):
            raise TypeMismatchInStatement(ast)
        self.prGreen("PASS: length comparison args and params")

        for i in range(len(list_of_params)):
            func_args = self.visit(list_of_args[i], param)
            func_args = func_args.typ if isinstance(func_args, VarZType) else func_args
            self.prLightGray("func_args: ")
            print(func_args)
            self.prLightGray("list_of_params[i]: ")
            print(list_of_params[i])
            self.prRed("check type: " + str(self.compareTypeInDecl(list_of_params[i], func_args)))
            if (
                not self.compareTypeInDecl(list_of_params[i], func_args)
            ):
                raise TypeMismatchInStatement(ast)
        self.prGreen("PASS: not same types args and params")

        if call_to_function.typ is None:
            return call_to_function
                
        if self.compareTypeInDecl(call_to_function.typ, VoidType):
            raise TypeMismatchInStatement(ast)
    
        self.prGreen("PASS: Function called is VoidType")
    
        return VarZType(call_to_function.typ)



    def visitIf(self, ast: If, param):
        # self.debugLogs(ast, param, "visitIf")
        print("\n\nvisitIf, ")
        expr_if = self.visit(ast.expr, param)
        expr_if = expr_if.typ if isinstance(expr_if, ZCodeType) else expr_if
        print("expr_if:", expr_if)

        if (expr_if is None):
            self.visit(ast.expr, param).typ = BoolType()

        if (not self.compareTypeInDecl(expr_if, BoolType())):
            raise TypeMismatchInStatement(ast)

        thenStmt = self.visit(ast.thenStmt, [{}] + param)
        thenStmt = thenStmt.typ if isinstance(
            thenStmt, ZCodeType) else thenStmt
        print("thenStmt:", thenStmt)

        if (ast.elifStmt):
            for elif_stmt in ast.elifStmt:
                print("\n\n visitElif")

                expr_elif = self.visit(elif_stmt[0], param)
                expr_elif = expr_elif.typ if isinstance(
                    expr_elif, ZCodeType) else expr_elif

                if (expr_elif is None):
                    self.visit(elif_stmt[0], param).typ = BoolType()
                if (not self.compareTypeInDecl(expr_elif, BoolType())):
                    raise TypeMismatchInStatement(ast)

                stmt_elif = self.visit(elif_stmt[1], param)
                stmt_elif = stmt_elif.typ if isinstance(
                    stmt_elif, ZCodeType) else stmt_elif
                if (stmt_elif is None):
                    stmt_elif = NumberType()
                if (not self.compareTypeInDecl(stmt_elif, NumberType())):
                    raise TypeMismatchInStatement(ast)

        elseStmt = None
        if (ast.elseStmt):
            elseStmt = self.visit(ast.elseStmt, [{}] + param)
            elseStmt = elseStmt.typ if isinstance(
                elseStmt, ZCodeType) else elseStmt
            print("elseStmt:", elseStmt)

    def visitFor(self, ast, param):
        print("\n\nvisitFor", ast.name.name)

        name = self.visit(ast.name, param)
        name = name.typ if isinstance(name, ZCodeType) else name

        condExpr = self.visit(ast.condExpr, param)
        condExpr = condExpr.typ if isinstance(
            condExpr, ZCodeType) else condExpr

        updExpr = self.visit(ast.updExpr, param)
        updExpr = updExpr.typ if isinstance(updExpr, ZCodeType) else updExpr

        if (name is None):
            self.visit(ast.name, param).typ = NumberType()

        if (not self.compareTypeInDecl(name, NumberType())):
            raise TypeMismatchInStatement(ast)
        print("---check ast.condExpr")
        if (condExpr is None):
            self.visit(ast.condExpr, param).typ = BoolType()

        if (not self.compareTypeInDecl(condExpr, BoolType())):
            raise TypeMismatchInStatement(ast)

        print("---check ast.updExpr")
        if (updExpr is None):
            self.visit(ast.updExpr, param).typ = NumberType()

        if (not self.compareTypeInDecl(updExpr, NumberType())):
            raise TypeMismatchInStatement(ast)

        print("---pass all check")

        self.ForBlockCounter += 1
        self.visit(ast.body, [{}] + param)
        self.ForBlockCounter -= 1

    def visitReturn(self, ast: Return, param):
        self.prYellow("\n\nvisitReturn")
        # print("ast: ", ast)
        function_type = None
        expr_type = None

        # If type of function is existed
        # --> function_type = self.function.typ
        if (self.function.typ is not None):
            function_type = self.function.typ
        else:
            function_type = None
        print("Check Function_type after checking self.function: ", function_type)
        # If have expr after Return --> return expr_type
        if (ast.expr):
            expr_type = self.visit(ast.expr, param)
            if (not self.Return):  # not return before
                if (expr_type is None):
                    raise TypeCannotBeInferred(ast)
                else:
                    self.Return = expr_type
                self.prGreen("PASS: Type cannot be inferred due to expr_type is None")
        else:
            self.Return = VoidType()

        if (function_type is None):
            print("Đéo có type của function")
            if (
                (
                    isinstance(expr_type, FuncZType)
                    or
                    isinstance(expr_type, VarZType)
                )
                and not isinstance(self.Return, VoidType)
            ):
                if (expr_type.typ is None):
                    print("Đéo có type của Expression luôn")
                    raise TypeCannotBeInferred(ast)
                function_type = expr_type.typ
                self.function.typ = expr_type.typ
                print("Đéo có type của function và có type của expression đã visit")

            else:
                print("Đéo có type của function và có type của expression")
                function_type = self.Return
                self.function.typ = self.Return
                print("function_type: ", function_type)
        elif (
            function_type is not None
            and
            (
                isinstance(expr_type, FuncZType)
                or
                isinstance(expr_type, VarZType)
            )
        ):
            print("có function_type và đéo có expr_type")
        elif (
            function_type is not None
            and
            not self.compareTypeInDecl(function_type, expr_type)
        ):
            raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, param):
        print("\n\nvisitAssign: ", ast.lhs, ast.rhs)
        """
            TODO giống phần kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
        """
        type_lhs = self.visit(ast.lhs, param)
        type_rhs = self.visit(ast.rhs, param)
        print("check visitAssign")

        if (isinstance(type_lhs, ArrayType)):
            type_lhs = ArrayZType(type_lhs.size, type_lhs.eleType)
            type_lhs = type_lhs.typ
        if (isinstance(type_rhs, ArrayType)):
            type_rhs = ArrayZType(type_rhs.size, type_rhs.eleType)
            type_rhs = type_rhs.typ
        type_lhs = type_lhs.typ if isinstance(
            type_lhs, ZCodeType) else type_lhs
        type_rhs = type_rhs.typ if isinstance(
            type_rhs, ZCodeType) else type_rhs

        print("type_lhs: ", type_lhs)
        print("type_rhs: ", type_rhs)

        if (
            type_lhs is None
            and
            type_rhs is None

        ):
            print("------case1------")
            raise TypeCannotBeInferred(ast)
        elif (
            type_lhs is not None
            and
            type_rhs is None
        ):
            print("------case2------")
            type_rhs = type_lhs
            # if (isinstance(type_rhs, ZCodeType)):
            self.visit(ast.rhs, param).typ = type_lhs
            return type_lhs
        elif (
            type_lhs is None
            and
            type_rhs is not None
        ):
            print("------case3------")
            type_lhs = type_rhs
            # if (isinstance(type_lhs, ZCodeType)):
            self.visit(ast.lhs, param).typ = type_rhs
            return type_rhs
        if not self.compareTypeInDecl(type_lhs, type_rhs):
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast: BinaryOp, param):
        self.prYellow("\n\nvisitBinaryOp: " + str(ast.left) + " " + str(ast.right))
        type_lhs = self.visit(ast.left, param)

        type_lhs = type_lhs.typ if isinstance(type_lhs, VarZType) else type_lhs
        op = ast.op
        self.prCyan("Operator: " +  str(op))
        # self.prPurple("type_lhs: " + str(self.visit(ast.left, param).typ))
        # self.prPurple("type_rhs: " + str(self.visit(ast.right, param).typ))
        if (
            op == '+'
            or
            op == '-'
            or
            op == '*'
            or
            op == '/'
            or
            op == '%'
        ):
            
            if (type_lhs is None):
                self.visit(ast.left, param).typ = NumberType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = NumberType()
                    return VarZType(NumberType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, NumberType())):
                        raise TypeMismatchInExpression()
                    return VarZType(NumberType())
            else: #type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, NumberType())): # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else: # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs
                    
                    if (type_rhs is None): # if rhs is none 
                        self.visit(ast.right, param).typ = NumberType()
                        return VarZType(NumberType())
                    else: # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, NumberType())):
                            raise TypeMismatchInExpression()
                        return VarZType(NumberType())                        
            # self.prCyan("Operator: " +  str(op))
            # if (
            #     type_rhs is None
            #     and
            #     type_lhs is None
            # ):
            #     self.visit(ast.left, param).typ = NumberType()
            #     self.visit(ast.right, param).typ = NumberType()                
            #     return VarZType(NumberType())
            # elif (
            #     type_lhs is None
            #     and
            #     type_rhs is not None
            # ):
            #     if (not self.compareTypeInDecl(type_rhs, NumberType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.left, param).typ = NumberType()
            #     return VarZType(NumberType())

            # elif (
            #     type_lhs is not None
            #     and
            #     type_rhs is None
            # ):
            #     if (not self.compareTypeInDecl(type_lhs, NumberType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.right, param).typ = NumberType()                
            #     return VarZType(NumberType())
            # else:
            #     if (not self.compareTypeInDecl(type_lhs, NumberType())
            #         or
            #         not self.compareTypeInDecl(type_rhs, NumberType())
            #         ):
            #         raise TypeMismatchInExpression(ast)
            # return VarZType(NumberType())
        elif (
            op == '='
            or
            op == '!='
            or
            op == '<'
            or
            op == '>'
            or
            op == '<='
            or
            op == '>='
        ):
            if (type_lhs is None):
                self.visit(ast.left, param).typ = NumberType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = NumberType()
                    return VarZType(BoolType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, NumberType())):
                        raise TypeMismatchInExpression()
                    return VarZType(BoolType())
            else: #type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, NumberType())): # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else: # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs
                    
                    if (type_rhs is None): # if rhs is none 
                        self.visit(ast.right, param).typ = NumberType()
                        return VarZType(BoolType())
                    else: # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, NumberType())):
                            raise TypeMismatchInExpression()
                        return VarZType(BoolType())                        
            # self.prCyan("Operator: " +  str(op))
            # if (
            #     type_rhs is None
            #     and
            #     type_lhs is None
            # ):
            #     self.visit(ast.left, param).typ = NumberType()
            #     self.visit(ast.right, param).typ = NumberType()
            #     return VarZType(BoolType())
            # elif (
            #     type_lhs is None
            #     and
            #     type_rhs is not None
            # ):
            #     if (not self.compareTypeInDecl(type_rhs, NumberType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.left, param).typ = NumberType()
            #     return VarZType(BoolType())
            # elif (
            #     type_lhs is not None
            #     and
            #     type_rhs is None
            # ):
            #     if (not self.compareTypeInDecl(type_lhs, NumberType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.right, param).typ = NumberType()
            # else:
            #     if (not self.compareTypeInDecl(type_lhs, NumberType())
            #         or
            #         not self.compareTypeInDecl(type_rhs, NumberType())
            #         ):
            #         raise TypeMismatchInExpression(ast)
            # return VarZType(BoolType())
        elif (
            op == 'and'
            or
            op == 'or'
        ):
            if (type_lhs is None):
                self.visit(ast.left, param).typ = BoolType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = BoolType()
                    return VarZType(BoolType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, BoolType())):
                        raise TypeMismatchInExpression()
                    return VarZType(BoolType())
            else: #type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, BoolType())): # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else: # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs
                    
                    if (type_rhs is None): # if rhs is none 
                        self.visit(ast.right, param).typ = BoolType()
                        return VarZType(BoolType())
                    else: # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, BoolType())):
                            raise TypeMismatchInExpression()
                        return VarZType(BoolType())                                    
            # self.prCyan("Operator: " +  str(op))
            # if (
            #     type_rhs is None
            #     and
            #     type_lhs is None
            # ):
            #     self.visit(ast.left, param).typ = BoolType()
            #     self.visit(ast.right, param).typ = BoolType()
            #     return VarZType(BoolType())
            # elif (
            #     type_lhs is None
            #     and
            #     type_rhs is not None
            # ):
            #     if (not self.compareTypeInDecl(type_rhs, BoolType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.left, param).typ = BoolType()
            #     return VarZType(BoolType())
            # elif (
            #     type_lhs is not None
            #     and
            #     type_rhs is None
            # ):
            #     if (not self.compareTypeInDecl(type_lhs, BoolType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.right, param).typ = BoolType()
            #     return VarZType(BoolType())
            # else:
            #     if (not self.compareTypeInDecl(type_lhs, BoolType())
            #         or
            #         not self.compareTypeInDecl(type_rhs, BoolType())
            #         ):
            #         raise TypeMismatchInExpression(ast)
                
            # return VarZType(BoolType())
        elif (
            op == '=='
        ):
            if (type_lhs is None):
                self.visit(ast.left, param).typ = StringType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = StringType()
                    return VarZType(BoolType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, StringType())):
                        raise TypeMismatchInExpression()
                    return VarZType(BoolType())
            else: #type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, StringType())): # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else: # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs
                    
                    if (type_rhs is None): # if rhs is none 
                        self.visit(ast.right, param).typ = StringType()
                        return VarZType(BoolType())
                    else: # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, StringType())):
                            raise TypeMismatchInExpression()
                        return VarZType(BoolType()) 
            # self.prCyan("Operator: " +  str(op))
            # if (
            #     type_rhs is None
            #     and
            #     type_lhs is None
            # ):
            #     self.visit(ast.left, param).typ = StringType()
            #     self.visit(ast.right, param).typ = StringType()
            #     return VarZType(BoolType())
            # elif (
            #     type_lhs is None
            #     and
            #     type_rhs is not None
            # ):
            #     if (not self.compareTypeInDecl(type_rhs, StringType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.left, param).typ = StringType()
            #     return VarZType(BoolType())
            # elif (
            #     type_lhs is not None
            #     and
            #     type_rhs is None
            # ):
            #     if (not self.compareTypeInDecl(type_lhs, StringType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.right, param).typ = StringType()
            #     return VarZType(BoolType())
            # else:
            #     if (not self.compareTypeInDecl(type_lhs, StringType())
            #         or
            #         not self.compareTypeInDecl(type_rhs, StringType())
            #         ):
            #         raise TypeMismatchInExpression(ast)
                
            # return VarZType(BoolType())
        elif (
            op == '...'
        ):
            if (type_lhs is None):
                self.visit(ast.left, param).typ = StringType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = StringType()
                    return VarZType(StringType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, StringType())):
                        raise TypeMismatchInExpression()
                    return VarZType(StringType())
            else: #type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, StringType())): # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else: # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(type_rhs, VarZType) else type_rhs
                    
                    if (type_rhs is None): # if rhs is none 
                        self.visit(ast.right, param).typ = StringType()
                        return VarZType(StringType())
                    else: # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, StringType())):
                            raise TypeMismatchInExpression()
                        return VarZType(StringType()) 
            # self.prCyan("Operator: " +  str(op))
            # if (
            #     type_rhs is None
            #     and
            #     type_lhs is None
            # ):
            #     self.visit(ast.left, param).typ = StringType()
            #     self.visit(ast.right, param).typ = StringType()
            #     self.prPurple("type_lhs: " + str(self.visit(ast.left, param).typ))
            #     self.prPurple("type_rhs: " + str(self.visit(ast.right, param).typ))
            #     return VarZType(StringType())
            # elif (
            #     type_lhs is None
            #     and
            #     type_rhs is not None
            # ):
            #     if (not self.compareTypeInDecl(type_rhs, StringType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.left, param).typ = StringType()                
            #     return VarZType(StringType())
            # elif (
            #     type_lhs is not None
            #     and
            #     type_rhs is None
            # ):
            #     if (not self.compareTypeInDecl(type_lhs, StringType())):
            #         raise TypeMismatchInExpression(ast)
            #     self.visit(ast.right, param).typ = StringType()       
            # else:
            #     if (not self.compareTypeInDecl(type_lhs, StringType())
            #         or
            #         not self.compareTypeInDecl(type_rhs, StringType())
            #         ):
            #         raise TypeMismatchInExpression(ast)
            # return VarZType(StringType())
    def visitUnaryOp(self, ast : UnaryOp, param):
        self.prYellow("\n\visitUnaryOp" + str(ast.operand) + " " + str(ast.op))
        operand = self.visit(ast.operand, param)
        operand = operand.typ if isinstance(operand, ZCodeType) else operand
        op = ast.op
        self.prPurple("operand: " + str(operand))
        if (
            op == '+'
            or
            op == '-'
        ):
            self.prCyan("Operator: " +  str(op))
            if (
                operand is None
            ):
                operand = NumberType()
                return VarZType(NumberType())
            else:
                if (not self.compareTypeInDecl(operand, NumberType())):
                    raise TypeMismatchInExpression(ast)
                self.visit(operand, param).typ = NumberType()
                return VarZType(NumberType())
        elif(
            op == 'not'
        ):
            self.prCyan("Operator: " +  str(op))
            if (
                operand is None
            ):
                operand = BoolType()
                return VarZType(BoolType())
            else:
                if (not self.compareTypeInDecl(operand, BoolType())):
                    raise TypeMismatchInExpression(ast)
                self.visit(operand, param).typ = BoolType()
                return VarZType(BoolType())
            # elif (
            #     type_lhs is not None
            #     and
            #     type_rhs is None
            # ):
            #     if (not self.compareTypeInDecl(type_lhs, NumberType())):
            #         raise TypeMismatchInExpression(ast)
            #     type_lhs = NumberType()
            #     type_rhs = NumberType()                
            #     return VarZType(NumberType())

        

    def visitArrayCell(self, ast, param):
        self.debugLogs(ast, param, "visitArrayCell")

    def visitArrayLiteral(self, ast, param):
        # self.debugLogs(ast, param, "visitArrayLiteral")
        for item in ast.value:
            self.visit(item, param)
        typ = self.visit(ast.value[0], param)
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)

    def visitBlock(self, ast: Block, param):
        print("visitBlock")
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
