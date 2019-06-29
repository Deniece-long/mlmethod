#coding:utf-8
import Computer
import re

abstractN=[]
caseN =[]
continueN=[]
doubleN=[]
extendsN=[]
forN=[]
importN=[]
letN=[]
packageN=[]
shortN=[]
thisN=[]
tryN=[]
whileN=[]
argumentsN=[]
catchN=[]
debuggerN=[]
elseN=[]
falseN=[]
inN=[]
longN=[]
privateN=[]
staticN=[]
throwN=[]
typeofN=[]
withN=[]
booleanN=[]
charN=[]
defaultN=[]
enumN=[]
finalN=[]
gotoN=[]
instanceofN=[]
nativeN=[]
protectedN=[]
superN=[]
throwsN=[]
yieldN=[]
breakN=[]
classN=[]
deleteN=[]
finallyN=[]
ifN=[]
intN=[]
newN=[]
publicN=[]
switchN=[]
transientN=[]
voidN=[]
byteN=[]
constN=[]
doN=[]
exportN=[]
floatN=[]
implementsN=[]
interfaceN=[]
nullN=[]
returnN=[]
synchronizedN=[]
trueN=[]
volatileN=[]
ArrayN=[]
InfinityN=[]
MathN=[]
prototypeN=[]
DateN=[]
isFiniteN=[]
NaNN=[]
StringN=[]
isNaNN=[]
nameN=[]
isPrototypeOfN=[]
NumberN=[]
undefinedN=[]
hasOwnPropertyN=[]
lengthN=[]
ObjectN=[]
valueOfN=[]

def keywordSum(filecontent):
    abstractN = filecontent.split('abstract')
    caseN = filecontent.split('case')
    continueN = filecontent.split('continue')
    doubleN = filecontent.split('double')
    extendsN = filecontent.split('extents')
    forN = filecontent.split('for')
    importN = filecontent.split('import')
    letN = filecontent.split('let')
    packageN = filecontent.split('package')
    shortN = filecontent.split('short')
    thisN = filecontent.split('this')
    tryN = filecontent.split('try')
    whileN = filecontent.split('while')
    argumentsN = filecontent.split('arguments')
    catchN = filecontent.split('catch')
    debuggerN = filecontent.split('debugger')
    elseN = filecontent.split('else')
    falseN = filecontent.split('false')
    inN = filecontent.split('in')
    longN = filecontent.split('long')
    privateN = filecontent.split('private')
    staticN = filecontent.split('static')
    throwN = filecontent.split('throw')
    typeofN = filecontent.split('typeof')
    withN = filecontent.split('with')
    booleanN = filecontent.split('boolean')
    charN = filecontent.split('char')
    defaultN = filecontent.split('default')
    enumN = filecontent.split('enum')
    finalN = filecontent.split('final')
    gotoN = filecontent.split('goto')
    instanceofN = filecontent.split('instanceof')
    nativeN = filecontent.split('native')
    protectedN = filecontent.split('protected')
    superN = filecontent.split('super')
    throwsN = filecontent.split('throws')
    yieldN = filecontent.split('yield')
    breakN = filecontent.split('break')
    classN = filecontent.split('class')
    deleteN = filecontent.split('delete')
    finallyN = filecontent.split('finally')

    intN = filecontent.split('int')
    newN = filecontent.split('new')
    publicN = filecontent.split('public')
    switchN = filecontent.split('switch')
    transientN = filecontent.split('transient')
    voidN = filecontent.split('void')
    byteN = filecontent.split('byte')
    constN = filecontent.split('const')
    doN = filecontent.split('do')
    exportN = filecontent.split('export')
    floatN = filecontent.split('float')
    implementsN = filecontent.split('implements')
    interfaceN = filecontent.split('interface')
    nullN = filecontent.split('null')
    returnN = filecontent.split('return')
    synchronizedN = filecontent.split('synchronized')
    trueN = filecontent.split('true')
    volatileN = filecontent.split('volatile')
    ArrayN = filecontent.split('Array')
    InfinityN = filecontent.split('Infinity')
    MathN = filecontent.split('Math')
    prototypeN = filecontent.split('prototype')
    DateN = filecontent.split('Date')
    isFiniteN = filecontent.split('isFinite')
    NaNN = filecontent.split('NaN')
    StringN = filecontent.split('String')
    isNaNN = filecontent.split('isNaN')
    nameN = filecontent.split('name')
    isPrototypeOfN = filecontent.split('isPrototypeOf')
    NumberN = filecontent.split('Number')
    undefinedN = filecontent.split('undefined')
    hasOwnPropertyN = filecontent.split('hasOwnProperty')
    lengthN = filecontent.split('length')
    ObjectN = filecontent.split('Object')
    valueOfN = filecontent.split('valueOf')
    count1 = 0
    count2 =0
    count3 =0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11= 0
    count12= 0
    count13 = 0
    count14 = 0
    count15 = 0
    count16 = 0
    count17 = 0
    count18 = 0
    count19 = 0
    count20 = 0
    count21 = 0
    count22 = 0
    count23 = 0
    count24 = 0
    count25 = 0
    count26 = 0
    count27 = 0
    count28 = 0
    count29 = 0
    count30 = 0
    count31 = 0
    count32 = 0
    count33 = 0
    count34 = 0
    count35 = 0
    count36 = 0
    count37 = 0
    count38 = 0
    count39 = 0
    count40 = 0
    count41 = 0
    count42 = 0
    count43 = 0
    count44 = 0
    count45 = 0
    count46 = 0
    count47 = 0
    count48 = 0
    count49 = 0
    count50 = 0
    count51= 0
    count52= 0
    count53= 0
    count54= 0
    count55= 0
    count56= 0
    count57= 0
    count58= 0
    count59 = 0
    count60 = 0
    count61 = 0
    count62 = 0
    count63 = 0
    count64 = 0
    count65 = 0
    count66 = 0
    count67 = 0
    count68 = 0
    count69 = 0
    count70 = 0
    count71 = 0
    count72 = 0
    count73 = 0
    count74 = 0
    count75 = 0
    count76 = 0
    count77 = 0
    count78 = 0
    count79 = 0
    count80 = 0
    count81 =0



    for i in abstractN:
        count1 += 1
    count1 -= 1
    # print('abstract:', count1)

    for i in caseN:
        count2 += 1
    count2 -= 1
    # print('case:', count2)

    for i in continueN:
        count3 += 1
    count3 -= 1
    # print('continue:', count3)

    for i in doubleN:
        count4 += 1
    count4 -= 1
    # print('double:', count4)

    for i in extendsN:
        count5 += 1
    count5 -= 1
    # print('extends:', count5)

    for i in forN:
        count6 += 1
    count6 -= 1
    # print('for:', count6)

    for i in importN:
        count7 += 1
    count7 -= 1
    # print('import:', count7)

    for i in letN:
        count8 += 1
    count8 -= 1
    # print('let:', count8)

    for i in packageN:
        count9 += 1
    count9 -= 1
    # print('package:',count9)

    for i in shortN:
        count10 += 1
    count10 -= 1
    # print('short:', count10)

    for i in thisN:
        count11 += 1
    count11 -= 1
    # print('this:', count11)

    for i in tryN:
        count12 += 1
    count12 -= 1
    # print('try:',count12)

    for i in whileN:
        count13 += 1
    count13 -= 1
    # print('while:',count13)

    for i in argumentsN:
        count14 += 1
    count14 -= 1
    # print('arguments',count14)

    for i in catchN:
        count15 += 1
    count15 -= 1
    # print('catch', count15)

    for i in debuggerN:
        count16 += 1
    count16 -= 1
    # print('debugger', count16)

    for i in elseN:
        count17 += 1
    count17 -= 1
    # print('else:',count17)

    for i in falseN:
        count18 += 1
    count18 -= 1
    # print('false:',count18)

    count19=Computer.functionSum(filecontent)
    # print('function:',count19)

    for i in inN:
        count20 += 1
    count20 -= 1
    # print('in:',count20)

    for i in longN:
        count21 += 1
    count21 -= 1
    # print('long',count21)

    for i in privateN:
        count22 += 1
    count22 -= 1
    # print('private:',count22)

    for i in staticN:
        count23 += 1
    count23 -= 1
    # print('static:',count23)

    for i in throwN:
        count24 += 1
    count24 -= 1
    # print('throw:',count24)

    for i in typeofN:
        count25 += 1
    count25 -= 1
    # print('typeof:',count25)

    for i in withN:
        count26 += 1
    count26 -= 1
    # print('with:',count26)

    for i in booleanN:
        count27 += 1
    count27 -= 1
    # print('boolean:',count27)

    for i in charN:
        count28 += 1
    count28 -= 1
    # print('char:',count28)

    for i in defaultN:
        count29 += 1
    count29 -= 1
    # print('default:',count29)

    for i in enumN:
        count30 += 1
    count30 -= 1
    # print('enum:',count30)

    for i in finalN:
        count31 += 1
    count31 -= 1
    # print('final:',count31)

    for i in gotoN:
        count32 += 1
    count32 -= 1
    # print('foto:',count32)

    for i in instanceofN:
        count33 += 1
    count33 -= 1
    # print('instanceof:',count33)

    for i in nativeN:
        count34 += 1
    count34 -= 1
    for i in protectedN:
        count35 += 1
    count35 -= 1
    for i in superN:
        count36 += 1
    count36 -= 1
    for i in throwN:
        count37 += 1
    count37 -= 1
    count38=Computer.varSum(filecontent)
    # print('var=',count38)
    for i in yieldN:
        count39 += 1
    count39 -= 1
    for i in breakN:
        count40 += 1
    count40 -= 1
    # print('break:',count40)

    for i in classN:
        count41 += 1
    count41 -= 1
    # print('class:',count41)

    for i in deleteN:
        count42 += 1
    count42 -= 1

    for i in finallyN:
        count43 += 1
    count43 -= 1
    # print('finally:',count43)

    pattern = re.compile(r'if\s?\(.*?\)(\s|\{)')
    nofDigitR = pattern.findall(filecontent)
    count44 = len(nofDigitR)
    # print('if:',count44)

    for i in intN:
        count45 += 1
    count45 -= 1
    # print('int:',count45)

    for i in newN:
        count46 += 1
    count46 -= 1
    # print('new:',count46)

    for i in publicN:
        count47 += 1
    count47 -= 1

    for i in switchN:
        count48 += 1
    count48 -= 1
    # print('switch:',count48)

    for i in transientN:
        count49 += 1
    count49 -= 1
    # print('transient:',count49)

    for i in voidN:
        count50 += 1
    count50 -= 1
    # print('void:',count50)

    for i in byteN:
        count51 += 1
    count51 -= 1
    # print('byte:',count51)
    for i in constN:
        count52 += 1
    count52 -= 1
    # print('const:',count52)
    for i in doN:
        count53 += 1
    count53 -= 1
    # print('do:',count53)
    for i in exportN:
        count54 += 1
    count54 -= 1
    # print('export:',count54)
    for i in floatN:
        count55 += 1
    count55 -= 1
    # print('float:',count55)
    for i in implementsN:
        count56 += 1
    count56 -= 1
    # print('implement:',count56)
    for i in interfaceN:
        count57 += 1
    count57 -= 1
    # print('interface:',count57)
    for i in nullN:
        count58 += 1
    count58 -= 1
    # print('null:',count58)
    for i in returnN:
        count59 += 1
    count59 -= 1
    # print('return:',count59)
    for i in synchronizedN:
        count60 += 1
    count60 -= 1
    # print('synchronized:',count60)
    for i in trueN:
        count61 += 1
    count61 -= 1
    # print('true:',count61)
    for i in volatileN:
        count62 += 1
    count62 -= 1
    # print('volatile',count62)
    for i in ArrayN:
        count63 += 1
    count63 -= 1
    # print('Array:',count63)

    for i in InfinityN:
        count64 += 1
    count64 -= 1
    # print('Infinity:',count64)
    for i in MathN:
        count65 += 1
    count65 -= 1
    # print('Math',count65)
    for i in prototypeN:
        count66 += 1
    count66 -= 1
    # print('prototype:', count66)
    for i in DateN:
        count67 += 1
    count67 -= 1
    # print('Date:',count67)
    for i in isFiniteN:
        count68 += 1
    count68 -= 1
    for i in NaNN:
        count69 += 1
    count69 -= 1
    # print('NaN',count69)
    for i in StringN:
        count70 += 1
    count70 -= 1
    # print('String:',count70)
    count71 = Computer.evalSum(filecontent)
    # print('eval:',count71)
    for i in isNaNN:
        count72 += 1
    count72 -= 1
    # print('isNaN:',count72)
    for i in nameN:
        count73 += 1
    count73 -= 1
    # print('name:',count73)
    count74=Computer.toStringSum(filecontent)
    # print('toString:',count74)
    for i in isPrototypeOfN:
        count75 += 1
    count75 -= 1
    # print('isPrototypeOf:',count75)
    for i in NumberN:
        count76 += 1
    count76 -= 1
    # print('Number:',count76)
    for i in undefinedN:
        count77 += 1
    count77 -= 1
    for i in hasOwnPropertyN:
        count78 += 1
    count78 -= 1
    # print('hasOwnProperty:', count78)
    for i in lengthN:
        count79 += 1
    count79 -= 1
    # print('length:', count79)
    for i in ObjectN:
        count80 += 1
    count80 -= 1
    # print('Object:', count80)
    for i in valueOfN:
        count81 += 1
    count81 -= 1
    # print('valueOf:', count81)
    return count1+count2+count3+count4+count5+count6+count7+count8+count9+count10+count11+count12+count13+\
           count14+count15+count16+count17+count18+count19+count20+count21+count22+count23+count24+count25+\
           count26+count27+count28+count29+count30+count31+count32+count33+count34+count35+count36+count37+\
           count38+count39+count40+count41+count42+count43+count44+count45+count46+count47+count48+count49+\
           count50+count51+count52+count53+count54+count55+count56+count57+count58+count59+count60+count61+\
           count62+count63+count64+count65+count66+count67+count68+count69+count70+count71+count72+count73+\
           count74+count75+count76+count77+count78+count79+count80+count81