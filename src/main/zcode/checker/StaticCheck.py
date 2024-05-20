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
        self.Return = None  # ! kiểm tra hàm hiện tại có return hay không

        #! lưu danh sách các hàm dưới dạng Dict

        self.list_of_function = [{
            "readNumber": FuncZType([], NumberType(), True),
            "readBool": FuncZType([], BoolType(), True),
            "readString": FuncZType([], StringType(), True),
            "writeNumber": FuncZType([NumberType()], VoidType(), True),
            "writeBool": FuncZType([BoolType()], VoidType(), True),
            "writeString": FuncZType([StringType()], VoidType(), True)
        }]

    def prRed(self, skk): print("\033[91m {}\033[00m".format(skk))

    def prGreen(self, skk): print("\033[92m {}\033[00m".format(skk))

    def prYellow(self, skk): print("\033[93m {}\033[00m" .format(skk))

    def prLightPurple(self, skk): print("\033[94m {}\033[00m" .format(skk))

    def prPurple(self, skk): print("\033[95m {}\033[00m" .format(skk))

    def prCyan(self, skk): print("\033[96m {}\033[00m" .format(skk))

    def prLightGray(self, skk): print("\033[97m {}\033[00m" .format(skk))

    def prBlack(self, skk): print("\033[98m {}\033[00m" .format(skk))

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
                # print("********* lhs.eleType: ", lhs.eleType)
                # print("********* rhs.eleType: ", rhs.eleType)
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

    def visitProgram(self, ast, param):
        # self.prYellow("visitProgram")
        for i in ast.decl:
            self.visit(i, param)

        for funcdecl_key in self.list_of_function[0].keys():
            if (self.list_of_function[0][funcdecl_key].body == False):
                raise NoDefinition(funcdecl_key)

        main_function = self.list_of_function[0].get("main")

        if not main_function:
            # print("No Entry Point due to not exists main")
            raise NoEntryPoint()
        else:
            if main_function.params:
                # print("No Entry Point due to params")
                raise NoEntryPoint()
            if not isinstance(main_function.typ, VoidType):
                # print("No Entry Point due to not being VoidType")
                raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, param):
        # self.prYellow("visitVarDecl: " + str(ast.name.name))
        # # print("-----ast: ", ast)
        # self.prCyan("ast: " + str(ast))
        # Redeclared error
        if (param[0].get(ast.name.name) is not None):
            raise Redeclared(Variable(), ast.name.name)

        # create a new param that has type is equal to current Type
        # if (isinstance(ast.varType, ArrayType)):
        #     self.prCyan("ast.varType:   " + str(ast.varType))
        #     param[0][ast.name.name] = ArrayType(len(), ast.varType)
        param[0][ast.name.name] = VarZType(ast.varType)

        # If exist variable initialization --> visit
        if (ast.varInit):
            lhs = param[0][ast.name.name]  # vardecl type object
            rhs = self.visit(ast.varInit, param)
            # self.prRed(str(lhs.typ))

            # self.prLightGray("vardecl lhs: " + str(lhs))
            # self.prLightGray("vardecl rhs: " + str(rhs))

            if (isinstance(rhs, NumberType)
                or
                isinstance(rhs, BoolType)
                or
                isinstance(rhs, StringType)
                ):
                rhs = VarZType(rhs)
            elif (isinstance(rhs, ArrayType)):
                rhs = ArrayZType(rhs.size, rhs.eleType)
            
            # if ((isinstance(rhs, ArrayZType)) and (isinstance(lhs, VarZType))):
            #     raise TypeMismatchInStatement(ast)
            # if (rhs is not ArrayZType):
            # self.prRed("rhs:"  + str(rhs))
            # self.prRed("lhs:"  + str(lhs))
            # self.prRed("rhs.typ:"  + str(rhs.typ))
            # self.prRed("lhs.typ:"  + str(lhs.typ))
            if (rhs.typ is None
                and
                lhs.typ is None
                ):
                # self.prGreen("Both rhs.typ and lhs.typ is None")
                raise TypeCannotBeInferred(ast)
            elif (lhs.typ is not None
                    and
                    rhs.typ is None
                ):
                # self.prGreen("lhs.typ is not None and rhs.typ is None")
                if (isinstance(rhs, ArrayZType)):
                    if (isinstance(lhs.typ, NumberType)
                        or isinstance(lhs.typ, StringType)
                        or isinstance(lhs.typ, BoolType)
                        ):
                        raise TypeMismatchInStatement(ast)
                    if (isinstance(lhs.typ, ArrayType)):
                        if not self.compareTypeInDecl(lhs.typ.eleType, rhs.typ):
                            raise TypeMismatchInStatement(ast)
                    # if (not isinstance(lhs.typ, ArrayType)):
                    #     self.prRed("case 1")
                    #     raise TypeMismatchInStatement(ast)
                    # else:
                    #     if not self.compareTypeInDecl(lhs.typ.eleType, rhs.typ):
                    #         raise TypeMismatchInStatement(ast)
                rhs.typ = lhs.typ
            elif (lhs.typ is None
                    and
                    rhs.typ is not None):
                # self.prGreen("lhs.typ is None and rhs.typ is not None")
                lhs.typ = rhs.typ
            else:
                # self.prGreen("Both rhs.typ and lhs.typ is not None")
                if (isinstance(rhs, ArrayZType)):
                    if (isinstance(lhs.typ, ArrayType)):
                        # if not self.compareTypeInDecl(lhs.typ.eleType, rhs.typ):
                        if not self.compareTypeInDecl(lhs.typ.eleType, rhs.typ):
                            raise TypeMismatchInStatement(ast)
                else:
                    if not self.compareTypeInDecl(lhs.typ, rhs.typ):
                        raise TypeMismatchInStatement(ast)
            # self.prRed(str(lhs.typ))

        # print("-----param: ", param)

        # self.prGreen("```pass visitVarDecl```")

        # return None

    def visitFuncDecl(self, ast: FuncDecl, param):
        # self.prYellow("visitFuncDecl: " + str(ast.name.name))
        # print("\n\nvisitFucnDecl", ast.name.name)
        check_exists_func = self.list_of_function[0].get(ast.name.name)

        # Check if exist in list of function
        if (check_exists_func):
            # self.prRed(str(check_exists_func))
            # self.prRed(str(check_exists_func.typ))

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
        # self.prPurple("self.Return before: " + str(self.Return))
        self.Return = None
        if (ast.body):
            self.visit(ast.body, [listParam] + param)
            self.function.body = True

            if self.Return is None:
                checker = self.list_of_function[0][ast.name.name].typ if isinstance(
                    self.list_of_function[0][ast.name.name], FuncZType) else self.list_of_function[0][ast.name.name]
                # self.prLightPurple(
                #     "function type: " + str(self.list_of_function[0][ast.name.name].typ))
                # self.prLightPurple("checker: " + str(checker))
                if checker is None:
                    self.list_of_function[0][ast.name.name].typ = VoidType()
                    # self.prLightPurple("function type - after assigning type: " +
                    #                    str(self.list_of_function[0][ast.name.name].typ))
                elif (not isinstance(checker, VoidType)):
                    raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast: Id, param):
        # self.debugLogs(ast, param, "visitId")
        # print("visitId", ast.name)
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

        return check_exist

    def visitCallExpr(self, ast: CallExpr, param):
        # self.prYellow("\n\nvisitCallExpr:  " + str(ast.name.name))
        # self.debugLogs(ast, param, "visitCallExpr")
        if (not self.list_of_function[0].get(ast.name.name)):
            raise Undeclared(Function(), ast.name.name)

        call_to_function = self.list_of_function[0].get(ast.name.name)
        list_of_params = call_to_function.params
        list_of_args = ast.args

        # print("call_to_function: ", call_to_function)
        # print("list_of_params: ", list_of_params)
        # print("list_of_args: ", list_of_args)

        if (len(list_of_params) != len(list_of_args)):
            raise TypeMismatchInExpression(ast)
        # self.prGreen("PASS: length comparison args and params")

        for i in range(len(list_of_params)):
            func_args = self.visit(list_of_args[i], param)
            func_args = func_args.typ if isinstance(
                func_args, VarZType) else func_args
            # self.prLightGray("func_args: " + str(func_args))
            # self.prLightGray("list_of_params[i]: " + str(list_of_params[i]))
            # self.prRed(
            #     "check type: " + str(self.compareTypeInDecl(list_of_params[i], func_args)))
            if (not self.compareTypeInDecl(list_of_params[i], func_args)):
                raise TypeMismatchInExpression(ast)
        # self.prGreen("PASS: not same types args and params")

        if call_to_function.typ is None:
            return call_to_function

        if self.compareTypeInDecl(call_to_function.typ, VoidType):
            raise TypeMismatchInExpression(ast)

        # self.prGreen("PASS: Function called is VoidType")

        return VarZType(call_to_function.typ)

    def visitCallStmt(self, ast, param):
        # self.prYellow("\n\nvisitCallStmt:  " + str(ast.name.name))
        if (not self.list_of_function[0].get(ast.name.name)):
            raise Undeclared(Function(), ast.name.name)

        call_to_function = self.list_of_function[0].get(ast.name.name)
        list_of_params = call_to_function.params
        list_of_args = ast.args

        # print("call_to_function: ", call_to_function)
        # print("list_of_params: ", list_of_params)
        # print("list_of_args: ", list_of_args)

        if (len(list_of_params) != len(list_of_args)):
            raise TypeMismatchInStatement(ast)
        # self.prGreen("PASS: length comparison args and params")

        for i in range(len(list_of_params)):
            func_args = self.visit(list_of_args[i], param)
            func_args = func_args.typ if isinstance(
                func_args, VarZType) else func_args
            # self.prLightGray("func_args: ")
            # print(func_args)
            # self.prLightGray("list_of_params[i]: ")
            # print(list_of_params[i])
            # self.prRed(
            #     "check type: " + str(self.compareTypeInDecl(list_of_params[i], func_args)))
            if (
                not self.compareTypeInDecl(list_of_params[i], func_args)
            ):
                raise TypeMismatchInStatement(ast)
        # self.prGreen("PASS: not same types args and params")

        if call_to_function.typ is None:
            return call_to_function

        if self.compareTypeInDecl(call_to_function.typ, VoidType):
            raise TypeMismatchInStatement(ast)

        # self.prGreen("PASS: Function called is VoidType")

        return VarZType(call_to_function.typ)

    def visitIf(self, ast: If, param):
        # self.debugLogs(ast, param, "visitIf")
        # print("\n\nvisitIf, ")
        expr_if = self.visit(ast.expr, param)
        expr_if = expr_if.typ if isinstance(expr_if, ZCodeType) else expr_if
        # print("expr_if:", expr_if)

        if (expr_if is None):
            self.visit(ast.expr, param).typ = BoolType()

        if (not self.compareTypeInDecl(expr_if, BoolType())):
            raise TypeMismatchInStatement(ast)

        thenStmt = self.visit(ast.thenStmt, [{}] + param)
        thenStmt = thenStmt.typ if isinstance(
            thenStmt, ZCodeType) else thenStmt
        # print("thenStmt:", thenStmt)

        if (ast.elifStmt):
            for elif_stmt in ast.elifStmt:
                # print("\n\n visitElif")

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
            # print("elseStmt:", elseStmt)

    def visitFor(self, ast, param):
        # print("\n\nvisitFor", ast.name.name)

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
        # print("---check ast.condExpr")
        if (condExpr is None):
            self.visit(ast.condExpr, param).typ = BoolType()

        if (not self.compareTypeInDecl(condExpr, BoolType())):
            raise TypeMismatchInStatement(ast)

        # print("---check ast.updExpr")
        if (updExpr is None):
            self.visit(ast.updExpr, param).typ = NumberType()

        if (not self.compareTypeInDecl(updExpr, NumberType())):
            raise TypeMismatchInStatement(ast)

        # print("---pass all check")

        self.ForBlockCounter += 1
        self.visit(ast.body, [{}] + param)
        self.ForBlockCounter -= 1

    def visitReturn(self, ast: Return, param):
        # self.prYellow("\n\nvisitReturn")
        # print("ast: ", ast)
        function_type = None
        expr_type = None

        # If type of function is existed
        # --> function_type = self.function.typ
        if (self.function.typ is not None):
            function_type = self.function.typ
        else:
            function_type = None
        # print("Check Function_type after checking self.function: ", function_type)
        # If have expr after Return --> return expr_type
        if (ast.expr):
            expr_type = self.visit(ast.expr, param)
            if (not self.Return):  # not return before
                if (expr_type is None):
                    raise TypeCannotBeInferred(ast)
                else:
                    self.Return = expr_type
                # self.prGreen(
                #     "PASS: Type cannot be inferred due to expr_type is None")
        else:
            self.Return = VoidType()

        if (function_type is None):
            # print("Đéo có type của function")
            if (
                (
                    isinstance(expr_type, FuncZType)
                    or
                    isinstance(expr_type, VarZType)
                )
                and not isinstance(self.Return, VoidType)
            ):
                if (expr_type.typ is None):
                    # print("Đéo có type của Expression luôn")
                    raise TypeCannotBeInferred(ast)
                function_type = expr_type.typ
                self.function.typ = expr_type.typ
                # print("Đéo có type của function và có type của expression đã visit")

            else:
                # print("Đéo có type của function và có type của expression")
                function_type = self.Return
                self.function.typ = self.Return
                # print("function_type: ", function_type)
        elif (
            function_type is not None
            and
            (
                isinstance(expr_type, FuncZType)
                or
                isinstance(expr_type, VarZType)
            )
        ):
            return
        elif (
            function_type is not None
            and
            not self.compareTypeInDecl(function_type, expr_type)
        ):
            raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, param):
        # print("\n\nvisitAssign: ", ast.lhs, ast.rhs)
        """
            TODO giống phần kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
        """
        type_lhs = self.visit(ast.lhs, param)
        type_rhs = self.visit(ast.rhs, param)
        # print("check visitAssign")

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

        # print("type_lhs: ", type_lhs)
        # print("type_rhs: ", type_rhs)

        if (
            type_lhs is None
            and
            type_rhs is None

        ):
            # print("------case1------")
            raise TypeCannotBeInferred(ast)
        elif (
            type_lhs is not None
            and
            type_rhs is None
        ):
            # print("------case2------")
            type_rhs = type_lhs
            # if (isinstance(type_rhs, ZCodeType)):
            self.visit(ast.rhs, param).typ = type_lhs
            return type_lhs
        elif (
            type_lhs is None
            and
            type_rhs is not None
        ):
            # print("------case3------")
            type_lhs = type_rhs
            # if (isinstance(type_lhs, ZCodeType)):
            self.visit(ast.lhs, param).typ = type_rhs
            return type_rhs
        if not self.compareTypeInDecl(type_lhs, type_rhs):
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast: BinaryOp, param):
        # self.prYellow("\n\nvisitBinaryOp: " +
        #               str(ast.left) + " " + str(ast.right))
        type_lhs = self.visit(ast.left, param)

        type_lhs = type_lhs.typ if isinstance(type_lhs, VarZType) else type_lhs
        op = ast.op
        # self.prCyan("Operator: " + str(op))
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
                type_rhs = type_rhs.typ if isinstance(
                    type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = NumberType()
                    return VarZType(NumberType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, NumberType())):
                        raise TypeMismatchInExpression()
                    return VarZType(NumberType())
            else:  # type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, NumberType())):  # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else:  # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(
                        type_rhs, VarZType) else type_rhs

                    if (type_rhs is None):  # if rhs is none
                        self.visit(ast.right, param).typ = NumberType()
                        return VarZType(NumberType())
                    else:  # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, NumberType())):
                            raise TypeMismatchInExpression()
                        return VarZType(NumberType())

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
                type_rhs = type_rhs.typ if isinstance(
                    type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = NumberType()
                    return VarZType(BoolType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, NumberType())):
                        raise TypeMismatchInExpression()
                    return VarZType(BoolType())
            else:  # type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, NumberType())):  # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else:  # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(
                        type_rhs, VarZType) else type_rhs

                    if (type_rhs is None):  # if rhs is none
                        self.visit(ast.right, param).typ = NumberType()
                        return VarZType(BoolType())
                    else:  # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, NumberType())):
                            raise TypeMismatchInExpression()
                        return VarZType(BoolType())

        elif (
            op == 'and'
            or
            op == 'or'
        ):
            if (type_lhs is None):
                self.visit(ast.left, param).typ = BoolType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(
                    type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = BoolType()
                    return VarZType(BoolType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, BoolType())):
                        raise TypeMismatchInExpression()
                    return VarZType(BoolType())
            else:  # type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, BoolType())):  # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else:  # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(
                        type_rhs, VarZType) else type_rhs

                    if (type_rhs is None):  # if rhs is none
                        self.visit(ast.right, param).typ = BoolType()
                        return VarZType(BoolType())
                    else:  # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, BoolType())):
                            raise TypeMismatchInExpression()
                        return VarZType(BoolType())
        elif (
            op == '=='
        ):
            if (type_lhs is None):
                self.visit(ast.left, param).typ = StringType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(
                    type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = StringType()
                    return VarZType(BoolType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, StringType())):
                        raise TypeMismatchInExpression()
                    return VarZType(BoolType())
            else:  # type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, StringType())):  # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else:  # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(
                        type_rhs, VarZType) else type_rhs

                    if (type_rhs is None):  # if rhs is none
                        self.visit(ast.right, param).typ = StringType()
                        return VarZType(BoolType())
                    else:  # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, StringType())):
                            raise TypeMismatchInExpression()
                        return VarZType(BoolType())

        elif (
            op == '...'
        ):
            if (type_lhs is None):
                self.visit(ast.left, param).typ = StringType()
                type_rhs = self.visit(ast.right, param)
                type_rhs = type_rhs.typ if isinstance(
                    type_rhs, VarZType) else type_rhs

                if (type_rhs is None):
                    self.visit(ast.right, param).typ = StringType()
                    return VarZType(StringType())
                else:
                    if (not self.compareTypeInDecl(type_rhs, StringType())):
                        raise TypeMismatchInExpression()
                    return VarZType(StringType())
            else:  # type_lhs is not None
                if (not self.compareTypeInDecl(type_lhs, StringType())):  # if lhs is not desired type
                    raise TypeMismatchInExpression(ast)
                else:  # if lhs is desired type
                    type_rhs = self.visit(ast.right, param)
                    type_rhs = type_rhs.typ if isinstance(
                        type_rhs, VarZType) else type_rhs

                    if (type_rhs is None):  # if rhs is none
                        self.visit(ast.right, param).typ = StringType()
                        return VarZType(StringType())
                    else:  # if rhs is not none --> check if desired type
                        if (not self.compareTypeInDecl(type_rhs, StringType())):
                            raise TypeMismatchInExpression()
                        return VarZType(StringType())

    def visitUnaryOp(self, ast: UnaryOp, param):
        # self.prYellow("\n\visitUnaryOp" + str(ast.operand) + " " + str(ast.op))
        operand = self.visit(ast.operand, param)
        operand = operand.typ if isinstance(operand, ZCodeType) else operand
        op = ast.op
        # self.prPurple("operand: " + str(operand))
        if (
            op == '+'
            or
            op == '-'
        ):
            # self.prCyan("Operator: " + str(op))
            if (
                operand is None
            ):
                self.visit(ast.operand, param).typ = NumberType()
                return VarZType(NumberType())
            else:
                if (not self.compareTypeInDecl(operand, NumberType())):
                    raise TypeMismatchInExpression(ast)
                self.visit(ast.operand, param).typ = NumberType()
                return VarZType(NumberType())
        elif (
            op == 'not'
        ):
            # self.prCyan("Operator: " + str(op))
            if (
                operand is None
            ):
                self.visit(ast.operand, param).typ = BoolType()
                return VarZType(BoolType())
            else:
                if (not self.compareTypeInDecl(operand, BoolType())):
                    raise TypeMismatchInExpression(ast)
                self.visit(operand, param).typ = BoolType()
                return VarZType(BoolType())

    def visitArrayCell(self, ast: ArrayCell, param):
        # self.prYellow("\n\n visitArrayCell: " + str(ast))
        array = self.visit(ast.arr, param)
        array = array.typ if isinstance(array, ZCodeType) else array
        # self.prLightGray("array: " + str(array))
        if (not isinstance(array, ArrayType)):
            raise TypeMismatchInExpression(ast)
        # self.prGreen("PASS: array is not ArrayType")
        if (len(array.size) < len(ast.idx)):
            raise TypeMismatchInExpression(ast)
        # self.prGreen("PASS: size of array is less than size ast.index")

        # self.prPurple("len(array): " + str(len(array.size)))
        # self.prPurple("len(ast.idx): " + str(len(ast.idx)))
        # self.prGreen("PASS: len of array is less than len of index")
        for index in ast.idx:
            checker = self.visit(index, param)
            # checker = checker.typ if isinstance(checker, ZCodeType) else checker
            # print("index checker: ", checker)
            if isinstance(checker, FuncZType):
                if (checker.typ is None):
                    if (self.list_of_function[0].get(index.name.name)
                        and
                        isinstance(self.list_of_function[0].get(
                                    index.name.name), FuncZType)
                        ):
                        self.list_of_function[0].get(
                            index.name.name).typ = NumberType()

            elif isinstance(checker, VarZType):
                # for scope in param:
                for scope in param:
                    if (scope.get(index.name) and isinstance(scope.get(index.name), VarZType)):
                        scope.get(index.name).typ = NumberType()
                        break

            elif (not isinstance(self.visit(index, param), NumberType)):
                raise TypeMismatchInExpression(ast)
            # self.prGreen("PASS: visit(index) is not NumberType")

        if (len(array.size) == len(ast.idx)):
            return VarZType(array.eleType)

        if len(array.size) > len(ast.idx):
            remaining_dimensions = array.size[len(ast.idx):]
            return ArrayZType(remaining_dimensions, array.eleType)

    def visitArrayLiteral(self, ast, param):
        # self.prYellow("\n\nvisitArrayLiteral: " + str(ast))
        #  ast: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), NumLit(1.0), NumLit(2.0)))
        checker = None # check array type
        for item in ast.value:
            checker = self.visit(item, param)
            checker = checker.typ if isinstance(
                checker, ZCodeType) else checker

            if ((self.compareTypeInDecl(checker, StringType)
                 or self.compareTypeInDecl(checker, BoolType)
                 or self.compareTypeInDecl(checker, NumberType)
                 )
                and checker is not ArrayType
                ):
                # self.prLightGray("ast.value is BSN and not an arrayType")
                break
        # print("checker: ", checker)
        if (
            (self.compareTypeInDecl(checker, StringType())
            or
            self.compareTypeInDecl(checker, BoolType())
            or
            self.compareTypeInDecl(checker, NumberType()))
            and checker is not ArrayType
            and checker is not None
        ):
            for item in ast.value:
                type_expr = self.visit(item, param)
                type_expr = type_expr.typ if isinstance(
                    type_expr, ZCodeType) else type_expr
                if (type_expr is None):
                    self.visit(item, param).typ = checker
                    # self.prRed("type_expr: " + str(type_expr))
                    # self.prRed("self.visit(item, param).typ: " + str(self.visit(item, param).typ))
                if (not self.compareTypeInDecl(type_expr, checker)
                    and
                    type_expr is not None
                    ):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)], checker)
        
        elif checker is None:
            # self.prRed("checker is None")
            type_expr = None
            # self.prRed("type_expr: " + str(type_expr))
            for item in ast.value:
                type_expr = self.visit(item, param)
                type_expr = type_expr.typ if isinstance(
                    type_expr, ZCodeType) else type_expr
                if (type_expr is ArrayType):
                    # self.prLightGray("type_expr is BSN and not an arrayType")
                    break
            
            # self.prRed("type_expr: " + str(type_expr))

            if (type_expr is not None):
                for item in ast.value:
                    type_expr_checker = self.visit(item, param)
                    type_expr_checker = type_expr_checker.typ if isinstance(
                        type_expr_checker, ZCodeType) else type_expr_checker
                    if (type_expr_checker is None):
                        self.visit(item, param).typ = type_expr
                        # self.prRed("type_expr_checker: " + str(type_expr_checker))
                        # self.prRed("self.visit(item, param).typ: " + str(self.visit(item, param).typ))
                    if (type_expr_checker is ArrayType):
                        if not self.compareTypeInDecl(type_expr_checker, type_expr):
                            raise TypeMismatchInExpression(ast)
                    if (not self.compareTypeInDecl(type_expr, type_expr_checker)
                        and
                        type_expr is not None
                        ):
                        raise TypeMismatchInExpression(ast)
                return ArrayType([len(ast.value)], type_expr)
            else:
                # self.prRed("checker is None and type_expr is None")
                return ArrayType([len(ast.value)], None)

        typ = self.visit(ast.value[0], param)
        typ = typ.typ if isinstance(typ, ZCodeType) else typ
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        # self.prRed("typ: " + str(typ))
        if (typ is None):
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)

    def visitBlock(self, ast: Block, param):
        # print("visitBlock")
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
