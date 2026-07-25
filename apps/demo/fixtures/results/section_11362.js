function binl_md5(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 98, UInt8: 1>
    // USED → r98 = param1
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2
    // CODE → <LoadConstUInt8>: <Reg8: 97, UInt8: 5>
    // USED → r97 = 5
    // CODE → <RShift>: <Reg8: 2, Reg8: 1, Reg8: 97>
    // USED → r2 = BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.RIGHT_SHIFT: '>>'>, right=Identifier(name='r97'))
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 98, Reg8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 32>
    // USED → r0 = 32
    // CODE → <Mod>: <Reg8: 4, Reg8: 1, Reg8: 0>
    // USED → r4 = BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.MODULO: '%'>, right=Identifier(name='r0'))
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 128>
    // USED → r0 = 128
    // CODE → <LShift>: <Reg8: 0, Reg8: 0, Reg8: 4>
    // USED → r0 = BinaryExpression(left=Identifier(name='r0'), operator=<BinaryOperator.LEFT_SHIFT: '<<'>, right=BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.MODULO: '%'>, right=Identifier(name='r0')))
    // CODE → <BitOr>: <Reg8: 0, Reg8: 3, Reg8: 0>
    // USED → r0 = BinaryExpression(left=Identifier(name='r3'), operator=<BinaryOperator.BITWISE_OR: '|'>, right=BinaryExpression(left=Identifier(name='r0'), operator=<BinaryOperator.LEFT_SHIFT: '<<'>, right=BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.MODULO: '%'>, right=Identifier(name='r0'))))
    // CODE → <PutByVal>: <Reg8: 98, Reg8: 2, Reg8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 64>
    // USED → r0 = 64
    // CODE → <Add>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r0'))
    // CODE → <LoadConstUInt8>: <Reg8: 96, UInt8: 9>
    // USED → r96 = 9
    // CODE → <URshift>: <Reg8: 0, Reg8: 0, Reg8: 96>
    // USED → r0 = BinaryExpression(left=BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r0')), operator=<BinaryOperator.UNSIGNED_RIGHT_SHIFT: '>>>'>, right=Identifier(name='r96'))
    // CODE → <LoadConstUInt8>: <Reg8: 95, UInt8: 4>
    // USED → r95 = 4
    // CODE → <LShift>: <Reg8: 0, Reg8: 0, Reg8: 95>
    // USED → r0 = BinaryExpression(left=BinaryExpression(left=BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r0')), operator=<BinaryOperator.UNSIGNED_RIGHT_SHIFT: '>>>'>, right=Identifier(name='r96')), operator=<BinaryOperator.LEFT_SHIFT: '<<'>, right=Identifier(name='r95'))
    // CODE → <LoadConstUInt8>: <Reg8: 94, UInt8: 14>
    // USED → r94 = 14
    // CODE → <AddN>: <Reg8: 0, Reg8: 0, Reg8: 94>
    // USED → r0 = BinaryExpression(left=BinaryExpression(left=BinaryExpression(left=BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r0')), operator=<BinaryOperator.UNSIGNED_RIGHT_SHIFT: '>>>'>, right=Identifier(name='r96')), operator=<BinaryOperator.LEFT_SHIFT: '<<'>, right=Identifier(name='r95')), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r94'))
    // CODE → <PutByVal>: <Reg8: 98, Reg8: 0, Reg8: 1>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 98, UInt8: 1, string_id: 139>  # String: 'length' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstZero>: <Reg8: 93>
    // USED → r93 = 0
    // CODE → <Less>: <Reg8: 0, Reg8: 93, Reg8: 0>
    // USED → r0 = BinaryExpression(left=Identifier(name='r93'), operator=<BinaryOperator.LESS_THAN: '<'>, right=BinaryExpression(left=BinaryExpression(left=BinaryExpression(left=BinaryExpression(left=Identifier(name='r1'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r0')), operator=<BinaryOperator.UNSIGNED_RIGHT_SHIFT: '>>>'>, right=Identifier(name='r96')), operator=<BinaryOperator.LEFT_SHIFT: '<<'>, right=Identifier(name='r95')), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r94')))
    // CODE → <LoadConstInt>: <Reg8: 9, Imm32: 1732584193>
    // USED → r9 = 1732584193
    // CODE → <LoadConstInt>: <Reg8: 8, Imm32: -271733879>
    // USED → r8 = -271733879
    // CODE → <LoadConstInt>: <Reg8: 7, Imm32: -1732584194>
    // USED → r7 = -1732584194
    // CODE → <LoadConstInt>: <Reg8: 6, Imm32: 271733878>
    // USED → r6 = 271733878
    // CODE → <GetEnvironment>: <Reg8: 92, UInt8: 0>
    // USED → r92 = getEnvironment(0)
    // CODE → <LoadConstUndefined>: <Reg8: 91>
    // USED → r91 = undefined
    // CODE → <LoadConstUInt8>: <Reg8: 90, UInt8: 7>
    // USED → r90 = 7
    // CODE → <LoadConstInt>: <Reg8: 89, Imm32: -680876936>
    // USED → r89 = -680876936
    // CODE → <LoadConstUInt8>: <Reg8: 88, UInt8: 1>
    // USED → r88 = 1
    // CODE → <LoadConstUInt8>: <Reg8: 87, UInt8: 12>
    // USED → r87 = 12
    // CODE → <LoadConstInt>: <Reg8: 86, Imm32: -389564586>
    // USED → r86 = -389564586
    // CODE → <LoadConstUInt8>: <Reg8: 85, UInt8: 2>
    // USED → r85 = 2
    // CODE → <LoadConstUInt8>: <Reg8: 84, UInt8: 17>
    // USED → r84 = 17
    // CODE → <LoadConstInt>: <Reg8: 83, Imm32: 606105819>
    // USED → r83 = 606105819
    // CODE → <LoadConstUInt8>: <Reg8: 82, UInt8: 3>
    // USED → r82 = 3
    // CODE → <LoadConstUInt8>: <Reg8: 81, UInt8: 22>
    // USED → r81 = 22
    // CODE → <LoadConstInt>: <Reg8: 80, Imm32: -1044525330>
    // USED → r80 = -1044525330
    // CODE → <LoadConstInt>: <Reg8: 79, Imm32: -176418897>
    // USED → r79 = -176418897
    // CODE → <LoadConstInt>: <Reg8: 78, Imm32: 1200080426>
    // USED → r78 = 1200080426
    // CODE → <LoadConstUInt8>: <Reg8: 77, UInt8: 6>
    // USED → r77 = 6
    // CODE → <LoadConstInt>: <Reg8: 76, Imm32: -1473231341>
    // USED → r76 = -1473231341
    // CODE → <LoadConstInt>: <Reg8: 75, Imm32: -45705983>
    // USED → r75 = -45705983
    // CODE → <LoadConstUInt8>: <Reg8: 74, UInt8: 8>
    // USED → r74 = 8
    // CODE → <LoadConstInt>: <Reg8: 73, Imm32: 1770035416>
    // USED → r73 = 1770035416
    // CODE → <LoadConstInt>: <Reg8: 72, Imm32: -1958414417>
    // USED → r72 = -1958414417
    // CODE → <LoadConstUInt8>: <Reg8: 71, UInt8: 10>
    // USED → r71 = 10
    // CODE → <LoadConstInt>: <Reg8: 70, Imm32: -42063>
    // USED → r70 = -42063
    // CODE → <LoadConstUInt8>: <Reg8: 69, UInt8: 11>
    // USED → r69 = 11
    // CODE → <LoadConstInt>: <Reg8: 68, Imm32: -1990404162>
    // USED → r68 = -1990404162
    // CODE → <LoadConstInt>: <Reg8: 67, Imm32: 1804603682>
    // USED → r67 = 1804603682
    // CODE → <LoadConstUInt8>: <Reg8: 66, UInt8: 13>
    // USED → r66 = 13
    // CODE → <LoadConstInt>: <Reg8: 65, Imm32: -40341101>
    // USED → r65 = -40341101
    // CODE → <LoadConstInt>: <Reg8: 64, Imm32: -1502002290>
    // USED → r64 = -1502002290
    // CODE → <LoadConstUInt8>: <Reg8: 63, UInt8: 15>
    // USED → r63 = 15
    // CODE → <LoadConstInt>: <Reg8: 62, Imm32: 1236535329>
    // USED → r62 = 1236535329
    // CODE → <LoadConstInt>: <Reg8: 61, Imm32: -165796510>
    // USED → r61 = -165796510
    // CODE → <LoadConstInt>: <Reg8: 60, Imm32: -1069501632>
    // USED → r60 = -1069501632
    // CODE → <LoadConstInt>: <Reg8: 59, Imm32: 643717713>
    // USED → r59 = 643717713
    // CODE → <LoadConstUInt8>: <Reg8: 58, UInt8: 20>
    // USED → r58 = 20
    // CODE → <LoadConstInt>: <Reg8: 57, Imm32: -373897302>
    // USED → r57 = -373897302
    // CODE → <LoadConstInt>: <Reg8: 56, Imm32: -701558691>
    // USED → r56 = -701558691
    // CODE → <LoadConstInt>: <Reg8: 55, Imm32: 38016083>
    // USED → r55 = 38016083
    // CODE → <LoadConstInt>: <Reg8: 54, Imm32: -660478335>
    // USED → r54 = -660478335
    // CODE → <LoadConstInt>: <Reg8: 53, Imm32: -405537848>
    // USED → r53 = -405537848
    // CODE → <LoadConstInt>: <Reg8: 52, Imm32: 568446438>
    // USED → r52 = 568446438
    // CODE → <LoadConstInt>: <Reg8: 51, Imm32: -1019803690>
    // USED → r51 = -1019803690
    // CODE → <LoadConstInt>: <Reg8: 50, Imm32: -187363961>
    // USED → r50 = -187363961
    // CODE → <LoadConstInt>: <Reg8: 49, Imm32: 1163531501>
    // USED → r49 = 1163531501
    // CODE → <LoadConstInt>: <Reg8: 48, Imm32: -1444681467>
    // USED → r48 = -1444681467
    // CODE → <LoadConstInt>: <Reg8: 47, Imm32: -51403784>
    // USED → r47 = -51403784
    // CODE → <LoadConstInt>: <Reg8: 46, Imm32: 1735328473>
    // USED → r46 = 1735328473
    // CODE → <LoadConstInt>: <Reg8: 45, Imm32: -1926607734>
    // USED → r45 = -1926607734
    // CODE → <LoadConstInt>: <Reg8: 44, Imm32: -378558>
    // USED → r44 = -378558
    // CODE → <LoadConstInt>: <Reg8: 43, Imm32: -2022574463>
    // USED → r43 = -2022574463
    // CODE → <LoadConstUInt8>: <Reg8: 42, UInt8: 16>
    // USED → r42 = 16
    // CODE → <LoadConstInt>: <Reg8: 41, Imm32: 1839030562>
    // USED → r41 = 1839030562
    // CODE → <LoadConstUInt8>: <Reg8: 40, UInt8: 23>
    // USED → r40 = 23
    // CODE → <LoadConstInt>: <Reg8: 39, Imm32: -35309556>
    // USED → r39 = -35309556
    // CODE → <LoadConstInt>: <Reg8: 38, Imm32: -1530992060>
    // USED → r38 = -1530992060
    // CODE → <LoadConstInt>: <Reg8: 37, Imm32: 1272893353>
    // USED → r37 = 1272893353
    // CODE → <LoadConstInt>: <Reg8: 36, Imm32: -155497632>
    // USED → r36 = -155497632
    // CODE → <LoadConstInt>: <Reg8: 35, Imm32: -1094730640>
    // USED → r35 = -1094730640
    // CODE → <LoadConstInt>: <Reg8: 34, Imm32: 681279174>
    // USED → r34 = 681279174
    // CODE → <LoadConstInt>: <Reg8: 33, Imm32: -358537222>
    // USED → r33 = -358537222
    // CODE → <LoadConstInt>: <Reg8: 32, Imm32: -722521979>
    // USED → r32 = -722521979
    // CODE → <LoadConstInt>: <Reg8: 31, Imm32: 76029189>
    // USED → r31 = 76029189
    // CODE → <LoadConstInt>: <Reg8: 30, Imm32: -640364487>
    // USED → r30 = -640364487
    // CODE → <LoadConstInt>: <Reg8: 29, Imm32: -421815835>
    // USED → r29 = -421815835
    // CODE → <LoadConstInt>: <Reg8: 28, Imm32: 530742520>
    // USED → r28 = 530742520
    // CODE → <LoadConstInt>: <Reg8: 27, Imm32: -995338651>
    // USED → r27 = -995338651
    // CODE → <LoadConstInt>: <Reg8: 26, Imm32: -198630844>
    // USED → r26 = -198630844
    // CODE → <LoadConstInt>: <Reg8: 25, Imm32: 1126891415>
    // USED → r25 = 1126891415
    // CODE → <LoadConstInt>: <Reg8: 24, Imm32: -1416354905>
    // USED → r24 = -1416354905
    // CODE → <LoadConstUInt8>: <Reg8: 23, UInt8: 21>
    // USED → r23 = 21
    // CODE → <LoadConstInt>: <Reg8: 22, Imm32: -57434055>
    // USED → r22 = -57434055
    // CODE → <LoadConstInt>: <Reg8: 21, Imm32: 1700485571>
    // USED → r21 = 1700485571
    // CODE → <LoadConstInt>: <Reg8: 20, Imm32: -1894986606>
    // USED → r20 = -1894986606
    // CODE → <LoadConstInt>: <Reg8: 19, Imm32: -1051523>
    // USED → r19 = -1051523
    // CODE → <LoadConstInt>: <Reg8: 18, Imm32: -2054922799>
    // USED → r18 = -2054922799
    // CODE → <LoadConstInt>: <Reg8: 17, Imm32: 1873313359>
    // USED → r17 = 1873313359
    // CODE → <LoadConstInt>: <Reg8: 16, Imm32: -30611744>
    // USED → r16 = -30611744
    // CODE → <LoadConstInt>: <Reg8: 15, Imm32: -1560198380>
    // USED → r15 = -1560198380
    // CODE → <LoadConstInt>: <Reg8: 14, Imm32: 1309151649>
    // USED → r14 = 1309151649
    // CODE → <LoadConstInt>: <Reg8: 13, Imm32: -145523070>
    // USED → r13 = -145523070
    // CODE → <LoadConstInt>: <Reg8: 12, Imm32: -1120210379>
    // USED → r12 = -1120210379
    // CODE → <LoadConstInt>: <Reg8: 11, Imm32: 718787259>
    // USED → r11 = 718787259
    // CODE → <LoadConstInt>: <Reg8: 10, Imm32: -343485551>
    // USED → r10 = -343485551
    // CODE → <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = Identifier(name='r9')
    // CODE → <Mov>: <Reg8: 3, Reg8: 8>
    r3 = Identifier(name='r8')
    // CODE → <Mov>: <Reg8: 2, Reg8: 7>
    r2 = Identifier(name='r7')
    // CODE → <Mov>: <Reg8: 1, Reg8: 6>
    r1 = Identifier(name='r6')
    // CODE → <JmpFalseLong>: <Addr32: 1808, Reg8: 0>  # Address: 00000940
    // Error: 'BinaryExpression' object has no attribute 'render'
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 119, Reg8: 92, UInt8: 10>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 114, Reg8: 5, Reg8: 93>
    // USED → r114 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r93'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 114>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUndefined>: <Reg8: 127>
    r127 = undefined
    // CODE → <Mov>: <Reg8: 126, Reg8: 9>
    r126 = Identifier(name='r9')
    // CODE → <Mov>: <Reg8: 125, Reg8: 8>
    r125 = Identifier(name='r8')
    // CODE → <Mov>: <Reg8: 124, Reg8: 7>
    r124 = Identifier(name='r7')
    // CODE → <Mov>: <Reg8: 123, Reg8: 6>
    r123 = Identifier(name='r6')
    // CODE → <Mov>: <Reg8: 121, Reg8: 90>
    r121 = Identifier(name='r90')
    // CODE → <Mov>: <Reg8: 120, Reg8: 89>
    r120 = Identifier(name='r89')
    // CODE → <Call>: <Reg8: 99, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 107, Reg8: 5, Reg8: 88>
    // USED → r107 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r88'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 107>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 6>
    r126 = Identifier(name='r6')
    // CODE → <Mov>: <Reg8: 125, Reg8: 99>
    r125 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 124, Reg8: 8>
    r124 = Identifier(name='r8')
    // CODE → <Mov>: <Reg8: 123, Reg8: 7>
    r123 = Identifier(name='r7')
    // CODE → <Mov>: <Reg8: 121, Reg8: 87>
    r121 = Identifier(name='r87')
    // CODE → <Mov>: <Reg8: 120, Reg8: 86>
    r120 = Identifier(name='r86')
    // CODE → <Call>: <Reg8: 104, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 100, Reg8: 5, Reg8: 85>
    // USED → r100 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r85'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 100>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 7>
    r126 = Identifier(name='r7')
    // CODE → <Mov>: <Reg8: 125, Reg8: 104>
    r125 = Identifier(name='r104')
    // CODE → <Mov>: <Reg8: 124, Reg8: 99>
    r124 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 123, Reg8: 8>
    r123 = Identifier(name='r8')
    // CODE → <Mov>: <Reg8: 121, Reg8: 84>
    r121 = Identifier(name='r84')
    // CODE → <Mov>: <Reg8: 120, Reg8: 83>
    r120 = Identifier(name='r83')
    // CODE → <Call>: <Reg8: 101, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 109, Reg8: 5, Reg8: 82>
    // USED → r109 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r82'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 109>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 8>
    r126 = Identifier(name='r8')
    // CODE → <Mov>: <Reg8: 125, Reg8: 101>
    r125 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 124, Reg8: 104>
    r124 = Identifier(name='r104')
    // CODE → <Mov>: <Reg8: 123, Reg8: 99>
    r123 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 121, Reg8: 81>
    r121 = Identifier(name='r81')
    // CODE → <Mov>: <Reg8: 120, Reg8: 80>
    r120 = Identifier(name='r80')
    // CODE → <Call>: <Reg8: 103, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 102, Reg8: 5, Reg8: 95>
    // USED → r102 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r95'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 102>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 99>
    r126 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 125, Reg8: 103>
    r125 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 124, Reg8: 101>
    r124 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 123, Reg8: 104>
    r123 = Identifier(name='r104')
    // CODE → <Mov>: <Reg8: 121, Reg8: 90>
    r121 = Identifier(name='r90')
    // CODE → <Mov>: <Reg8: 120, Reg8: 79>
    r120 = Identifier(name='r79')
    // CODE → <Call>: <Reg8: 99, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 111, Reg8: 5, Reg8: 97>
    // USED → r111 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r97'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 111>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 104>
    r126 = Identifier(name='r104')
    // CODE → <Mov>: <Reg8: 125, Reg8: 99>
    r125 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 124, Reg8: 103>
    r124 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 123, Reg8: 101>
    r123 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 121, Reg8: 87>
    r121 = Identifier(name='r87')
    // CODE → <Mov>: <Reg8: 120, Reg8: 78>
    r120 = Identifier(name='r78')
    // CODE → <Call>: <Reg8: 105, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 104, Reg8: 5, Reg8: 77>
    // USED → r104 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r77'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 104>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 101>
    r126 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 125, Reg8: 105>
    r125 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 124, Reg8: 99>
    r124 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 123, Reg8: 103>
    r123 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 121, Reg8: 84>
    r121 = Identifier(name='r84')
    // CODE → <Mov>: <Reg8: 120, Reg8: 76>
    r120 = Identifier(name='r76')
    // CODE → <Call>: <Reg8: 101, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 113, Reg8: 5, Reg8: 90>
    // USED → r113 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r90'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 113>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 103>
    r126 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 125, Reg8: 101>
    r125 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 124, Reg8: 105>
    r124 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 123, Reg8: 99>
    r123 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 121, Reg8: 81>
    r121 = Identifier(name='r81')
    // CODE → <Mov>: <Reg8: 120, Reg8: 75>
    r120 = Identifier(name='r75')
    // CODE → <Call>: <Reg8: 110, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 106, Reg8: 5, Reg8: 74>
    // USED → r106 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r74'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 106>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 99>
    r126 = Identifier(name='r99')
    // CODE → <Mov>: <Reg8: 125, Reg8: 110>
    r125 = Identifier(name='r110')
    // CODE → <Mov>: <Reg8: 124, Reg8: 101>
    r124 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 123, Reg8: 105>
    r123 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 121, Reg8: 90>
    r121 = Identifier(name='r90')
    // CODE → <Mov>: <Reg8: 120, Reg8: 73>
    r120 = Identifier(name='r73')
    // CODE → <Call>: <Reg8: 103, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 0, Reg8: 5, Reg8: 96>
    // USED → r0 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r96'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 105>
    r126 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 125, Reg8: 103>
    r125 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 124, Reg8: 110>
    r124 = Identifier(name='r110')
    // CODE → <Mov>: <Reg8: 123, Reg8: 101>
    r123 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 121, Reg8: 87>
    r121 = Identifier(name='r87')
    // CODE → <Mov>: <Reg8: 120, Reg8: 72>
    r120 = Identifier(name='r72')
    // CODE → <Call>: <Reg8: 112, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 108, Reg8: 5, Reg8: 71>
    // USED → r108 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r71'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 108>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 101>
    r126 = Identifier(name='r101')
    // CODE → <Mov>: <Reg8: 125, Reg8: 112>
    r125 = Identifier(name='r112')
    // CODE → <Mov>: <Reg8: 124, Reg8: 103>
    r124 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 123, Reg8: 110>
    r123 = Identifier(name='r110')
    // CODE → <Mov>: <Reg8: 121, Reg8: 84>
    r121 = Identifier(name='r84')
    // CODE → <Mov>: <Reg8: 120, Reg8: 70>
    r120 = Identifier(name='r70')
    // CODE → <Call>: <Reg8: 105, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 99, Reg8: 5, Reg8: 69>
    // USED → r99 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r69'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 99>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 110>
    r126 = Identifier(name='r110')
    // CODE → <Mov>: <Reg8: 125, Reg8: 105>
    r125 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 124, Reg8: 112>
    r124 = Identifier(name='r112')
    // CODE → <Mov>: <Reg8: 123, Reg8: 103>
    r123 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 121, Reg8: 81>
    r121 = Identifier(name='r81')
    // CODE → <Mov>: <Reg8: 120, Reg8: 68>
    r120 = Identifier(name='r68')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 110, Reg8: 5, Reg8: 87>
    // USED → r110 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r87'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 110>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 103>
    r126 = Identifier(name='r103')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 105>
    r124 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 123, Reg8: 112>
    r123 = Identifier(name='r112')
    // CODE → <Mov>: <Reg8: 121, Reg8: 90>
    r121 = Identifier(name='r90')
    // CODE → <Mov>: <Reg8: 120, Reg8: 67>
    r120 = Identifier(name='r67')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 101, Reg8: 5, Reg8: 66>
    // USED → r101 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r66'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 101>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 112>
    r126 = Identifier(name='r112')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 105>
    r123 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 121, Reg8: 87>
    r121 = Identifier(name='r87')
    // CODE → <Mov>: <Reg8: 120, Reg8: 65>
    r120 = Identifier(name='r65')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 112, Reg8: 5, Reg8: 94>
    // USED → r112 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r94'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 112>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 105>
    r126 = Identifier(name='r105')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 84>
    r121 = Identifier(name='r84')
    // CODE → <Mov>: <Reg8: 120, Reg8: 64>
    r120 = Identifier(name='r64')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 105, Reg8: 5, Reg8: 63>
    // USED → r105 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r63'))
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 105>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 81>
    r121 = Identifier(name='r81')
    // CODE → <Mov>: <Reg8: 120, Reg8: 62>
    r120 = Identifier(name='r62')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadFromEnvironment>: <Reg8: 119, Reg8: 92, UInt8: 11>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 107>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 97>
    r121 = Identifier(name='r97')
    // CODE → <Mov>: <Reg8: 120, Reg8: 61>
    r120 = Identifier(name='r61')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 104>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 96>
    r121 = Identifier(name='r96')
    // CODE → <Mov>: <Reg8: 120, Reg8: 60>
    r120 = Identifier(name='r60')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 99>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 94>
    r121 = Identifier(name='r94')
    // CODE → <Mov>: <Reg8: 120, Reg8: 59>
    r120 = Identifier(name='r59')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 114>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 58>
    r121 = Identifier(name='r58')
    // CODE → <Mov>: <Reg8: 120, Reg8: 57>
    r120 = Identifier(name='r57')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 111>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 97>
    r121 = Identifier(name='r97')
    // CODE → <Mov>: <Reg8: 120, Reg8: 56>
    r120 = Identifier(name='r56')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 108>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 96>
    r121 = Identifier(name='r96')
    // CODE → <Mov>: <Reg8: 120, Reg8: 55>
    r120 = Identifier(name='r55')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 105>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 94>
    r121 = Identifier(name='r94')
    // CODE → <Mov>: <Reg8: 120, Reg8: 54>
    r120 = Identifier(name='r54')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 102>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 58>
    r121 = Identifier(name='r58')
    // CODE → <Mov>: <Reg8: 120, Reg8: 53>
    r120 = Identifier(name='r53')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 97>
    r121 = Identifier(name='r97')
    // CODE → <Mov>: <Reg8: 120, Reg8: 52>
    r120 = Identifier(name='r52')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 112>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 96>
    r121 = Identifier(name='r96')
    // CODE → <Mov>: <Reg8: 120, Reg8: 51>
    r120 = Identifier(name='r51')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 109>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 94>
    r121 = Identifier(name='r94')
    // CODE → <Mov>: <Reg8: 120, Reg8: 50>
    r120 = Identifier(name='r50')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 106>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 58>
    r121 = Identifier(name='r58')
    // CODE → <Mov>: <Reg8: 120, Reg8: 49>
    r120 = Identifier(name='r49')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 101>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 97>
    r121 = Identifier(name='r97')
    // CODE → <Mov>: <Reg8: 120, Reg8: 48>
    r120 = Identifier(name='r48')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 100>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 96>
    r121 = Identifier(name='r96')
    // CODE → <Mov>: <Reg8: 120, Reg8: 47>
    r120 = Identifier(name='r47')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 113>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 94>
    r121 = Identifier(name='r94')
    // CODE → <Mov>: <Reg8: 120, Reg8: 46>
    r120 = Identifier(name='r46')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 110>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 58>
    r121 = Identifier(name='r58')
    // CODE → <Mov>: <Reg8: 120, Reg8: 45>
    r120 = Identifier(name='r45')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadFromEnvironment>: <Reg8: 119, Reg8: 92, UInt8: 12>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 111>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 95>
    r121 = Identifier(name='r95')
    // CODE → <Mov>: <Reg8: 120, Reg8: 44>
    r120 = Identifier(name='r44')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 106>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 69>
    r121 = Identifier(name='r69')
    // CODE → <Mov>: <Reg8: 120, Reg8: 43>
    r120 = Identifier(name='r43')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 99>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 42>
    r121 = Identifier(name='r42')
    // CODE → <Mov>: <Reg8: 120, Reg8: 41>
    r120 = Identifier(name='r41')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 112>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 40>
    r121 = Identifier(name='r40')
    // CODE → <Mov>: <Reg8: 120, Reg8: 39>
    r120 = Identifier(name='r39')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 107>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 95>
    r121 = Identifier(name='r95')
    // CODE → <Mov>: <Reg8: 120, Reg8: 38>
    r120 = Identifier(name='r38')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 102>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 69>
    r121 = Identifier(name='r69')
    // CODE → <Mov>: <Reg8: 120, Reg8: 37>
    r120 = Identifier(name='r37')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 113>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 42>
    r121 = Identifier(name='r42')
    // CODE → <Mov>: <Reg8: 120, Reg8: 36>
    r120 = Identifier(name='r36')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 108>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 40>
    r121 = Identifier(name='r40')
    // CODE → <Mov>: <Reg8: 120, Reg8: 35>
    r120 = Identifier(name='r35')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 101>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 95>
    r121 = Identifier(name='r95')
    // CODE → <Mov>: <Reg8: 120, Reg8: 34>
    r120 = Identifier(name='r34')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 114>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 69>
    r121 = Identifier(name='r69')
    // CODE → <Mov>: <Reg8: 120, Reg8: 33>
    r120 = Identifier(name='r33')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 109>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 42>
    r121 = Identifier(name='r42')
    // CODE → <Mov>: <Reg8: 120, Reg8: 32>
    r120 = Identifier(name='r32')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 104>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 40>
    r121 = Identifier(name='r40')
    // CODE → <Mov>: <Reg8: 120, Reg8: 31>
    r120 = Identifier(name='r31')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 95>
    r121 = Identifier(name='r95')
    // CODE → <Mov>: <Reg8: 120, Reg8: 30>
    r120 = Identifier(name='r30')
    // CODE → <Call>: <Reg8: 118, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 110>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 118>
    r125 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 69>
    r121 = Identifier(name='r69')
    // CODE → <Mov>: <Reg8: 120, Reg8: 29>
    r120 = Identifier(name='r29')
    // CODE → <Call>: <Reg8: 117, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 105>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 117>
    r125 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 124, Reg8: 118>
    r124 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 42>
    r121 = Identifier(name='r42')
    // CODE → <Mov>: <Reg8: 120, Reg8: 28>
    r120 = Identifier(name='r28')
    // CODE → <Call>: <Reg8: 116, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 100>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 116>
    r125 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 124, Reg8: 117>
    r124 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 123, Reg8: 118>
    r123 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 121, Reg8: 40>
    r121 = Identifier(name='r40')
    // CODE → <Mov>: <Reg8: 120, Reg8: 27>
    r120 = Identifier(name='r27')
    // CODE → <Call>: <Reg8: 115, Reg8: 119, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadFromEnvironment>: <Reg8: 103, Reg8: 92, UInt8: 13>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 114>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 118>
    r126 = Identifier(name='r118')
    // CODE → <Mov>: <Reg8: 125, Reg8: 115>
    r125 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 124, Reg8: 116>
    r124 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 123, Reg8: 117>
    r123 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 121, Reg8: 77>
    r121 = Identifier(name='r77')
    // CODE → <Mov>: <Reg8: 120, Reg8: 26>
    r120 = Identifier(name='r26')
    // CODE → <Call>: <Reg8: 114, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 113>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 117>
    r126 = Identifier(name='r117')
    // CODE → <Mov>: <Reg8: 125, Reg8: 114>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r93'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 115>
    r124 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 123, Reg8: 116>
    r123 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 121, Reg8: 71>
    r121 = Identifier(name='r71')
    // CODE → <Mov>: <Reg8: 120, Reg8: 25>
    r120 = Identifier(name='r25')
    // CODE → <Call>: <Reg8: 113, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 112>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 116>
    r126 = Identifier(name='r116')
    // CODE → <Mov>: <Reg8: 125, Reg8: 113>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r90'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 114>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r93'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 115>
    r123 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 121, Reg8: 63>
    r121 = Identifier(name='r63')
    // CODE → <Mov>: <Reg8: 120, Reg8: 24>
    r120 = Identifier(name='r24')
    // CODE → <Call>: <Reg8: 112, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 111>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 115>
    r126 = Identifier(name='r115')
    // CODE → <Mov>: <Reg8: 125, Reg8: 112>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r94'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 113>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r90'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 114>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r93'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 23>
    r121 = Identifier(name='r23')
    // CODE → <Mov>: <Reg8: 120, Reg8: 22>
    r120 = Identifier(name='r22')
    // CODE → <Call>: <Reg8: 111, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 110>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 114>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r93'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 111>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r97'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 112>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r94'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 113>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r90'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 77>
    r121 = Identifier(name='r77')
    // CODE → <Mov>: <Reg8: 120, Reg8: 21>
    r120 = Identifier(name='r21')
    // CODE → <Call>: <Reg8: 110, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 109>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 113>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r90'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 110>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r87'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 111>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r97'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 112>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r94'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 71>
    r121 = Identifier(name='r71')
    // CODE → <Mov>: <Reg8: 120, Reg8: 20>
    r120 = Identifier(name='r20')
    // CODE → <Call>: <Reg8: 109, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 108>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 112>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r94'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 109>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r82'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 110>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r87'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 111>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r97'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 63>
    r121 = Identifier(name='r63')
    // CODE → <Mov>: <Reg8: 120, Reg8: 19>
    r120 = Identifier(name='r19')
    // CODE → <Call>: <Reg8: 108, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 107>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 111>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r97'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 108>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r71'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 109>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r82'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 110>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r87'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 23>
    r121 = Identifier(name='r23')
    // CODE → <Mov>: <Reg8: 120, Reg8: 18>
    r120 = Identifier(name='r18')
    // CODE → <Call>: <Reg8: 107, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 106>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 110>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r87'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 107>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r88'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 108>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r71'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 109>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r82'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 77>
    r121 = Identifier(name='r77')
    // CODE → <Mov>: <Reg8: 120, Reg8: 17>
    r120 = Identifier(name='r17')
    // CODE → <Call>: <Reg8: 106, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 105>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 109>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r82'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 106>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r74'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 107>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r88'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 108>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r71'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 71>
    r121 = Identifier(name='r71')
    // CODE → <Mov>: <Reg8: 120, Reg8: 16>
    r120 = Identifier(name='r16')
    // CODE → <Call>: <Reg8: 105, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 104>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 108>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r71'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 105>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r63'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 106>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r74'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 107>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r88'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 63>
    r121 = Identifier(name='r63')
    // CODE → <Mov>: <Reg8: 120, Reg8: 15>
    r120 = Identifier(name='r15')
    // CODE → <Call>: <Reg8: 104, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 101>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 107>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r88'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 104>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r77'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 105>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r63'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 106>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r74'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 23>
    r121 = Identifier(name='r23')
    // CODE → <Mov>: <Reg8: 120, Reg8: 14>
    r120 = Identifier(name='r14')
    // CODE → <Call>: <Reg8: 101, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 102>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 106>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r74'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 101>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r66'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 104>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r77'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 105>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r63'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 77>
    r121 = Identifier(name='r77')
    // CODE → <Mov>: <Reg8: 120, Reg8: 13>
    r120 = Identifier(name='r13')
    // CODE → <Call>: <Reg8: 102, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 99>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 105>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r63'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 102>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r95'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 101>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r66'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 104>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r77'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 71>
    r121 = Identifier(name='r71')
    // CODE → <Mov>: <Reg8: 120, Reg8: 12>
    r120 = Identifier(name='r12')
    // CODE → <Call>: <Reg8: 99, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 100>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 104>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r77'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 99>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r69'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 102>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r95'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 101>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r66'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 63>
    r121 = Identifier(name='r63')
    // CODE → <Mov>: <Reg8: 120, Reg8: 11>
    r120 = Identifier(name='r11')
    // CODE → <Call>: <Reg8: 100, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByVal>: <Reg8: 122, Reg8: 98, Reg8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 126, Reg8: 101>
    r126 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r66'))
    // CODE → <Mov>: <Reg8: 125, Reg8: 100>
    r125 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r85'))
    // CODE → <Mov>: <Reg8: 124, Reg8: 99>
    r124 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r69'))
    // CODE → <Mov>: <Reg8: 123, Reg8: 102>
    r123 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r95'))
    // CODE → <Mov>: <Reg8: 121, Reg8: 23>
    r121 = Identifier(name='r23')
    // CODE → <Mov>: <Reg8: 120, Reg8: 10>
    r120 = Identifier(name='r10')
    // CODE → <Call>: <Reg8: 101, Reg8: 103, UInt8: 8>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 92, UInt8: 14>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call3>: <Reg8: 9, Reg8: 0, Reg8: 91, Reg8: 102, Reg8: 9>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Call3>: <Reg8: 8, Reg8: 0, Reg8: 91, Reg8: 101, Reg8: 8>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Call3>: <Reg8: 7, Reg8: 0, Reg8: 91, Reg8: 100, Reg8: 7>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Call3>: <Reg8: 6, Reg8: 0, Reg8: 91, Reg8: 99, Reg8: 6>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Add>: <Reg8: 5, Reg8: 5, Reg8: 42>
    // USED → r5 = BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r42'))
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 98, UInt8: 1, string_id: 139>  # String: 'length' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    // USED → r4 = Identifier(name='r9')
    // CODE → <Mov>: <Reg8: 3, Reg8: 8>
    // USED → r3 = Identifier(name='r8')
    // CODE → <Mov>: <Reg8: 2, Reg8: 7>
    // USED → r2 = Identifier(name='r7')
    // CODE → <Mov>: <Reg8: 1, Reg8: 6>
    // USED → r1 = Identifier(name='r6')
    // CODE → <JLessLong>: <Addr32: -1795, Reg8: 5, Reg8: 0>  # Address: 00000236
    if (BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r42')) < BinaryExpression(left=Identifier(name='r5'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r96'))) { /* jump to label_566 */ }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <NewArray>: <Reg8: 0, UInt16: 4>
    // USED → r0 = [] /* capacity hint: 4 */
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 4, UInt8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 3, UInt8: 1>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 2, UInt8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 1, UInt8: 3>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Ret>: <Reg8: 0>
    ReturnStatement(argument=Identifier(name='r0'))
}