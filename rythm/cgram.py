CGTXT = {
    'up': [
        '    []          ',
        '  [][][]        ',
        '[][][][][]      ',
        '[][]  [][]      ',
        '[]      []      ',
    ],
    'dn': [
        '        [][][]  ',
        '      []  []  []',
        '      []      []',
        '      [][]  [][]',
        '        [][][]  ',
    ],
    'updn': [
        '    []  [][][]  ',
        '  [][][]  []  []',
        '[][][][]      []',
        '[][]  [][]  [][]',
        '[]      [][][]  ',
    ],
    'lf': [
        '      [][][]    ',
        '    [][][]      ',
        '  [][][]        ',
        '    [][][]      ',
        '      [][][]    ',
    ],
    'rt': [
        '    [][][]      ',
        '      [][][]    ',
        '        [][][]  ',
        '      [][][]    ',
        '    [][][]      ',
    ],
    'b': [
        '[][][][]        ',
        '[][]  [][]      ',
        '[][][][]        ',
        '[][]  [][]      ',
        '[][][][]        ',
    ],
    'a': [
        '        [][][]  ',
        '      [][]  [][]',
        '      [][][][][]',
        '      [][]  [][]',
        '      [][]  [][]',
    ],
    'ba': [
        '[][][]    [][]  ',
        '[][]  [][]  [][]',
        '[][][]  [][][][]',
        '[][]  [][]  [][]',
        '[][][]  []  [][]',
    ]
}

CGINTROTXT = {
    'R': [
        '[][][][][][]    ',
        '[][][][][][][][]',
        '[][]        [][]',
        '[][][][][][][][]',
        '[][][][][][]    ',
    ],
    'r': [
        '[][]      [][]  ',
        '[][]      [][]  ',
        '[][]        [][]',
        '[][]        [][]',
        '                ',
    ],
    'Y': [
        '[][]        [][]',
        '[][]        [][]',
        '  [][]    [][]  ',
        '  [][][][][][]  ',
        '    [][][][]    ',
    ],
    'y': [
        '      [][]      ',
        '      [][]      ',
        '      [][]      ',
        '      [][]      ',
        '                ',
    ],
    'T': [
        '[][][][][][][][]',
        '[][][][][][][][]',
        '      [][]      ',
        '      [][]      ',
        '      [][]      ',
    ],
    'H': [
        '[][]        [][]',
        '[][]        [][]',
        '[][]        [][]',
        '[][][][][][][][]',
        '[][][][][][][][]',
    ],
    'h': [
        '[][]        [][]',
        '[][]        [][]',
        '[][]        [][]',
        '[][]        [][]',
        '                ',
    ],
    'M': [
        '[][]        [][]',
        '[][][]    [][][]',
        '[][][][][][][][]',
        '[][][][][][][][]',
        '[][]  [][]  [][]',
    ],
}


def _load(txt):
    '''rotate txt dict format into binary data and store opcode'''
    op = {}
    data = []
    for i, (cgtitle, cgvalue) in enumerate(txt.items()):
        op[cgtitle] = f'CG{i}'
        for y in reversed(range(0, 16, 2)):
            data.append(
                'B{:02d}'.format(
                    sum(
                        2**j if v[y:y+2] == '[]' else 0
                        for j, v in enumerate(reversed(cgvalue))
                    )
                )
            )
    return op, data

CG, CGDATA = _load(CGTXT)

CGINTRO, CGINTRODATA = _load(CGINTROTXT)
