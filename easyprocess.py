# 此函数作用是对初始语料进行分词处理后，作为训练模型的语料
def cut_txt(old_file):
    import jieba
    global cut_file     # 分词之后保存的文件名
    cut_file = old_file + '_cut.txt'

    try:
        fi = open(old_file, 'r', encoding='utf-8')
    except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
        print(Exception, ":", e)    # 追踪错误详细信息

    text = fi.read()  # 获取文本内容
    new_text = jieba.cut(text, cut_all=False)  # 精确模式
    str_out = ' '.join(new_text).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
        .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '')     # 去掉标点符号
    fo = open(cut_file, 'w', encoding='utf-8')
    fo.write(str_out)
