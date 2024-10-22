import spacy
import json
import re
import copy
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

wordlist_path = resource_path('wordlist3.0.json')
iwnlp_path = resource_path('IWNLP.Lemmatizer_20181001.json')
model_spacy_path = resource_path('/Users/yishi/anaconda3/envs/calculator/lib/python3.11/site-packages/de_dep_news_trf/de_dep_news_trf-3.7.2')



from iwnlp.iwnlp_wrapper import IWNLPWrapper
lemmatizer = IWNLPWrapper(lemmatizer_path=iwnlp_path)

# 加载Spacy的德语模型
nlp = spacy.load(model_spacy_path)

# 读取可分动词的JSON文件
with open(wordlist_path, 'r', encoding='utf-8') as file:
    separable_verbs = json.load(file)

# json文件转换成字典
trennbare_woeter = {}
for item in separable_verbs["Trennbare Woerter"]:
    trennbare_woeter[item["Vorsilbe"]] = item["Woerter"]

# token.tag_更靠谱 测试一下准确率，与词表进行对比
# form有空格，且pos是verb-->可分动词
with open("IWNLP.Lemmatizer_20181001.json", "r", encoding="utf-8") as file1:
    iwnlp = json.load(file1)

# 预处理：去掉空行和多余空格
def preprocess(sentences):
    cleaned_space = re.sub(r'\s+', ' ', sentences).strip()
    cleaned_newline = re.sub(r'\n+', ' ', cleaned_space).strip()
    return cleaned_newline

def printLine(line = [], flag = False):
    for i in range(len(line)):
        print(line[i][2], end = ' ')
    if flag:
        print("\n")

def findClause():
    conj = 0
    for index in range(len(processed_spacy)):
        line = processed_spacy[index]
        for i in range(len(line)):
            if line[i][0] == 'SCONJ':
                conj = conj+1
                print(conj)
            if conj > 0:
                print(line[i][2], end=' ')
            if (line[i][0] == 'VERB' or line[i][0] == 'AUX') and conj > 0:
                conj = conj - 1

def process_trennbare_woerter(processed_spacy):
    # 检查标点前是否为可分前缀
    for index in range(len(processed_spacy)):
        line = processed_spacy[index]
        prob_vorsilbe = line[-2][2]  # 检查最后一个词的lemma
        if prob_vorsilbe in trennbare_woeter.keys():  # 最后一个词的lemma为可分前缀，则检查句子中的动词
            verbexistsinline = False
            i = len(line)-3
            while i >= 0 and verbexistsinline is False:
                for j in range(len(line[i][1])):
                    if line[i][3] == "VVFIN" or line[i][0] == "AUX":
                        verbexistsinline = True
                    if (line[i][3] == "VVFIN" or line[i][0] == "AUX") and (prob_vorsilbe + line[i][1][j]) in trennbare_woeter[prob_vorsilbe]:
                        # 可分前缀删掉，动词替换成可分动词原形
                        line[-2][0] = "TPRFX"
                        line[i][1][j] = prob_vorsilbe + line[i][1][j]
                        # print(len(line))
                        # print(len(line[-2]))
                        # print(len(line[-2][1]))
                        # print(j)
                        # print(line)
                        line[-2][1][0] = line[i][1][j]
                        line[i][1][0] = line[i][1][j]

                        # print(line[i][1][j], line[i][3], 'Line: ', end = ' ')
                        # printLine(line, True)
                i = i - 1
            # 若本句中无动词，则先于此前第2句找，再于此前第1句中找。（前一句可能为插入语）
            trennbarverbexistsinline2 = False
            if verbexistsinline is False and processed_spacy[index - 1][-1][2] == ',' and processed_spacy[index - 2][-1][2] == ',':
                line2 = processed_spacy[index - 2]
                i = len(line2) - 2
                while i >= 0 and trennbarverbexistsinline2 is False:
                    for j in range(len(line2[i][1])):
                        if (line2[i][3] == "VVFIN" or line2[i][0] == "AUX") and (prob_vorsilbe + line2[i][1][j]) in trennbare_woeter[prob_vorsilbe]:
                            # 可分前缀删掉，动词替换成可分动词原形
                            trennbarverbexistsinline2 = True
                            line[-2][0] = "TPRFX"
                            line2[i][1][j] = prob_vorsilbe + line2[i][1][j]
                            line[-2][1][0] = line[i][1][j]
                            # print(line2[i][1][j], line2[i][3], 'Line-2 :', end = ' ')
                            # printLine(line2, False)
                            # printLine(line1, False)
                            # printLine(line, True)
                    i = i - 1
            trennbarverbexistsinline1 = False
            if verbexistsinline is False and trennbarverbexistsinline2 is False and processed_spacy[index - 1][-1][2] == ',':
                line1 = processed_spacy[index - 1]
                i = len(line1) - 2
                while i >= 0 and trennbarverbexistsinline1 is False:
                    for j in range(len(line1[i][1])):
                        if (line1[i][3] == "VVFIN" or line1[i][0] == "AUX") and (prob_vorsilbe + line1[i][1][j]) in \
                                trennbare_woeter[prob_vorsilbe]:
                            # 可分前缀删掉，动词替换成可分动词原形
                            line[-2][0] = "TPRFX"
                            line1[i][1][j] = prob_vorsilbe + line1[i][1][j]
                            line[-2][1][j] = line[i][1][j]
                            # print(line1[i][1][j], line1[i][3], 'Line-1 :', end = ' ')
                            # printLine(line1, False)
                            # printLine(line, True)
                    i = i - 1
# 检查并列连词(und, oder, aber, denn, sondern)前面的词是否为可分前缀
    for index in range(len(processed_spacy)):
        line = processed_spacy[index]
        for i in range(len(line)-1):
            if i != 0 and line[i][2] in ["und", "oder", "aber", "denn", "sondern"] and line[i - 1][2] in trennbare_woeter.keys():
                prob_vorsilbe = line[i - 1][2]
                for j in range(i):
                    for k in range(len(line[j][1])):
                        if (line[j][0] == "VERB" or line[j][0] == "AUX") and (prob_vorsilbe + line[j][1][k]) in trennbare_woeter[prob_vorsilbe]:
                            # 可分前缀删掉，动词替换成可分动词原形
                            line[i - 1][0] = "TPRFX"
                            line[j][1][k] = prob_vorsilbe + line[j][1][k]
                            line[i - 1][1][k] = line[j][1][k]
                            # print(line[j][1][k], 'ADUSO :', end = ' ')
                            # printLine(line, True)
                        break
    final_text = []
    for index in range(len(processed_spacy)):
        for j in range(len(processed_spacy[index])):
            final_text.append(processed_spacy[index][j])
            #print(f"{processed_spacy[index][j][2]} {processed_spacy[index][j][0]} {processed_spacy[index][j][1][0]}") #记得删掉
    return final_text

def calculate_rate(text, known_words): 
    preprocessed_sentences = preprocess(text)
    doc = nlp(preprocessed_sentences)


    processed_spacy = []
    current_sentence = []
    processed_token = []
    # 对于所有动词，使用iwnlp的lemma；其他词用spacy。
    iw_Lemma = None
    for token in doc:
        if token.pos_ == "VERB":
            iw_Lemma = lemmatizer.lemmatize(token.text, pos_universal_google='VERB')
        if iw_Lemma is not None:
            # if len(iw_Lemma) > 1:
              #  print(token.text)
              #  print(iw_Lemma)
            processed_token.append([token.pos_,  iw_Lemma, token.text, token.tag_])
        else:
            processed_token.append([token.pos_, [token.lemma_], token.text, token.tag_])
            # print([token.pos_,  iw_Lemma, token.text])
            # print([token.pos_, token.lemma_, token.text])
        iw_Lemma = None
    # 以标点为分界，每个词形还原之后的小句存在一个列表内（包括标点），除非逗号连接两个并列的adj或adv
    for i in range(len(processed_token)):
        if processed_token[i][0] != 'PUNCT':  # 当前元素不是标点
            current_sentence.append(processed_token[i])
        else:
            if processed_token[i][2] == ',':
                if (processed_token[i - 1][0] == 'ADJ' and processed_token[i + 1][0] == 'ADJ') or (processed_token[i - 1][0] == 'ADV' and processed_token[i + 1][0] == 'ADV'):  # 将elif和if语句分开写，以规避优先级和下标溢出的问题。
                    # print(processed_token[i - 1], processed_token[i + 1])
                    current_sentence.append([processed_token[i][0],['OMITTED'],processed_token[i][2],processed_token[i][3]])
                    continue
            if current_sentence:  # 相当于current_sentence != []
                current_sentence.append(processed_token[i])
                processed_spacy.append(current_sentence)
                current_sentence = []
            else:  # 连续标点，合并为一个列表。
                processed_spacy[-1][-1][2] = processed_spacy[-1][-1][2] + processed_token[i][2]
                continue


# for i in processed_spacy:
#     print (i)
# print(processed_spacy)

    processed_text = process_trennbare_woerter(processed_spacy)
    #print(processed_text)#记得给删掉
    wordcount = 0
    new_words = []
    for i in range(len(processed_text)):
        isNewWord = False
        if processed_text[i][0] == 'PUNCT':
            word = ''
        else:
            word = processed_text[i][1][0]
            if processed_text[i][0] != 'TPRFX':
                wordcount = wordcount + 1
        if word and (word not in known_words):
            isNewWord = True
            if (processed_text[i][0] != 'TPRFX') and (word not in new_words):
                new_words.append(word)
        processed_text[i] = [processed_text[i][2],isNewWord]
    result = {'wordcount':wordcount,'newwordscount':len(new_words),'konwnwordscount':wordcount-len(new_words),'rate':len(new_words)/wordcount,'newwordslist':new_words,'text':processed_text}
    # print(result)
    return wordcount,len(new_words),wordcount-len(new_words),len(new_words)/wordcount,new_words,processed_text


