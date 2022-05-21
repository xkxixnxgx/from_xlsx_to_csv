import xlsxwriter


# def as_xlsx(self):
#     output = BytesIO()
#     workbook = xlsxwriter.Workbook(output)
#     worksheet = workbook.add_worksheet()
#     cell_format = workbook.add_format()
#     cell_format.set_text_wrap('\n')

#     for i, node in enumerate(self.data):
#         worksheet.write(i, 0, node.answer.id)
#         worksheet.write(i, 1, node.answer.text)
#         worksheet.write(i, 2, '\n'.join([q.text for q in node.questions]), cell_format)
#         worksheet.write(i, 3, '\n'.join(node.answer.tags), cell_format)
#         if not node.answer.comment:
#             worksheet.write(i, 4, ' ')
#         else:
#             worksheet.write(i, 4, node.answer.comment)

#     workbook.close()
#     return output.getvalue()


# def from_xlsx(self, file_obj):
#     df = pd.read_excel(file_obj, index_col=None, header=None)
#     df = df.replace(np.nan, '', regex=True)

#     nodes = []
#     for i, row in df.iterrows():
#         answer_map = AnswerMapper(
#             id=row[0],
#             text=row[1],
#             comment=row[4] if len(row) > 3 else None,
#             tags=row[3].split('\n') if len(row) > 2 else None
#         )
#         questions_map = [
#             QuestionMapper(text=q)
#             for q in row[2].split('\n')
#         ]
#         nodes.append(FAQNodeMapper(answer=answer_map, questions=questions_map))
#     return FAQMapper(data=nodes)



PATH_FILE_XLSX = '~/dict'
PATH_FILE_CSV = '~/dict'


def decode():
    print('start')


if __name__ == '__main__':
    decode()
