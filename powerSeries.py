import math
import numpy as np
import sympy as sy
import pdb
from sympy.parsing.sympy_parser import parse_expr
from sympy import init_printing

def main():
    init_printing()
    coefficientsList = logPowerSeries(5,3)
    a=["10","4","-3","5"]
    inversePowerSeries(a)

def logPowerSeries(p, mod):
    x = sy.symbols('x')
    coefficientsDict = {}
    coefficientsDict['l0'] = 1
    sy.var('l0')
    sy.var('v0')
    coefficientsNames = []
    vNames = []
    coefficientsNames.append('l0')
    vNames.append('v0')
    coefficientsList = ['1']
    for i in range(mod-1):
        sy.var('l{}'.format(i+1))
        sy.var('v{}'.format(i+1))
        coefficientsNames.append('l{}'.format(i+1))
        vNames.append('v{}'.format(i+1))
        newCoefficient = logCoefficients(coefficientsDict, coefficientsNames, vNames, 5, i+1)
        coefficientsDict['l{}'.format(i+1)] = newCoefficient
        coefficientsList.append(newCoefficient)
    print(coefficientsList)
    logx = ""
    for i in range(len(coefficientsNames)):
        logx += "({}*x**{}) + ".format(coefficientsDict[coefficientsNames[i]],p**i)
    powerSeries = logx[:-2]
    print(sy.latex(parse_expr(powerSeries)))
    return coefficientsList

def logCoefficients(coefficientsDict, coefficientsNames, vNames, p, index):
    sumString = ""
    for i in range(len(coefficientsNames)):
        sumString += "{}*{}**{}**{}+".format(coefficientsNames[i], vNames[-(i+1)],p,i)

    sy.var('dummy')
    lhsExpression = parse_expr('dummy*{}'.format(coefficientsNames[-1]))
    lhsExpression = lhsExpression.subs(dummy,p)
    sumString = sumString[:-1]
    rhsExpression = parse_expr(sumString)
    rhsExpression = rhsExpression.subs(v0, p)
    for key in coefficientsDict:
        toReplace = str(key)
        rhsExpression = rhsExpression.subs(toReplace, coefficientsDict[key])

    variable = sy.symbols(coefficientsNames[-1])
    newCoefficient = sy.solveset(sy.Eq(lhsExpression, rhsExpression),variable)
    newCoefficientList = list(newCoefficient)
    #print("newCoefficientasfasd: {}".format(newCoefficientList[0]))
    return "({})".format(newCoefficientList[0])

def inversePowerSeries(coefficientsList):
    firstCoefficient = parse_expr(coefficientsList[0])
    inverseCoefficientsList = [str(1/firstCoefficient)]
    #pdb.set_trace()
    for n in range(1,len(coefficientsList)):
        newInverseCoefficient = ""
        for i in range(n):
            newInverseCoefficient += "({}*{})+".format(coefficientsList[i+1], inverseCoefficientsList[n-(i+1)])
        newInverseCoefficient = "-{}*({})".format(inverseCoefficientsList[0], newInverseCoefficient[:-1])
        inverseCoefficientsList.append(newInverseCoefficient)


    for i in range(len(inverseCoefficientsList)):
         print(parse_expr(inverseCoefficientsList[i]))







if __name__ == '__main__':
    main()
