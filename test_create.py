# test_create
# pupose: WebClassでEQテストを実施するための問題を生成する
# author: Katsuhiro Morishita
# create: 2015-04-07
# license: MIT/PD

q_list = []
with open("test_list.csv", "r", encoding="utf-8") as fr:
    lines = fr.readlines()
    for line in lines:
        line = line.rstrip()
        field = line.split("\t")
        q = field[1]
        q_list.append(q)
        print(q)

_point = 10
with open("test_source.csv", "w", encoding="utf-8") as fw:
    fw.write("point,area,difficulty,style,answer,question,description,option1,option2,option3,option4,option5,option6,option7,option8,option9,option10,option11,option12,option13,option14,option15,option16,option17,option18,option19,option20,option21,option22,option23,option24,option25,option26\n")
    for q in q_list:
        fw.write("{0},, ,level,,{1},,非常に当てはまる,全く当てはまらない,dummy,dummy,dummy,\n".format(_point, q))

