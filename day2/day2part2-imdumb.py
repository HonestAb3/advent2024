def fixAscDecForealYe(lineData):
    for i in range(1, len(lineData) - 1):
        if lineData[i] == lineData[i - 1] or lineData[i] == lineData[i + 1]:
            del lineData[i]
            break
        elif lineData[i] > lineData[i - 1]:
            if lineData[i] > lineData[i + 1] and lineData[i - 1] == lineData[i + 1]:
                if i < len(lineData) - 2:
                    if lineData[i + 2] > lineData[i + 1]:
                        del lineData[i + 1]
                    else:
                        del lineData[i - 1]
                break
            elif lineData[i] > lineData[i + 1]:
                if lineData[i - 1] > lineData[i + 1]:
                    del lineData[i - 1]
                else:
                    del lineData[i]
                break
        elif lineData[i] < lineData[i - 1]:
            if lineData[i] < lineData[i + 1] and lineData[i - 1] == lineData[i + 1]:
                if i < len(lineData) - 2:
                    if lineData[i + 2] < lineData[i + 1]:
                        del lineData[i + 1]
                    else:
                        del lineData[i - 1]
                break
            elif lineData[i] < lineData[i + 1]:
                if lineData[i - 1] > lineData[i + 1]:
                    del lineData[i]
                else:
                    del lineData[i + 1]
                break
    return lineData


def fixAscDecForeal(lineData):
    for i in range(1, len(lineData) - 1):
        if lineData[i] == lineData[i - 1] or lineData[i] == lineData[i + 1]:
            del lineData[i]
            break
        elif lineData[i] > lineData[i - 1]:
            if lineData[i] > lineData[i + 1] and lineData[i - 1] == lineData[i + 1]:
                if i < len(lineData) - 2:
                    if lineData[i + 2] > lineData[i + 1]:
                        del lineData[i + 1]
                    else:
                        del lineData[i - 1]
                break
            elif (
                lineData[i] > lineData[i + 1]
            ):  # and lineData[i - 1] > lineData[i + 1]:
                del lineData[i]
                break
        elif lineData[i] < lineData[i - 1]:
            if lineData[i] < lineData[i + 1] and lineData[i - 1] == lineData[i + 1]:
                if i < len(lineData) - 2:
                    if lineData[i + 2] < lineData[i + 1]:
                        del lineData[i + 1]
                    else:
                        del lineData[i - 1]
                break
            elif (
                lineData[i] < lineData[i + 1]
            ):  # and lineData[i - 1] > lineData[i + 1]:
                del lineData[i]
                break
    return lineData


def fixAscDec(lineData):
    dirC = 0
    brokenPos = 0
    for i in range(0, len(lineData) - 1):
        if lineData[i] > lineData[i + 1]:
            if dirC == 0:
                dirC -= 1
            elif dirC == 1:
                brokenPos = i
                del lineData[brokenPos]
                break
        elif lineData[i] < lineData[i + 1]:
            if dirC == 0:
                dirC += 1
            elif dirC == -1:
                brokenPos = i
                del lineData[brokenPos]
                break
        else:
            del lineData[i]
            break

    return lineData


def fixNearEnough(lineData):
    for i in range(1, len(lineData) - 1):
        if lineData[i] == lineData[i - 1] or lineData[i] == lineData[i + 1]:
            del lineData[i]
            break
        elif (
            abs(lineData[i] - lineData[i - 1]) > 3
            and abs(lineData[i] - lineData[i + 1]) > 3
        ):
            del lineData[i]
            break
        elif (
            abs(lineData[i] - lineData[i - 1]) > 3
            and abs(lineData[i] - lineData[i + 1]) <= 3
        ):
            del lineData[i - 1]
            break
        elif (
            abs(lineData[i] - lineData[i - 1]) <= 3
            and abs(lineData[i] - lineData[i + 1]) > 3
        ):
            del lineData[i + 1]
            break
    return lineData
