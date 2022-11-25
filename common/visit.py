import commons


def run():
    inp = input("请输入您想访问页面的url：  ").strip()

    if hasattr(commons, inp):

        func = getattr(commons, inp)

        func()

    else:

        print("404")


if __name__ == '__main__':
    # s = [
    #     {"no": 28, "score": 90},
    #     {"no": 25, "score": 90},
    #     {"no": 1, "score": 100},
    #     {"no": 2, "score": 20},
    # ]
    # print("original s: ", s)
    # # 单级排序，仅按照score排序
    # s = sorted(s, key=lambda e: e.__getitem__('score'))
    # print(s)

    unchange_files = [{'Files': [{'File': {'FileType': 'Constituent', 'ObjectId': 'a9ed4ce0-74d3-4e14-b58d-c566a8b748bc',
                          'Description': ' ', 'FileName': '140963563408_transcript.xml',
                          'FileCreated': '2016-12-02T16:01:03.125Z', 'Designator': 'EDT-1',
                          'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                          'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL',
                          'Language': 'en', 'MimeType': 'application/xml',
                          'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/a9ed4ce0-74d3-4e14-b58d-c566a8b748bc?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                 '_key_': 'EDT-1'}, {'File': {'ObjectId': '22ce4be9-56b4-4f1e-8689-520703ee0a5c', 'Designator': 'RDL-7',
                                              'FileType': 'Constituent', 'Description': ' ',
                                              'FileName': '140963563408_transcript.xml',
                                              'FileCreated': '2016-12-02T16:01:03.125Z',
                                              'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                                              'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705',
                                              'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml',
                                              'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/22ce4be9-56b4-4f1e-8689-520703ee0a5c?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                                     '_key_': 'RDL-7'}, {
                    'File': {'Designator': 'RDL-6', 'FileType': 'Constituent', 'Description': ' ',
                             'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z',
                             'ObjectId': '89f15f85-586e-4060-8299-05cbbca0c1ac',
                             'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                             'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL',
                             'Language': 'en', 'MimeType': 'application/xml',
                             'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/89f15f85-586e-4060-8299-05cbbca0c1ac?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                    '_key_': 'RDL-6'}, {
                    'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml',
                             'FileCreated': '2016-12-02T16:01:03.125Z',
                             'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                             'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Designator': 'RDL-5',
                             'ObjectId': 'ed2efe01-6289-4b83-ac0f-f5c6a81e1c9f', 'Source': 'ATL', 'Language': 'en',
                             'MimeType': 'application/xml',
                             'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/ed2efe01-6289-4b83-ac0f-f5c6a81e1c9f?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                    '_key_': 'RDL-5'}, {'File': {'FileType': 'Constituent', 'Description': ' ',
                                                 'ObjectId': '4c0e5136-b5a9-4f32-9cd5-bacb61feab2f',
                                                 'FileName': '140963563408_transcript.xml',
                                                 'FileCreated': '2016-12-02T16:01:03.125Z',
                                                 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0',
                                                 'FileSize': 52258, 'Designator': 'RDL-4',
                                                 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705',
                                                 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml',
                                                 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/4c0e5136-b5a9-4f32-9cd5-bacb61feab2f?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                                        '_key_': 'RDL-4'}, {
                    'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml',
                             'FileCreated': '2016-12-02T16:01:03.125Z',
                             'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                             'Designator': 'RDL-3', 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705',
                             'ObjectId': 'd05374ac-4a14-450d-8eeb-3acb58d89f75', 'Source': 'ATL', 'Language': 'en',
                             'MimeType': 'application/xml',
                             'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/d05374ac-4a14-450d-8eeb-3acb58d89f75?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                    '_key_': 'RDL-3'}, {
                    'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml',
                             'FileCreated': '2016-12-02T16:01:03.125Z',
                             'ObjectId': 'e74fe509-b964-4ef3-8ac2-065aa2c40c05',
                             'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'Designator': 'RDL-2',
                             'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705',
                             'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml',
                             'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/e74fe509-b964-4ef3-8ac2-065aa2c40c05?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                    '_key_': 'RDL-2'}, {
                    'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml',
                             'Designator': 'EDT', 'FileCreated': '2016-12-02T16:01:03.125Z',
                             'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                             'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL',
                             'ObjectId': 'dc795c26-5659-4164-86b8-8b939a8ab039', 'Language': 'en',
                             'MimeType': 'application/xml',
                             'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/dc795c26-5659-4164-86b8-8b939a8ab039?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                    '_key_': 'EDT'}, {
                    'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml',
                             'ObjectId': 'bd05fdcc-f80d-4ed4-bd14-4756d3ac87b6',
                             'FileCreated': '2016-12-02T16:01:03.125Z', 'Designator': 'RDL-10',
                             'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                             'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL',
                             'Language': 'en', 'MimeType': 'application/xml',
                             'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/bd05fdcc-f80d-4ed4-bd14-4756d3ac87b6?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                    '_key_': 'RDL-10'}, {
                    'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml',
                             'FileCreated': '2016-12-02T16:01:03.125Z',
                             'ObjectId': '5ff0d063-a91f-49dc-89e6-ada04f2a9599',
                             'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258,
                             'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL',
                             'Designator': 'RDL-9', 'Language': 'en', 'MimeType': 'application/xml',
                             'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/5ff0d063-a91f-49dc-89e6-ada04f2a9599?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                    '_key_': 'RDL-9'}, {'File': {'Designator': 'RDL-8', 'FileType': 'Constituent',
                                                 'ObjectId': '44d40c16-1f8a-49b2-b5cd-8dc92a2aa241', 'Description': ' ',
                                                 'FileName': '140963563408_transcript.xml',
                                                 'FileCreated': '2016-12-02T16:01:03.125Z',
                                                 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0',
                                                 'FileSize': 52258,
                                                 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705',
                                                 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml',
                                                 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/44d40c16-1f8a-49b2-b5cd-8dc92a2aa241?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'},
                                        '_key_': 'RDL-8'}]}]



    s1 = [{'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'Designator': 'EDT', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'ObjectId': 'dc795c26-5659-4164-86b8-8b939a8ab039', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/dc795c26-5659-4164-86b8-8b939a8ab039?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'EDT'}, {'File': {'FileType': 'Constituent', 'ObjectId': 'a9ed4ce0-74d3-4e14-b58d-c566a8b748bc', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Designator': 'EDT-1', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/a9ed4ce0-74d3-4e14-b58d-c566a8b748bc?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'EDT-1'}, {'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'ObjectId': 'bd05fdcc-f80d-4ed4-bd14-4756d3ac87b6', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Designator': 'RDL-10', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/bd05fdcc-f80d-4ed4-bd14-4756d3ac87b6?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-10'}, {'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'ObjectId': 'e74fe509-b964-4ef3-8ac2-065aa2c40c05', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'Designator': 'RDL-2', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/e74fe509-b964-4ef3-8ac2-065aa2c40c05?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-2'}, {'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'Designator': 'RDL-3', 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'ObjectId': 'd05374ac-4a14-450d-8eeb-3acb58d89f75', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/d05374ac-4a14-450d-8eeb-3acb58d89f75?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-3'}, {'File': {'FileType': 'Constituent', 'Description': ' ', 'ObjectId': '4c0e5136-b5a9-4f32-9cd5-bacb61feab2f', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'Designator': 'RDL-4', 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/4c0e5136-b5a9-4f32-9cd5-bacb61feab2f?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-4'}, {'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Designator': 'RDL-5', 'ObjectId': 'ed2efe01-6289-4b83-ac0f-f5c6a81e1c9f', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/ed2efe01-6289-4b83-ac0f-f5c6a81e1c9f?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-5'}, {'File': {'Designator': 'RDL-6', 'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'ObjectId': '89f15f85-586e-4060-8299-05cbbca0c1ac', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/89f15f85-586e-4060-8299-05cbbca0c1ac?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-6'}, {'File': {'ObjectId': '22ce4be9-56b4-4f1e-8689-520703ee0a5c', 'Designator': 'RDL-7', 'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/22ce4be9-56b4-4f1e-8689-520703ee0a5c?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-7'}, {'File': {'Designator': 'RDL-8', 'FileType': 'Constituent', 'ObjectId': '44d40c16-1f8a-49b2-b5cd-8dc92a2aa241', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/44d40c16-1f8a-49b2-b5cd-8dc92a2aa241?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-8'}, {'File': {'FileType': 'Constituent', 'Description': ' ', 'FileName': '140963563408_transcript.xml', 'FileCreated': '2016-12-02T16:01:03.125Z', 'ObjectId': '5ff0d063-a91f-49dc-89e6-ada04f2a9599', 'Store': 'ecp:9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0', 'FileSize': 52258, 'ContentItem': 'ecp:9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705', 'Source': 'ATL', 'Designator': 'RDL-9', 'Language': 'en', 'MimeType': 'application/xml', 'FileLink': 'https://preprod.retrieval.cdf.int.refinitiv.com/v1/data-store/distributionpair/ecp%3A9-c90fb2bf-dfcd-4d91-a35b-473f8b0d66b0/objects/5ff0d063-a91f-49dc-89e6-ada04f2a9599?content_items=ecp%3A9-af6cd4b1-3d8c-4e40-b5cc-20326e9ed705&version=ecp%3A9-70eaa654-ffe6-442c-b89d-87418f8802af'}, '_key_': 'RDL-9'}]




    s = sorted(unchange_files[0]['Files'], key=lambda e: e.__getitem__('_key_'))
    s1 = sorted(s1, key=lambda e: e.__getitem__('_key_'))

    print(s1)