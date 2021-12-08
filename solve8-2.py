inp = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''
inp = list(list(inp.split("\n")))
count = 0
for i in range(len(inp)):
    oneLow = ""
    oneHigh = ""
    zeroLeftLow = ""
    sigs = inp[i].split(" | ")[0].split(" ")
    out = inp[i].split(" | ")[1].split(" ")
    digits = [""]*10
    for sig in sigs:
        if len(sig) == 2:
            digits[1] = sig
        elif len(sig) == 3:
            digits[7] = sig
        elif len(sig) == 4:
            digits[4] = sig
        elif len(sig) == 7:
            digits[8] = sig
    for sig in sigs:
        if len(sig) == 5 and digits[1][0] in sig and digits[1][1] in sig:
            digits[3] = sig
        if len(sig) == 6 and digits[1][0] in sig and digits[1][1] not in sig:
            digits[6] = sig
            oneLow = digits[1][0]
            oneHigh = digits[1][1]
        if len(sig) == 6 and digits[1][1] in sig and digits[1][0] not in sig:
            digits[6] = sig
            oneLow = digits[1][1]
            oneHigh = digits[1][0]
    for sig in sigs:
        if len(sig) == 5 and oneHigh not in sig and oneLow in sig:
            digits[5] = sig
        if len(sig) == 5 and oneHigh in sig and oneLow not in sig:
            digits[2] = sig
    for d in digits[2]:
        if d not in digits[3]:
            zeroLeftLow = d
    for sig in sigs:
        if len(sig) == 6 and sig != digits[6] and zeroLeftLow in sig:
            digits[0] = sig
        if len(sig) == 6 and sig != digits[6] and zeroLeftLow not in sig:
            digits[9] = sig
    digits = list(map(set, digits))
    count += int("".join(map(lambda x: str(digits.index(set(x))), out)))
print(count)