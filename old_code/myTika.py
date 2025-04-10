import sys
from tika import parser, unpack
import docx2txt
import xml.etree.ElementTree as ET
import xmltodict
import json
print("Initiate Python & Tika", sys.argv)

"""
 @Param int         NoQ             Number of Questions
 @Param int         NoA             Number of Answers
 @Param string      DocxPath        Path to Docx File
 @Param string      OutputMedia     Path to Export Media
 @Param string      Action          Output Configuration        // Default = "get_all"
 @Param boolean     ExtractImage    Extract Images From Docx    // Default = True
 @Param boolean     ExtractText     Extract Text From Docx      // Default = True
"""
# def tikaExtractDocx(NoQ, DocxPath, OutputMedia, ):
def tikaExtractDocx(NoQ, NoA):
    parsed_pdf = parser.from_file("./uploads/Q_With_Image_2.docx", xmlContent=False, )
    take_paragraph = parsed_pdf["content"].strip("\n").split("\n")
    # parsed_pdf = parser.from_file(sys.argv[1], xmlContent=True)
    formattedMetadata = "{}".format(parsed_pdf["metadata"])
    MYJSONOBJ = json.dumps(parsed_pdf["content"])

    cleansed_letter = []
    while "" in take_paragraph:
        take_paragraph.remove("")

    # GET DISCUSSIONS
    # for letter in take_paragraph:
    #     if "Pembahasan: " in letter:
    #         print(letter)


    # GET QUESTIONS
    # for letter in take_paragraph:
    #     n = 0
    #     while n <= 7:
    #         n += 1
    #         if letter[0:3] == str(n)+". ":
    #             print(letter)


    # GET ALL [Questions, Answers, Discussions]
    # question_answer = []
    # question_answer_length = len(question_answer)
    # start = 0
    # end = len(take_paragraph)
    # step = 1 + NoA + 2
    # for i in range(start, end, step):
    #     question_answer.append(take_paragraph[i:i + step])
    #
    # for question in question_answer:
    #     n = 0
    #     while n <= question_answer_length:
    #         print(question)
    #         n += 1


    # Get Answers
    arr_of_answer = []
    question_answer_length = len(arr_of_answer)
    start = 1
    end = len(take_paragraph)
    step = NoA

    print(range(start, end, step))

    for i in range(start, end, step):
        print(take_paragraph[i:i + step])
        arr_of_answer.append(take_paragraph[i:i + step])

    # for text in take_paragraph:
    #     print(text)

    # print(arr_of_answer)


    # print("Metadata Info: \n{}".format(parsed_pdf["metadata"]))
    # print(xmltodict.parse(xmlData))
    # return parsed_pdf['content']
    # return dict([('metadata', parsed_pdf['metadata']), ('content', parsed_pdf['content'])])


# def bytesToImage():
#     # b = base64.decodebytes(tikaExtractDocx())
#     myImg = Image.frombytes('RGBA', (256, 256), tikaExtractDocx(), 'raw')
#     img = Image.open(io.BytesIO(myImg))
#     img.show()


def extractImage():
    text = docx2txt.process(sys.argv[1], sys.argv[2])
    return text


# bytesToImage()
# extractImage()
# tikaExtractDocx(7, sys.argv[1], sys.argv[2])
tikaExtractDocx(7, 5)
# print(tikaExtractDocx())
# os.write(3, bytes('{"dt" : "This is a test"}\n', 'utf8'))
# sys.stdout.write(tikaExtractDocx())


