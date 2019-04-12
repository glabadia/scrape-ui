#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3000-303F : punctuation
# 3040-309F : hiragana
# 30A0-30FF : katakana
# FF00-FFEF : Full-width roman + half-width katakana
#   FF00-FF0F/FF1A-FF20/FF3B-FF40/FF5B-FF9F
#   \uff00-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff9f
# 4E00-9FAF : Common and uncommon kanji

# 2605-2606 : Stars
# 2190-2195 : Arrows
# u203B     : Weird asterisk thing

#   japanese
#   var regex = /[\u3000-\u303F]|[\u3040-\u309F]|[\u30A0-\u30FF]|[\uFF00-\uFFEF]|[\u4E00-\u9FAF]|[\u2605-\u2606]|[\u2190-\u2195]|\u203B/g;

# str = u'[DMSM-8433] 加護亜依 Kago Ai – 加護亜依 vs. FRIDAY'
# jap_make_model = "'14  Alfa Romeo Sprint ｽﾌﾟﾘﾝﾄｼﾞｭﾆｱ"
# regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+ (?=[A-Za-z ]+–)'
# p = re.compile(regex, re.U)
# match = p.sub("", str)
# print(match.encode("UTF-8"))

# ipath = "./data/NCDC/上海/虹桥/9705626661750dat.txt"
import re
# ipath = "'09  Ford Mustang V8 GT Premium"
# ipath = "'14  Alfa Romeo Sprint ｽﾌﾟﾘﾝﾄｼﾞｭﾆｱ "
# ipath = "15  Mercedes-Benz ＳＬＫ２００ Trend ＋ＡＭＧ Sports Ｐ"
ipath = "'12  Alfa Romeo HB ｼﾞｭﾘｴｯﾀ ｺﾝﾍﾟﾃｨﾂｨｵ-ﾈ"
# ipath = "13  Nissan Atlas フラ Top"
# JAP_SEARCH = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+'
# \uff00-\uff9f = full-width roman/half-width katakana
#   2/18/2019
#   \uff00-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff9f
#   2/19/2019
#   \uff00\uff1a-\uff20\uff3b-\uff40\uff5b-\uff9f
#   did not include some full-width characters that looked like english alphabet
JAP_SEARCH = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00\uff1a-\uff20\uff3b-\uff40\uff5b-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+'


def find_japanese_char(input):
    # v = re.findall(JAP_SEARCH, ipath)  # => []
    v = re.findall(JAP_SEARCH, input)  # => []
    # print(v)
    # return True if len(v) > 0 else False
    return True if v else False


# print(find_japanese_char(ipath))
