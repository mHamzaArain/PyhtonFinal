#program to extract link
target = r'B:\Python Course\Ch18_Working_with_files\Ch18_Ex2\html.txt'
extract = r'B:\Python Course\Ch18_Working_with_files\Ch18_Ex2\extract.txt'

def url_finder(link):
    if "href" in link:
        comma_split = link.split('\"')  #   ' \" '
        return [each for each in comma_split if each[-4: ].lower() == ".com" ]

# pdb.set_trace()
def transfer(target, extract):
        with open(target) as rf:
                with open(extract, 'w') as wf:
                        for line in rf.readlines():
                                contain_url = url_finder(line)
                                if contain_url != None:   
                                        for extractedLink in contain_url:
                                                wf.write(f"\n>  {extractedLink}")
                wf.close()
        rf.close()

transfer(target, extract)