def firstMatched(file, determine):
    for line in file:
        if line.find(determine+'\n') != -1:
            return file.index(line)

def findHeadingPosition(file, headings):
    milestones = []
    contents = []
    startAt = 0
    for heading in headings:
        lineMatched = firstMatched(file, heading)
        milestones.append(lineMatched)
        headings.update({heading: {"content": len(milestones)}})
        contents.append(file[startAt:lineMatched])
        startAt = lineMatched + 1
    milestones.append(len(file))
    contents.append(file[lineMatched:len(file)])
    return mappingHeadings(headings, contents)

def mappingHeadings(headings, contents):
    try:
        result = {}
        for heading in headings:
            result.update({heading: contents[headings.get(heading).get('content')]})
        return result
    except NameError:
        print(NameError)