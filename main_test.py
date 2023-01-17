import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '-10\n2\n'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*uadrant 2[\w,\W]*', lines[0])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '2\n-10\n'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*uadrant 4[\w,\W]*', lines[0])
    assert res != None
    print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '-10\n-10\n'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*Quadrant 3[\w,\W]*', lines[0])
    assert res != None
    print(res.group())


def test_main_4():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10\n10\n'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*Quadrant 1[\w,\W]*', lines[0])
    assert res != None
    print(res.group())
