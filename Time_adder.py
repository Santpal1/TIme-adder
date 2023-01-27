def add_time(st_time, duration, day = False):

    lst = ["","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    chr = 0

    for i in st_time:
        if i.isdigit():
            chr = chr * 10 + int(i)
        else:
            break
    
    for a in st_time:
        if a == "P":
            chr += 12

    dhr = 0

    for j in duration:
        if j.isdigit():
            dhr = dhr * 10 + int(j)
        else:
            break
    
    nhr = chr + dhr

    for k in st_time:
        if k == ":":
            cmn = int(st_time[st_time.index(k) + 1]) * 10 + int(st_time[st_time.index(k) + 2])
        else:
            continue

    for l in duration:
        if l == ":":
            dmn = int(duration[duration.index(l) + 1]) * 10 + int(duration[duration.index(l) + 2])
        else:
            continue
    
    nmn = cmn + dmn

    while nmn >= 60:
        nmn -= 60
        nhr += 1

    x = nhr
    newday = day

    if lst.index(day) == 6:
        newday = ""

    if day in lst:
        while x >= 24:
            nday = lst[lst.index(newday) + 1]
            newday = nday
            x -= 24
            nhr = x
    else:
        if x >= 24:
            nday = " "
            nhr -= 12
    if nhr > 12:
        nhr -= 12
        print(f"{nhr} : {nmn} PM , {nday}")
    else:
        print(f"{nhr} : {nmn} AM, {nday}")

add_time("3:40 PM", "72:20", "")
