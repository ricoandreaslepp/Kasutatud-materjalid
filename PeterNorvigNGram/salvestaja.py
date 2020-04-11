# salvestamine(str(algoritmi nimi), def lahendamisfunktsioon, str(parandatava tekstifaili nimi))
def salvestamine(algoritm, funkt, pfail):
    from xlwt import Workbook
    import os

    wb = Workbook()

    sheet = wb.add_sheet(algoritm, cell_overwrite_ok=True)
    sheet.write(0, 0, "ALG")
    sheet.write(0, 1, "VALE/ÕIGE")
    sheet.write(0, 2, "PARANDATUD")
    sheet.write(0, 3, "PAKKUMISED")
    sheet.write(0, 4, "ANALÜÜS")
    sheet.write(0, 5, "PARANDUS")

    i = funkt(sheet) + 1

    sheet.write(i, 0, "SELGITUS")
    sheet.write(i, 2, "VÄÄRTUS")
    sheet.write(i, 3, "ÜHIK")
    i -= 1
    #
    sheet.write(i + 2, 0, "Vigaseid sõnu (v.a GRAMVIGA):")
    sheet.write(i + 2, 2, 'COUNTIF(E1:E' + str(i) + ', "VALE")')
    sheet.write(i + 2, 3, "sõna")
    #
    sheet.write(i + 3, 0, "Kokku vigaseid sõnu tekstis:")
    sheet.write(i + 3, 2, 'COUNTIF(E1:E' + str(i) + ', "VALE") + COUNTIF(E1:E' + str(i) + ', "GRAMVIGA")')
    sheet.write(i + 3, 3, "sõna")
    #
    sheet.write(i + 4, 0, "Esimene osakaal:")
    sheet.write(i + 4, 2, 'ROUND(COUNTIF(F1:F' + str(i) + ', "ÕIGE1") / COUNTIF(E1:E' + str(i) + ', "VALE") * 100, 3)')
    sheet.write(i + 4, 3, "%")
    #
    sheet.write(i + 5, 0, "Teine osakaal:")
    sheet.write(i + 5, 2, 'ROUND((COUNTIF(F1:F' + str(i) + ', "ÕIGE1") + COUNTIF(F1:F' + str(
        i) + ', "ÕIGE2")) / (COUNTIF(E1:E' + str(i) + ', "VALE")) * 100, 3)')
    sheet.write(i + 5, 3, "%")
    #
    sheet.write(i + 6, 0, "Kolmas osakaal:")
    sheet.write(i + 6, 2, 'ROUND((COUNTIF(F1:F' + str(i) + ', "ÕIGE1") + COUNTIF(F1:F' + str(
        i) + ',"ÕIGE2") + COUNTIF(F1:F' + str(i) + ', "GRAMÕIGE")) /(COUNTIF(E1:E' + str(
        i) + ', "VALE") + COUNTIF(E1:E' + str(i) + ', "GRAMVIGA")) * 100, 3)')
    sheet.write(i + 6, 3, "%")

    os.chdir("../../PeterNorvigNGram/testid/")
    wb.save(algoritm + ' parandused (' + pfail + ').xls')
    os.chdir("../../")
