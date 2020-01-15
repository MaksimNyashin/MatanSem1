NEED_WRITE_IN_FILE = False

def main():
    import codecs
    fi = codecs.open("Tickets.txt", "r", "utf-8")
    s = fi.read()
    fi.close()
    a = s.split('\n\n')
    a[0] = a[0].split('\n')
    a[1] = a[1].split('\n')
    fo = codecs.open("mainPart.tex", "w", "utf-8")
    fo.write("\\tableofcontents\n")
    for j in range(2):
        fo.write("\\newpage\n")
        if j == 0:
            fo.write("\\section{Билеты}\n")
        else:
            fo.write("\\section{Требуемые определения}\n")
        for i in range(len(a[j])):
            num = str(j) + str((i + 1) // 10) + str((i + 1) % 10)
            fo.write("\\subsection{%s}\n\\input{src/%s.tex}\n" % (a[j][i], num))
            # fo.write("\\newpage\n")
            fo.write("\\skip\n")
            '''if NEED_WRITE_IN_FILE:
                ff = codecs.open("src/%s.tex" % (num), "w", "utf-8")
                st = "Билет" if j == 0 else "Определение"
                ff.write("%s %d: %s" % (st, i + 1, a[j][i]))
                ff.close()'''
        

    fo.close()

main()
